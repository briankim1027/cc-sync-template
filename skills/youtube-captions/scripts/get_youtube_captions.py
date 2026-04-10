#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Captions Extractor using Apify API

Extracts captions/subtitles from YouTube videos using Apify Actors.
Supports both plain text and timestamped format.
"""

import sys
import json
import time
import re
from urllib.request import Request, urlopen, quote
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse, parse_qs

# Fix Windows console encoding issues
if sys.platform == 'win32':
    import codecs
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')


def extract_video_id(url):
    """
    Extract video ID from YouTube URL.

    Args:
        url: YouTube URL string

    Returns:
        Video ID string or None if not found
    """
    parsed = urlparse(url)

    # Standard format: youtube.com/watch?v=VIDEO_ID
    if parsed.netloc in ['www.youtube.com', 'youtube.com', 'm.youtube.com']:
        if parsed.path == '/watch':
            query_params = parse_qs(parsed.query)
            return query_params.get('v', [None])[0]

    return None


def call_apify_actor_sync(actor_id, run_input, api_key, timeout=180):
    """
    Call Apify Actor synchronously and get results.

    Args:
        actor_id: Apify Actor ID
        run_input: Input parameters for the Actor
        api_key: Apify API key
        timeout: Maximum wait time in seconds

    Returns:
        Dictionary containing results or error
    """
    # Use synchronous endpoint that waits for completion
    # Format: /v2/acts/{actorId}/run-sync-get-dataset-items
    sync_url = f"https://api.apify.com/v2/acts/{quote(actor_id, safe='')}/run-sync-get-dataset-items?token={api_key}&timeout={timeout}"

    try:
        request = Request(
            sync_url,
            data=json.dumps(run_input).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
            method='POST'
        )

        with urlopen(request, timeout=timeout) as response:
            results = json.loads(response.read().decode('utf-8'))

        return {
            'success': True,
            'results': results
        }

    except HTTPError as e:
        error_body = ''
        try:
            error_body = e.read().decode('utf-8')
            error_data = json.loads(error_body)
            error_msg = error_data.get('error', {}).get('message', str(e.reason))
        except:
            error_msg = f"{e.code}: {e.reason}"

        if e.code == 401:
            error_msg = "Invalid Apify API key"
        elif e.code == 404:
            error_msg = f"Actor '{actor_id}' not found. Please verify the Actor ID."
        elif e.code == 400:
            error_msg = f"Invalid input parameters: {error_msg}"

        return {'success': False, 'error': error_msg}
    except URLError as e:
        return {'success': False, 'error': f"Network error: {e.reason}"}
    except Exception as e:
        return {'success': False, 'error': f"Unexpected error: {str(e)}"}


def format_captions(raw_results, include_timestamps=True, plain_text_only=False):
    """
    Format caption results for display.

    Args:
        raw_results: Raw results from Apify Actor
        include_timestamps: Whether to include timestamps
        plain_text_only: Whether to output only plain text

    Returns:
        Formatted caption data
    """
    if not raw_results or len(raw_results) == 0:
        return {'captions': [], 'text': ''}

    # Extract caption data from results
    caption_data = raw_results[0] if isinstance(raw_results, list) else raw_results

    captions = []
    full_text = []

    # Handle various result structures from different Actors
    if 'subtitles' in caption_data:
        # Structure with 'subtitles' array
        subtitle_data = caption_data.get('subtitles', [])
        if isinstance(subtitle_data, list):
            for item in subtitle_data:
                if isinstance(item, dict):
                    text = item.get('text', '')
                    if text:
                        full_text.append(text)
                        if include_timestamps and not plain_text_only:
                            captions.append({
                                'start': item.get('start', item.get('startTime', 0)),
                                'duration': item.get('duration', item.get('dur', 0)),
                                'text': text
                            })
                elif isinstance(item, str):
                    full_text.append(item)

    elif 'transcript' in caption_data:
        # Structure with 'transcript' key
        transcript = caption_data.get('transcript', '')
        if isinstance(transcript, str):
            full_text.append(transcript)
        elif isinstance(transcript, list):
            for item in transcript:
                if isinstance(item, dict):
                    text = item.get('text', '')
                    if text:
                        full_text.append(text)
                        if include_timestamps and not plain_text_only:
                            captions.append({
                                'start': item.get('start', item.get('startTime', 0)),
                                'duration': item.get('duration', item.get('dur', 0)),
                                'text': text
                            })
                elif isinstance(item, str):
                    full_text.append(item)

    elif 'text' in caption_data:
        # Direct text field
        text = caption_data.get('text', '')
        if text:
            full_text.append(text)

    # If no structured caption found, try to extract any text content
    if not full_text:
        for key, value in caption_data.items():
            if isinstance(value, str) and len(value) > 50:
                full_text.append(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str):
                        full_text.append(item)

    return {
        'captions': captions if not plain_text_only else [],
        'text': ' '.join(full_text).strip()
    }


def main():
    """Main function to handle command-line execution."""
    if len(sys.argv) < 3:
        print("Usage: python get_youtube_captions.py <YOUTUBE_URL> <APIFY_API_KEY> [ACTOR_ID] [--plain-text] [--no-timestamps]")
        print("\nArguments:")
        print("  YOUTUBE_URL        YouTube video URL")
        print("  APIFY_API_KEY      Your Apify API key")
        print("  ACTOR_ID           (Optional) Specific Apify Actor to use")
        print("\nOptions:")
        print("  --plain-text       Output only plain text without JSON structure")
        print("  --no-timestamps    Exclude timestamps from output")
        print("\nExample:")
        print('  python get_youtube_captions.py "https://www.youtube.com/watch?v=..." "YOUR_API_KEY"')
        print('  python get_youtube_captions.py "https://..." "API_KEY" "streamers/youtube-scraper"')
        sys.exit(1)

    url = sys.argv[1]
    api_key = sys.argv[2]

    # Optional Actor ID
    actor_id = None
    if len(sys.argv) > 3 and not sys.argv[3].startswith('--'):
        actor_id = sys.argv[3]

    # Parse options
    plain_text_only = '--plain-text' in sys.argv
    include_timestamps = '--no-timestamps' not in sys.argv

    # Extract video ID
    video_id = extract_video_id(url)

    if not video_id:
        print(json.dumps({
            'success': False,
            'error': 'Invalid YouTube URL format'
        }, indent=2))
        sys.exit(1)

    # Default Actor if not specified
    if not actor_id:
        # Try popular YouTube caption/scraper actors
        actor_id = 'streamers/youtube-scraper'  # General YouTube scraper

    # Prepare input for the Actor
    run_input = {
        'startUrls': [{'url': url}],
        'maxResults': 1
    }

    # Run the Actor
    print(f"Running Apify Actor: {actor_id}...", file=sys.stderr)
    result = call_apify_actor_sync(actor_id, run_input, api_key)

    if not result['success']:
        output = {
            'success': False,
            'error': result['error'],
            'suggestion': 'Try specifying a different Actor ID as the third argument, e.g., "streamers/youtube-scraper"'
        }
        print(json.dumps(output, indent=2))
        sys.exit(1)

    # Format the captions
    formatted = format_captions(
        result['results'],
        include_timestamps=include_timestamps,
        plain_text_only=plain_text_only
    )

    if not formatted['text']:
        print(json.dumps({
            'success': False,
            'error': 'No captions found in Actor results. The video may not have captions, or try a different Actor.',
            'raw_results': result['results'] if len(str(result['results'])) < 1000 else 'Results too large to display'
        }, indent=2))
        sys.exit(1)

    # Output results
    if plain_text_only:
        print(formatted['text'])
    else:
        output = {
            'success': True,
            'video_id': video_id,
            'video_url': url,
            'actor_used': actor_id,
            'text': formatted['text'],
            'captions': formatted['captions']
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))

    sys.exit(0)


if __name__ == '__main__':
    main()
