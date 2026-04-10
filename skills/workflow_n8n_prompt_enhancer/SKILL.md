---
name: n8n-prompt-enhancer
description: Transform vague workflow automation requests into comprehensive, production-ready n8n workflow prompts. Use when users provide simple or incomplete workflow descriptions (e.g., "I need an email automation" or "send slack messages when customers sign up") that need to be enhanced with detailed trigger configuration, node sequences, data transformations, and error handling specifications.
---

# N8N Prompt Enhancer

## Overview

This skill transforms brief, vague workflow automation requests into comprehensive, structured n8n workflow prompts that AI agents can use to build production-ready automation workflows. The skill adds essential details including trigger configuration, node sequencing, data transformation logic, error handling strategies, and testing checklists.

## When to Use This Skill

Activate this skill when users request n8n workflow automation with:
- Simple descriptions lacking technical detail ("I need email automation")
- Missing critical components (no trigger, error handling, or data flow specified)
- Vague automation goals without implementation specifics
- Requests containing keywords: workflow, automation, n8n, trigger, send, notify, integrate

**Do NOT use** for:
- Already detailed workflow specifications with complete node sequences
- Non-automation tasks (general programming, data analysis, etc.)
- Other automation platforms (Zapier, Make.com, etc.)

## Transformation Workflow

### Step 1: Analyze the User Request

Extract key information from the vague request:
- **Primary action**: What needs to happen? (send email, post to Slack, update database)
- **Trigger event**: What starts the workflow? (webhook, schedule, manual, form submission)
- **Data sources**: Where does data come from?
- **Recipients/targets**: Where does data go?

### Step 2: Apply Structured Template

Transform the request using the structured markdown template from `assets/workflow_template.md`:

**Required Sections:**
1. **Workflow Objective** - Clear statement of what the workflow accomplishes
2. **Trigger Configuration** - Detailed trigger type and expected data format
3. **Node Sequence & Logic** - Step-by-step workflow with specific n8n nodes
4. **Data Transformation** - Input/output formats and transformation logic
5. **Error Handling** - Retry strategies, fallbacks, and error notifications
6. **Testing Checklist** - Validation steps for workflow testing

### Step 3: Enhance with n8n Best Practices

Reference `references/n8n_nodes.md` and `references/workflow_patterns.md` to:
- Select appropriate n8n nodes for each step
- Apply common workflow patterns (conditional routing, data enrichment, etc.)
- Include realistic data transformation expressions
- Add production-grade error handling from `references/error_handling.md`

### Step 4: Add Placeholders for Clarification

Use `[specify...]` or `[choose...]` placeholders for details that require user input:
- `[specify use case: customer onboarding/order confirmation/weekly newsletter]`
- `[sender email]`
- `[Google Sheets/Database/Slack]`

Leave these placeholders for the AI agent to discuss with the user during implementation.

## Example Transformations

### Example 1: Simple Email Request

**Input:**
```
"I need an email automation."
```

**Output:**
```markdown
# N8N Workflow: Email Automation System

## Workflow Objective
Create an automated email workflow for [specify use case: customer onboarding/order confirmation/weekly newsletter]

## Trigger Configuration
- **Trigger Type**: [Webhook/Schedule/Manual/Form Submission]
- **Trigger Details**:
  - If Webhook: POST endpoint to receive data
  - If Schedule: Cron expression (e.g., "0 9 * * 1" for Monday 9am)
  - Data expected: email, name, [additional fields]

## Node Sequence & Logic
1. **Trigger Node**: Webhook/Schedule trigger
2. **Data Validation**: Check required fields (email, name)
3. **Conditional Logic**: Filter/route based on criteria
4. **Email Composition**:
   - From: [sender email]
   - To: {{$json["email"]}}
   - Subject: [dynamic subject]
   - Body: [HTML template or plain text]
5. **Send Email**: Gmail/SMTP/SendGrid node
6. **Log Result**: Store sent status to database/sheet

## Data Transformation
- Input: `{email, name, [custom fields]}`
- Transform: Format data for email template
- Output: Delivery status and timestamp

## Error Handling
- Retry failed emails (3 attempts with 5min delay)
- Send admin notification on persistent failures
- Log errors to [Google Sheets/Database/Slack]

## Testing Checklist
- [ ] Test with valid email address
- [ ] Test with invalid email format
- [ ] Verify email delivery
- [ ] Check error notifications
```

### Example 2: Slack Notification Request

**Input:**
```
"Send slack messages when customers sign up"
```

**Output:**
```markdown
# N8N Workflow: Customer Signup Slack Notifications

## Workflow Objective
Automatically send Slack notifications to #sales channel when new customers complete signup

## Trigger Configuration
- **Trigger Type**: Webhook
- **Trigger Details**:
  - Method: POST
  - Authentication: API key in header
  - Payload: {userId, email, name, plan, signupDate}

## Node Sequence & Logic
1. **Webhook Trigger**: Receive signup event
2. **Data Validation**: Verify required fields exist
3. **User Enrichment** (optional): Fetch additional user data from database
4. **Format Message**: Create Slack message with blocks
5. **Send to Slack**: Post to #sales channel
6. **Log Activity**: Record notification in tracking sheet

## Data Transformation
- Input: `{userId, email, name, plan, signupDate}`
- Transform: Format into Slack blocks with user details
- Message template:
  ```
  🎉 New Customer Signup!
  Name: {{$json["name"]}}
  Email: {{$json["email"]}}
  Plan: {{$json["plan"]}}
  Signed up: {{$json["signupDate"]}}
  ```

## Error Handling
- Retry Slack posting on failure (2 retries)
- Fallback: Send email notification if Slack fails
- Alert DevOps if webhook receives malformed data

## Testing Checklist
- [ ] Test webhook with sample payload
- [ ] Verify Slack message formatting
- [ ] Test with missing optional fields
- [ ] Validate error notifications
```

## Resources

### References

- **n8n_nodes.md** - Common n8n node types, configurations, and use cases
- **workflow_patterns.md** - Best practices and common automation patterns
- **error_handling.md** - Error handling strategies for production workflows

### Assets

- **workflow_template.md** - Base template for structured workflow prompts

## Quality Standards

Enhanced prompts must include:
- ✅ Clear workflow objective
- ✅ Specific trigger configuration with expected data format
- ✅ Complete node sequence (minimum 4-6 nodes)
- ✅ Data transformation details with example formats
- ✅ Error handling with retry logic and fallbacks
- ✅ Testing checklist (minimum 3-4 items)
- ✅ Placeholders for user-specific details

Avoid:
- ❌ Generic descriptions without technical specifics
- ❌ Missing error handling or testing sections
- ❌ Assuming implementation details without placeholders
- ❌ Incomplete node sequences or data flows
