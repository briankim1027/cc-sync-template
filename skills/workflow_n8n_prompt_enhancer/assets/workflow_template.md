# N8N Workflow: [Workflow Name]

## Workflow Objective
[Clear, concise statement of what this workflow accomplishes. Be specific about the business goal and expected outcome.]

Example:
- "Automatically send welcome emails to new customers within 5 minutes of signup"
- "Synchronize customer data between CRM and email marketing platform daily at 2am"
- "Send Slack notifications when high-priority support tickets are created"

---

## Trigger Configuration

**Trigger Type**: [Webhook/Schedule/Manual/Form Submission/Email/Watch]

**Trigger Details**:

### If Webhook:
- **Method**: [POST/GET/PUT/DELETE]
- **Path**: [/webhook/custom-path]
- **Authentication**: [None/Header Auth/Query Auth/Basic Auth]
  - If authenticated: `X-API-Key: [your-key]` or `Authorization: Bearer [token]`
- **Expected Payload**:
  ```json
  {
    "field1": "value",
    "field2": "value",
    "field3": "value"
  }
  ```

### If Schedule:
- **Cron Expression**: [e.g., "0 9 * * 1-5" for weekdays at 9am]
- **Timezone**: [UTC/America/New_York/etc.]
- **Common Patterns**:
  - Daily at specific time: `"0 14 * * *"` (2pm daily)
  - Every X hours: `"0 */6 * * *"` (every 6 hours)
  - Weekly: `"0 9 * * 1"` (Mondays at 9am)
  - Monthly: `"0 0 1 * *"` (1st of month at midnight)

### If Manual:
- **Use Case**: [Testing/Admin operations/One-off tasks]
- **Parameters**: [Any manual input required]

### If Form Submission:
- **Form Fields**:
  - Field 1: [Name] (Type: text/email/number/date)
  - Field 2: [Name] (Type: text/email/number/date)
- **Submit Button**: [Custom text]
- **Success Redirect**: [Optional URL]

---

## Node Sequence & Logic

Detailed step-by-step workflow with specific n8n node types:

### 1. [Trigger Node Name]
**Node Type**: [Webhook/Schedule/Manual/Form]
**Purpose**: [What initiates this workflow]
**Output**: [Data format or fields provided]

### 2. [Validation Node Name]
**Node Type**: [IF/Code/Function]
**Purpose**: Validate input data and check required fields
**Logic**:
```javascript
// Example validation
const required = ['email', 'name'];
const missing = required.filter(field => !$json[field]);
if (missing.length > 0) {
  throw new Error(`Missing: ${missing.join(', ')}`);
}
```
**Outputs**:
- Valid → Continue to processing
- Invalid → Send error response

### 3. [Data Processing Node Name]
**Node Type**: [Set/Code/HTTP Request]
**Purpose**: [Transform, enrich, or fetch additional data]
**Operations**:
- Transform field X to Y
- Fetch additional data from [API/Database]
- Calculate derived values
**Output**:
```json
{
  "processedField1": "value",
  "processedField2": "value",
  "enrichedData": {}
}
```

### 4. [Conditional Logic Node Name] (if applicable)
**Node Type**: [IF/Switch]
**Purpose**: Route based on conditions
**Conditions**:
- **Route A**: [Condition description]
  - Example: `{{$json["status"]}} equals "premium"`
  - Action: [What happens on this path]
- **Route B**: [Condition description]
  - Example: `{{$json["status"]}} equals "standard"`
  - Action: [What happens on this path]
- **Default**: [Fallback action]

### 5. [Primary Action Node Name]
**Node Type**: [Gmail/Slack/HTTP Request/Database]
**Purpose**: [Main action this workflow performs]
**Configuration**:
- **If Email**:
  - From: [sender@domain.com]
  - To: `{{$json["email"]}}`
  - Subject: [Dynamic subject with expressions]
  - Body: [HTML/Text template]
