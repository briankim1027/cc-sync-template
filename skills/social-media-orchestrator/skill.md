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

**CRITICAL**: Generate THREE separate markdown files instead of a single combined document.

## File Generation Strategy

Upon execution, create three individual files in the user's current working directory:

1. `instagram_[topic-slug].md` - Instagram content with 3 caption versions
2. `linkedin_[topic-slug].md` - LinkedIn professional post
3. `threads_[topic-slug].md` - Threads Korean-language content

**Naming Convention:**
- Extract key topic words and create a slug (lowercase, hyphenated)
- Example: "나만의 vibecoding app 만들기" → `vibecoding`
- Remove special characters, keep only alphanumeric and hyphens

## File Generation Workflow

```
User Input → Parse Topic → Generate Slug → Create 3 Files in Parallel
├─ Write instagram_[slug].md
├─ Write linkedin_[slug].md
└─ Write threads_[slug].md
```

## Structured Output Format

### Template 1: `instagram_[slug].md`

```markdown
# Instagram 게시물: [Topic Name]

**생성일**: [YYYY-MM-DD]
**타겟 오디언스**: [Target Audience]

---

## CAPTION VERSION A: Storytelling Approach

[Hook with personal connection]

[Body paragraphs with emotional journey]

[Natural product integration]

[CTA]

---

**HASHTAGS:**
[5-10 relevant hashtags]

---

**NOTES:**
- **Target Audience**: [specific audience]
- **Best For**: [use case]
- **Key Strength**: [unique selling point]

---

## CAPTION VERSION B: Value-First Approach

[Educational hook]

[Problem-solution framework]

[Data/benefits]

[CTA]

---

**HASHTAGS:**
[5-10 relevant hashtags]

---

**NOTES:**
- **Target Audience**: [specific audience]
- **Best For**: [use case]
- **Key Strength**: [unique selling point]

---

## CAPTION VERSION C: Direct Response Approach

[Bold hook]

[Problem agitation]

[Solution with urgency]

[Strong CTA]

---

**HASHTAGS:**
[5-10 relevant hashtags]

---

**NOTES:**
- **Target Audience**: [specific audience]
- **Best For**: [use case]
- **Key Strength**: [unique selling point]

---

## 📊 Instagram 최적화 팁

### 최적 게시 시간
- **평일**: [specific times based on audience]
- **주말**: [specific times]

### 포맷 활용 옵션
- **Stories**: [specific tactics]
- **Reels**: [video ideas]
- **Carousel**: [multi-image concepts]

### 참여 유도 전략
- [Engagement tactic 1]
- [Engagement tactic 2]
- [Engagement tactic 3]

### 버전 선택 가이드
- **Version A**: [when to use]
- **Version B**: [when to use]
- **Version C**: [when to use]

---

## 📈 성과 측정 지표

### 추적해야 할 KPI
- **Engagement Rate**: 목표 5-8%
- **Saves**: 목표 15-20%
- **Profile Visits**: 목표 10-15%
- **Link Clicks**: [tracking method]
- **Story Engagement**: [metrics to watch]

### 성공 벤치마크
- [Benchmark 1]
- [Benchmark 2]
- [Benchmark 3]
```

---

### Template 2: `linkedin_[slug].md`

```markdown
# LinkedIn 게시물: [Topic Name]

**생성일**: [YYYY-MM-DD]
**타겟 오디언스**: [Target Audience]

---

## 게시물 본문

[Professional hook]

[Problem/background context]

[Solution introduction with key features]
• Feature 1
• Feature 2
• Feature 3

[Results/proof with data]

[Value proposition]

[Engagement CTA]

[Professional hashtags]

---

## 📊 LinkedIn 최적화 팁

### 최적 게시 시간
- **화-목 오전**: [specific times]
- **점심시간**: [specific times]
- **피해야 할 시간**: [times to avoid]

### 참여 전략
- **게시 후 30분**: [specific actions]
- **관련 그룹 공유**: [where to share]
- **후속 콘텐츠**: [follow-up ideas]
- **댓글 질 향상**: [engagement techniques]

### 전문성 포지셔닝
- **연결 주제**: [related topics]
- **업계 트렌드**: [trends to leverage]
- **권위 구축**: [credibility tactics]

### 네트워크 타겟팅
- **직접 타겟**: [specific roles]
- **간접 영향**: [secondary audience]
- **멘션 전략**: [who to tag]
- **연결 확장**: [networking tactics]

---

## 📈 성과 측정 지표

### 추적해야 할 KPI

**노출 및 도달**
- **Post Impressions**: 목표 [range]
- **Unique Viewers**: [percentage]
- **Follower/Non-follower Ratio**: [metric]

**참여 지표**
- **Engagement Rate**: 목표 3-5%
- **Comment Quality**: [quality indicators]
- **Shares**: [target number]

**전환 지표**
- **Connection Requests**: [target]
- **Profile Views**: 목표 5-10%
- **InMail**: [business inquiries]

### 성공 벤치마크
- [Benchmark 1]
- [Benchmark 2]
- [Benchmark 3]
```

