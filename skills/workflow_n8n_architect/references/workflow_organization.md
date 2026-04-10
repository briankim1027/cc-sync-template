# N8N Workflow Organization Best Practices

Guidelines for structuring, organizing, and managing n8n workflows at scale.

## Workflow Naming Conventions

### Standard Format
```
[Environment] [Category] - [Purpose]
```

**Examples**:
- `[PROD] Customer - Signup Notifications`
- `[DEV] Billing - Invoice Generation`
- `[STAGING] Support - Ticket Routing`

### Categories
- **Customer**: Customer-facing automations
- **Internal**: Internal operations
- **Integration**: Third-party integrations
- **Monitoring**: System monitoring and alerts
- **Data**: Data processing and ETL

---

## Workflow Complexity Management

### Simple Workflows (1-10 nodes)
- Single responsibility
- Linear or simple branching
- Keep in one workflow

**Example**: Send Slack notification on form submission

### Medium Workflows (11-20 nodes)
- Multiple steps with branching
- Some parallel processing
- Consider sub-workflows for repeated logic

**Example**: Customer onboarding with multiple notifications

### Complex Workflows (21+ nodes)
- **Required**: Break into sub-workflows
- Use Execute Workflow nodes
- Maintain clear boundaries

**Example**: Order processing with payment, inventory, shipping, notifications

---

## Sub-Workflow Pattern

### When to Use Sub-Workflows

1. **Reusable Logic**: Same operation used in multiple workflows
2. **Complexity Reduction**: Main workflow >20 nodes
3. **Team Boundaries**: Different teams own different parts
4. **Testing**: Isolate testable components

### Sub-Workflow Structure

**Main Workflow**:
```
[Trigger] → [Validate] → [Execute: Process Order] → [Execute: Send Notifications]
```

**Sub-Workflow: Process Order**:
```
[Workflow Trigger] → [Check Inventory] → [Process Payment] → [Update Database]
```

**Sub-Workflow: Send Notifications**:
```
[Workflow Trigger] → [Email Customer] → [Slack Sales Team] → [Update CRM]
```

### Execute Workflow Node

```json
{
  "parameters": {
    "source": "database",
    "workflowId": {
      "__rl": true,
      "value": "sub-workflow-id",
      "mode": "id"
    },
    "options": {}
  },
  "name": "Execute: Process Order",
  "type": "n8n-nodes-base.executeWorkflow",
  "typeVersion": 1
}
```

### Data Passing

**Parent to Sub-Workflow**:
```json
{
  "parameters": {
    "workflowInputData": "={{$json}}"
  }
}
```

**Sub-Workflow to Parent**:
Sub-workflow's final node output is returned to parent.

---

## Workflow Folder Structure

Organize workflows conceptually (using tags):

```
Production Workflows/
├── Customer Facing/
│   ├── Signup Notifications
│   ├── Order Confirmations
│   └── Account Updates
├── Internal Operations/
│   ├── Daily Reports
│   ├── Data Backups
│   └── System Monitoring
└── Integrations/
    ├── CRM Sync
    ├── Analytics Export
    └── Payment Processing
```

**Implementation**: Use n8n tags

```json
{
  "tags": [
    {
      "id": "tag-id-1",
      "name": "production"
    },
    {
      "id": "tag-id-2",
      "name": "customer-facing"
    }
  ]
}
```

---

## Node Organization Within Workflows

### 1. Visual Layout

**Horizontal Flow** (Left to Right):
```
[Trigger] → [Process 1] → [Process 2] → [Output]
```

**Vertical Branching**:
```
         → [Success Path] →
[Split]                    [Merge]
         → [Error Path] →
```

**Standard Positions**:
- Start: `[250, 300]`
- Horizontal spacing: 200px
- Vertical spacing: 200px for branches

### 2. Node Naming

**Descriptive Names**:
- ✅ "Validate Email Format"
- ✅ "Fetch User from CRM"
- ✅ "Send Slack to #sales"
- ❌ "HTTP Request"
- ❌ "IF"
- ❌ "Set"

