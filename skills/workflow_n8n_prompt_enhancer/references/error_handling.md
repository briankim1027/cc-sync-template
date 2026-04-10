# N8N Error Handling Strategies

This reference provides comprehensive error handling patterns and best practices for building resilient n8n workflows.

## Error Handling Principles

### 1. Fail Fast, Recover Gracefully
- Detect errors early in the workflow
- Validate input before expensive operations
- Provide clear error messages
- Implement appropriate recovery strategies

### 2. Error Categories

**Transient Errors** (temporary, retryable):
- Network timeouts
- Rate limiting (HTTP 429)
- Service unavailable (HTTP 503)
- Temporary database locks

**Permanent Errors** (not retryable):
- Invalid credentials (HTTP 401)
- Not found (HTTP 404)
- Validation failures (HTTP 400)
- Malformed data

**Partial Errors**:
- Batch processing with some failures
- Multi-step workflows with intermediate failures

### 3. Error Handling Strategies

**Retry**: For transient errors
**Fallback**: Use alternative approach
**Alert**: Notify team of critical errors
**Log**: Record error details for debugging
**Graceful Degradation**: Continue with reduced functionality
**Circuit Breaker**: Stop after repeated failures

---

## Error Handling Patterns

### Pattern 1: Basic Try-Catch with Error Trigger

**Structure**:
```
Main Workflow:
→ Operation (may fail)
→ Success path

Error Workflow:
Error Trigger (listens to main workflow)
→ Log Error
→ Send Alert
```

**Example**:
```
Main Workflow: "Process Orders"
→ Fetch Orders (Database)
→ Process Each Order
→ Update Status

Error Workflow: "Process Orders - Error Handler"
Error Trigger (workflow: "Process Orders")
→ Set Error Details
→ Log to Error Database
→ Send Slack Alert
```

**When to Use**:
- Simple workflows with centralized error handling
- When you want to separate error logic from main flow

**Implementation**:
```javascript
// In main workflow, errors automatically trigger error workflow

// In error workflow
const errorData = {
  workflow: $json.workflow.name,
  execution: $json.execution.id,
  error: $json.error.message,
  timestamp: new Date().toISOString(),
  node: $json.node.name
};

return { json: errorData };
```

---

### Pattern 2: Retry with Exponential Backoff

**Structure**:
```
Main Workflow:
→ Set Retry Counter (0)
→ Try Operation
→ Success

Error Workflow:
→ Check Retry Count
→ IF (count < max_retries)
   → Calculate Backoff Time
   → Wait (exponential: 1s, 2s, 4s, 8s...)
   → Increment Counter
   → Retry Operation (call main workflow via webhook)
→ ELSE
   → Give Up
   → Alert Admin
   → Log Final Failure
```

**Example**:
```
Main: "API Call with Retry"
→ HTTP Request (external API)

Error: "API Call - Retry Handler"
→ Get Current Retry Count (from Database by execution ID)
→ IF (retryCount < 3)
   → Calculate Wait: Math.pow(2, retryCount) seconds
   → Wait Node
   → Increment Retry Count (Database)
   → Webhook to Main Workflow
→ ELSE
   → Send Alert: "API call failed after 3 retries"
   → Log Permanent Failure
```

**Backoff Calculation**:
```javascript
// Exponential backoff with jitter
const baseDelay = 1000; // 1 second
const maxDelay = 32000; // 32 seconds
const retryCount = $json.retryCount || 0;

const exponentialDelay = Math.min(
  baseDelay * Math.pow(2, retryCount),
  maxDelay
);

// Add jitter to prevent thundering herd
const jitter = Math.random() * 1000;
const delayMs = exponentialDelay + jitter;

return {
  json: {
    delayMs,
    delaySeconds: delayMs / 1000,
    retryCount
  }
};
```

**When to Use**:
- External API calls
- Database operations with temporary locks
- Services with rate limiting
- Network-dependent operations

---

### Pattern 3: Fallback Strategy

**Structure**:
```
→ Try Primary Method
→ IF (error)
   → Try Secondary Method
   → IF (error)
      → Try Tertiary Method
      → IF (error)
         → Use Default/Manual Process
```

**Example**:
```
Send Notification:
→ Try Slack API
→ Error Trigger → Try Email (Gmail)
   → Error Trigger → Try Email (SMTP Backup)
      → Error Trigger → Log to Database for Manual Follow-up
         → Alert Admin
```

