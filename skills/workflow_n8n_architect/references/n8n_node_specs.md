# N8N Node JSON Specifications

Complete reference for n8n node JSON structures, parameters, and configuration formats.

## Node Structure Basics

Every n8n node follows this base structure:

```json
{
  "parameters": {},           // Node-specific configuration
  "id": "uuid",              // Unique node identifier
  "name": "Node Name",       // Display name in workflow
  "type": "n8n-nodes-base.nodetype",  // Node type identifier
  "typeVersion": 1,          // Node version
  "position": [x, y],        // Canvas position
  "credentials": {}          // Optional: credential references
}
```

## Trigger Nodes

### Webhook Trigger

```json
{
  "parameters": {
    "httpMethod": "POST",
    "path": "webhook-path",
    "responseMode": "onReceived",
    "responseData": "firstEntryJson",
    "options": {
      "rawBody": false,
      "allowedOrigins": ""
    }
  },
  "id": "webhook-node-id",
  "name": "Webhook",
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 1,
  "position": [250, 300],
  "webhookId": "generated-webhook-id"
}
```

**Parameters**:
- `httpMethod`: "GET" | "POST" | "PUT" | "DELETE" | "PATCH" | "HEAD"
- `path`: Webhook URL path (string)
- `responseMode`: "onReceived" | "lastNode" | "responseNode"
- `responseData`: "firstEntryJson" | "firstEntryBinary" | "allEntries" | "noData"
- `options.rawBody`: boolean (preserve raw request body)
- `options.allowedOrigins`: string (CORS origins)

**Authentication**:
```json
{
  "parameters": {
    "authentication": "headerAuth",
    "options": {}
  },
  "credentials": {
    "httpHeaderAuth": {
      "id": "credential-id",
      "name": "Header Auth"
    }
  }
}
```

### Schedule Trigger

```json
{
  "parameters": {
    "rule": {
      "interval": [
        {
          "field": "cronExpression",
          "expression": "0 9 * * 1-5"
        }
      ]
    }
  },
  "id": "schedule-node-id",
  "name": "Schedule",
  "type": "n8n-nodes-base.scheduleTrigger",
  "typeVersion": 1,
  "position": [250, 300]
}
```

**Cron Expressions**:
- Daily at 9am: `"0 9 * * *"`
- Every 6 hours: `"0 */6 * * *"`
- Weekdays at 2pm: `"0 14 * * 1-5"`
- First of month: `"0 0 1 * *"`

### Manual Trigger

```json
{
  "parameters": {},
  "id": "manual-trigger-id",
  "name": "When clicking 'Test workflow'",
  "type": "n8n-nodes-base.manualTrigger",
  "typeVersion": 1,
  "position": [250, 300]
}
```

## Logic Nodes