**Naming Pattern**: `[Action] [Object] [Context]`

**Examples**:
- "Check if Premium User"
- "Transform to API Format"
- "Log Error to Database"

### 3. Color Coding

Use node colors to indicate purpose:

- 🔴 **Red**: Error handling nodes
- 🟢 **Green**: Success paths
- 🟡 **Yellow**: Conditional logic
- 🔵 **Blue**: Data transformation
- ⚪ **Gray**: Logging/debugging
- 🟣 **Purple**: External API calls

### 4. Sticky Notes

Add workflow documentation:

```json
{
  "name": "Workflow Note",
  "type": "n8n-nodes-base.stickyNote",
  "typeVersion": 1,
  "position": [250, 150],
  "parameters": {
    "content": "## Customer Signup Flow\n\nProcesses new customer signups:\n1. Validates data\n2. Creates CRM record\n3. Sends notifications\n\nSLA: < 5 seconds",
    "height": 200,
    "width": 400
  }
}
```

**Use Cases**:
- Workflow overview
- Complex logic explanation
- SLA requirements
- Known issues/limitations

---

## Workflow Templates

Create reusable workflow templates:

### Template: Webhook → Process → Notify

**Base Structure**:
```
[Webhook Trigger]
  → [Validate Input]
  → [IF Valid?]
      ├─ Yes → [Process Data] → [Send Success Notification] → [Respond 200]
      └─ No → [Send Error Notification] → [Respond 400]
```

**Variables to Replace**:
- Webhook path
- Validation rules
- Processing logic
- Notification channels

### Template: Scheduled Report

**Base Structure**:
```
[Schedule Trigger]
  → [Fetch Data]
  → [Transform to Report Format]
  → [Generate Charts/Tables]
  → [Send Email Report]
  → [Log Execution]
```

---

## Version Control Integration

### Git Workflow for n8n

1. **Export Workflows**:
```bash
# Export workflow JSON
curl -X GET http://n8n:5678/api/v1/workflows/123 > workflow.json
```

2. **Commit to Git**:
```bash
git add workflows/
git commit -m "Update customer signup workflow"
git push
```

3. **Import to n8n**:
```bash
# Import workflow
curl -X POST http://n8n:5678/api/v1/workflows \
  -H "Content-Type: application/json" \
  -d @workflow.json
```

### Branching Strategy

```
main (production workflows)
  ├─ develop (development workflows)
  ├─ feature/new-integration
  └─ hotfix/urgent-fix
```

---

## Workflow Dependencies

### Mapping Dependencies

Document which workflows depend on others:

```yaml
workflow: "Customer Signup"
depends_on:
  - "Create CRM Record" (sub-workflow)
  - "Send Welcome Email" (sub-workflow)
  - "Error Handler" (error workflow)

workflow: "Create CRM Record"
depends_on:
  - CRM API credential
  - Customer Database credential

workflow: "Send Welcome Email"
depends_on:
  - Gmail OAuth2 credential
  - Email Templates (external resource)
```

### Dependency Management

Create a dependency matrix:

| Workflow | Sub-Workflows | Credentials | External APIs |
|----------|---------------|-------------|---------------|
| Customer Signup | Create CRM Record, Send Email | Gmail, CRM API | CRM, Email Service |
| Order Processing | Process Payment, Update Inventory | Stripe, PostgreSQL | Stripe, Inventory API |

---

## Error Workflow Organization

### Centralized Error Handler

**Pattern**: One error workflow per workflow category

```
Customer Workflows → "Customer Error Handler"
Billing Workflows → "Billing Error Handler"
Integration Workflows → "Integration Error Handler"
```

**Error Handler Structure**:
```
[Error Trigger]
  → [Parse Error Details]
  → [Switch by Error Type]
      ├─ Critical → [Page On-Call] + [Create Incident]
      ├─ Warning → [Send Slack Alert]
      └─ Info → [Log to Database]
  → [Update Error Dashboard]
```

---

## Workflow Documentation Standards

### Required Documentation

