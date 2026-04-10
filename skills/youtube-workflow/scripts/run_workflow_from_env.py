#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run YouTube Workflow from .env File

Convenience script that loads configuration from .env file
and runs the complete workflow.
"""

import sys
import os
import subprocess

# Fix Windows console encoding
if sys.platform == 'win32':
    import codecs
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')


def load_env_file(env_path):
    """
    Load environment variables from .env file.

    Args:
        env_path: Path to .env file

    Returns:
        Dictionary of environment variables
    """
    env_vars = {}

    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()

                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue

                # Parse KEY=VALUE
                if '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip()

        return env_vars

    except Exception as e:
        print(f"Error loading .env file: {e}", file=sys.stderr)
        return {}


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python run_workflow_from_env.py <YOUTUBE_URL> [ENV_FILE]")
        print("\nArguments:")
        print("  YOUTUBE_URL    YouTube video URL to process")
        print("  ENV_FILE       (Optional) Path to .env file (default: .env)")
        print("\nExample:")
        print('  python run_workflow_from_env.py "https://www.youtube.com/watch?v=..." ".env"')
        print("\n.env file should contain:")
        print("  YOUTUBE_API_KEY=...")
        print("  APIFY_API_KEY=...")
        print("  EMAIL_RECIPIENTS=user@example.com")
        print("  GMAIL_SENDER=sender@gmail.com")
        print("  GMAIL_APP_PASSWORD=...")
        sys.exit(1)

    url = sys.argv[1]
    env_file = sys.argv[2] if len(sys.argv) > 2 else '.env'

    # Load environment variables
    env_vars = load_env_file(env_file)

    if not env_vars:
        print(f"Failed to load environment variables from: {env_file}", file=sys.stderr)
        sys.exit(1)

    # Get required values
    youtube_api_key = env_vars.get('YOUTUBE_API_KEY')
    apify_api_key = env_vars.get('APIFY_API_KEY')
    email_recipients = env_vars.get('EMAIL_RECIPIENTS') or env_vars.get('eMail')
    output_dir = env_vars.get('OUTPUT_DIR', './youtube_summaries')

    if not youtube_api_key:
        print("Error: YOUTUBE_API_KEY not found in .env file", file=sys.stderr)
        sys.exit(1)

    if not apify_api_key:
        print("Error: APIFY_API_KEY not found in .env file", file=sys.stderr)
        sys.exit(1)

    # Run workflow
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workflow_script = os.path.join(script_dir, 'run_youtube_workflow.py')

    command = [
        'python',
        workflow_script,
        url,
        youtube_api_key,
        apify_api_key
    ]

    if email_recipients:
        command.append(email_recipients)

    command.extend(['--output', output_dir])

    print(f"Running workflow for: {url}")
    print(f"Output directory: {output_dir}")

    try:
        result = subprocess.run(command, check=True)
        sys.exit(result.returncode)
    except subprocess.CalledProcessError as e:
        print(f"Workflow failed with error code: {e.returncode}", file=sys.stderr)
        sys.exit(e.returncode)


if __name__ == '__main__':
    main()
