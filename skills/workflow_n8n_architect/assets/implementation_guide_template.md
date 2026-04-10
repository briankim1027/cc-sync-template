# Implementation Guide: [Workflow Name]

Complete node-by-node configuration instructions for implementing this n8n workflow.

---

## Prerequisites

Before starting implementation:
- [ ] n8n instance accessible (v1.0+)
- [ ] Required credentials prepared
- [ ] Network access to external services
- [ ] Test data prepared

---

## Credential Setup

### Credential 1: [Credential Name]

**Type**: [slackApi/gmailOAuth2/httpHeaderAuth/postgres/etc.]
**Purpose**: [What this credential is used for]

**Setup Steps**:
1. [Step 1 description]
2. [Step 2 description]
3. Navigate to n8n → Credentials → Add Credential
4. Select [Credential Type]
5. Configure with values from steps above
6. Test connection
7. Save as "[Credential Display Name]"

**Configuration Values**:
```
Field 1: [value or instruction]
Field 2: [value or instruction]
```

Repeat for each required credential.

---

## Workflow Import

### Option 1: Import JSON File

1. Download `workflow_[workflow-name].json`
2. Open n8n instance
3. Navigate to Workflows
4. Click "Import from File"
5. Select downloaded JSON
6. Verify import successful
7. Proceed to node configuration below

### Option 2: Manual Creation

Follow node-by-node instructions below to build from scratch.

---

## Node-by-Node Configuration

### Node 1: [Node Name]

**Node Type**: `[n8n-nodes-base.webhook]`
**Position**: `[250, 300]`
**Purpose**: [Brief description of what this node does]

#### Configuration

**Basic Parameters**:
```
Parameter Name: Value
HTTP Method: POST
Path: webhook-path-name
Response Mode: When Last Node Finishes
Authentication: Header Auth (if applicable)
```

**Detailed Settings**:

1. **HTTP Method**
   - Select: `POST` (or GET/PUT/DELETE)
   - Why: [Explanation]

2. **Webhook Path**
   - Enter: `/[your-webhook-path]`
   - Example: `/customer-signup`
   - Note: Must be unique across workflows

3. **Response Settings**
   - Response Mode: `onReceived` or `lastNode`
   - Response Data: `firstEntryJson`

4. **Authentication** (if required)
   - Type: Header Auth
   - Credential: [Select credential from dropdown]

#### Node JSON (Reference)

```json
{
  "parameters": {
    "httpMethod": "POST",
    "path": "webhook-path",
    "responseMode": "lastNode"
  },
  "id": "node-uuid-1",
  "name": "[Node Name]",
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 1,
  "position": [250, 300]
}
```

#### Testing This Node

1. Click "Listen for Test Event" or "Execute Node"
2. Send test request:
   ```bash
   curl -X POST https://your-n8n.com/webhook/webhook-path \
     -H "Content-Type: application/json" \
     -d '{"test": "data"}'
   ```
3. Verify data appears in node output
4. Check response is received

#### Expected Output

```json
{
  "headers": {...},
  "params": {},
  "query": {},
  "body": {
    "field1": "value1",
    "field2": "value2"
  }
}
```

#### Common Issues

**Issue**: Webhook returns 404
- **Cause**: Workflow not active or path incorrect
- **Solution**: Activate workflow, verify webhook path

**Issue**: No data received
- **Cause**: Request format mismatch
- **Solution**: Ensure Content-Type header is application/json

---

### Node 2: [Node Name]

**Node Type**: `[n8n-nodes-base.if]`
**Position**: `[450, 300]`
**Purpose**: [Description]

#### Configuration

**Condition Type**: String/Number/Boolean

**Conditions**:
```
Condition 1:
  Value 1: ={{$json["fieldName"]}}
  Operation: equals/contains/etc.
  Value 2: expected-value

Condition 2 (if multiple):
  [Configuration]

Combine: all (AND) or any (OR)
```

**Detailed Steps**:

