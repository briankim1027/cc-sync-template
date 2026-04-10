# N8N Workflow Patterns and Best Practices

This reference documents common workflow patterns and architectural best practices for building production-ready n8n automations.

## Common Workflow Patterns

### 1. Webhook → Process → Notify Pattern

**Use Case**: External system triggers automation, process data, send notification

**Structure**:
```
Webhook Trigger
→ Validate Input (Function/IF)
→ Process Data (Set/Code/HTTP Request)
→ Store Result (Database/Google Sheets)
→ Send Notification (Slack/Email)
→ Respond to Webhook
```

**Example**: New customer signup notification
```
Webhook (signup event)
→ Validate (check required fields)
→ Create User Record (Database)
→ Send Welcome Email (Gmail)
→ Notify Sales Team (Slack)
→ Return Success Response
```

**Best Practices**:
- Always validate webhook payload before processing
- Respond to webhook early if possible (async processing)
- Include timestamp in stored data
- Log all webhook calls for debugging

---

### 2. Schedule → Fetch → Transform → Export Pattern

**Use Case**: Periodic data synchronization or reporting

**Structure**:
```
Schedule Trigger
→ Fetch Data (HTTP Request/Database)
→ Transform Data (Code/Set/Function)
→ Aggregate/Format (Item Lists/Merge)
→ Export (Google Sheets/Email/Database)
→ Send Summary (Email/Slack)
```

**Example**: Daily sales report
```
Schedule (every day at 9am)
→ Fetch Orders (Database query)
→ Calculate Metrics (Code node)
→ Format Report (Set nodes)
→ Update Dashboard (Google Sheets)
→ Email Summary (Gmail)
```

**Best Practices**:
- Use appropriate schedule intervals (avoid unnecessary runs)
- Add date range filters to data fetching
- Include execution timestamp in reports
- Handle empty results gracefully

---

### 3. Form → Validate → Multi-Step Process Pattern

**Use Case**: User-initiated workflows with multiple steps

**Structure**:
```
Form Trigger
→ Validate Input (IF/Function)
→ Step 1: Initial Processing
→ Step 2: External API Call
→ Step 3: Store Data
→ Wait (if needed)
→ Step 4: Follow-up Action
→ Success Response
```

**Example**: Lead qualification workflow
```
Form Submission
→ Validate Email Format
→ Check Duplicate (Database lookup)
→ Enrich Lead Data (Clearbit API)
→ Score Lead (Code node)
→ IF (score > threshold)
   → High Priority: Notify Sales (Slack)
   → Low Priority: Add to Nurture (Marketing Platform)
→ Store in CRM (HTTP Request)
→ Thank You Response
```

**Best Practices**:
- Provide immediate feedback to user
- Validate all inputs before processing
- Use friendly error messages
- Log form submissions for analysis

---

### 4. Monitor → Detect Change → Alert Pattern

**Use Case**: Continuous monitoring and alerting

**Structure**:
```
Schedule Trigger (frequent interval)
→ Fetch Current State (API/Database)
→ Compare with Previous State (Code/IF)
→ Detect Changes
→ IF (change detected)
   → Alert (Slack/Email/SMS)
   → Update State (Database)
```

**Example**: Website uptime monitor
```
Schedule (every 5 minutes)
→ HTTP Request (check website)
→ IF (status != 200)
   → Get Last Status (Database)
   → IF (was up before)
      → Alert Team (Slack + Email)
      → Create Incident (PagerDuty)
   → Update Status (Database: down)
→ ELSE (status = 200)
   → Update Status (Database: up)
```

**Best Practices**:
- Store state to detect changes
- Avoid alert fatigue (debounce repeated alerts)
- Include relevant context in alerts
- Add recovery notifications

---

### 5. Batch Processing Pattern

**Use Case**: Process large datasets efficiently

**Structure**:
```
Trigger
→ Fetch All Items (API/Database)
→ Split Out Items (Item Lists)
→ Process Each Item (Code/HTTP)
→ Aggregate Results (Item Lists)
→ Store Results (Database)
→ Summary Notification
```

**Example**: Process invoice batch
```
Schedule (daily)
→ Fetch Pending Invoices (Database)
→ Split Out (one per item)
→ FOR EACH Invoice:
   → Generate PDF (API)
   → Send Email (Gmail)
   → Update Status (Database)
→ Aggregate (success/failure counts)
→ Send Summary (Slack)
```

**Best Practices**:
- Add batch size limits to prevent timeouts
- Include error handling per item
- Track processed items to resume on failure
- Use batching for external API calls when supported

---

### 6. Conditional Routing Pattern

