# Workflow Architecture: [Workflow Name]

## Overview

**Workflow ID**: [workflow-uuid]
**Category**: [Customer/Internal/Integration/Monitoring/Data]
**Environment**: [Development/Staging/Production]
**Created**: [Date]
**Last Updated**: [Date]
**Owner**: [Team/Person]

## Business Objective

[Clear statement of what this workflow accomplishes and why it exists]

**Example**:
"Automatically send Slack notifications to the sales team within 30 seconds when new customers complete signup, enabling immediate engagement and reducing response time from 4 hours to <1 minute."

---

## Workflow Topology

### Visual Diagram

```
[Trigger Node]
    ↓
[Validation Node]
    ↓
[IF Condition] ─┬─ TRUE → [Success Path Node 1] → [Success Path Node 2] → [Final Action]
                │
                └─ FALSE → [Error Handler] → [Error Notification] → [Error Response]
                               ↓
                          [Error Logging]
```

### Flow Type

**Pattern**: [Linear/Branching/Parallel/Hybrid]

- **Linear**: A → B → C → D (sequential processing)
- **Branching**: Conditional routing with IF/Switch nodes
- **Parallel**: Multiple operations executing simultaneously
- **Hybrid**: Combination of above patterns

---

## Node Inventory

### Total Node Count: [X]

| Node # | Node Name | Node Type | Purpose | Critical |
|--------|-----------|-----------|---------|----------|
| 1 | [Webhook] | n8n-nodes-base.webhook | Receive customer signup event | ✅ Yes |
| 2 | [Validate Email] | n8n-nodes-base.if | Check email format is valid | ✅ Yes |
| 3 | [Enrich User Data] | n8n-nodes-base.httpRequest | Fetch additional user info from CRM | ⚠️ No |
| 4 | [Format Message] | n8n-nodes-base.set | Prepare Slack message format | ✅ Yes |
| 5 | [Send to Slack] | n8n-nodes-base.slack | Post notification to #sales | ✅ Yes |
| 6 | [Log Activity] | n8n-nodes-base.postgres | Record event in database | ⚠️ No |
| 7 | [Respond Success] | n8n-nodes-base.respondToWebhook | Return 200 OK | ✅ Yes |
| 8 | [Error Handler] | n8n-nodes-base.set | Format error response | ✅ Yes |

**Critical Nodes**: Nodes essential for core functionality
**Non-Critical**: Enhancement nodes that can fail without breaking core flow

---

## Data Flow

### Input Data Format

**Source**: [Webhook/Schedule/Manual/etc.]
**Format**: JSON
**Schema**:
```json
{
  "userId": "string (uuid)",
  "email": "string (email format)",
  "name": "string",
  "plan": "string (premium|standard|basic)",
  "signupDate": "string (ISO 8601)"
}
```

**Sample Input**:
```json
{
  "userId": "550e8400-e29b-41d4-a716-446655440000",
  "email": "user@example.com",
  "name": "John Doe",
  "plan": "premium",
  "signupDate": "2024-01-15T14:30:00Z"
}
```

### Data Transformations

**Transformation Points**:

1. **Node 2 → Node 3**: Validation
   - Input: Raw webhook payload
   - Transform: Email validation check
   - Output: Valid/Invalid flag

2. **Node 4**: Message Formatting
   - Input: User data + CRM enrichment
   - Transform: Format for Slack blocks
   - Output: Formatted Slack message

3. **Node 6**: Database Logging
   - Input: Complete user data
   - Transform: Extract relevant fields
   - Output: Database insert statement

### Output Data Format

**Success Response**:
```json
{
  "status": "success",
  "message": "Notification sent successfully",
  "notificationId": "uuid",
  "timestamp": "ISO 8601"
}
```

**Error Response**:
```json
{
  "status": "error",
  "error": "Email validation failed",
  "code": "VALIDATION_ERROR",
  "timestamp": "ISO 8601"
}
```

---

## Connection Map

### Node Connections

