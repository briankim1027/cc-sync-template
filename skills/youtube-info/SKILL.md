---
name: youtube-info
description: Extract video ID from YouTube URLs and fetch detailed video information (title, description, channel, views, likes, captions) using YouTube Data API v3. Use when users provide YouTube links and request video metadata, statistics, or caption availability.
---

# YouTube Video Info Fetcher

This skill extracts video IDs from YouTube URLs and retrieves comprehensive video information using the YouTube Data API v3.

## When to Use This Skill

Use this skill when users:
- Provide YouTube URLs and request video information
- Ask about video metadata (title, description, channel, publication date)
- Request video statistics (views, likes, comments)
- Inquire about caption/subtitle availability
- Need thumbnail URLs for video images
- Want to analyze or extract data from YouTube videos

**Trigger phrases:**
- "Get info about this YouTube video"
- "What's the title of this video?"
- "How many views does this have?"
- "Does this video have captions?"
- "Tell me about this YouTube link"

## Supported URL Format

The skill currently supports the standard YouTube URL format:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtube.com/watch?v=VIDEO_ID`
- `http://www.youtube.com/watch?v=VIDEO_ID`
- `https://m.youtube.com/watch?v=VIDEO_ID`

## How to Use This Skill

### Step 1: Extract Video ID from URL

Parse the YouTube URL to extract the video ID. The video ID is the value of the `v` query parameter.

**Example:**
- URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- Video ID: `dQw4w9WgXcQ`

### Step 2: Get API Key

Retrieve the YouTube API key from the `.env` file:
```bash
YOUTUBE_API_KEY=YOUR_API_KEY
```

The user's environment should have this key configured. If not available, inform the user to set up the API key.

### Step 3: Execute the Script

Run the bundled script `scripts/get_youtube_info.py` with the YouTube URL and API key:

```bash
python scripts/get_youtube_info.py "<YOUTUBE_URL>" "<API_KEY>"
```

**Example:**
```bash
python scripts/get_youtube_info.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "AIzaSyAfbll6E84_2Edwk5xuLzRLpN0DTvWKVoY"
```

### Step 4: Parse and Present Results

The script outputs JSON with the following structure:

**Success Response:**
```json
{
  "success": true,
  "video_id": "dQw4w9WgXcQ",
  "title": "Video Title",
  "description": "Video description...",
  "channel_title": "Channel Name",
  "channel_id": "UC...",
  "published_at": "2009-10-25T06:57:33Z",
  "thumbnails": {...},
  "view_count": "1234567890",
  "like_count": "12345678",
  "comment_count": "123456",
  "duration": "PT3M33S",
  "caption": "true",
  "tags": ["tag1", "tag2"]
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error description"
}
```

Present the information to the user in a clear, readable format. Highlight key information based on the user's specific request.

### Step 5: Handle Errors Gracefully

Common errors to handle:
- **Invalid URL format**: Inform user and request a valid YouTube URL
- **Video not found**: Video may be private, deleted, or invalid ID
- **API quota exceeded**: YouTube Data API has daily quota limits
- **Invalid API key**: Check `.env` configuration or API key validity
- **Network errors**: Connection issues or API unavailability

## Information Available

The skill provides access to:

### Basic Metadata
- Video title
- Video description
- Channel name and ID
- Publication date
- Video tags

### Statistics
- View count
- Like count (may be hidden by uploader)
- Comment count (may be 0 if disabled)

### Content Details
- Video duration (ISO 8601 format: PT3M33S)
- Caption availability (true/false)
- Thumbnail URLs (default, medium, high, standard, maxres)

## Additional Resources

For detailed API information, consult `references/youtube_api.md` which includes:
- Complete API response structure
- Error handling guidelines
- Quota information and best practices
- Duration format explanation
- Common issues and solutions

## Example Workflows

### Example 1: Basic Video Info Request
```
User: "Get info about https://www.youtube.com/watch?v=dQw4w9WgXcQ"

1. Extract video ID: dQw4w9WgXcQ
2. Load API key from .env
3. Execute: python scripts/get_youtube_info.py "https://..." "API_KEY"
4. Present formatted results:
   Title: [Video Title]
   Channel: [Channel Name]
   Views: [View Count]
   Published: [Date]
   Duration: [Duration]
   Captions: [Available/Not Available]
```

### Example 2: Specific Statistic Request
```
User: "How many views does this video have? https://www.youtube.com/watch?v=..."

1. Extract video ID and fetch info
2. Focus response on view_count field
3. Present: "This video has [X] views"
```

### Example 3: Caption Check
```
User: "Does this video have subtitles? https://www.youtube.com/watch?v=..."

1. Extract video ID and fetch info
2. Check caption field
3. Present: "Yes, captions are available" or "No captions available"
```

## Notes

- The script uses only Python standard library (no external dependencies required)
- API responses are cached by the script only for the duration of execution
- Video statistics are current at the time of the API call
- Some fields may be unavailable if the uploader has hidden them (e.g., like counts)
- For caption content retrieval, a separate API endpoint is required (not included in this skill)