**Implementation**:
```javascript
// Track which methods were attempted
const attempts = $json.attempts || [];
attempts.push({
  method: 'slack',
  timestamp: new Date().toISOString(),
  error: $json.error?.message
});

// Determine next fallback
const fallbackOrder = ['slack', 'gmail', 'smtp', 'database'];
const currentIndex = fallbackOrder.indexOf($json.currentMethod);
const nextMethod = fallbackOrder[currentIndex + 1];

return {
  json: {
    attempts,
    nextMethod,
    hasNextMethod: !!nextMethod,
    originalMessage: $json.originalMessage
  }
};
```

**When to Use**:
- Critical notifications that must be delivered
- Services with backup systems
- Multi-channel communication requirements

---

### Pattern 4: Batch Error Handling

**Structure**:
```
→ Fetch Items (100 items)
→ Split Out
→ FOR EACH Item:
   → Try Process Item
   → IF (success)
      → Add to Success List
   → IF (error)
      → Add to Failure List
→ Aggregate Results
→ IF (any failures)
   → Log Failed Items
   → Send Summary Alert
   → Optional: Retry Failed Items
```

**Example**:
```
Process Invoice Batch:
→ Fetch Pending Invoices
→ Split Out
→ FOR EACH Invoice:
   → Try:
      → Generate PDF
      → Send Email
      → Mark as Sent
   → Catch:
      → Log Error with Invoice ID
      → Add to Failed List
→ Aggregate:
   → Success Count
   → Failure Count
   → Failed Invoice IDs
→ IF (failures > 0)
   → Send Summary to Admin
   → Create Retry Queue
```

**Implementation**:
```javascript
// Process items with error tracking
const results = {
  success: [],
  failed: [],
  total: items.length
};

for (const item of items) {
  try {
    // Process item
    const result = await processItem(item);
    results.success.push({
      id: item.id,
      result
    });
  } catch (error) {
    results.failed.push({
      id: item.id,
      error: error.message,
      data: item
    });
  }
}

results.successRate = (results.success.length / results.total * 100).toFixed(2);

return { json: results };
```

**When to Use**:
- Batch processing workflows
- Import/export operations
- Bulk API operations
- Mass email sends

---

### Pattern 5: Circuit Breaker

**Structure**:
```
→ Check Circuit Status (Database)
→ IF (circuit OPEN)
   → Return Error Immediately (don't try)
   → Log Circuit Open Event
→ ELSE IF (circuit CLOSED)
   → Try Operation
   → IF (success)
      → Reset Failure Count
   → IF (error)
      → Increment Failure Count
      → IF (failures >= threshold)
         → Open Circuit
         → Alert Admin
→ Wait (cooldown period)
→ Set Circuit to HALF-OPEN
→ Retry Operation
```

**Example**:
```
Call External API:
→ Get Circuit State (Database: "api_x_circuit")
→ IF (state = "OPEN" && timeout not expired)
   → Return Cached Response or Error
   → Skip API call
→ ELSE
   → Try API Call
   → IF (success)
      → Set Circuit: CLOSED
      → Reset Failure Count
   → IF (error)
      → Increment Failure Count
      → IF (failures >= 5 in last 60s)
         → Set Circuit: OPEN
         → Set Cooldown: 5 minutes
         → Alert: "Circuit breaker opened for API X"
```

**Circuit States**:
```javascript
const circuitState = {
  CLOSED: 'closed',     // Normal operation
  OPEN: 'open',         // Failing, reject requests
  HALF_OPEN: 'half_open' // Testing if service recovered
};

// Circuit breaker logic
const circuit = await getCircuitStatus('api_x');

if (circuit.state === circuitState.OPEN) {
  const timeoutExpired = Date.now() > circuit.openedAt + circuit.timeout;

  if (!timeoutExpired) {
    throw new Error('Circuit breaker is OPEN');
  } else {
    circuit.state = circuitState.HALF_OPEN;
  }
}

// Try operation
try {
  const result = await callAPI();

  // Success in HALF_OPEN -> transition to CLOSED
  if (circuit.state === circuitState.HALF_OPEN) {
    circuit.state = circuitState.CLOSED;
    circuit.failures = 0;
  }

  return result;
} catch (error) {
  circuit.failures++;

  if (circuit.failures >= circuit.threshold) {
    circuit.state = circuitState.OPEN;
    circuit.openedAt = Date.now();
  }

  throw error;
}
```

**When to Use**:
- Frequently failing external services
- Expensive operations that fail often
- Preventing cascading failures
- Protecting against service degradation