1. Add IF node to canvas
2. Connect from previous node
3. Configure conditions:
   - Click "Add Condition"
   - Select condition type (string/number/boolean)
   - Set Value 1 using expression: `={{$json["fieldName"]}}`
   - Choose operation
   - Set Value 2 (can be static or expression)

4. **For Multiple Conditions**:
   - Click "Add Condition" again
   - Configure as above
   - Set Combine to:
     - `all`: All conditions must be true (AND logic)
     - `any`: At least one must be true (OR logic)

#### Node JSON

```json
{
  "parameters": {
    "conditions": {
      "string": [
        {
          "value1": "={{$json[\"fieldName\"]}}",
          "operation": "equal",
          "value2": "expected-value"
        }
      ]
    },
    "combineOperation": "all"
  },
  "id": "node-uuid-2",
  "name": "[Node Name]",
  "type": "n8n-nodes-base.if",
  "typeVersion": 1,
  "position": [450, 300]
}
```

#### Testing

Test both TRUE and FALSE paths:

**TRUE Test**:
```json
Input: {"fieldName": "expected-value"}
Expected: Routes to output 0 (TRUE branch)
```

**FALSE Test**:
```json
Input: {"fieldName": "other-value"}
Expected: Routes to output 1 (FALSE branch)
```

#### Common Expressions

```javascript
// Check if field exists
={{$json["field"] !== undefined}}

// Check if not empty
={{$json["field"] && $json["field"].length > 0}}

// Case-insensitive comparison
={{$json["field"].toLowerCase() === "value"}}

// Check number range
={{$json["age"] >= 18 && $json["age"] < 65}}
```

---

### Node 3: [Node Name]

**Node Type**: `[n8n-nodes-base.set]`
**Position**: `[650, 300]`
**Purpose**: [Description]

#### Configuration

**Mode**: Manual (recommended) or JavaScript

**Fields to Set**:

1. **Field Name**: `newFieldName`
   - **Type**: String/Number/Boolean/Object
   - **Value**: `={{$json["sourceField"]}}`
   - **Purpose**: [Why this field is needed]

2. **Field Name**: `computedField`
   - **Type**: String
   - **Value**: `={{$json["first"]}} {{$json["last"]}}`
   - **Purpose**: Combine fields

Repeat for each field.

**Options**:
- Include Other Fields: Yes/No
  - Yes: Keeps existing fields
  - No: Only keeps configured fields

#### Node JSON

```json
{
  "parameters": {
    "mode": "manual",
    "duplicateItem": false,
    "assignments": {
      "assignments": [
        {
          "name": "fieldName",
          "value": "={{$json[\"sourceField\"]}}",
          "type": "string"
        }
      ]
    },
    "options": {
      "includeOtherFields": true
    }
  },
  "id": "node-uuid-3",
  "name": "[Node Name]",
  "type": "n8n-nodes-base.set",
  "typeVersion": 3,
  "position": [650, 300]
}
```

#### Common Transformations

```javascript
// Lowercase email
={{$json["email"].toLowerCase()}}

// Format date
={{new Date($json["date"]).toISOString()}}

// Concatenate strings
={{$json["first"]}} {{$json["last"]}}

// Default value if empty
={{$json["field"] || "default"}}

// Conditional value
={{$json["premium"] ? "VIP" : "Standard"}}

// Extract substring
={{$json["text"].substring(0, 100)}}

// Array operations
={{$json["items"].length}}
={{$json["items"].join(", ")}}
={{$json["items"].map(i => i.name)}}
```

---

### Node 4: [External Service Node]

**Node Type**: `[n8n-nodes-base.slack/gmail/httpRequest]`
**Position**: `[850, 300]`
**Purpose**: [Description]

#### Configuration

**Resource**: [message/channel/etc.]
**Operation**: [post/send/get/etc.]

**Required Fields**:
```
Field 1: [Value or expression]
Field 2: [Value or expression]
```

**Credential**: Select [Credential Name] from dropdown

**Example: Slack Node**:
```
Resource: Message
Operation: Post
Channel: #channel-name
Text: ={{$json["message"]}}
Credential: Slack Production API
```

