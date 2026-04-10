#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Summary Data Preparation

Collects video metadata and captions to prepare for summary generation.
Integrates youtube-info and youtube-captions skills.
"""

import sys
import json
import subprocess
import os
from pathlib import Path

# Fix Windows console encoding issues
if sys.platform == 'win32':
    import codecs
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')


def run_command(command, timeout=180):
    """
    Run a shell command and return output.

    Args:
        command: Command list to execute
        timeout: Maximum execution time in seconds

    Returns:
        Dictionary with success status and output/error
    """
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding='utf-8',
            errors='replace'
        )

        if result.returncode == 0:
            return {
                'success': True,
                'output': result.stdout.strip()
            }
        else:
            return {
                'success': False,
                'error': result.stderr.strip() or result.stdout.strip()
            }
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'error': f'Command timed out after {timeout} seconds'
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def get_video_info(url, youtube_api_key, skills_dir):
    """
    Get video metadata using youtube-info skill.

    Args:
        url: YouTube URL
        youtube_api_key: YouTube Data API key
        skills_dir: Path to skills directory

    Returns:
        Dictionary with video info or error
    """
    script_path = os.path.join(skills_dir, 'youtube-info', 'scripts', 'get_youtube_info.py')

    if not os.path.exists(script_path):
        return {
            'success': False,
            'error': f'youtube-info script not found at {script_path}'
        }

    command = ['python', script_path, url, youtube_api_key]
    result = run_command(command)

    if result['success']:
        try:
            info = json.loads(result['output'])
            return info
        except json.JSONDecodeError as e:
            return {
                'success': False,
                'error': f'Failed to parse video info: {e}'
            }
    else:
        return result


def get_video_captions(url, apify_api_key, skills_dir, actor_id=None):
    """
    Get video captions using youtube-captions skill.

    Args:
        url: YouTube URL
        apify_api_key: Apify API key
        skills_dir: Path to skills directory
        actor_id: Optional Apify Actor ID

    Returns:
        Dictionary with captions or error
    """
    script_path = os.path.join(skills_dir, 'youtube-captions', 'scripts', 'get_youtube_captions.py')

    if not os.path.exists(script_path):
        return {
            'success': False,
            'error': f'youtube-captions script not found at {script_path}'
        }

    command = ['python', script_path, url, apify_api_key]
    if actor_id:
        command.append(actor_id)

    result = run_command(command, timeout=300)

    if result['success']:
        try:
            captions = json.loads(result['output'])
            return captions
        except json.JSONDecodeError as e:
            return {
                'success': False,
                'error': f'Failed to parse captions: {e}'
            }
    else:
        return result


def format_duration(iso_duration):
    """
    Convert ISO 8601 duration to HH:MM:SS format.

    Args:
        iso_duration: Duration in ISO 8601 format (e.g., PT3M33S)

    Returns:
        Duration in HH:MM:SS format
    """
    import re

    if not iso_duration:
        return '00:00:00'

    # Parse ISO 8601 duration
    pattern = r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?'
    match = re.match(pattern, iso_duration)

    if not match:
        return '00:00:00'

    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


def main():
    """Main function to prepare summary data."""
    if len(sys.argv) < 4:
        print("Usage: python prepare_summary_data.py <YOUTUBE_URL> <YOUTUBE_API_KEY> <APIFY_API_KEY> [ACTOR_ID] [--output FILE]")
        print("\nArguments:")
        print("  YOUTUBE_URL        YouTube video URL")
        print("  YOUTUBE_API_KEY    YouTube Data API key")
        print("  APIFY_API_KEY      Apify API key for captions")
        print("  ACTOR_ID           (Optional) Specific Apify Actor to use")
        print("\nOptions:")
        print("  --output FILE      Save output to JSON file")
        print("\nExample:")
        print('  python prepare_summary_data.py "https://www.youtube.com/watch?v=..." "YOUTUBE_KEY" "APIFY_KEY"')
        sys.exit(1)

    url = sys.argv[1]
    youtube_api_key = sys.argv[2]
    apify_api_key = sys.argv[3]

    # Optional Actor ID
    actor_id = None
    output_file = None

    for i in range(4, len(sys.argv)):
        if sys.argv[i] == '--output' and i + 1 < len(sys.argv):
            output_file = sys.argv[i + 1]
        elif not sys.argv[i].startswith('--'):
            actor_id = sys.argv[i]

    # Find skills directory
    # Assume skills are in C:\Users\c\.claude\skills
    skills_dir = r'C:\Users\c\.claude\skills'

    print("Collecting video information...", file=sys.stderr)

    # Get video info
    info_result = get_video_info(url, youtube_api_key, skills_dir)

    if not info_result.get('success'):
        output = {
            'success': False,
            'error': f"Failed to get video info: {info_result.get('error', 'Unknown error')}",
            'video_info': None,
            'captions': None
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
        sys.exit(1)

    print("Collecting video captions...", file=sys.stderr)

    # Get captions
    captions_result = get_video_captions(url, apify_api_key, skills_dir, actor_id)

    # Prepare combined output
    output = {
        'success': True,
        'video_url': url,
        'video_info': {
            'title': info_result.get('title', 'N/A'),
            'channel_title': info_result.get('channel_title', 'N/A'),
            'published_at': info_result.get('published_at', 'N/A'),
            'duration': format_duration(info_result.get('duration', '')),
            'duration_iso': info_result.get('duration', ''),
            'view_count': info_result.get('view_count', 'N/A'),
            'like_count': info_result.get('like_count', 'N/A'),
            'description': info_result.get('description', '')[:500] + '...' if len(info_result.get('description', '')) > 500 else info_result.get('description', '')
        },
        'captions': {
            'success': captions_result.get('success', False),
            'text': captions_result.get('text', '') if captions_result.get('success') else None,
            'timestamped': captions_result.get('captions', []) if captions_result.get('success') else [],
            'error': captions_result.get('error') if not captions_result.get('success') else None
        },
        'ready_for_summary': captions_result.get('success', False)
    }

    # Output to file or stdout
    json_output = json.dumps(output, indent=2, ensure_ascii=False)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(json_output)
        print(f"Data saved to: {output_file}", file=sys.stderr)
    else:
        print(json_output)

    if not output['ready_for_summary']:
        print("\nWarning: Captions not available. Summary will be limited to video metadata only.", file=sys.stderr)

    sys.exit(0 if output['ready_for_summary'] else 1)


if __name__ == '__main__':
    main()
