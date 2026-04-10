#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Workflow Automation

Complete workflow: URL → Info + Captions → Summary Prompt → Email
Integrates youtube-info, youtube-captions, and youtube-summary skills.
"""

import sys
import json
import subprocess
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from datetime import datetime

# Fix Windows console encoding issues
if sys.platform == 'win32':
    import codecs
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')


def log(message, level='INFO'):
    """Print log message with timestamp."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] [{level}] {message}", file=sys.stderr)


def run_command(command, timeout=300):
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


def collect_video_data(url, youtube_api_key, apify_api_key, skills_dir):
    """
    Collect video info and captions using youtube-summary skill.

    Args:
        url: YouTube URL
        youtube_api_key: YouTube Data API key
        apify_api_key: Apify API key
        skills_dir: Path to skills directory

    Returns:
        Dictionary with collected data or error
    """
    log("Step 1/3: Collecting video data...")

    script_path = os.path.join(skills_dir, 'youtube-summary', 'scripts', 'prepare_summary_data.py')

    if not os.path.exists(script_path):
        return {
            'success': False,
            'error': f'youtube-summary script not found at {script_path}'
        }

    command = ['python', script_path, url, youtube_api_key, apify_api_key]
    result = run_command(command, timeout=300)

    if result['success']:
        try:
            data = json.loads(result['output'])

            if not data.get('ready_for_summary'):
                log("Warning: Captions not available. Summary will be limited.", 'WARN')

            return data
        except json.JSONDecodeError as e:
            return {
                'success': False,
                'error': f'Failed to parse video data: {e}'
            }
    else:
        return result


def generate_summary_prompt(video_data, template_path):
    """
    Generate a prompt for Claude to create the summary.

    Args:
        video_data: Collected video information
        template_path: Path to summary template

    Returns:
        Prompt string for summary generation
    """
    log("Step 2/3: Generating summary prompt...")

    # Read template
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    except Exception as e:
        log(f"Failed to read template: {e}", 'ERROR')
        template = "# YouTube 영상 요약\n\n[템플릿을 찾을 수 없습니다]"

    # Extract video info
    video_info = video_data.get('video_info', {})
    captions = video_data.get('captions', {})

    # Build prompt
    prompt = f"""# YouTube 영상 학습용 요약 생성

## 요청사항

다음 YouTube 영상에 대한 구조화된 학습용 요약을 생성해주세요.

## 영상 정보

- **제목**: {video_info.get('title', 'N/A')}
- **채널**: {video_info.get('channel_title', 'N/A')}
- **재생시간**: {video_info.get('duration', 'N/A')}
- **조회수**: {video_info.get('view_count', 'N/A')}
- **게시일**: {video_info.get('published_at', 'N/A')}
- **URL**: {video_data.get('video_url', 'N/A')}

## 영상 설명

{video_info.get('description', 'N/A')}

"""

    # Add captions if available
    if captions.get('success') and captions.get('text'):
        caption_text = captions['text']
        # Limit caption length for prompt
        if len(caption_text) > 10000:
            caption_text = caption_text[:10000] + "\n\n[... 자막이 너무 길어 일부만 표시합니다 ...]"

        prompt += f"""## 전체 자막 (Transcript)

{caption_text}

"""
    else:
        prompt += """## 자막 정보

⚠️ 자막을 사용할 수 없습니다. 영상 제목, 설명, 메타데이터를 기반으로 요약을 생성해주세요.

"""

    # Add instructions
    prompt += f"""## 요약 생성 지침

아래 템플릿 형식을 따라 학습용 구조화 요약을 생성해주세요:

{template}

## 중요 요구사항

1. **숫자 기반 인사이트**: 자막에서 언급된 구체적인 수치, 퍼센트, 통계를 추출하고 맥락과 함께 설명
2. **핵심 개념**: 정의 → 작동원리 → 오해하기 쉬운 포인트 순서로 설명
3. **탐구형 질문**: Bloom's Taxonomy를 따라 이해→적용→분석→창조 단계별 질문 생성
4. **구간별 요약**: 타임스탬프가 있다면 3-7개 구간으로 나누어 요약
5. **실용성**: Do/Don't 체크리스트와 적용 시나리오 포함

위 지침을 따라 Markdown 형식으로 요약을 생성해주세요.
"""

    return prompt


