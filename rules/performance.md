# Performance & Context Management Rules

**Purpose**: Optimize Claude Code performance and manage context window effectively.

---

## 🪟 Context Window Management

### The Context Window Problem

**Your token budget:**

- Base context window: **200,000 tokens**
- With 25 MCPs active: **~70,000 tokens** 😱
- With 10 MCPs active: **~150,000 tokens** ✅

### Critical Rule: MCP Server Limits

> [!IMPORTANT]
> **Never activate more than 10 MCP servers per project**

**Global Configuration:**

- 20-30 MCP servers configured is fine
- Keep **under 10 enabled** per project
- Under 80 total tools active

---

## 🔧 MCP Server Management

### Categorize Your MCPs

**Essential (Always Active):**

```json
{
  "mcpServers": {
    "filesystem": {},
    "memory": {},
    "github": {}
  }
}
```

**Development Tools (Project-Specific):**

```json
{
  "mcpServers": {
    "sequential-thinking": {},
    "playwright": {},
    "convex": {}
  }
}
```

**Search & Research (On-Demand):**

```json
{
  "mcpServers": {
    "tavily-mcp": {},
    "brave-search": {},
    "firecrawl": {}
  }
}
```

**Special Purpose (Rarely Used):**

```json
{
  "mcpServers": {
    "figma": {},
    "notion": {},
    "slack": {},
    "supabase": {}
  }
}
```

### Per-Project MCP Configuration

**Create `CLAUDE.md` in each project:**

```markdown
# Project: E-commerce Platform

## Disabled MCPs

disabledMcpServers:

- slack
- notion
- figma
- everart
- elevenlabs
- hyperbrowser
- puppeteer
- apify
- codex
- shrimp-task-manager
- taskmaster-ai
- magic
- mcp-youtube
- supabase

## Active MCPs (9)

- filesystem (essential)
- memory (essential)
- github (essential)
- sequential-thinking (development)
- playwright (testing)
- convex (database)
- tavily-mcp (research)
- brave-search (research)
- firecrawl (web scraping)

## Project Context

Full-stack e-commerce platform built with Next.js, using Convex for backend.
Requires browser testing with Playwright for E2E tests.
```

### Dynamic MCP Activation

**Enable MCP only when needed:**

```bash
# Working on API → enable API tools
# Working on UI → enable Figma, design tools
# Working on docs → enable Notion
# Need web scraping → enable Puppeteer, Firecrawl
```

---

## 🎯 Model Selection

### Choose the Right Model

**opus** - Complex reasoning, critical work

- Architecture decisions
- Security reviews
- Complex bug fixes
- TDD implementation
- Critical code reviews

**sonnet** - Balanced performance (default)

- General development
- Feature implementation
- Refactoring
- Documentation
- Most day-to-day tasks

**haiku** - Fast, simple tasks

- Simple edits
- Formatting
- Quick questions
- File renaming
- Basic analysis

### Model Selection in Agent Definitions

```markdown
---
name: security-engineer
model: opus # Critical security work
---

---

name: frontend-engineer
model: sonnet # General development

---

---

name: formatter
model: haiku # Simple formatting

---
```

---

## 📦 Token Optimization Strategies

### 1. Strategic File Viewing

**❌ DON'T:**

```typescript
// View entire 2000-line file
view_file("src/app/page.tsx"); // Wastes tokens
```

**✅ DO:**

```typescript
// View specific sections
view_file('src/app/page.tsx', startLine: 100, endLine: 200)

// Use grep to find relevant code
grep_search('function handleSubmit', 'src/')
```

### 2. Efficient Code Search

**Use targeted searches:**

```bash
# ✅ Specific search
grep_search('interface User', 'src/types/')

# ❌ Broad search (too many results)
grep_search('user', 'src/')
```

### 3. Incremental File Viewing

**View file outline first:**

```typescript
// 1. Get file outline
view_file_outline("src/components/UserProfile.tsx");

// 2. View only needed sections
// Based on outline, identify specific functions/classes to view
```

---

## 🗜️ Context Compression Techniques

### 1. Archive Old Conversations

**Regularly archive:**

- Completed features
- Resolved bugs
- Old explorations

**Extract learnings before archiving:**

- Save patterns to `LEARNINGS.md`
- Document decisions
- Update project docs

### 2. Session Boundaries

**Start fresh sessions for:**

- New features
- Different domains
- After long debugging sessions

**Before starting new session:**

- Extract important patterns
- Update documentation
- Save state in `CLAUDE.md`

### 3. Strategic Compaction

**Use `/learn` command to extract and compress:**

```bash
# Extract pattern from current session
/learn Extract the authentication middleware pattern

# This adds to LEARNINGS.md and reduces context needed in future
```

### 4. Reference External Docs

**Instead of including full docs:**