**In Workflow (Sticky Notes)**:
1. Overview: Purpose and high-level flow
2. Prerequisites: Required credentials, external services
3. SLA: Expected execution time
4. Contact: Team/person responsible

**External Documentation**:
1. README.md: Detailed explanation
2. CHANGELOG.md: Version history
3. RUNBOOK.md: Troubleshooting guide

### README Template

```markdown
# Workflow: Customer Signup Notifications

## Purpose
Sends Slack and email notifications when new customers sign up.

## Trigger
Webhook: POST /customer-signup

## Data Flow
1. Receive signup data via webhook
2. Validate required fields
3. Create CRM record
4. Send Slack notification to #sales
5. Send welcome email to customer
6. Log activity to database

## Dependencies
- Credentials: Slack API, Gmail OAuth2, PostgreSQL
- Sub-Workflows: Create CRM Record, Send Welcome Email
- External Services: CRM API, Email Service

## SLA
- Execution time: < 5 seconds
- Success rate: > 99%

## Error Handling
- Retries: 3 attempts with exponential backoff
- Error Workflow: "Customer Error Handler"
- Alerting: Slack #alerts channel

## Testing
See TESTING.md for test procedures

## Contact
Team: Customer Success
Owner: @jane-doe
```

---

## Performance Optimization

### 1. Minimize Node Count

Combine operations where possible:

**Before** (3 nodes):
```
[Set: Add Field 1] → [Set: Add Field 2] → [Set: Add Field 3]
```

**After** (1 node):
```
[Set: Add All Fields]
```

### 2. Use Parallel Execution

Independent operations should run in parallel:

**Sequential** (slow):
```
[API Call 1] → [API Call 2] → [API Call 3]
Total: 15 seconds
```

**Parallel** (fast):
```
      → [API Call 1] →
[Split]→ [API Call 2] → [Merge]
      → [API Call 3] →
Total: 5 seconds
```

### 3. Batch Operations

Process items in batches:

```
[Fetch 1000 Items] → [Split to Batches of 100] → [Process Batch] → [Aggregate]
```

### 4. Cache Frequently Accessed Data

Use static data or external cache:

```
[Check Cache] → IF cached
                  ├─ Yes → [Use Cached Data]
                  └─ No → [Fetch from API] → [Update Cache]
```

---

## Workflow Lifecycle

### Development → Staging → Production

**Development**:
- Tag: `[DEV]`
- Test credentials
- Manual trigger
- Frequent changes

**Staging**:
- Tag: `[STAGING]`
- Production-like credentials
- Real triggers
- Final validation

**Production**:
- Tag: `[PROD]`
- Production credentials
- Active triggers
- Change control required

### Deployment Checklist

- [ ] Code review completed
- [ ] All tests passing
- [ ] Credentials configured
- [ ] Error handling tested
- [ ] Documentation updated
- [ ] Monitoring enabled
- [ ] Team notified
- [ ] Rollback plan ready

---

## Monitoring and Observability

### Execution Logging

Add logging nodes at key points:

```
[Start] → [Log: Started]
        → [Process]
        → [Log: Completed]
        → [Error Handler] → [Log: Failed]
```

### Metrics to Track

- Execution count (per hour/day)
- Success rate (%)
- Average execution time (seconds)
- Error rate (%)
- API call counts

### Dashboards

Create monitoring dashboards:

```
Workflow Dashboard:
- Total executions today
- Success rate (last 24h)
- Error count (last hour)
- Slowest executions
- Most common errors
```

---

## Cleanup and Maintenance

### Regular Maintenance Tasks

**Weekly**:
- Review failed executions
- Check execution times
- Validate credentials

**Monthly**:
- Archive old executions
- Update dependencies
- Review and optimize slow workflows
- Audit credential usage

**Quarterly**:
- Major version updates
- Architecture review
- Performance optimization
- Documentation update

### Deprecation Process

1. **Mark as Deprecated**: Add tag `[DEPRECATED]`
2. **Document Replacement**: Link to new workflow
3. **Grace Period**: 30 days minimum
4. **Disable**: Turn off workflow
5. **Archive**: Move to archive folder
6. **Delete**: After 90 days retention