---

### Template 3: `threads_[slug].md`

```markdown
# Threads 게시물: [Topic Name]

**생성일**: [YYYY-MM-DD]
**타겟 오디언스**: [Target Audience]
**톤**: 친근한 반말

---

## 게시물 본문

[친근한 hook with 이모지]

[공감 유도 본문]

[제품 자연스럽게 소개]

[개인 경험 공유]

[댓글 유도 질문]

[3-5개 해시태그]

---

## 📊 Threads 최적화 팁

### 최적 게시 시간 (한국 기준)
- **평일 점심**: 12:00-13:30
- **평일 퇴근**: 18:00-20:00
- **주말 오전**: 10:00-12:00
- **피해야 할 시간**: [times to avoid]

### 골든 30분 전략
[First 30 minutes action plan]

### 참여 극대화 전략
- **양자택일 질문**: [examples]
- **개인 경험 유도**: [tactics]
- **밈 연계**: [ideas]

### 시리즈 콘텐츠 아이디어
- **Day 1**: [topic]
- **Day 2**: [topic]
- **Day 3**: [topic]

---

## 📈 성과 측정 지표

### 핵심 KPI

**참여율 지표**
- **Reply Rate**: 목표 8-12%
- **Repost Count**: 목표 5-8%
- **Like Rate**: 목표 15-20%

**알고리즘 성과**
- **First 30-Min Engagement**: 60-70%
- **Engagement Velocity**: [metric]
- **Conversation Depth**: [target]

**성장 지표**
- **Follow Conversion**: 2-5%
- **Profile Visits**: 8-12%
- **Saves**: [percentage]

### 성공 벤치마크
- [Benchmark 1]
- [Benchmark 2]
- [Benchmark 3]
```

---

## File Generation Best Practices

**After creating files:**
1. ✅ Confirm all 3 files were created successfully
2. ✅ Provide file paths to user
3. ✅ Give brief summary of what's in each file
4. ✅ Suggest next steps (review, customize, post)

**Quality assurance:**
- Each file must be self-contained and complete
- Cross-reference platform strategies where relevant
- Include platform-specific best practices
- Provide actionable metrics and benchmarks

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

### User Input:
```
"나만의 vibecoding app 만들기를 주제로 소셜미디어 게시물 만들어줘"
```

### Skill Execution Process:
1. **Parse Input**: Extract topic (vibecoding app), create slug (`vibecoding`), infer target (developers)
2. **Parallel Execution**: Invoke instagram-caption-creator, linkedin-sales-post-generator, threads-content-creator-kr simultaneously
3. **File Generation**: Create 3 separate markdown files using Write tool
4. **Confirmation**: Report successful file creation to user

### Expected Output - File Creation:

**Files Created:**
```
✅ instagram_vibecoding.md
✅ linkedin_vibecoding.md
✅ threads_vibecoding.md
```

**User Response:**
```
완료! 3개의 마크다운 파일을 현재 프로젝트 폴더에 생성했어요 📝

## 생성된 파일:

1. **instagram_vibecoding.md**
   - 3가지 캡션 버전 (Storytelling, Value-First, Direct Response)
   - 각 버전별 타겟, 용도, 강점 분석
   - 최적화 팁, 성과 측정 지표

2. **linkedin_vibecoding.md**
   - 전문적인 포스트 본문
   - 참여 전략, 네트워크 타겟팅
   - 고급 활용 전략, A/B 테스트 아이디어

3. **threads_vibecoding.md**
   - 한국어 친근한 반말 톤
   - 골든 30분 전략
   - 바이럴 팁, 크로스 플랫폼 연계

각 파일은 독립적으로 사용 가능하며, 플랫폼별 최적화 가이드가 포함되어 있습니다.
```

### File Content Structure:

**instagram_vibecoding.md includes:**
- 3 caption variations with different strategic approaches
- Platform-specific hashtags for each version
- Target audience and use case notes
- Instagram optimization tips (posting times, format options, engagement tactics)
- Performance metrics and benchmarks

**linkedin_vibecoding.md includes:**
- Professional post with problem-solution framework
- Data-driven results and value proposition
- LinkedIn optimization tips (posting times, engagement strategy)
- Network targeting and professional positioning guidance
- Success metrics and KPIs

**threads_vibecoding.md includes:**
- Korean-language casual content with conversational tone
- Threads optimization tips (golden 30 minutes, posting times)
- Engagement maximization strategies
- Series content ideas
- Algorithm-focused performance metrics

### Key Features Demonstrated:
- ✅ **Separate Files**: Each platform gets its own complete, self-contained file
- ✅ **Consistent Naming**: Clear, predictable file naming convention
- ✅ **Complete Content**: Each file includes full content + optimization guidance
- ✅ **Platform-Adapted**: Tone, structure, and strategies tailored to each platform
- ✅ **Immediate Usability**: Files ready to use without additional editing
