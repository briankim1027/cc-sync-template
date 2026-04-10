# Node Generation Rules

Rules and patterns for generating n8n node JSON from architecture specifications.

## General Node Structure

Every node must include:
```json
{
  "parameters": {},      // Node-specific config
  "id": "uuid",         // Unique identifier
  "name": "Node Name",  // Display name
  "type": "n8n-nodes-base.nodetype",
  "typeVersion": 1,     // Node version
  "position": [x, y]    // Canvas position
}
```

## Node Type Mapping

| Specification | n8n Node Type | typeVersion |
|---------------|---------------|-------------|
| Webhook/HTTP Trigger | n8n-nodes-base.webhook | 1 |
| Schedule/Cron | n8n-nodes-base.scheduleTrigger | 1 |
| Manual | n8n-nodes-base.manualTrigger | 1 |
| IF/Conditional | n8n-nodes-base.if | 1 |
| Switch | n8n-nodes-base.switch | 1 |
| Set/Transform | n8n-nodes-base.set | 3 |
| Code/Function | n8n-nodes-base.code | 2 |
| HTTP Request | n8n-nodes-base.httpRequest | 4 |
| Slack | n8n-nodes-base.slack | 2 |
| Gmail | n8n-nodes-base.gmail | 2 |
| PostgreSQL | n8n-nodes-base.postgres | 2 |
| Google Sheets | n8n-nodes-base.googleSheets | 4 |
| Respond Webhook | n8n-nodes-base.respondToWebhook | 1 |
| Wait | n8n-nodes-base.wait | 1 |
| Merge | n8n-nodes-base.merge | 2 |

## Parameter Generation Rules

### Rule 1: Extract from Specification

**Specification Example**:
```markdown
### Node: Validate Email
Type: IF
Condition: email field is not empty
```

**Generated Parameters**:
```json
{
  "parameters": {
    "conditions": {
      "string": [
        {
          "value1": "={{$json[\"email\"]}}",
          "operation": "isNotEmpty"
        }
      ]
    }
  }
}
```

### Rule 2: Apply Defaults

If parameter not specified, use sensible defaults:

**Webhook Defaults**:
```json
{
  "parameters": {
    "httpMethod": "POST",
    "responseMode": "onReceived",
    "options": {}
  }
}
```

**Set Node Defaults**:
```json
{
  "parameters": {
    "mode": "manual",
    "duplicateItem": false,
    "options": {
      "includeOtherFields": true
    }
  }
}
```

### Rule 3: Transform Expressions

Convert natural language to n8n expressions:

| Specification | n8n Expression |
|---------------|----------------|
| "email field" | `={{$json["email"]}}` |
| "user's name" | `={{$json["name"]}}` |
| "current timestamp" | `={{new Date().toISOString()}}` |
| "lowercase email" | `={{$json["email"].toLowerCase()}}` |
| "combine first and last" | `={{$json["first"]}} {{$json["last"]}}` |

## Position Calculation

### Layout Rules

**Horizontal Spacing**: 200px between nodes
**Vertical Spacing**: 200px for branches
**Start Position**: [250, 300]

**Calculation**:
```python
def calculate_position(node_index, branch_index=0):
    x = 250 + (node_index * 200)
    y = 300 + (branch_index * 200)
    return [x, y]
```

**Examples**:
- Node 1 (Trigger): [250, 300]
- Node 2: [450, 300]
- Node 3a (TRUE branch): [650, 200]
- Node 3b (FALSE branch): [650, 400]
- Node 4 (Merge): [850, 300]

## ID Generation

**Rule**: Generate unique UUIDs for each node

```python
import uuid

node_id = str(uuid.uuid4())
# Example: "550e8400-e29b-41d4-a716-446655440000"
```

**Webhook Nodes**: Also generate webhookId
```python
webhook_id = str(uuid.uuid4())
```

## Credential Mapping

**Specification**:
```markdown
Credential: Slack Production API (slackApi)
```

**Generated**:
```json
{
  "credentials": {
    "slackApi": {
      "id": "credential-placeholder-id",
      "name": "Slack Production API"
    }
  }
}
```

**Note**: Credential IDs are placeholders - replaced on import

## Common Transformations

### Webhook Node

**Spec**: "POST webhook at /customer-signup"
**JSON**:
```json
{
  "parameters": {
    "httpMethod": "POST",
    "path": "customer-signup",
    "responseMode": "onReceived"
  },
  "type": "n8n-nodes-base.webhook"
}
```

### IF Node

**Spec**: "Check if status equals 'active'"
**JSON**:
```json
{
  "parameters": {
    "conditions": {
      "string": [
        {
          "value1": "={{$json[\"status\"]}}",
          "operation": "equal",
          "value2": "active"
        }
      ]
    }
  },
  "type": "n8n-nodes-base.if"
}
```

### Set Node

**Spec**: "Add timestamp field with current time"
**JSON**:
```json
{
  "parameters": {
    "mode": "manual",
    "assignments": {
      "assignments": [
        {
          "name": "timestamp",
          "value": "={{new Date().toISOString()}}",
          "type": "string"
        }
      ]
    }
  },
  "type": "n8n-nodes-base.set"
}
```

### HTTP Request

**Spec**: "POST to https://api.example.com/users with email and name"
**JSON**:
```json
{
  "parameters": {
    "method": "POST",
    "url": "https://api.example.com/users",
    "sendBody": true,
    "bodyParameters": {
      "parameters": [
        {"name": "email", "value": "={{$json[\"email\"]}}"},
        {"name": "name", "value": "={{$json[\"name\"]}}"}
      ]
    }
  },
  "type": "n8n-nodes-base.httpRequest"
}
```

## Validation Rules

After generation, validate:

✅ All required fields present
✅ Valid node type
✅ Parameters match node type schema
✅ Expressions properly formatted
✅ Position values are numbers
✅ ID is unique
✅ Credentials structure valid
