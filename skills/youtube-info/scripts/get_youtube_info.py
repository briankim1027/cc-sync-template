#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Video Info Fetcher

Extracts video ID from YouTube URL and fetches detailed information using YouTube Data API v3.
"""

import re
import sys
import json
import os
from urllib.parse import urlparse, parse_qs
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# Fix Windows console encoding issues
if sys.platform == 'win32':
    import codecs
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')


def extract_video_id(url):
    """
    Extract video ID from various YouTube URL formats.

    Supported formats:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtube.com/watch?v=VIDEO_ID
    - http://www.youtube.com/watch?v=VIDEO_ID

    Args:
        url: YouTube URL string

    Returns:
        Video ID string or None if not found
    """
    # Parse URL
    parsed = urlparse(url)

    # Standard format: youtube.com/watch?v=VIDEO_ID
    if parsed.netloc in ['www.youtube.com', 'youtube.com', 'm.youtube.com']:
        if parsed.path == '/watch':
            query_params = parse_qs(parsed.query)
            return query_params.get('v', [None])[0]

    return None


def fetch_video_info(video_id, api_key):
    """
    Fetch video information from YouTube Data API v3.

    Args:
        video_id: YouTube video ID
        api_key: YouTube Data API key

    Returns:
        Dictionary containing video information
    """
    # API endpoint
    base_url = "https://www.googleapis.com/youtube/v3/videos"

    # Request parts
    parts = ['snippet', 'statistics', 'contentDetails']

    # Build request URL
    url = f"{base_url}?part={','.join(parts)}&id={video_id}&key={api_key}"

    try:
        # Make API request
        with urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))

        # Check if video exists
        if not data.get('items'):
            return {
                'success': False,
                'error': 'Video not found or is private/deleted'
            }

        video = data['items'][0]
        snippet = video.get('snippet', {})
        statistics = video.get('statistics', {})
        content_details = video.get('contentDetails', {})

        # Extract relevant information
        info = {
            'success': True,
            'video_id': video_id,
            'title': snippet.get('title', 'N/A'),
            'description': snippet.get('description', 'N/A'),
            'channel_title': snippet.get('channelTitle', 'N/A'),
            'channel_id': snippet.get('channelId', 'N/A'),
            'published_at': snippet.get('publishedAt', 'N/A'),
            'thumbnails': snippet.get('thumbnails', {}),
            'view_count': statistics.get('viewCount', 'N/A'),
            'like_count': statistics.get('likeCount', 'N/A'),
            'comment_count': statistics.get('commentCount', 'N/A'),
            'duration': content_details.get('duration', 'N/A'),
            'caption': content_details.get('caption', 'false'),
            'tags': snippet.get('tags', [])
        }

        return info

    except HTTPError as e:
        error_msg = f"HTTP Error {e.code}: {e.reason}"
        if e.code == 403:
            error_msg += " - Check API key validity and quota"
        return {'success': False, 'error': error_msg}
    except URLError as e:
        return {'success': False, 'error': f"Network error: {e.reason}"}
    except Exception as e:
        return {'success': False, 'error': f"Unexpected error: {str(e)}"}


def main():
    """Main function to handle command-line execution."""
    if len(sys.argv) < 3:
        print("Usage: python get_youtube_info.py <YOUTUBE_URL> <API_KEY>")
        print("\nExample:")
        print('  python get_youtube_info.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "YOUR_API_KEY"')
        sys.exit(1)

    url = sys.argv[1]
    api_key = sys.argv[2]

    # Extract video ID
    video_id = extract_video_id(url)

    if not video_id:
        print(json.dumps({
            'success': False,
            'error': 'Invalid YouTube URL format'
        }, indent=2))
        sys.exit(1)

    # Fetch video info
    info = fetch_video_info(video_id, api_key)

    # Output JSON
    print(json.dumps(info, indent=2, ensure_ascii=False))

    # Exit with appropriate code
    sys.exit(0 if info.get('success') else 1)


if __name__ == '__main__':
    main()