- **If Slack**:
  - Channel: [#channel-name]
  - Message: [Format with blocks or plain text]
- **If HTTP Request**:
  - URL: [API endpoint]
  - Method: [POST/GET/PUT]
  - Headers: [Required headers]
  - Body: [JSON payload]
- **If Database**:
  - Operation: [Insert/Update/Query]
  - Table: [table_name]
  - Fields: [Field mappings]

### 6. [Logging/Storage Node Name]
**Node Type**: [Google Sheets/Database/HTTP Request]
**Purpose**: Record workflow execution and results
**Data Stored**:
- Execution timestamp
- Input data (sanitized)
- Result status (success/failure)
- Any relevant IDs or references

### 7. [Response Node Name] (for webhooks)
**Node Type**: [Respond to Webhook]
**Purpose**: Send response back to caller
**Response**:
```json
{
  "status": "success",
  "message": "Workflow completed",
  "data": {
    "id": "{{$json['id']}}",
    "timestamp": "{{new Date().toISOString()}}"
  }
}
```

---

## Data Transformation

### Input Data Format
```json
{
  "field1": "description and example value",
  "field2": "description and example value",
  "field3": "description and example value"
}
```

### Transformation Logic
Document how data flows and transforms through the workflow:

1. **Initial Input**: Raw data from trigger
2. **Validation**: Check and sanitize fields
3. **Enrichment**: Add computed or fetched data
4. **Formatting**: Prepare for final output/action
5. **Output**: Final data structure

### Example Transformations
```javascript
// Transform email to lowercase
{{$json["email"].toLowerCase()}}

// Format date
{{new Date($json["signupDate"]).toLocaleDateString()}}

// Concatenate fields
{{$json["firstName"]}} {{$json["lastName"]}}

// Conditional value
{{$json["plan"] === "premium" ? "VIP" : "Standard"}}
```

### Output Data Format
```json
{
  "outputField1": "description and example",
  "outputField2": "description and example",
  "metadata": {
    "processedAt": "ISO timestamp",
    "status": "success/failure"
  }
}
```

---

## Error Handling

### Error Detection
Identify operations that may fail:
- [ ] External API calls
- [ ] Database operations
- [ ] Email sending
- [ ] Data validation
- [ ] Network operations

### Error Handling Strategy

**For Transient Errors** (temporary, retryable):
- **Retry Logic**:
  - Max retries: [3]
  - Backoff strategy: [Exponential: 1s, 2s, 4s]
  - Total timeout: [30 seconds]
- **Examples**: Network timeout, rate limiting (429), service unavailable (503)

**For Permanent Errors** (not retryable):
- **Action**: [Log and alert immediately]
- **Examples**: Invalid credentials (401), not found (404), validation failure (400)

**Fallback Mechanisms**:
1. **Primary Method**: [Main approach]
   - If fails → Try Secondary Method
2. **Secondary Method**: [Backup approach]
   - If fails → Try Tertiary Method
3. **Tertiary Method**: [Last resort]
   - If fails → Manual intervention required

### Error Notifications

**Critical Errors** (immediate attention):
- Send to: [Slack #incidents + Email to on-call + SMS]
- Include: Error details, workflow name, execution ID, timestamp
- Example: Payment processing failures, data loss risk

**Warning Level** (attention needed):
- Send to: [Slack #alerts + Email summary]
- Include: Error count, affected items, suggested action
- Example: Elevated error rate, API rate limiting

**Info Level** (awareness):
- Log to: [Database/Google Sheets]
- Include: Basic error info for debugging
- Example: Successfully retried errors, expected failures

### Error Logging

**Log Structure**:
```json
{
  "timestamp": "ISO 8601 timestamp",
  "workflow": "Workflow Name",
  "executionId": "n8n execution ID",
  "errorType": "error category",
  "errorMessage": "detailed error message",
  "node": "failed node name",
  "retryCount": "number of retries attempted",
  "inputData": "sanitized input (no sensitive data)",
  "severity": "critical/warning/info"
}
```

**Error Log Destination**: [Google Sheets/Database Table/External Logging Service]

### Circuit Breaker (if applicable)
For frequently failing external services:
- **Failure Threshold**: [5 failures in 60 seconds]
- **Open Circuit Duration**: [5 minutes]
- **Action When Open**: [Return cached data / Send error response / Alert admin]

---

## Testing Checklist

Validate workflow functionality before production deployment:

### Input Validation Tests
- [ ] Test with valid, complete input data
- [ ] Test with missing required fields
- [ ] Test with invalid data types
- [ ] Test with edge case values (empty strings, null, very long values)

### Success Path Tests
- [ ] Verify primary action completes successfully
- [ ] Confirm data is transformed correctly
- [ ] Check output format matches expectations
- [ ] Validate data is stored/logged properly

### Error Handling Tests
- [ ] Test retry logic with simulated transient errors
- [ ] Verify fallback mechanisms work
- [ ] Confirm error notifications are sent
- [ ] Check error logging captures all details

### Integration Tests
- [ ] Test webhook endpoint responds correctly
- [ ] Verify external API integrations work
- [ ] Confirm database operations succeed
- [ ] Test email/message delivery

### Performance Tests
- [ ] Measure workflow execution time
- [ ] Test with maximum expected load
- [ ] Verify no timeouts under normal conditions
- [ ] Check resource usage (if applicable)

### Security Tests
- [ ] Verify authentication is required (if applicable)
- [ ] Confirm sensitive data is not logged
- [ ] Test with malicious input (SQL injection, XSS attempts)
- [ ] Validate authorization checks work

---

## Production Deployment

### Pre-Deployment Checklist
- [ ] All tests passing
- [ ] Error handling tested and verified
- [ ] Credentials configured correctly
- [ ] Monitoring and logging set up
- [ ] Team notified of deployment
- [ ] Rollback plan documented

### Monitoring
Track these metrics:
- Execution count (per hour/day)
- Success rate (percentage)
- Average execution time
- Error rate and types
- API usage and rate limits

### Maintenance
- Review error logs [daily/weekly]
- Check dead letter queue for failed items
- Update workflow as APIs/requirements change
- Optimize based on performance metrics

---

## Notes and Considerations

### Assumptions
[Document any assumptions made about data, services, or environment]
- Example: "Assumes email service is available 24/7"
- Example: "Expects webhook payload to always include userId"

### Limitations
[List known limitations or constraints]
- Example: "Rate limited to 100 requests per minute"
- Example: "Cannot process attachments larger than 10MB"

### Future Enhancements
[Optional improvements or features to add later]
- Example: "Add support for batch processing"
- Example: "Implement caching to reduce API calls"

### Dependencies
[External services or systems this workflow relies on]
- [ ] [Service/API name and version]
- [ ] [Database or data source]
- [ ] [Authentication service]
- [ ] [Notification channels]

---

## Placeholders for Customization

Throughout this template, replace the following placeholders with actual values:

- `[Workflow Name]` - Descriptive name for the workflow
- `[specify use case...]` - Specific business scenario
- `[sender email]` - Actual sender email address
- `[API endpoint]` - Real API URL
- `[Database/Table]` - Actual database and table names
- `[Channel name]` - Real Slack channel or notification destination
- `[Field names]` - Actual data field names
- `[Cron expression]` - Specific schedule timing
- `[threshold/limit]` - Actual numeric values

These placeholders should be discussed with the user during implementation to gather specific requirements.