**Use Case**: Different processing paths based on conditions

**Structure**:
```
Trigger
→ Classify/Evaluate (IF/Switch)
→ Route A: High Priority Processing
→ Route B: Standard Processing
→ Route C: Low Priority Processing
→ Merge (if needed)
→ Final Action
```

**Example**: Support ticket routing
```
Email Trigger (support inbox)
→ Extract Priority (Code: parse subject/body)
→ Switch (by priority)
   → Output 1 (Urgent):
      → Create High Priority Ticket
      → Notify On-Call Engineer
   → Output 2 (Normal):
      → Create Standard Ticket
      → Add to Queue
   → Output 3 (Low):
      → Create Low Priority Ticket
      → Auto-tag for bulk processing
→ Log Ticket Creation
```

**Best Practices**:
- Always include default/fallback path
- Keep routing logic simple and readable
- Document routing criteria
- Test all paths

---

### 7. Data Enrichment Pattern

**Use Case**: Enhance data from multiple sources

**Structure**:
```
Trigger
→ Receive Basic Data
→ Parallel Branches:
   → Fetch Details A (API 1)
   → Fetch Details B (API 2)
   → Fetch Details C (Database)
→ Merge (by key field)
→ Transform Combined Data
→ Output Enriched Data
```

**Example**: Customer data enrichment
```
Webhook (new lead)
→ Parallel:
   → Get Company Info (Clearbit)
   → Get Social Profiles (FullContact)
   → Check Existing Data (CRM)
→ Merge (by email)
→ Calculate Lead Score (Code)
→ Update CRM with Full Profile
```

**Best Practices**:
- Use parallel execution when possible
- Handle missing data gracefully
- Set timeouts for external calls
- Merge by reliable key fields

---

### 8. Error Recovery Pattern

**Use Case**: Robust error handling and retry logic

**Structure**:
```
Main Workflow:
→ Try Operation
→ Success Path

Error Workflow:
Error Trigger
→ Parse Error Details
→ IF (retryable error)
   → Wait
   → Retry Operation (webhook to main workflow)
   → IF (max retries exceeded)
      → Alert Admin
      → Log to Error Database
→ ELSE (non-retryable)
   → Alert Admin Immediately
   → Log to Error Database
```

**Example**: API call with retry
```
Main:
→ HTTP Request (external API)
→ Process Response
→ Success

Error:
Error Trigger
→ Get Error Details
→ IF (status = 429 or 503)
   → Increment Retry Count (Database)
   → IF (count < 3)
      → Wait (exponential backoff)
      → Retry API Call
   → ELSE
      → Alert Admin (Slack)
→ ELSE
   → Log Error
   → Alert Admin
```

**Best Practices**:
- Implement exponential backoff for retries
- Set maximum retry limits
- Distinguish transient vs permanent errors
- Log all errors with context

---

### 9. Multi-Channel Notification Pattern

**Use Case**: Send notifications through multiple channels

**Structure**:
```
Trigger
→ Format Message Data
→ Parallel Branches:
   → Email (Gmail/SMTP)
   → Slack (team channel)
   → SMS (Twilio)
   → Push Notification (FCM)
→ Aggregate Results
→ Log Delivery Status
```

**Example**: Critical alert distribution
```
Monitor Detects Issue
→ Format Alert Message
→ Parallel:
   → Send Email (Gmail)
   → Post to Slack (#incidents)
   → Send SMS (Twilio to on-call)
   → Create Ticket (Jira)
→ Wait for All
→ Log All Delivery Statuses
```

**Best Practices**:
- Use parallel execution for speed
- Don't fail entire workflow if one channel fails
- Track delivery status per channel
- Allow channel-specific formatting

---

### 10. API Aggregation Pattern

**Use Case**: Combine data from multiple APIs

**Structure**:
```
Trigger
→ Parallel API Calls:
   → Service A
   → Service B
   → Service C
→ Merge Results
→ Transform Combined Data
→ Return/Store Aggregated Response
```

**Example**: Dashboard data aggregation
```
Schedule (hourly)
→ Parallel:
   → Get Analytics (Google Analytics)
   → Get Sales (Stripe)
   → Get Support (Zendesk)
   → Get Marketing (Mailchimp)
→ Merge All Data
→ Calculate KPIs (Code)
→ Update Dashboard (Google Sheets)
→ Post Summary (Slack)
```

**Best Practices**:
- Set timeouts for all API calls
- Handle partial failures gracefully
- Cache results when appropriate
- Use pagination for large datasets

---

## Architectural Best Practices

### Data Validation