```
Webhook (Node 1)
  └─> Validate Email (Node 2)
        ├─> TRUE: Enrich User Data (Node 3)
        │         └─> Format Message (Node 4)
        │               └─> Send to Slack (Node 5)
        │                     └─> Log Activity (Node 6)
        │                           └─> Respond Success (Node 7)
        │
        └─> FALSE: Error Handler (Node 8)
                     └─> Respond Error (Response Node)
```

### Connection Details

| From Node | To Node | Connection Type | Output Index | Notes |
|-----------|---------|-----------------|--------------|-------|
| Webhook | Validate Email | main | 0 | All webhook data passed |
| Validate Email | Enrich User Data | main | 0 | TRUE branch - valid email |
| Validate Email | Error Handler | main | 1 | FALSE branch - invalid email |
| Send to Slack | Log Activity | main | 0 | Success path continues |
| Error Handler | Respond Error | main | 0 | Error path ends |

---

## Credentials Required

| Credential Name | Type | Purpose | Environment | Critical |
|----------------|------|---------|-------------|----------|
| Slack Production API | slackApi | Post messages to Slack | Production | ✅ Yes |
| CRM API Key | httpHeaderAuth | Fetch user data from CRM | Production | ⚠️ No |
| Production Database | postgres | Log workflow executions | Production | ⚠️ No |

**Setup Instructions**: See `references/credential_setup.md`

---

## Error Handling Strategy

### Error Detection Points

1. **Node 2 (Validation)**: Email format validation
   - Error Type: Validation Error
   - Handling: Route to error handler
   - User Impact: Receives error response

2. **Node 3 (CRM Enrichment)**: API call failure
   - Error Type: Transient (retry possible)
   - Handling: Retry 3x with backoff, continue with basic data if fails
   - User Impact: None (optional enrichment)

3. **Node 5 (Slack)**: Message posting failure
   - Error Type: Critical (core function)
   - Handling: Retry 2x, send alert to admin if fails
   - User Impact: None (notification sent, confirmation returned)

### Error Workflow

**Linked Error Workflow**: [Error Workflow ID/Name]

**Error Triggers**:
- Uncaught exceptions
- Node execution failures
- Timeout errors

**Error Actions**:
1. Parse error details
2. Log to error database
3. Send alert to #incidents Slack channel
4. Create ticket in error tracking system

### Retry Strategy

**Transient Errors** (Network, Rate Limit):
- Max Retries: 3
- Backoff: Exponential (1s, 2s, 4s)
- Total Timeout: 30 seconds

**Permanent Errors** (Validation, Auth):
- No Retries
- Immediate error response

---

## Performance Characteristics

### Expected Metrics

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Average Execution Time | < 5 seconds | > 10 seconds |
| Success Rate | > 99% | < 95% |
| API Call Latency | < 2 seconds | > 5 seconds |
| Database Write Time | < 500ms | > 2 seconds |

### Bottlenecks

**Potential Bottlenecks**:
1. CRM API call (Node 3): 1-3 seconds
2. Slack API rate limits: 1 req/second per channel
3. Database connections: Limited pool

**Optimizations**:
- Parallel execution not applicable (linear dependency)
- Caching CRM data: Consider for frequent lookups
- Async logging: Non-blocking database writes

---

## Dependencies

### External Services

| Service | Purpose | SLA | Fallback |
|---------|---------|-----|----------|
| Slack API | Notifications | 99.9% | Email notification |
| CRM API | User enrichment | 99% | Skip enrichment |
| PostgreSQL | Activity logging | 99.9% | Queue for later |

### Sub-Workflows

None

### Upstream Workflows

**Triggers This Workflow**:
- Customer signup system webhook

**Data Dependencies**:
- Requires valid customer data from signup form

### Downstream Impact

**Workflows Depending on This**:
- Customer analytics dashboard (reads logged data)

---

## Testing Strategy

### Unit Testing

Test each node individually:

**Node 2 (Validation)**:
```json
Test Cases:
1. Valid email: user@example.com → TRUE
2. Invalid email: invalid.email → FALSE
3. Missing email: null → FALSE
```

### Integration Testing

Test complete workflow paths:

**Happy Path**:
1. Input: Valid signup data
2. Expected: Slack notification sent, DB logged, 200 response

