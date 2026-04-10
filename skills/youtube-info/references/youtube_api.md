# YouTube Data API v3 Reference

## API Overview

The YouTube Data API v3 allows applications to retrieve video information, including metadata, statistics, and content details.

### Base URL
```
https://www.googleapis.com/youtube/v3/videos
```

### Authentication
Requires an API key passed as a query parameter:
```
?key=YOUR_API_KEY
```

## API Request Structure

### Required Parameters
- `part`: Comma-separated list of resource properties (snippet, statistics, contentDetails)
- `id`: Video ID
- `key`: API key

### Example Request
```
GET https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,contentDetails&id=dQw4w9WgXcQ&key=YOUR_API_KEY
```

## Response Structure

### Successful Response
```json
{
  "items": [
    {
      "id": "VIDEO_ID",
      "snippet": {
        "title": "Video Title",
        "description": "Video description",
        "channelTitle": "Channel Name",
        "channelId": "CHANNEL_ID",
        "publishedAt": "2009-10-25T06:57:33Z",
        "thumbnails": {
          "default": {"url": "...", "width": 120, "height": 90},
          "medium": {"url": "...", "width": 320, "height": 180},
          "high": {"url": "...", "width": 480, "height": 360},
          "standard": {"url": "...", "width": 640, "height": 480},
          "maxres": {"url": "...", "width": 1280, "height": 720}
        },
        "tags": ["tag1", "tag2"]
      },
      "statistics": {
        "viewCount": "1234567890",
        "likeCount": "12345678",
        "commentCount": "123456"
      },
      "contentDetails": {
        "duration": "PT3M33S",
        "caption": "true"
      }
    }
  ]
}
```

### Key Fields

#### snippet (Basic Metadata)
- `title`: Video title
- `description`: Video description (may be truncated)
- `channelTitle`: Channel name
- `channelId`: Unique channel identifier
- `publishedAt`: Publication timestamp (ISO 8601 format)
- `thumbnails`: Available thumbnail URLs in various resolutions
- `tags`: Video tags/keywords (if available)

#### statistics (Engagement Metrics)
- `viewCount`: Total view count
- `likeCount`: Total likes (may be hidden by uploader)
- `commentCount`: Total comments (may be disabled)

#### contentDetails (Content Information)
- `duration`: Video duration in ISO 8601 format (PT#M#S)
- `caption`: Whether captions are available ("true"/"false")

### Error Responses

#### 400 Bad Request
```json
{
  "error": {
    "code": 400,
    "message": "Invalid value for parameter 'id'",
    "errors": [...]
  }
}
```

#### 403 Forbidden
```json
{
  "error": {
    "code": 403,
    "message": "The request cannot be completed because you have exceeded your quota",
    "errors": [...]
  }
}
```

**Common causes:**
- Invalid API key
- API key not enabled for YouTube Data API v3
- Quota exceeded (default: 10,000 units/day)

#### 404 Not Found
Video does not exist, is private, or has been deleted. The API returns an empty items array.

## Duration Format

YouTube uses ISO 8601 duration format:
- `PT3M33S` = 3 minutes, 33 seconds
- `PT1H30M` = 1 hour, 30 minutes
- `PT45S` = 45 seconds
- `PT2H` = 2 hours

## Quota Costs

Each API request consumes quota units:
- Video list request: 1 unit per part parameter

Default quota: 10,000 units/day

## Common Issues

### Video Not Found
The API returns `items: []` when:
- Video ID is invalid
- Video is private
- Video has been deleted
- Video is age-restricted (requires authentication)

### Missing Statistics
Some statistics may be unavailable:
- `likeCount`: Hidden if uploader disabled like counts
- `commentCount`: 0 or missing if comments are disabled

### Caption Availability
The `caption` field only indicates if captions exist, not whether they're auto-generated or manually created. To retrieve actual captions, use the Captions API (separate endpoint).

## Best Practices

1. **Cache Results**: Video metadata doesn't change frequently
2. **Handle Quota Limits**: Implement exponential backoff for 403 errors
3. **Validate Video IDs**: Check format before making API calls
4. **Handle Missing Data**: Statistics may be null or hidden
5. **Error Handling**: Always check for error responses and empty items arrays

## API Key Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable YouTube Data API v3
4. Create credentials (API Key)
5. Restrict API key to YouTube Data API v3 for security
6. Store API key in `.env` file as `YOUTUBE_API_KEY`
