# Apify API Reference for YouTube Caption Extraction

## Overview

Apify is a cloud platform for web scraping and automation. It provides "Actors" - pre-built automation tools that can be run via API.

### Key Concepts

- **Actor**: A serverless microservice that performs a specific task (e.g., YouTube caption extraction)
- **Run**: An execution instance of an Actor
- **Dataset**: Storage for Actor output data
- **API Token**: Authentication credential for API access

## Base URL
```
https://api.apify.com/v2
```

## Authentication

All API requests require an API token passed as a query parameter:
```
?token=YOUR_API_KEY
```

API keys are stored in `.env` as:
```
APIFY_API_KEY=apify_api_...
```

## Running an Actor

### Step 1: Start Actor Run

**Endpoint**: `POST /acts/{actorId}/runs`

**Request**:
```http
POST https://api.apify.com/v2/acts/simpleapi/youtube-video-subtitles-scraper/runs?token=YOUR_TOKEN
Content-Type: application/json

{
  "videoUrls": ["https://www.youtube.com/watch?v=VIDEO_ID"],
  "language": "en"
}
```

**Response**:
```json
{
  "data": {
    "id": "RUN_ID",
    "actId": "ACTOR_ID",
    "status": "RUNNING",
    "defaultDatasetId": "DATASET_ID",
    "startedAt": "2025-01-15T10:00:00.000Z"
  }
}
```

### Step 2: Check Run Status

**Endpoint**: `GET /actor-runs/{runId}`

**Request**:
```http
GET https://api.apify.com/v2/actor-runs/RUN_ID?token=YOUR_TOKEN
```

**Response**:
```json
{
  "data": {
    "id": "RUN_ID",
    "status": "SUCCEEDED",
    "defaultDatasetId": "DATASET_ID",
    "finishedAt": "2025-01-15T10:01:30.000Z"
  }
}
```

**Status Values**:
- `READY`: Waiting to start
- `RUNNING`: Currently executing
- `SUCCEEDED`: Completed successfully
- `FAILED`: Error occurred
- `ABORTED`: User cancelled
- `TIMED-OUT`: Exceeded time limit

### Step 3: Retrieve Results

**Endpoint**: `GET /datasets/{datasetId}/items`

**Request**:
```http
GET https://api.apify.com/v2/datasets/DATASET_ID/items?token=YOUR_TOKEN
```

**Response**:
```json
[
  {
    "videoUrl": "https://www.youtube.com/watch?v=VIDEO_ID",
    "subtitles": [
      {
        "start": 0.0,
        "duration": 2.5,
        "text": "Caption text here"
      }
    ]
  }
]
```

## YouTube Caption Actors

### 1. YouTube Video Subtitles Scraper
**Actor ID**: `simpleapi/youtube-video-subtitles-scraper`

**Input Parameters**:
```json
{
  "videoUrls": ["https://www.youtube.com/watch?v=..."],
  "language": "en"
}
```

**Features**:
- Supports multiple languages
- Auto-detects available captions
- Returns timestamped subtitles

**Output Structure**:
```json
{
  "videoUrl": "...",
  "subtitles": [
    {"start": 0, "duration": 2.5, "text": "..."}
  ]
}
```

### 2. YouTube Video Captions Scraper
**Actor ID**: `scrapearchitect/youtube-video-captions-scraper`

**Input Parameters**:
```json
{
  "videoUrls": ["https://www.youtube.com/watch?v=..."],
  "language": "en",
  "format": "json3"
}
```

**Supported Formats**:
- `json3`: JSON with timing data
- `vtt`: WebVTT subtitle format
- `srv1`, `srv2`, `srv3`: YouTube internal formats
- `ttml`: Timed Text Markup Language

### 3. YouTube Transcript Scraper
**Actor ID**: `xtech/youtube-transcript-scraper-pro`

**Features**:
- Multi-language support
- Auto-generated caption support
- Translation support