**Error Path**:
1. Input: Invalid email
2. Expected: Error response, no Slack message

### Load Testing

**Test Scenarios**:
- 10 concurrent executions: < 5s each
- 100 executions/minute: No rate limit errors
- Sustained load: No memory leaks

---

## Deployment Information

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2024-01-15 | Initial release | Team Name |
| 1.1 | 2024-02-01 | Added CRM enrichment | Developer Name |

### Deployment Checklist

Pre-deployment:
- [ ] All credentials configured in production
- [ ] Error workflow deployed
- [ ] Monitoring dashboard created
- [ ] Team trained on workflow
- [ ] Runbook documented

Post-deployment:
- [ ] Smoke tests passed
- [ ] Monitoring alerts configured
- [ ] Documentation updated
- [ ] Stakeholders notified

---

## Monitoring and Alerts

### Metrics Tracked

**Application Metrics**:
- Execution count (per hour)
- Success/failure ratio
- Average execution time
- Error types and frequencies

**Business Metrics**:
- Customer notifications delivered
- Time to notification (< 30s SLA)
- Notification delivery rate

### Alert Rules

**Critical Alerts** (Page on-call):
- Success rate < 95% over 5 minutes
- No executions in last 30 minutes (during business hours)
- Error rate > 10 errors/minute

**Warning Alerts** (Slack notification):
- Execution time > 10 seconds
- CRM API failures > 5%
- Database connection warnings

---

## Operational Runbook

### Common Issues

**Issue 1: Slack Rate Limiting**
- Symptoms: 429 errors from Slack API
- Cause: Too many messages to same channel
- Solution: Implement message queuing, batch notifications
- Prevention: Monitor notification rate

**Issue 2: CRM API Timeout**
- Symptoms: Node 3 times out
- Cause: CRM service slow response
- Solution: Increase timeout, use cached data
- Prevention: Monitor CRM API health

### Manual Intervention Procedures

**Disable Workflow**:
```
1. Open n8n workflow editor
2. Click "Active" toggle to disable
3. Notify team in #incidents channel
4. Document reason in incident log
```

**Emergency Rollback**:
```
1. Disable current version
2. Activate previous version from backup
3. Verify critical path functionality
4. Monitor for 30 minutes
5. Investigate root cause
```

---

## Design Decisions and Rationale

### Decision 1: Linear vs Parallel Processing

**Decision**: Linear processing
**Rationale**: Each step depends on previous (validation → enrichment → formatting → sending)
**Alternative Considered**: Parallel Slack + DB logging
**Trade-offs**: Slightly slower (500ms) but simpler error handling

### Decision 2: Optional CRM Enrichment

**Decision**: Allow workflow to continue if CRM fails
**Rationale**: Core notification more important than enriched data
**Alternative Considered**: Fail entire workflow on CRM error
**Trade-offs**: Less data quality, but higher reliability

### Decision 3: Synchronous Response

**Decision**: Wait for Slack confirmation before responding
**Rationale**: Ensure notification delivered before confirming to caller
**Alternative Considered**: Async processing with immediate 202 response
**Trade-offs**: Slightly slower response, but guaranteed delivery confirmation

---

## Future Enhancements

**Planned Improvements**:
1. Add email fallback for Slack failures (Priority: High)
2. Implement message templating system (Priority: Medium)
3. Add A/B testing for message formats (Priority: Low)
4. Batch notifications for multiple signups (Priority: Low)

**Technical Debt**:
- CRM API client needs retry logic refactoring
- Database connection pooling optimization needed

---

## References

- **Implementation Guide**: `implementation_guide_[workflow-name].md`
- **Workflow JSON**: `workflow_[workflow-name].json`
- **Implementation Checklist**: `checklist_[workflow-name].md`
- **Validation Report**: `validation_[workflow-name].md`

---

## Contact and Ownership

**Team**: [Team Name]
**Owner**: [Primary Contact]
**Slack Channel**: [#team-channel]
**On-Call**: [Rotation/Person]
**Documentation**: [Link to detailed docs]