```markdown
# ❌ DON'T paste entire documentation

# ✅ DO reference specific sections

See API authentication docs: [link]
Relevant section: "OAuth Flow" (pages 12-15)
```

---

## 📊 Monitor Context Usage

### Check Context Window

**Indicators of context pressure:**

- Slower responses
- Truncated outputs
- "Context too long" errors
- Forgetting earlier conversation

**When this happens:**

1. Review active MCPs → disable unused
2. Start new session
3. Extract learnings
4. Compress project context

### Tools to Monitor

```bash
# Check MCP count
cat ~/.claude/settings.json | grep -c '"command"'

# List active MCPs
grep -A 1 '"mcpServers"' ~/.claude/settings.json
```

---

## 🚀 Performance Optimization

### 1. Lazy Loading

**Load resources only when needed:**

```typescript
// ✅ GOOD - Lazy load heavy components
const HeavyComponent = lazy(() => import("./HeavyComponent"));

// ✅ GOOD - Conditional MCP activation
if (needsWebScraping) {
  // Activate Puppeteer
}
```

### 2. Caching Strategies

**Cache frequently used data:**

```typescript
// Cache API responses
const cache = new Map();

async function fetchUser(id: string) {
  if (cache.has(id)) {
    return cache.get(id);
  }

  const user = await api.getUser(id);
  cache.set(id, user);
  return user;
}
```

### 3. Efficient Prompts

**Structure for cacheability:**

```markdown
# ✅ GOOD - Stable, cacheable prefix

System: You are a senior developer...
Project context: [stable project info]
Current task: [specific task]

# ❌ BAD - Everything changes each time

Here's what I need today with all the context mixed together...
```

---

## 🎛️ Configuration Best Practices

### Global Settings

**`~/.claude/settings.json` - Global defaults:**

```json
{
  "model": "sonnet", // Default model
  "mcpServers": {
    // Configure all MCPs here
    // But disable most per-project
  }
}
```

### Project Settings

**Project `CLAUDE.md` - Project overrides:**

```markdown
# Override model for this project

model: opus # This project needs more reasoning

# Disable most MCPs

disabledMcpServers: [...]

# Project-specific context

[Keep minimal, focused context]
```

---

## 📈 Performance Metrics

### Track Performance

**Monitor:**

- Response time
- Context window usage
- MCP tool usage
- Session length

**Optimize based on:**

- Which MCPs are rarely used → disable
- Which tasks take longest → use faster model or optimize prompt
- When context fills up → start new session sooner

---

## ✅ Performance Checklist

Before each session:

- [ ] Check active MCPs (should be ≤10)
- [ ] Review `disabledMcpServers` in project `CLAUDE.md`
- [ ] Select appropriate model (opus/sonnet/haiku)
- [ ] Clear model (sonnet) for general tasks

During session:

- [ ] Use targeted file viewing
- [ ] Use grep for specific searches
- [ ] Extract learnings regularly
- [ ] Monitor response times

After session:

- [ ] Extract important patterns
- [ ] Update `LEARNINGS.md`
- [ ] Archive if session was long
- [ ] Document decisions in project docs

---

## 🎯 Quick Reference

### MCP Server Count Guidelines

| Project Type     | Essential | Dev Tools | Search | Special | Total |
| ---------------- | --------- | --------- | ------ | ------- | ----- |
| **Web App**      | 3         | 3         | 2      | 1       | **9** |
| **API Only**     | 3         | 2         | 2      | 0       | **7** |
| **Data Science** | 3         | 2         | 2      | 2       | **9** |
| **Mobile**       | 3         | 3         | 1      | 2       | **9** |

### Model Selection Quick Guide

| Task Type           | Model  | Reason             |
| ------------------- | ------ | ------------------ |
| Architecture design | opus   | Complex reasoning  |
| Security review     | opus   | Critical decisions |
| General coding      | sonnet | Balanced           |
| Refactoring         | sonnet | Balanced           |
| Documentation       | sonnet | Balanced           |
| Simple edits        | haiku  | Fast               |
| Formatting          | haiku  | Fast               |

### Context Window Indicators

| Tokens Used | Status      | Action               |
| ----------- | ----------- | -------------------- |
| < 50k       | 🟢 Healthy  | Continue             |
| 50k - 100k  | 🟡 Moderate | Monitor              |
| 100k - 150k | 🟠 High     | Consider new session |
| > 150k      | 🔴 Critical | Start new session    |

---

## 📚 Resources

- [MCP Server Directory](https://github.com/modelcontextprotocol/servers)
- [Claude Context Window Docs](https://docs.anthropic.com/claude/docs)
- Token optimization techniques in Longform Guide

---

**Remember**: Performance optimization is continuous. Monitor, measure, and adjust based on your specific needs.
