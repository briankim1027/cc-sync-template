---
name: social-media-orchestrator
description: Orchestrate multi-platform social media content generation by executing Instagram, LinkedIn, and Threads content creation skills in parallel from a single user input. Use when users need cohesive social media campaigns across multiple platforms simultaneously.
---

# Social Media Orchestrator

Unified workflow for generating platform-optimized social media content across Instagram, LinkedIn, and Threads from a single product/service description.

## Purpose

Streamline social media content creation by coordinating three specialized content generation skills in a single workflow. Transform one product/service description into three platform-specific, sales-optimized posts tailored to each platform's audience and format requirements.

## When to Use This Skill

Activate this skill when users request:
- Multi-platform social media content from a single input
- Simultaneous content for Instagram, LinkedIn, and Threads
- Cross-platform social media campaigns
- Consistent messaging across different social platforms
- Keywords: "all platforms", "social media campaign", "multi-platform", "Instagram + LinkedIn + Threads"

Example triggers:
- "Create social media posts for my new product across all platforms"
- "I need Instagram, LinkedIn, and Threads content for this launch"
- "Generate a multi-platform campaign for this service"

## Execution Workflow

### 1. Input Collection

Collect comprehensive product/service information from the user:
- Product/service name and description
- Target audience and key benefits
- Call-to-action (CTA) or promotional goal
- Optional: tone preference, specific hashtags, links

### 2. Parallel Skill Execution

Execute three content generation skills **concurrently** using parallel tool calls for maximum efficiency:

```
Skill Tool Calls (in single message):
├─ instagram-caption-creator [input]
├─ linkedin-sales-post-generator [input]
└─ threads-content-creator-kr [input]
```

**Critical**: Make all three Skill tool calls in a **single response message** to enable true parallel execution. Never call sequentially unless a skill fails.

### 3. Result Aggregation

Collect outputs from all three skills and structure them clearly by platform.

### 4. Error Handling

Handle individual skill failures gracefully:
- If 1-2 skills fail: Return successful results + error notification for failed platform(s)
- If all skills fail: Report comprehensive error and request user guidance
- Never abort entire workflow due to single skill failure

### 5. Output Presentation

Present results in structured format:

```markdown
# 🎯 Multi-Platform Social Media Content

## 📸 INSTAGRAM
[Instagram caption result]

## 💼 LINKEDIN
[LinkedIn post result]

## 🧵 THREADS (한국어)
[Threads content result]

---
💡 **Usage Tips**:
- Customize CTAs for each platform
- Review hashtags for platform relevance
- Adjust tone based on audience engagement patterns
```

## Advanced Usage

### Optional Parameters

Support customization through user preferences:
- **Tone**: professional, casual, enthusiastic, educational
- **Length**: short, medium, long (varies by platform constraints)
- **Focus**: product features, customer benefits, brand story
- **Language**: Korean/English mix for Threads, English for others

### Platform-Specific Optimization

Leverage each underlying skill's strengths:
- **Instagram**: Visual storytelling, emoji usage, hashtag strategy (instagram-caption-creator methodology)
- **LinkedIn**: Professional value proposition, industry insights (linkedin-sales-post-generator methodology)
- **Threads**: Conversational Korean tone, viral engagement tactics (threads-content-creator-kr methodology)

## Implementation Notes

**Efficiency**: Always use parallel execution pattern - this reduces total execution time by ~66% compared to sequential execution.

**Consistency**: While each platform receives optimized content, maintain consistent core messaging across all three outputs to ensure cohesive campaign narrative.

**Scalability**: Architecture supports adding additional platform skills (Twitter, Facebook, etc.) by extending parallel execution pattern.

## Example Interaction

**User Input**:
```
"Generate social media posts for my AI-powered fitness app that personalizes workout plans. Target audience is busy professionals aged 25-40. CTA is to download the free trial."
```

**Skill Execution**:
1. Invoke social-media-orchestrator skill
2. Execute 3 platform skills in parallel with identical input
3. Return structured multi-platform content package

**Expected Output**: Three platform-optimized posts maintaining consistent "AI fitness for busy professionals" messaging while adapting format, tone, and style for Instagram (visual/lifestyle), LinkedIn (professional value), and Threads (conversational Korean).