def send_email_smtp(recipients, subject, body_html, body_text=None, smtp_config=None):
    """
    Send email using SMTP.

    Args:
        recipients: List of email addresses or comma-separated string
        subject: Email subject
        body_html: HTML body content
        body_text: Plain text alternative (optional)
        smtp_config: SMTP configuration dict (optional)

    Returns:
        Dictionary with success status
    """
    log("Step 3/3: Sending email...")

    # Parse recipients
    if isinstance(recipients, str):
        recipients = [r.strip() for r in recipients.split(',')]

    # Default SMTP config for Gmail
    if smtp_config is None:
        smtp_config = {
            'server': 'smtp.gmail.com',
            'port': 587,
            'use_tls': True
        }

    # Create message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = recipients[0]  # Use first recipient as sender
    msg['To'] = ', '.join(recipients)

    # Attach text and HTML parts
    if body_text:
        part1 = MIMEText(body_text, 'plain', 'utf-8')
        msg.attach(part1)

    part2 = MIMEText(body_html, 'html', 'utf-8')
    msg.attach(part2)

    try:
        # For Gmail, we'll create a simple SMTP connection
        # Note: This requires "Less secure app access" or App Password
        log(f"Attempting to send email to: {', '.join(recipients)}")

        # Gmail SMTP usually requires authentication
        # For this automation, we'll save the prompt to a file instead
        # and instruct user to send manually or configure SMTP

        return {
            'success': False,
            'error': 'SMTP requires authentication. Email content saved to file instead.',
            'note': 'Please configure Gmail App Password or use manual sending.'
        }

    except Exception as e:
        return {
            'success': False,
            'error': f'Failed to send email: {str(e)}'
        }


