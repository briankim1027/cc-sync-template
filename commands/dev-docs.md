---
name: dev-docs
description: Create structured dev documentation (plan/context/tasks) for complex tasks that survive context resets
---

# Dev Docs Generator

Create a three-file documentation structure for the current task to survive context resets.

## Instructions

When the user invokes `/dev-docs [task-description]`, do the following:

### Step 1: Determine Task Name
- Convert the task description to kebab-case
- Example: "implement user authentication" → `implement-user-authentication`

### Step 2: Create Directory
```
dev/active/[task-name]/
```

### Step 3: Create Three Files

#### File 1: `[task-name]-plan.md`
```markdown
# [Task Name] - Implementation Plan

**Created:** YYYY-MM-DD
**Last Updated:** YYYY-MM-DD
**Status:** In Progress

## Executive Summary
[What we're building and why - 2-3 sentences]

## Current State
[What exists now, what's the starting point]

## Proposed Future State
[What the end result should look like]

## Implementation Phases

### Phase 1: [Phase Name] (estimated effort)
- Task 1.1: [Specific task]
  - Acceptance: [How to verify]
- Task 1.2: [Specific task]
  - Acceptance: [How to verify]

### Phase 2: [Phase Name] (estimated effort)
...

## Risk Assessment
- Risk 1: [Description] → Mitigation: [Plan]

## Success Metrics
- [ ] [Measurable outcome 1]
- [ ] [Measurable outcome 2]
```

#### File 2: `[task-name]-context.md`
```markdown
# [Task Name] - Context

**Last Updated:** YYYY-MM-DD

## SESSION PROGRESS (YYYY-MM-DD)

### Completed
- (none yet)

### In Progress
- Starting Phase 1

### Blockers
- (none)

## Key Files
| File | Purpose | Status |
|------|---------|--------|
| [path] | [what it does] | [new/modified/existing] |

## Important Decisions
| Decision | Rationale | Date |
|----------|-----------|------|
| [what was decided] | [why] | YYYY-MM-DD |

## Technical Constraints
- [constraint 1]

## Quick Resume
To continue this task:
1. Read this file for current state
2. Check tasks file for what's next
3. Refer to plan for overall strategy
```

#### File 3: `[task-name]-tasks.md`
```markdown
# [Task Name] - Task Checklist

**Last Updated:** YYYY-MM-DD

## Phase 1: [Phase Name]
- [ ] Task 1.1: [description]
- [ ] Task 1.2: [description]

## Phase 2: [Phase Name]
- [ ] Task 2.1: [description]
- [ ] Task 2.2: [description]

## Discovered Tasks
(Tasks found during implementation)
- [ ] ...
```

### Step 4: Analyze Context
Before creating the files:
1. Read relevant source files to understand current state
2. Identify key files that will be affected
3. Break the task into logical phases
4. Estimate effort for each phase

### Step 5: Confirm
After creating the files, tell the user:
```
Dev docs created at: dev/active/[task-name]/
- [task-name]-plan.md      (strategic plan)
- [task-name]-context.md   (key decisions & progress)
- [task-name]-tasks.md     (checklist)

Update context.md frequently during implementation.
Use /dev-docs-update before context resets.
```

## When to Use
- Complex multi-step tasks (>2 hours)
- Tasks spanning multiple sessions
- Features with many moving parts
- Refactoring large systems

## When NOT to Use
- Simple bug fixes
- Single-file changes
- Quick updates