**Example: HTTP Request Node**:
```
Method: POST
URL: https://api.example.com/endpoint
Authentication: Predefined Credential
Headers:
  - Content-Type: application/json
Body:
  - field1: ={{$json["value1"]}}
  - field2: ={{$json["value2"]}}
```

#### Node JSON

```json
{
  "parameters": {
    "resource": "message",
    "operation": "post",
    "channel": "#channel-name",
    "text": "={{$json[\"message\"]}}"
  },
  "id": "node-uuid-4",
  "name": "[Node Name]",
  "type": "n8n-nodes-base.slack",
  "typeVersion": 2,
  "position": [850, 300],
  "credentials": {
    "slackApi": {
      "id": "credential-uuid",
      "name": "Slack Production API"
    }
  }
}
```

#### Testing

1. Execute node with test data
2. Verify action completed (message sent, API called, etc.)
3. Check external service for result
4. Verify response data is correct

#### Troubleshooting

**Authentication Errors**:
- Verify credential is selected
- Test credential connection
- Check API key/token validity

**Rate Limiting**:
- Add Wait node before this node
- Implement retry logic
- Check API rate limits

---

## Node Connections

After configuring all nodes, connect them:

### Connection Map

```
[Node 1] → [Node 2]
           ├─ TRUE (output 0) → [Node 3] → [Node 4]
           └─ FALSE (output 1) → [Error Node]
```

### Creating Connections

1. Click and drag from output port of source node
2. Drop on input port of target node
3. Verify connection arrow appears
4. For IF/Switch nodes:
   - Output 0 (top): TRUE branch
   - Output 1 (bottom): FALSE branch

---

## End-to-End Testing

### Test Case 1: Happy Path

**Input**:
```json
{
  "field1": "valid-value",
  "field2": "test data"
}
```

**Expected Flow**:
```
Node 1 (Receive) → Node 2 (TRUE) → Node 3 (Transform) → Node 4 (Send)
```

**Expected Output**:
```json
{
  "status": "success",
  "result": "..."
}
```

### Test Case 2: Error Path

**Input**:
```json
{
  "field1": "invalid-value"
}
```

**Expected Flow**:
```
Node 1 (Receive) → Node 2 (FALSE) → Error Handler
```

**Expected Output**:
```json
{
  "status": "error",
  "message": "Validation failed"
}
```

---

## Activation and Deployment

### Pre-Activation Checklist

- [ ] All nodes configured correctly
- [ ] All credentials assigned
- [ ] All connections verified
- [ ] Test executions successful
- [ ] Error paths tested
- [ ] Documentation reviewed

### Activation Steps

1. Click workflow name to edit title
2. Rename to production name
3. Add tags: `[production]`, `[category]`
4. Click "Active" toggle switch
5. Verify "Active" badge appears
6. Test webhook endpoint (if applicable)
7. Monitor first few executions

### Post-Deployment

1. Monitor executions for 1 hour
2. Verify success rate > 99%
3. Check logs for errors
4. Update team documentation
5. Notify stakeholders

---

## Monitoring and Maintenance

### Metrics to Track

- Execution count (hourly/daily)
- Success rate (%)
- Average execution time
- Error rate and types

### Regular Maintenance

**Weekly**:
- Review failed executions
- Check execution times
- Verify credentials valid

**Monthly**:
- Optimize slow nodes
- Update dependencies
- Review and clean execution history

---

## Support and Troubleshooting

### Common Issues

See architecture document for detailed runbook.

### Getting Help

- **Team Channel**: [#team-slack-channel]
- **On-Call**: [Rotation/Contact]
- **Documentation**: [Link]

---

## Appendix: Complete Node List

| # | Node Name | Type | Configuration Complexity |
|---|-----------|------|-------------------------|
| 1 | [Name] | [Type] | Simple/Medium/Complex |
| 2 | [Name] | [Type] | Simple/Medium/Complex |
| ... | ... | ... | ... |

---

**Implementation Time Estimate**: [X hours/days]
**Difficulty Level**: [Beginner/Intermediate/Advanced]
**Last Updated**: [Date]