**Always validate input data early**:
```javascript
// Example validation in Code node
const required = ['email', 'name', 'phone'];
const missing = required.filter(field => !$json[field]);

if (missing.length > 0) {
  throw new Error(`Missing required fields: ${missing.join(', ')}`);
}

// Validate email format
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (!emailRegex.test($json.email)) {
  throw new Error('Invalid email format');
}
```

### Naming Conventions

**Use descriptive node names**:
- ❌ Bad: "HTTP Request", "IF", "Set"
- ✅ Good: "Fetch User from CRM", "Check if Premium User", "Add Timestamp"

**Organize with color coding**:
- 🔴 Red: Error handling nodes
- 🟢 Green: Success paths
- 🟡 Yellow: Warnings or conditional logic
- 🔵 Blue: Data transformation
- ⚫ Gray: Logging/debugging

### Workflow Documentation

**Add notes to complex workflows**:
- Document business logic
- Explain conditional routing
- Note API rate limits
- Mark temporary/experimental nodes

**Use sticky notes**:
```
"Rate Limit: 100 requests/min
Current usage: ~50/min
Increase wait time if errors occur"
```

### Security Best Practices

1. **Never hardcode credentials**: Use n8n credentials manager
2. **Validate webhooks**: Check authentication tokens
3. **Sanitize user input**: Prevent injection attacks
4. **Use HTTPS**: For all webhook endpoints
5. **Limit data exposure**: Only log necessary information
6. **Rotate secrets**: Regularly update API keys

### Performance Optimization

**Minimize workflow execution time**:
- Use parallel branches when possible
- Batch API requests when supported
- Cache frequently accessed data
- Use pagination for large datasets
- Set appropriate timeouts

**Example parallel execution**:
```
# Sequential (slow): 15 seconds total
API Call 1 (5s) → API Call 2 (5s) → API Call 3 (5s)

# Parallel (fast): 5 seconds total
Parallel:
├─ API Call 1 (5s)
├─ API Call 2 (5s)
└─ API Call 3 (5s)
```

### Testing Strategies

**Test incrementally**:
1. Build and test each node individually
2. Use manual trigger for testing
3. Test with sample data first
4. Validate error paths
5. Test with production-like data
6. Enable workflow and monitor

**Create test data**:
```javascript
// Test data generator in Code node
return [
  {
    json: {
      email: 'test@example.com',
      name: 'Test User',
      plan: 'premium',
      signupDate: new Date().toISOString()
    }
  }
];
```

### Monitoring and Logging

**Log important events**:
```
Trigger
→ Log: "Workflow started"
→ Process
→ IF (success)
   → Log: "Success - processed N items"
→ ELSE
   → Log: "Failed - error details"
```

**Track metrics**:
- Workflow execution count
- Success/failure rates
- Average execution time
- Error frequencies
- API usage

### Workflow Organization

**Split complex workflows**:
- Main workflow: Core logic
- Sub-workflow: Reusable components
- Error workflow: Centralized error handling
- Utility workflow: Common transformations

**Use execute workflow node**:
```
Main Workflow
→ Execute Workflow: "Send Notification"
→ Execute Workflow: "Log to Database"
```

### Environment Management

**Use environment variables**:
- `{{$env.API_BASE_URL}}`
- `{{$env.ADMIN_EMAIL}}`
- `{{$env.ENVIRONMENT}}` (dev/staging/prod)

**Separate dev/prod workflows**:
- Prefix workflow names: "[DEV]", "[PROD]"
- Use different credentials
- Different notification channels

## Common Pitfalls to Avoid

1. **No error handling**: Always handle potential failures
2. **Hardcoded values**: Use variables and expressions
3. **Missing validation**: Validate input early
4. **Infinite loops**: Add exit conditions
5. **Too complex**: Break into sub-workflows
6. **No logging**: Add logging for debugging
7. **Ignoring rate limits**: Respect API limits
8. **No testing**: Test before enabling
9. **Poor naming**: Use descriptive names
10. **No documentation**: Document complex logic

## Workflow Complexity Guidelines

**Simple Workflow** (5-10 nodes):
- Single trigger
- Linear processing
- Basic error handling
- One primary output

**Medium Workflow** (10-25 nodes):
- Conditional routing
- Multiple integrations
- Comprehensive error handling
- Parallel processing

**Complex Workflow** (25+ nodes):
- Multiple branching paths
- Sub-workflow calls
- Advanced error recovery
- Multiple data sources
- Extensive transformations

**Consider splitting when**:
- Workflow becomes hard to understand
- Too many nested conditions
- Reusable components emerge
- Different teams own different parts