## Error Handling

### Common HTTP Status Codes

**400 Bad Request**:
```json
{
  "error": {
    "type": "INVALID_INPUT",
    "message": "Invalid input parameters"
  }
}
```

**401 Unauthorized**:
```json
{
  "error": {
    "type": "AUTHENTICATION_ERROR",
    "message": "Invalid API token"
  }
}
```

**404 Not Found**:
- Actor doesn't exist
- Run ID not found
- Dataset not found

**429 Too Many Requests**:
- Rate limit exceeded
- Wait before retrying

### Run Failures

**Actor Run Failed**:
- Video has no captions
- Video is private/deleted
- Network issues during scraping
- Actor timeout (usually 300 seconds)

**Check Actor logs**:
```http
GET https://api.apify.com/v2/actor-runs/RUN_ID/log?token=YOUR_TOKEN
```

## Best Practices

### 1. Polling Strategy

Wait 3-5 seconds between status checks:
```python
import time

while status != 'SUCCEEDED':
    time.sleep(3)
    # Check status
```

### 2. Timeout Handling

Set reasonable timeouts (recommended: 300 seconds):
```python
timeout = 300  # 5 minutes
start_time = time.time()

while time.time() - start_time < timeout:
    # Check status
```

### 3. Language Selection

Common language codes:
- `en`: English
- `ko`: Korean
- `ja`: Japanese
- `es`: Spanish
- `fr`: French
- `de`: German
- `zh`: Chinese

Use `auto` for automatic language detection.

### 4. Quota Management

- Free tier: 5,000 Actor compute units/month
- Monitor usage in Apify Console
- Implement retry logic for quota errors

## Caption Output Formats

### Timestamped Format
```json
{
  "captions": [
    {
      "start": 0.0,
      "duration": 2.5,
      "text": "First caption"
    },
    {
      "start": 2.5,
      "duration": 3.0,
      "text": "Second caption"
    }
  ]
}
```

### Plain Text Format
```
First caption Second caption Third caption...
```

### SRT Format
```
1
00:00:00,000 --> 00:00:02,500
First caption

2
00:00:02,500 --> 00:00:05,500
Second caption
```

## Troubleshooting

### No Captions Available
```json
{
  "error": "Video has no available captions"
}
```

**Solutions**:
- Check if video has manual or auto-generated captions
- Try different language codes
- Verify video is public and accessible

### Actor Timeout
```json
{
  "error": "Actor run timed out"
}
```

**Solutions**:
- Increase timeout parameter
- Try again (temporary network issues)
- Check Actor status page for incidents

### Rate Limiting
```json
{
  "error": "Rate limit exceeded"
}
```

**Solutions**:
- Wait before retrying (exponential backoff)
- Upgrade Apify plan for higher limits
- Batch requests efficiently

## API Limits

### Free Tier
- 5,000 compute units/month
- Max 100 concurrent runs
- 30-day data retention

### Rate Limits
- 30 requests/second per IP
- 200 requests/second per account

### Run Limits
- Max run duration: 24 hours (configurable)
- Max dataset size: 200 MB (free tier)

## Additional Resources

- Apify Documentation: https://docs.apify.com
- Actor Store: https://apify.com/store
- Python Client: https://docs.apify.com/api/client/python
- API Reference: https://docs.apify.com/api/v2

## Sources

- [API client for Python | Apify Documentation](https://docs.apify.com/api/client/python)
- [Running Actors | Platform | Apify Documentation](https://docs.apify.com/platform/actors/running)
- [Run Actor and retrieve data via API | Academy](https://docs.apify.com/academy/api/run-actor-and-retrieve-data-via-api)
- [YouTube Video Captions Scraper · Apify](https://apify.com/scrapearchitect/youtube-video-captions-scraper)
- [YouTube Video Subtitles Scraper · Apify](https://apify.com/simpleapi/youtube-video-subtitles-scraper)
