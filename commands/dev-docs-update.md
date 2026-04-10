---
name: dev-docs-update
description: Update existing dev docs before context reset or at session end
---

# Dev Docs Update

Update existing dev documentation to capture current session progress before context reset.

## Instructions

When the user invokes `/dev-docs-update`:

### Step 1: Find Active Dev Docs
Look for directories under `dev/active/` in the current project.

If multiple tasks exist, ask which one to update.
If only one exists, update it automatically.

### Step 2: Update context.md

**Focus on the SESSION PROGRESS section:**

1. Read the current context file
2. Move completed items from "In Progress" to "Completed"
3. Add newly completed work to "Completed"
4. Update "In Progress" with current work
5. Add any new "Blockers"
6. Update the "Key Files" table with any new files
7. Add any new "Important Decisions"
8. Update "Quick Resume" instructions
9. Update the "Last Updated" date

### Step 3: Update tasks.md

1. Read the current tasks file
2. Check off completed tasks: `- [ ]` → `- [x]`
3. Add any new discovered tasks under "Discovered Tasks"
4. Update phase status indicators
5. Update the "Last Updated" date

### Step 4: Update plan.md (if scope changed)

Only if the scope or approach changed:
1. Update affected phases
2. Add new phases if discovered
3. Update risk assessment
4. Update the "Last Updated" date

### Step 5: Confirm

```
Dev docs updated: dev/active/[task-name]/

Updated:
- context.md: SESSION PROGRESS refreshed
- tasks.md: [N] tasks completed, [M] new tasks added
- plan.md: [updated/unchanged]

Safe to reset context. Resume by reading these files.
```

## Automatic Triggers

Consider suggesting `/dev-docs-update` when:
- Context window is getting large
- User mentions "ending session" or "taking a break"
- Major milestone is completed
- Before switching to a different task