---

### Pattern 6: Dead Letter Queue

**Structure**:
```
Main Workflow:
→ Try Process Item
→ IF (error after retries)
   → Move to Dead Letter Queue
   → Tag with Error Details
   → Continue Processing Next Item

Admin Workflow:
→ Review Dead Letter Queue
→ Fix Issues
→ Reprocess or Discard
```

**Example**:
```
Process Webhooks:
→ FOR EACH Webhook:
   → Try Process (3 retries)
   → IF (still failing)
      → Write to DLQ (Database/Google Sheets)
      → Include: payload, error, timestamp, retry count
      → Tag: "needs_review"
   → Continue to Next

Admin Review:
→ Query DLQ Items
→ Analyze Errors
→ Fix Data/Configuration
→ Resubmit to Main Workflow
→ Mark as Processed
```

**DLQ Data Structure**:
```javascript
const deadLetterItem = {
  id: generateId(),
  originalPayload: $json.webhookData,
  error: {
    message: $json.error.message,
    stack: $json.error.stack,
    node: $json.error.node
  },
  attempts: $json.retryCount,
  firstAttempt: $json.firstAttemptTime,
  lastAttempt: new Date().toISOString(),
  status: 'pending_review',
  workflow: 'Process Webhooks',
  executionId: $executionId
};

// Write to DLQ
await writeToDLQ(deadLetterItem);

// Alert if DLQ growing
const dlqSize = await getDLQSize();
if (dlqSize > 100) {
  await alertAdmin(`DLQ has ${dlqSize} items`);
}
```

**When to Use**:
- Message processing systems
- Event-driven workflows
- Data ingestion pipelines
- When manual review of failures is acceptable

---

## Error Notification Strategies

### Notification Severity Levels

**CRITICAL** (immediate action required):
- System-wide failures
- Data loss risk
- Security breaches
- Payment processing failures

**Channels**: Slack + Email + SMS
**Timing**: Immediate
**Example**:
```
→ Send Slack: @channel in #incidents
→ Send Email: to on-call engineer
→ Send SMS: via Twilio
→ Create PagerDuty Incident
```

**WARNING** (attention needed):
- Elevated error rates
- API rate limiting
- Slow performance
- Partial batch failures

**Channels**: Slack + Email
**Timing**: Immediate, but grouped if frequent
**Example**:
```
→ Post to Slack #alerts (no @channel)
→ Email summary to team
→ Log to monitoring dashboard
```

**INFO** (awareness only):
- Successfully recovered errors
- Circuit breaker state changes
- Retry successes
- DLQ items

**Channels**: Slack or Email
**Timing**: Batched summary (hourly/daily)
**Example**:
```
→ Log to database
→ Include in daily summary email
→ Update monitoring metrics
```

### Alert Fatigue Prevention

**Debouncing**:
```javascript
// Don't alert on every error - wait for pattern
const recentErrors = await getRecentErrors('api_x', 5 * 60 * 1000); // 5 min

if (recentErrors.length >= 5) {
  await sendAlert(`API X failing repeatedly: ${recentErrors.length} errors`);
  await clearErrorBuffer('api_x');
}
```

**Grouping**:
```javascript
// Group similar errors in single notification
const errorGroups = groupBy(errors, 'errorType');

const summary = Object.entries(errorGroups).map(([type, errors]) =>
  `${type}: ${errors.length} occurrences`
).join('\n');

await sendAlert(`Error Summary:\n${summary}`);
```

**Rate Limiting**:
```javascript
// Don't send same alert more than once per hour
const lastAlertTime = await getLastAlertTime('api_failure');
const oneHourAgo = Date.now() - 60 * 60 * 1000;

if (!lastAlertTime || lastAlertTime < oneHourAgo) {
  await sendAlert('API failure detected');
  await setLastAlertTime('api_failure', Date.now());
}
```

---

## Error Logging Best Practices

### What to Log

**Always Include**:
- Timestamp (ISO 8601)
- Workflow name and execution ID
- Error message and type
- Failed node name
- Input data (sanitized)
- Retry count (if applicable)

**Optionally Include**:
- Stack trace (for debugging)
- User ID or session ID
- Request/response data
- System metrics (memory, CPU)

### Log Levels

