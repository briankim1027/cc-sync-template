---
name: youtube-workflow
description: Complete automated workflow for YouTube video analysis. Takes a URL and automatically collects metadata, extracts captions, generates learning-focused summary prompts, and prepares email delivery. Orchestrates youtube-info, youtube-captions, and youtube-summary skills into a single automated pipeline. Use when users want end-to-end YouTube video summarization with minimal manual steps.
---

# YouTube Workflow Automation

This skill provides a complete automated workflow for YouTube video analysis, integrating three specialized skills into a seamless pipeline.

## When to Use This Skill

Use this skill when users:
- Want complete YouTube video analysis with minimal effort
- Need automated video summarization from URL to email
- Request "process this YouTube video end-to-end"
- Want to automate recurring video analysis tasks
- Need batch processing of multiple videos

## Workflow Architecture

```
youtube-workflow (Orchestrator)
    │
    ├─→ Step 1: youtube-info → Video metadata
    ├─→ Step 2: youtube-captions → Full transcript
    ├─→ Step 3: youtube-summary → Summary prompt generation
    ├─→ Step 4: File Output (JSON, Markdown, HTML)
    └─→ Step 5: Email Delivery (optional, Gmail SMTP)
```

## Required Dependencies

1. **youtube-info** → `C:\Users\c\.claude\skills\youtube-info\`
2. **youtube-captions** → `C:\Users\c\.claude\skills\youtube-captions\`
3. **youtube-summary** → `C:\Users\c\.claude\skills\youtube-summary\`

## How to Use This Skill

### Quick Start (Recommended)

**Step 1:** Prepare `.env` file:
```env
YOUTUBE_API_KEY=your_key_here
APIFY_API_KEY=your_key_here
EMAIL_RECIPIENTS=user@example.com
```

**Step 2:** Run workflow:
```bash
python scripts/run_workflow_from_env.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Manual Execution

```bash
python scripts/run_youtube_workflow.py \
  "YOUTUBE_URL" "YOUTUBE_API_KEY" "APIFY_API_KEY" "email@example.com" \
  --output "./summaries"
```

### Through Claude

Simply ask Claude to "Process this YouTube video" with the URL and it will execute the workflow.

## Output Files

| File | Format | Contents | Usage |
|------|--------|----------|-------|
| `{title}_{ts}_data.json` | JSON | Metadata, transcript, caption segments, status | Archive, reprocessing |
| `{title}_{ts}_prompt.md` | Markdown | Structured prompt for Claude with context | Copy to Claude for summary |
| `{title}_{ts}_email_draft.html` | HTML | Formatted email with video info | Send via Gmail or email client |

## Configuration

### Option 1: .env File (Recommended)

```env
# Required
YOUTUBE_API_KEY=your_key_here
APIFY_API_KEY=your_key_here

# Optional
EMAIL_RECIPIENTS=user1@example.com,user2@example.com
GMAIL_SENDER=sender@gmail.com
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
OUTPUT_DIR=./youtube_summaries
APIFY_ACTOR_ID=streamers/youtube-scraper
```

Use template: `assets/workflow_config_template.env`

### Option 2: Command Line Arguments

Pass all values directly as positional args.

### Option 3: Environment Variables

Set `YOUTUBE_API_KEY`, `APIFY_API_KEY`, `EMAIL_RECIPIENTS` in shell.

## Email Delivery

### Automatic Email (Gmail)

1. Get App Password: https://myaccount.google.com/apppasswords
2. Add `GMAIL_SENDER` and `GMAIL_APP_PASSWORD` to `.env`
3. Run: `python scripts/send_email.py "sender" "password" "recipient" "subject" "draft.html" "prompt.md"`

### Manual Email

Open the generated `email_draft.html` in browser and copy to your email client.

## Workflow Execution Flow

### Normal Flow
```
1. Collecting video data → youtube-info + youtube-captions
2. Generating summary prompt → Load template, build prompt
3. Saving output files → data.json, prompt.md, email_draft.html
4. Workflow completed
```

### Partial Success (No Captions)
Continues with metadata only, generates limited summary prompt.

### Failure Scenarios

| Error | Solution |
|-------|----------|
| youtube-info fails | Check YouTube API key, verify video is public, check quota |
| youtube-captions fails | Try different Apify Actor, check quota, video may have no captions |
| File save fails | Check permissions, ensure disk space |

## Advanced Usage

### Batch Processing

```bash
while IFS= read -r url; do
  python scripts/run_workflow_from_env.py "$url"
  sleep 10  # Respect API rate limits
done < video_urls.txt
```

### CI/CD Integration

See `references/workflow_guide.md` for GitHub Actions setup and CI/CD configuration.

## Error Handling

**Network Timeouts**: Default 300s, automatic retries, partial result fallback.
**API Failures**: YouTube API down → metadata from URL; Apify down → skip captions.
**File System**: Permission fallback, disk space handling, path length management.

## Performance

| Metric | Value |
|--------|-------|
| Video info | 2-5 seconds |
| Captions | 10-30 seconds (60-120s for >1hr videos) |
| Prompt generation | 1-2 seconds |
| **Total** | **15-40 seconds typical** |
| Disk per video | 50-500 KB |
| Memory | 50-100 MB during execution |

**API Quotas**: YouTube: 1 unit/video, Apify: 10-50 units/video.

## Best Practices

1. **API Key Management**: Use `.env`, add to `.gitignore`, rotate periodically, never commit to Git
2. **Output Organization**: Organize by date folders, archive old summaries
3. **Automation**: Schedule with cron, monitor API quotas, set up failure alerts
4. **Quality Control**: Review prompts before sending, verify caption accuracy

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "youtube-summary script not found" | Install youtube-summary skill, check path |
| "Captions not available" | Try different Apify Actor, continue with metadata-only |
| "Email sending failed" | Check Gmail App Password, verify recipients |
| "Timeout after 300 seconds" | Use `--timeout 600`, check network |

**Debug Mode**: `export DEBUG=1` before running.

## Additional Resources

- **references/workflow_guide.md**: Complete usage guide with CI/CD setup
- **assets/workflow_config_template.env**: Configuration template
- **Related Skills**: youtube-info, youtube-captions, youtube-summary
- YouTube Data API: https://developers.google.com/youtube/v3
- Apify Platform: https://apify.com

## Notes

- Designed for hands-off operation
- Manual intervention only for Claude summary generation
- Email delivery fully automated with Gmail App Password
- Scales to batch processing with minimal modifications
