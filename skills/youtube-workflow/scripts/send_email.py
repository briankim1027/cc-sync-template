#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Email Sender for YouTube Workflow

Sends generated summaries via Gmail SMTP.
Requires Gmail App Password for authentication.
"""

import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# Fix Windows console encoding
if sys.platform == 'win32':
    import codecs
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')


def send_gmail(sender_email, sender_password, recipients, subject, body_html, attachments=None):
    """
    Send email via Gmail SMTP.

    Args:
        sender_email: Sender's Gmail address
        sender_password: Gmail App Password (not regular password)
        recipients: List of recipient email addresses
        subject: Email subject
        body_html: HTML body content
        attachments: Optional list of file paths to attach

    Returns:
        Dictionary with success status
    """
    try:
        # Create message
        msg = MIMEMultipart('mixed')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipients)

        # Attach HTML body
        html_part = MIMEMultipart('alternative')
        html_content = MIMEText(body_html, 'html', 'utf-8')
        html_part.attach(html_content)
        msg.attach(html_part)

        # Attach files
        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as f:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(f.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename= {os.path.basename(file_path)}'
                        )
                        msg.attach(part)

        # Connect to Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        server.send_message(msg)
        server.quit()

        return {
            'success': True,
            'message': f'Email sent successfully to {", ".join(recipients)}'
        }

    except smtplib.SMTPAuthenticationError:
        return {
            'success': False,
            'error': 'Authentication failed. Please check your Gmail App Password.',
            'help': 'Get an App Password at: https://myaccount.google.com/apppasswords'
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def main():
    """Main function for standalone email sending."""
    if len(sys.argv) < 6:
        print("Usage: python send_email.py <SENDER_EMAIL> <APP_PASSWORD> <RECIPIENTS> <SUBJECT> <HTML_FILE> [ATTACHMENTS...]")
        print("\nArguments:")
        print("  SENDER_EMAIL    Sender's Gmail address")
        print("  APP_PASSWORD    Gmail App Password")
        print("  RECIPIENTS      Comma-separated recipient emails")
        print("  SUBJECT         Email subject")
        print("  HTML_FILE       Path to HTML file for email body")
        print("  ATTACHMENTS     (Optional) Files to attach")
        print("\nExample:")
        print('  python send_email.py "sender@gmail.com" "app_password" "user1@example.com,user2@example.com" "Subject" "email.html" "attachment.pdf"')
        print("\nNote: Get Gmail App Password at https://myaccount.google.com/apppasswords")
        sys.exit(1)

    sender_email = sys.argv[1]
    app_password = sys.argv[2]
    recipients = [r.strip() for r in sys.argv[3].split(',')]
    subject = sys.argv[4]
    html_file = sys.argv[5]
    attachments = sys.argv[6:] if len(sys.argv) > 6 else []

    # Read HTML file
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            body_html = f.read()
    except Exception as e:
        print(f"Error reading HTML file: {e}", file=sys.stderr)
        sys.exit(1)

    # Send email
    result = send_gmail(sender_email, app_password, recipients, subject, body_html, attachments)

    if result['success']:
        print(result['message'])
        sys.exit(0)
    else:
        print(f"Error: {result['error']}", file=sys.stderr)
        if 'help' in result:
            print(f"Help: {result['help']}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