### IF Node

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
      ],
      "number": [
        {
          "value1": "={{$json[\"age\"]}}",
          "operation": "larger",
          "value2": 18
        }
      ]
    },
    "combineOperation": "all"
  },
  "id": "if-node-id",
  "name": "Check Status",
  "type": "n8n-nodes-base.if",
  "typeVersion": 1,
  "position": [450, 300]
}
```

**Condition Types**:
- `string`: String comparisons
- `number`: Numeric comparisons
- `boolean`: True/false checks
- `dateTime`: Date/time comparisons

**String Operations**:
- `equal`, `notEqual`, `contains`, `notContains`
- `startsWith`, `notStartsWith`, `endsWith`, `notEndsWith`
- `regex`, `isEmpty`, `isNotEmpty`

**Number Operations**:
- `equal`, `notEqual`, `larger`, `largerEqual`, `smaller`, `smallerEqual`
- `isEmpty`, `isNotEmpty`

**Combine Operations**:
- `all`: AND (all conditions must match)
- `any`: OR (at least one condition must match)

### Switch Node

```json
{
  "parameters": {
    "mode": "rules",
    "rules": {
      "rules": [
        {
          "name": "Premium Users",
          "renameOutput": true,
          "outputKey": "premium",
          "conditions": {
            "string": [
              {
                "value1": "={{$json[\"plan\"]}}",
                "operation": "equal",
                "value2": "premium"
              }
            ]
          }
        },
        {
          "name": "Standard Users",
          "renameOutput": true,
          "outputKey": "standard",
          "conditions": {
            "string": [
              {
                "value1": "={{$json[\"plan\"]}}",
                "operation": "equal",
                "value2": "standard"
              }
            ]
          }
        }
      ]
    },
    "fallbackOutput": "extra"
  },
  "id": "switch-node-id",
  "name": "Route by Plan",
  "type": "n8n-nodes-base.switch",
  "typeVersion": 1,
  "position": [450, 300]
}
```

**Modes**:
- `rules`: Evaluate conditions for each output
- `expression`: Use JavaScript expression

## Data Processing Nodes

### Set Node

```json
{
  "parameters": {
    "mode": "manual",
    "duplicateItem": false,
    "assignments": {
      "assignments": [
        {
          "name": "fullName",
          "value": "={{$json[\"firstName\"]}} {{$json[\"lastName\"]}}",
          "type": "string"
        },
        {
          "name": "timestamp",
          "value": "={{new Date().toISOString()}}",
          "type": "string"
        },
        {
          "name": "isActive",
          "value": "={{$json[\"status\"] === \"active\"}}",
          "type": "boolean"
        }
      ]
    },
    "options": {}
  },
  "id": "set-node-id",
  "name": "Transform Data",
  "type": "n8n-nodes-base.set",
  "typeVersion": 3,
  "position": [650, 300]
}
```

**Field Types**:
- `string`: Text values
- `number`: Numeric values
- `boolean`: True/false
- `array`: Arrays
- `object`: Objects

### Code Node (JavaScript)

```json
{
  "parameters": {
    "mode": "runOnceForAllItems",
    "jsCode": "// Access all input items\nconst items = $input.all();\n\n// Process each item\nfor (const item of items) {\n  item.json.processed = true;\n  item.json.timestamp = new Date().toISOString();\n}\n\nreturn items;"
  },
  "id": "code-node-id",
  "name": "Custom Logic",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [650, 300]
}
```

**Modes**:
- `runOnceForAllItems`: Process all items together
- `runOnceForEachItem`: Process items individually

**Available Objects**:
- `$input`: Access input data
- `$json`: Current item's JSON data (in runOnceForEachItem mode)
- `$binary`: Binary data
- `$env`: Environment variables
- `$now`: Current date/time
- `$today`: Today's date

### Merge Node

```json
{
  "parameters": {
    "mode": "append",
    "options": {}
  },
  "id": "merge-node-id",
  "name": "Merge",
  "type": "n8n-nodes-base.merge",
  "typeVersion": 2,
  "position": [850, 300]
}
```

**Modes**:
- `append`: Combine all items sequentially
- `keepKeyMatches`: Match items by key field
- `mergeByIndex`: Merge items at same index
- `mergeByPosition`: Combine items by position
- `multiplex`: Create all combinations

## Communication Nodes

### Slack Node

```json
{
  "parameters": {
    "resource": "message",
    "operation": "post",
    "channel": "#general",
    "text": "={{$json[\"message\"]}}",
    "attachments": [],
    "otherOptions": {
      "mrkdwn": true,
      "username": "n8n Bot"
    }
  },
  "id": "slack-node-id",
  "name": "Send to Slack",
  "type": "n8n-nodes-base.slack",
  "typeVersion": 2,
  "position": [850, 300],
  "credentials": {
    "slackApi": {
      "id": "credential-id",
      "name": "Slack API"
    }
  }
}
```

**Message Formatting** (Slack Blocks):
```json
{
  "parameters": {
    "blocksUi": {
      "blocksValues": [
        {
          "type": "section",
          "text": {
            "type": "mrkdwn",
            "text": "*New Customer Signup*\n\nName: {{$json[\"name\"]}}\nEmail: {{$json[\"email\"]}}"
          }
        }
      ]
    }
  }
}
```

### Gmail Node

```json
{
  "parameters": {
    "resource": "message",
    "operation": "send",
    "emailType": "html",
    "toList": "={{$json[\"email\"]}}",
    "subject": "={{$json[\"subject\"]}}",
    "message": "<h1>Welcome!</h1><p>Thank you for signing up.</p>",
    "options": {
      "ccList": "",
      "bccList": "",
      "replyTo": "noreply@example.com"
    }
  },
  "id": "gmail-node-id",
  "name": "Send Email",
  "type": "n8n-nodes-base.gmail",
  "typeVersion": 2,
  "position": [850, 300],
  "credentials": {
    "gmailOAuth2": {
      "id": "credential-id",
      "name": "Gmail OAuth2"
    }
  }
}
```

### HTTP Request Node

```json
{
  "parameters": {
    "method": "POST",
    "url": "https://api.example.com/users",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "httpHeaderAuth",
    "sendHeaders": true,
    "headerParameters": {
      "parameters": [
        {
          "name": "Content-Type",
          "value": "application/json"
        }
      ]
    },
    "sendBody": true,
    "bodyParameters": {
      "parameters": [
        {
          "name": "email",
          "value": "={{$json[\"email\"]}}"
        },
        {
          "name": "name",
          "value": "={{$json[\"name\"]}}"
        }
      ]
    },
    "options": {
      "timeout": 30000,
      "redirect": {
        "redirect": {
          "followRedirects": true,
          "maxRedirects": 5
        }
      }
    }
  },
  "id": "http-node-id",
  "name": "API Call",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [650, 300],
  "credentials": {
    "httpHeaderAuth": {
      "id": "credential-id",
      "name": "API Key Header"
    }
  }
}
```

**Methods**: GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS

**Authentication Types**:
- `none`: No authentication
- `predefinedCredentialType`: Use n8n credentials
- `genericCredentialType`: Generic auth

**Body Types**:
- `json`: JSON body
- `form`: Form data
- `formData`: Multipart form data
- `raw`: Raw body
- `n8n-binary-data`: Binary data

## Database Nodes

### Postgres Node

```json
{
  "parameters": {
    "operation": "executeQuery",
    "query": "INSERT INTO users (email, name, created_at) VALUES ($1, $2, NOW())",
    "additionalFields": {
      "queryParameters": "={{$json[\"email\"]}},={{$json[\"name\"]}}"
    }
  },
  "id": "postgres-node-id",
  "name": "Insert User",
  "type": "n8n-nodes-base.postgres",
  "typeVersion": 2,
  "position": [850, 300],
  "credentials": {
    "postgres": {
      "id": "credential-id",
      "name": "Postgres DB"
    }
  }
}
```

**Operations**:
- `executeQuery`: Execute raw SQL
- `insert`: Insert records
- `update`: Update records
- `delete`: Delete records

### Google Sheets Node

```json
{
  "parameters": {
    "operation": "append",
    "documentId": {
      "__rl": true,
      "value": "spreadsheet-id",
      "mode": "id"
    },
    "sheetName": {
      "__rl": true,
      "value": "Sheet1",
      "mode": "name"
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": {
        "email": "={{$json[\"email\"]}}",
        "name": "={{$json[\"name\"]}}",
        "timestamp": "={{new Date().toISOString()}}"
      }
    },
    "options": {}
  },
  "id": "sheets-node-id",
  "name": "Log to Sheet",
  "type": "n8n-nodes-base.googleSheets",
  "typeVersion": 4,
  "position": [1050, 300],
  "credentials": {
    "googleSheetsOAuth2Api": {
      "id": "credential-id",
      "name": "Google Sheets OAuth2"
    }
  }
}
```

## Utility Nodes

### Respond to Webhook

```json
{
  "parameters": {
    "options": {
      "responseCode": 200,
      "responseHeaders": {
        "entries": [
          {
            "name": "Content-Type",
            "value": "application/json"
          }
        ]
      },
      "responseBody": "={{{\n  \"status\": \"success\",\n  \"id\": $json[\"id\"],\n  \"message\": \"Processed successfully\"\n}}}",
      "responseData": "noData"
    }
  },
  "id": "respond-node-id",
  "name": "Respond",
  "type": "n8n-nodes-base.respondToWebhook",
  "typeVersion": 1,
  "position": [1250, 300]
}
```

### Wait Node

```json
{
  "parameters": {
    "unit": "seconds",
    "amount": 300,
    "resume": "afterTimeInterval"
  },
  "id": "wait-node-id",
  "name": "Wait 5 Minutes",
  "type": "n8n-nodes-base.wait",
  "typeVersion": 1,
  "position": [850, 300]
}
```

**Resume Modes**:
- `afterTimeInterval`: Wait fixed duration
- `atSpecificTime`: Wait until specific date/time
- `onWebhookCall`: Wait for webhook trigger

## Error Handling Nodes

### Error Trigger

```json
{
  "parameters": {
    "triggerOn": "specificWorkflow",
    "workflowId": {
      "__rl": true,
      "value": "workflow-id",
      "mode": "id"
    }
  },
  "id": "error-trigger-id",
  "name": "Error Handler",
  "type": "n8n-nodes-base.errorTrigger",
  "typeVersion": 1,
  "position": [250, 500]
}
```

### Stop and Error Node

```json
{
  "parameters": {
    "errorMessage": "={{\"Validation failed: \" + $json[\"error\"]}}"
  },
  "id": "stop-error-node-id",
  "name": "Stop with Error",
  "type": "n8n-nodes-base.stopAndError",
  "typeVersion": 1,
  "position": [650, 500]
}
```

## Connection Structure

Connections link nodes together:

```json
{
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Validate Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Validate Data": {
      "main": [
        [
          {
            "node": "Process Success",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Handle Error",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

**Connection Structure**:
- Key: Source node name
- `main`: Array of output branches
- Each branch: Array of connections
- Each connection:
  - `node`: Target node name
  - `type`: Connection type ("main")
  - `index`: Output index (0-based)

**Multiple Outputs** (IF/Switch nodes):
```json
{
  "IF Node": {
    "main": [
      [
        {
          "node": "True Branch",
          "type": "main",
          "index": 0
        }
      ],
      [
        {
          "node": "False Branch",
          "type": "main",
          "index": 0
        }
      ]
    ]
  }
}
```

## Credential References

```json
{
  "credentials": {
    "slackApi": {
      "id": "credential-uuid",
      "name": "Slack Account"
    },
    "gmailOAuth2": {
      "id": "credential-uuid",
      "name": "Gmail OAuth2"
    }
  }
}
```

## Common Expression Patterns

**Access JSON Fields**:
```javascript
{{$json["fieldName"]}}
{{$json["nested"]["field"]}}
{{$json["array"][0]}}
```

**String Operations**:
```javascript
{{$json["email"].toLowerCase()}}
{{$json["name"].toUpperCase()}}
{{$json["text"].trim()}}
{{$json["str"].substring(0, 10)}}
```

**Date/Time**:
```javascript
{{new Date().toISOString()}}
{{new Date($json["date"]).toLocaleDateString()}}
{{Date.now()}}
```

**Conditionals**:
```javascript
{{$json["status"] === "active" ? "Active User" : "Inactive"}}
{{$json["age"] >= 18 ? "adult" : "minor"}}
```

**Array Operations**:
```javascript
{{$json["items"].length}}
{{$json["items"].join(", ")}}
{{$json["items"].map(i => i.name)}}
```

## Node Positioning

Nodes are positioned on a canvas with [x, y] coordinates:

```json
{
  "position": [250, 300]
}
```

**Layout Guidelines**:
- Horizontal spacing: 200-250 pixels between nodes
- Vertical spacing: 200 pixels for parallel branches
- Start position: [250, 300] for first node
- Flow left-to-right for linear workflows
- Use vertical space for conditional branches

**Example Layout**:
```
Node 1: [250, 300]   (Trigger)
Node 2: [500, 300]   (Processing)
Node 3a: [750, 200]  (Success branch)
Node 3b: [750, 400]  (Error branch)
Node 4: [1000, 300]  (Final)
```

## Workflow Metadata

Complete workflow structure:

```json
{
  "name": "Workflow Name",
  "nodes": [...],
  "connections": {...},
  "pinData": {},
  "settings": {
    "executionOrder": "v1",
    "saveManualExecutions": true,
    "callerPolicy": "workflowsFromSameOwner",
    "errorWorkflow": "workflow-id"
  },
  "staticData": null,
  "tags": [
    {
      "createdAt": "2024-01-01T00:00:00.000Z",
      "updatedAt": "2024-01-01T00:00:00.000Z",
      "id": "tag-id",
      "name": "production"
    }
  ],
  "triggerCount": 1,
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "versionId": "version-uuid"
}
```

**Settings**:
- `executionOrder`: "v0" | "v1" (execution order version)
- `saveManualExecutions`: boolean (save manual test runs)
- `callerPolicy`: Workflow calling permissions
- `errorWorkflow`: ID of error handling workflow