def save_output_files(video_data, summary_prompt, output_dir):
    """
    Save workflow outputs to files.

    Args:
        video_data: Collected video data
        summary_prompt: Generated summary prompt
        output_dir: Output directory path

    Returns:
        Dictionary with file paths
    """
    log("Saving output files...")

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Generate filename from video title
    video_title = video_data.get('video_info', {}).get('title', 'video')
    # Sanitize filename
    safe_title = "".join(c for c in video_title if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_title = safe_title[:50]  # Limit length

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    files = {}

    # Save video data JSON
    data_file = os.path.join(output_dir, f'{safe_title}_{timestamp}_data.json')
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(video_data, f, indent=2, ensure_ascii=False)
    files['data'] = data_file
    log(f"Saved video data: {data_file}")

    # Save summary prompt
    prompt_file = os.path.join(output_dir, f'{safe_title}_{timestamp}_prompt.md')
    with open(prompt_file, 'w', encoding='utf-8') as f:
        f.write(summary_prompt)
    files['prompt'] = prompt_file
    log(f"Saved summary prompt: {prompt_file}")

    # Create email draft
    email_file = os.path.join(output_dir, f'{safe_title}_{timestamp}_email_draft.html')
    email_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1 {{ color: #333; }}
        .meta {{ background: #f4f4f4; padding: 15px; margin: 20px 0; border-radius: 5px; }}
        .prompt {{ background: #fff; border-left: 4px solid #4CAF50; padding: 15px; margin: 20px 0; }}
        pre {{ background: #f8f8f8; padding: 10px; overflow-x: auto; }}
    </style>
</head>
<body>
    <h1>YouTube 영상 학습용 요약 요청</h1>

    <div class="meta">
        <h2>📺 영상 정보</h2>
        <ul>
            <li><strong>제목:</strong> {video_data.get('video_info', {}).get('title', 'N/A')}</li>
            <li><strong>채널:</strong> {video_data.get('video_info', {}).get('channel_title', 'N/A')}</li>
            <li><strong>재생시간:</strong> {video_data.get('video_info', {}).get('duration', 'N/A')}</li>
            <li><strong>조회수:</strong> {video_data.get('video_info', {}).get('view_count', 'N/A')}</li>
            <li><strong>URL:</strong> <a href="{video_data.get('video_url')}">{video_data.get('video_url')}</a></li>
        </ul>
    </div>

    <div class="prompt">
        <h2>📝 요약 생성 프롬프트</h2>
        <p>아래 프롬프트를 Claude에게 제공하여 구조화된 요약을 생성하세요:</p>
        <p><strong>프롬프트 파일:</strong> <code>{os.path.basename(prompt_file)}</code></p>
    </div>

    <hr>

    <p><em>생성 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</em></p>
    <p><em>이 이메일은 YouTube Workflow 스킬에 의해 자동 생성되었습니다.</em></p>
</body>
</html>"""

    with open(email_file, 'w', encoding='utf-8') as f:
        f.write(email_html)
    files['email'] = email_file
    log(f"Saved email draft: {email_file}")

    return files


def main():
    """Main workflow function."""
    if len(sys.argv) < 4:
        print("Usage: python run_youtube_workflow.py <YOUTUBE_URL> <YOUTUBE_API_KEY> <APIFY_API_KEY> [EMAIL_RECIPIENTS] [--output DIR]")
        print("\nArguments:")
        print("  YOUTUBE_URL         YouTube video URL")
        print("  YOUTUBE_API_KEY     YouTube Data API key")
        print("  APIFY_API_KEY       Apify API key")
        print("  EMAIL_RECIPIENTS    (Optional) Comma-separated email addresses")
        print("\nOptions:")
        print("  --output DIR        Output directory for files (default: current directory)")
        print("\nExample:")
        print('  python run_youtube_workflow.py "https://www.youtube.com/watch?v=..." "YOUTUBE_KEY" "APIFY_KEY" "user@example.com"')
        sys.exit(1)

    url = sys.argv[1]
    youtube_api_key = sys.argv[2]
    apify_api_key = sys.argv[3]

    # Optional arguments
    email_recipients = None
    output_dir = os.getcwd()

    for i in range(4, len(sys.argv)):
        if sys.argv[i] == '--output' and i + 1 < len(sys.argv):
            output_dir = sys.argv[i + 1]
        elif not sys.argv[i].startswith('--') and '@' in sys.argv[i]:
            email_recipients = sys.argv[i]

    # Find skills directory
    skills_dir = r'C:\Users\c\.claude\skills'
    template_path = os.path.join(skills_dir, 'youtube-summary', 'assets', 'summary_template.md')

    log("=== YouTube Workflow Automation Started ===")
    log(f"Video URL: {url}")

    # Step 1: Collect video data
    video_data = collect_video_data(url, youtube_api_key, apify_api_key, skills_dir)

    if not video_data.get('success'):
        log(f"Failed to collect video data: {video_data.get('error')}", 'ERROR')
        print(json.dumps(video_data, indent=2))
        sys.exit(1)

    log(f"✓ Video data collected: {video_data.get('video_info', {}).get('title', 'Unknown')}")

    # Step 2: Generate summary prompt
    summary_prompt = generate_summary_prompt(video_data, template_path)
    log(f"✓ Summary prompt generated ({len(summary_prompt)} characters)")

    # Step 3: Save output files
    files = save_output_files(video_data, summary_prompt, output_dir)
    log(f"✓ Output files saved to: {output_dir}")

    # Step 4: Email (optional)
    if email_recipients:
        email_result = send_email_smtp(
            email_recipients,
            f"YouTube 요약: {video_data.get('video_info', {}).get('title', 'Video')}",
            open(files['email'], 'r', encoding='utf-8').read()
        )

        if email_result.get('success'):
            log("✓ Email sent successfully")
        else:
            log(f"Email not sent: {email_result.get('error')}", 'WARN')
            log(f"Note: {email_result.get('note', '')}", 'INFO')

    # Final output
    log("=== Workflow Completed ===")

    output = {
        'success': True,
        'video_url': url,
        'video_title': video_data.get('video_info', {}).get('title'),
        'files': {
            'data': files['data'],
            'prompt': files['prompt'],
            'email_draft': files['email']
        },
        'next_steps': [
            f"1. Review the summary prompt: {files['prompt']}",
            "2. Copy the prompt and ask Claude to generate the summary",
            "3. Review and edit the generated summary",
            f"4. Send the email draft: {files['email']}"
        ]
    }

    print(json.dumps(output, indent=2, ensure_ascii=False))
    sys.exit(0)


if __name__ == '__main__':
    main()
