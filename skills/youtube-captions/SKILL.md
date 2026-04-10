---
name: youtube-captions
description: Extract captions and subtitles from YouTube videos using Apify API. Supports both plain text and timestamped formats. Use when users request video transcripts, captions, or subtitles from YouTube URLs.
---

# YouTube Captions Extractor

This skill extracts captions and subtitles from YouTube videos using Apify's YouTube caption scraping Actors.

## When to Use This Skill

Use this skill when users:
- Request video transcripts or captions from YouTube
- Ask for subtitle text from a YouTube video
- Want to extract spoken content from YouTube videos
- Need timestamped caption data for analysis
- Ask about what's said in a YouTube video

**Trigger phrases:**
- "Get captions from this YouTube video"
- "Extract subtitles from this video"
- "What does this video say?"
- "Give me the transcript of this video"
- "Download subtitles from YouTube"

## Supported Features

- **Plain text extraction**: Full transcript without timestamps
- **Timestamped captions**: Captions with start time and duration
- **Multiple languages**: Auto-detect or specify language
- **Auto-generated captions**: Support for both manual and auto-generated subtitles

## How to Use This Skill

### Step 1: Extract Video ID from URL

Parse the YouTube URL to extract the video ID (same as youtube-info skill).

**Example:**
- URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- Video ID: `dQw4w9WgXcQ`

### Step 2: Get API Key

Retrieve the Apify API key from the `.env` file:
```bash
APIFY_API_KEY=apify_api_...
```

The user's environment should have this key configured. If not available, inform the user to set up the Apify API key.

### Step 3: Execute the Script

Run the bundled script `scripts/get_youtube_captions.py` with the YouTube URL and API key:

```bash
python scripts/get_youtube_captions.py "<YOUTUBE_URL>" "<APIFY_API_KEY>" [ACTOR_ID] [OPTIONS]
```

**Basic usage:**
```bash
python scripts/get_youtube_captions.py "https://www.youtube.com/watch?v=..." "apify_api_..."
```

**With specific Actor:**
```bash
python scripts/get_youtube_captions.py "URL" "API_KEY" "streamers/youtube-scraper"
```

**Options:**

- `ACTOR_ID`: (Optional) Specific Apify Actor to use for extraction
- `--plain-text`: Output only plain text without JSON structure
- `--no-timestamps`: Exclude timestamps from output

**Examples:**

```bash
# Get full JSON output with timestamps (uses default Actor)
python scripts/get_youtube_captions.py "https://www.youtube.com/watch?v=..." "API_KEY"

# Use specific Actor
python scripts/get_youtube_captions.py "URL" "API_KEY" "streamers/youtube-scraper"

# Get only plain text
python scripts/get_youtube_captions.py "URL" "API_KEY" --plain-text

# Get JSON without timestamps
python scripts/get_youtube_captions.py "URL" "API_KEY" --no-timestamps
```

### Step 4: Parse and Present Results

The script outputs JSON with the following structure:

**Success Response (with timestamps):**
```json
{
  "success": true,
  "video_id": "dQw4w9WgXcQ",
  "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "text": "Full transcript text...",
  "captions": [
    {
      "start": 0.0,
      "duration": 2.5,
      "text": "First caption segment"
    },
    {
      "start": 2.5,
      "duration": 3.0,
      "text": "Second caption segment"
    }
  ]
}
```

**Plain text output:**
```
Full transcript text with all captions concatenated...
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error description"
}
```

Present the captions to the user in a clear, readable format based on their request:
- For full transcript requests, show the `text` field
- For timestamped requests, format the `captions` array nicely
- For specific time ranges, filter the captions array

### Step 5: Handle Errors Gracefully

Common errors to handle:

**No Captions Available:**
- Video doesn't have captions/subtitles
- Captions are disabled by uploader
- Video is private or deleted

**API Issues:**
- Invalid Apify API key
- Quota exceeded (free tier: 5,000 compute units/month)
- Actor timeout (usually after 5 minutes)
- Network connectivity issues

**URL Issues:**
- Invalid YouTube URL format
- Video ID extraction failed

## Information Available

The skill provides:

### Full Transcript
Complete text of all captions concatenated together, useful for:
- Content analysis
- Text search
- Summary generation
- Translation

### Timestamped Captions
Individual caption segments with timing information:
- `start`: Start time in seconds
- `duration`: Duration in seconds
- `text`: Caption text

Useful for:
- Creating subtitle files
- Syncing with video playback
- Finding specific moments
- Time-based analysis

## Technical Details

### Apify Actor Used
Primary Actor: `simpleapi/youtube-video-subtitles-scraper`

**Why this Actor:**
- Reliable caption extraction
- Supports multiple languages
- Returns structured timestamped data
- Free tier friendly
- Well-maintained

**Alternative Actors:**
If the primary Actor fails, consider:
- `scrapearchitect/youtube-video-captions-scraper`: Supports multiple export formats
- `xtech/youtube-transcript-scraper-pro`: Multi-language and translation support

### Execution Time
- Typical run: 10-30 seconds
- Timeout: 300 seconds (5 minutes)
- Polling interval: 3 seconds

### API Rate Limits
- Apify free tier: 5,000 compute units/month
- Rate limit: 30 requests/second per IP
- Each caption extraction: ~10-50 compute units

## Additional Resources

For detailed Apify API information, consult `references/apify_api.md` which includes:
- Complete API reference
- Actor run workflow
- Error handling guidelines
- Quota management
- Best practices
- Troubleshooting guide

## Example Workflows

### Example 1: Basic Transcript Request
```
User: "Get the transcript from https://www.youtube.com/watch?v=dQw4w9WgXcQ"

1. Extract video ID: dQw4w9WgXcQ
2. Load Apify API key from .env
3. Execute: python scripts/get_youtube_captions.py "https://..." "API_KEY"
4. Present full transcript from 'text' field
```

### Example 2: Timestamped Captions
```
User: "I need the captions with timestamps from this video: https://..."

1. Extract video ID and fetch captions
2. Execute with default settings (includes timestamps)
3. Format and display captions array:
   [00:00 - 00:02] First caption
   [00:02 - 00:05] Second caption
   ...
```

### Example 3: Plain Text Only
```
User: "Just give me the text from this video, no timestamps"

1. Extract video ID
2. Execute: python scripts/get_youtube_captions.py "URL" "KEY" --plain-text
3. Display clean text output
```

### Example 4: Find Specific Content
```
User: "What does the video say about X at around 2 minutes?"

1. Extract full captions with timestamps
2. Filter captions where start time is around 120 seconds
3. Present relevant caption segments
```

## Error Recovery

### No Captions Available
**Response**: "This video doesn't have captions available. The video may have captions disabled, or they might be restricted."

### API Quota Exceeded
**Response**: "Apify API quota exceeded. You've used your monthly limit. Upgrade your Apify plan or wait until next month."

### Actor Timeout
**Response**: "Caption extraction timed out. This can happen with very long videos or temporary network issues. Please try again."

### Invalid API Key
**Response**: "Invalid Apify API key. Please check your .env file and ensure APIFY_API_KEY is set correctly."

## Notes

- The script uses only Python standard library (no external dependencies required except for Apify API)
- Caption extraction typically takes 10-30 seconds
- Auto-generated captions are supported but may have accuracy issues
- Language detection is automatic but can be specified if needed
- Very long videos (>3 hours) may take longer or timeout
- Private videos and age-restricted videos cannot be accessed