```javascript
const logLevels = {
  ERROR: 'error',     // Failures requiring attention
  WARN: 'warn',       // Potential issues
  INFO: 'info',       // Normal operation events
  DEBUG: 'debug'      // Detailed debugging info
};

const logEntry = {
  level: logLevels.ERROR,
  timestamp: new Date().toISOString(),
  workflow: 'Process Orders',
  executionId: $executionId,
  node: 'Send Email',
  message: 'Failed to send email',
  error: {
    type: 'SMTPError',
    message: $json.error.message,
    code: $json.error.code
  },
  context: {
    orderId: $json.orderId,
    email: $json.email,
    retryCount: $json.retryCount
  }
};
```

### Sensitive Data Handling

**Never log**:
- Passwords or API keys
- Credit card numbers
- Social security numbers
- Personal health information

**Sanitize before logging**:
```javascript
function sanitizeForLogging(data) {
  const sanitized = { ...data };

  // Mask email
  if (sanitized.email) {
    sanitized.email = sanitized.email.replace(
      /(.{2})(.*)(@.*)/,
      '$1***$3'
    );
  }

  // Remove sensitive fields
  delete sanitized.password;
  delete sanitized.apiKey;
  delete sanitized.creditCard;

  // Truncate long fields
  if (sanitized.notes && sanitized.notes.length > 200) {
    sanitized.notes = sanitized.notes.substring(0, 200) + '...';
  }

  return sanitized;
}
```

---

## Error Recovery Checklist

For each workflow, consider:

- [ ] **Input Validation**: Validate early to fail fast
- [ ] **Error Detection**: Identify error-prone operations
- [ ] **Retry Logic**: Implement for transient errors
- [ ] **Backoff Strategy**: Exponential backoff for retries
- [ ] **Fallback Plan**: Alternative approach if primary fails
- [ ] **Error Logging**: Log all errors with context
- [ ] **Alerting**: Notify team of critical errors
- [ ] **Monitoring**: Track error rates and patterns
- [ ] **Circuit Breaker**: Protect against cascading failures
- [ ] **Dead Letter Queue**: Handle unrecoverable errors
- [ ] **Testing**: Test error paths and recovery
- [ ] **Documentation**: Document error scenarios

---

## Common Error Scenarios

### API Errors

**Rate Limiting (429)**:
```
→ Detect HTTP 429
→ Extract Retry-After header
→ Wait (Retry-After duration)
→ Retry request
```

**Timeout**:
```
→ Set timeout: 30 seconds
→ IF (timeout)
   → Retry with exponential backoff
   → Max 3 retries
   → Alert if all fail
```

**Authentication (401)**:
```
→ Detect HTTP 401
→ Refresh access token
→ Retry original request
→ IF (still 401)
   → Alert admin: "Credentials expired"
   → Stop workflow
```

### Database Errors

**Connection Lost**:
```
→ Detect connection error
→ Reconnect with retry
→ Resume transaction if possible
→ Rollback and alert if not
```

**Deadlock**:
```
→ Detect deadlock error
→ Wait (random 1-5 seconds)
→ Retry transaction
→ Max 3 retries
```

**Constraint Violation**:
```
→ Detect unique constraint error
→ Check if duplicate is acceptable
→ IF (acceptable)
   → Skip or update existing
→ ELSE
   → Alert and log
```

### Network Errors

**DNS Resolution Failed**:
```
→ Retry with different DNS
→ Use IP address if available
→ Alert network team
```

**Connection Refused**:
```
→ Check if service is down
→ Use fallback endpoint
→ Alert DevOps team
```

---

## Testing Error Handling

### Error Injection

Intentionally trigger errors to test handling:

```javascript
// Test mode flag
const isTestMode = $env.TEST_MODE === 'true';

if (isTestMode && $json.testScenario === 'api_timeout') {
  throw new Error('Simulated API timeout');
}

if (isTestMode && $json.testScenario === 'rate_limit') {
  throw new Error('HTTP 429: Rate limited');
}

// Normal operation
return await callAPI();
```

### Error Scenarios to Test

1. **Transient Errors**: Network timeouts, temporary unavailability
2. **Permanent Errors**: Invalid credentials, not found
3. **Partial Failures**: Batch with some successes, some failures
4. **Rate Limiting**: Exceeding API limits
5. **Data Validation**: Invalid or malformed input
6. **Resource Exhaustion**: Out of memory, disk full
7. **Cascading Failures**: Multiple dependent services failing

### Monitoring Error Metrics

Track and alert on:
- Error rate (errors per minute/hour)
- Error types distribution
- Retry success rate
- Average time to recovery
- Circuit breaker state changes
- Dead letter queue size
