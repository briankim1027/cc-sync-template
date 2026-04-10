---
name: youtube-summary
description: Generate structured, learning-focused summaries of YouTube videos by combining metadata and captions. Creates comprehensive summaries following academic learning frameworks (Cornell Notes, Bloom's Taxonomy, Feynman Technique). Use when users request video summaries, learning notes, or structured analysis of YouTube content.
---

# YouTube Video Summary Generator

This skill generates structured, learning-focused summaries of YouTube videos by integrating video metadata and captions, following academic learning frameworks.

## When to Use This Skill

Use this skill when users:
- Request a summary or analysis of a YouTube video
- Want to create learning notes from educational videos
- Need structured breakdowns of video content
- Ask for key takeaways, insights, or concepts from videos
- Want to study or review video content efficiently

**Trigger phrases:**
- "Summarize this YouTube video"
- "Create learning notes from this video"
- "What are the key points in this video?"
- "Give me a structured summary of this video"
- "Help me understand and learn from this video"

## Summary Framework

This skill follows a comprehensive learning-focused framework that includes:

### 1. Top-Level Summary (5-Line Overview)
- One-sentence conclusion
- 3 core themes
- 3 key numbers/evidence points
- 2 application scenarios
- 3 inquiry questions

### 2. Structured Content Analysis
- **Key Themes**: Problem/context → Solution/argument → Evidence
- **Core Concepts**: Definition → How it works → Common misconceptions
- **Quantitative Insights**: Numbers with context, comparison, and limitations
- **Inquiry Questions**: Following Bloom's Taxonomy (Understand → Apply → Analyze → Create)

### 3. Timeline-Based Breakdown
- 3-7 segments with timestamps
- Each segment includes: theme, concept, evidence, takeaway, questions

### 4. Practical Application
- Do/Don't checklist
- Assumptions and risks
- Verification plan (optional)

## How to Use This Skill

### Step 1: Prepare Video Data

Run the bundled script `scripts/prepare_summary_data.py` to collect video information and captions:

```bash
python scripts/prepare_summary_data.py "<YOUTUBE_URL>" "<YOUTUBE_API_KEY>" "<APIFY_API_KEY>" [ACTOR_ID] [--output FILE]
```

**Example:**
```bash
python scripts/prepare_summary_data.py \
  "https://www.youtube.com/watch?v=dQw4w9WgXcQ" \
  "AIzaSy..." \
  "apify_api_..." \
  --output video_data.json
```

**With specific Apify Actor:**
```bash
python scripts/prepare_summary_data.py "URL" "YOUTUBE_KEY" "APIFY_KEY" "streamers/youtube-scraper"
```

The script will:
1. Fetch video metadata (title, duration, views, description) using youtube-info skill
2. Fetch video captions/transcript using youtube-captions skill
3. Combine data into a structured JSON format
4. Save to file (if --output specified) or print to stdout

### Step 2: Generate Summary with Claude

Once you have the video data, use it to generate a summary following the template:

1. **Read the summary template**: `assets/summary_template.md` provides the structure
2. **Review the summary guide**: `references/summary_guide.md` explains the methodology
3. **Request Claude to generate the summary** using this prompt:

```
I have YouTube video data (metadata + captions) and need a structured learning summary.

Video Data:
[Paste the JSON output from Step 1]

Please create a comprehensive learning-focused summary following the template in assets/summary_template.md.

Key requirements:
- Use the summary guide framework (references/summary_guide.md)
- Include all required sections
- Extract quantitative insights with context
- Create inquiry questions at multiple cognitive levels
- Organize by themes, not chronologically
- Focus on learning and application

Generate the summary in Markdown format.
```

### Step 3: Review and Refine

Use the quality checklist from the template:
- ✅ **Logic**: Claims → Evidence → Conclusions connected?
- ✅ **Evidence**: Numbers/conditions/ranges specified?
- ✅ **Learning**: Can you explain concepts in your own words?
- ✅ **Readability**: One idea per paragraph, no timeline overlap?

## Required Dependencies

This skill integrates two other skills:

1. **youtube-info**: For video metadata
   - Location: `C:\Users\c\.claude\skills\youtube-info\`
   - Required: YouTube Data API key

2. **youtube-captions**: For video transcripts
   - Location: `C:\Users\c\.claude\skills\youtube-captions\`
   - Required: Apify API key

Both skills must be installed for this skill to work.

## Output Structure

### JSON Output (from prepare_summary_data.py)

```json
{
  "success": true,
  "video_url": "https://...",
  "video_info": {
    "title": "Video Title",
    "channel_title": "Channel Name",
    "published_at": "2025-01-15T10:00:00Z",
    "duration": "00:15:30",
    "view_count": "1000000",
    "like_count": "50000",
    "description": "..."
  },
  "captions": {
    "success": true,
    "text": "Full transcript...",
    "timestamped": [
      {"start": 0, "duration": 2.5, "text": "..."}
    ]
  },
  "ready_for_summary": true
}
```

### Markdown Summary (generated by Claude)

The summary follows the template structure with:
- Executive summary (5 lines)
- Video metadata
- Structured analysis (themes, concepts, insights, questions)
- Timeline breakdown
- Application checklist
- Assumptions and risks

## Learning Framework Integration

This skill incorporates proven learning methodologies:

### Cornell Notes System
- Structured format with cues, notes, and summary
- Enables effective review and self-testing
- Organizes information hierarchically

### Bloom's Taxonomy
- Questions progress through cognitive levels:
  1. **Remember/Understand**: What was said?
  2. **Apply**: How do I use this?
  3. **Analyze**: Why does this work?
  4. **Evaluate**: What are limitations?
  5. **Create**: How can I extend this?

### Feynman Technique
- Explain concepts in simple terms
- Identify knowledge gaps
- Refine understanding through teaching

## Example Workflow

### Example 1: Educational Video Summary

```
User: "Summarize this machine learning tutorial: https://www.youtube.com/watch?v=..."

Assistant workflow:
1. Run: python scripts/prepare_summary_data.py "URL" "YOUTUBE_KEY" "APIFY_KEY" --output ml_video.json
2. Read ml_video.json
3. Generate summary following template:
   - Extract: 3 core ML concepts
   - Identify: Mathematical formulas and their meaning
   - Create: Application examples and practice questions
   - Organize: By concept, not chronologically
4. Present: Structured learning notes in Markdown
```

### Example 2: Business Presentation Summary

```
User: "Create notes from this startup pitch: https://www.youtube.com/watch?v=..."

Assistant workflow:
1. Prepare data with: python scripts/prepare_summary_data.py "URL" "YOUTUBE_KEY" "APIFY_KEY"
2. Focus summary on:
   - Business model and value proposition
   - Market size and opportunity (quantitative)
   - Competitive advantages
   - Financial projections and metrics
   - Risk factors and assumptions
3. Create Do/Don't checklist for entrepreneurs
```

### Example 3: Technical Talk Summary

```
User: "Help me learn from this conference talk on distributed systems"

Assistant workflow:
1. Collect data and save to file
2. Generate summary emphasizing:
   - Architecture patterns and trade-offs
   - Performance metrics with context
   - Implementation challenges
   - Design decisions and rationale
3. Create inquiry questions for deeper understanding:
   - Why this approach over alternatives?
   - What changes if scale increases 10x?
   - How would I adapt this to my system?
```

## Additional Resources

### Template Files
- **assets/summary_template.md**: Complete summary structure
- Use this as a guide when generating summaries

### Reference Documentation
- **references/summary_guide.md**: Comprehensive methodology guide
- Explains the three-expert collaboration approach
- Details quality checklist and best practices

## Error Handling

### No Captions Available
If captions cannot be retrieved:
- The script will still provide video metadata
- Summary will be limited to description and metadata analysis
- Suggest user enable captions or try different Apify Actor

### API Failures
- YouTube API: Video info fails → Use basic metadata from URL
- Apify API: Captions fail → Metadata-only summary
- Both fail: Provide clear error message with troubleshooting steps

### Long Videos
For videos longer than 60 minutes:
- Segment into 5-10 minute chunks
- Focus on key sections
- May require manual review of full transcript

## Quality Standards

Every summary should include:
- ✅ At least 3 quantitative insights with context
- ✅ Questions at multiple Bloom's taxonomy levels
- ✅ Clear evidence-to-conclusion connections
- ✅ Practical application scenarios
- ✅ Identified assumptions and limitations

## Notes

- Summary quality depends on caption availability and accuracy
- Auto-generated captions may have errors affecting analysis
- Very technical content may require domain knowledge for proper interpretation
- The template emphasizes learning over simple content reduction
- Summaries are optimized for review and knowledge transfer

## Integration with Other Skills

This skill orchestrates two other YouTube skills:

```
youtube-summary
    ↓
    ├─→ youtube-info (metadata)
    │     - Title, duration, views
    │     - Channel, publish date
    │     - Description
    │
    └─→ youtube-captions (transcript)
          - Full text
          - Timestamped segments
```

The combined data enables comprehensive, learning-focused summaries that go beyond simple transcription.
