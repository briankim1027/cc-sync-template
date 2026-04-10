# N8N Node Connection Patterns

Common patterns for connecting nodes and designing data flow in n8n workflows.

## Basic Connection Patterns

### 1. Linear Flow (Sequential)

**Pattern**: A → B → C → D

**Use Case**: Simple sequential processing

**Example**:
```
[Webhook] → [Validate] → [Transform] → [API Call] → [Respond]
```

**JSON**:
```json
{
  "connections": {
    "Webhook": {
      "main": [[{"node": "Validate", "type": "main", "index": 0}]]
    },
    "Validate": {
      "main": [[{"node": "Transform", "type": "main", "index": 0}]]
    },
    "Transform": {
      "main": [[{"node": "API Call", "type": "main", "index": 0}]]
    },
    "API Call": {
      "main": [[{"node": "Respond", "type": "main", "index": 0}]]
    }
  }
}
```

---

### 2. Conditional Branching (IF)

**Pattern**:
```
A → [IF] → True: B → D
        → False: C → D
```

**Use Case**: Route based on conditions

**Example**:
```
[Webhook] → [IF Premium?]
              ├─ Yes → [Premium Flow] → [Send Email]
              └─ No → [Standard Flow] → [Send Email]
```

**JSON**:
```json
{
  "connections": {
    "Webhook": {
      "main": [[{"node": "IF Premium?", "type": "main", "index": 0}]]
    },
    "IF Premium?": {
      "main": [
        [{"node": "Premium Flow", "type": "main", "index": 0}],
        [{"node": "Standard Flow", "type": "main", "index": 0}]
      ]
    },
    "Premium Flow": {
      "main": [[{"node": "Send Email", "type": "main", "index": 0}]]
    },
    "Standard Flow": {
      "main": [[{"node": "Send Email", "type": "main", "index": 0}]]
    }
  }
}
```

**Key Points**:
- IF node has 2 outputs: index 0 (true), index 1 (false)
- Both branches can merge back to same node

---

### 3. Multi-Way Routing (Switch)

**Pattern**:
```
A → [Switch] → Route 1: B
             → Route 2: C
             → Route 3: D
             → Default: E
```

**Use Case**: Route to multiple paths based on value

**Example**:
```
[Webhook] → [Switch by Priority]
              ├─ Critical → [Page Engineer]
              ├─ High → [Email Team]
              ├─ Medium → [Create Ticket]
              └─ Default → [Log Only]
```

**JSON**:
```json
{
  "connections": {
    "Webhook": {
      "main": [[{"node": "Switch by Priority", "type": "main", "index": 0}]]
    },
    "Switch by Priority": {
      "main": [
        [{"node": "Page Engineer", "type": "main", "index": 0}],
        [{"node": "Email Team", "type": "main", "index": 0}],
        [{"node": "Create Ticket", "type": "main", "index": 0}],
        [{"node": "Log Only", "type": "main", "index": 0}]
      ]
    }
  }
}
```

---

### 4. Parallel Execution

**Pattern**:
```
A → [Split] → B
            → C  → [Merge] → D
            → D
```

**Use Case**: Execute multiple operations simultaneously

**Example**:
```
[Webhook] → [Validate]
              ├─ [Send Slack] ──┐
              ├─ [Send Email] ──┤
              └─ [Log to DB] ────┴─ [Merge] → [Respond]
```

**JSON**:
```json
{
  "connections": {
    "Webhook": {
      "main": [[{"node": "Validate", "type": "main", "index": 0}]]
    },
    "Validate": {
      "main": [[
        {"node": "Send Slack", "type": "main", "index": 0},
        {"node": "Send Email", "type": "main", "index": 0},
        {"node": "Log to DB", "type": "main", "index": 0}
      ]]
    },
    "Send Slack": {
      "main": [[{"node": "Merge", "type": "main", "index": 0}]]
    },
    "Send Email": {
      "main": [[{"node": "Merge", "type": "main", "index": 0}]]
    },
    "Log to DB": {
      "main": [[{"node": "Merge", "type": "main", "index": 0}]]
    },
    "Merge": {
      "main": [[{"node": "Respond", "type": "main", "index": 0}]]
    }
  }
}
```

**Benefits**:
- Faster execution (parallel processing)
- Independent operations don't block each other
- Use Merge node to wait for all completions

---

### 5. Error Handling Pattern

**Pattern**:
```
[Main Flow] → [Try Operation] → Success Path
[Error Workflow] ← [Error Trigger] ← Errors from Main Flow
```

**Example**:
```
Main Workflow:
  [Webhook] → [API Call] → [Process] → [Respond]

Error Workflow:
  [Error Trigger] → [Log Error] → [Notify Admin] → [Store in DLQ]
```

**Main Workflow JSON**:
```json
{
  "name": "Main Workflow",
  "settings": {
    "errorWorkflow": "error-workflow-id"
  },
  "nodes": [...],
  "connections": {...}
}
```

**Error Workflow JSON**:
```json
{
  "name": "Error Handler",
  "nodes": [
    {
      "parameters": {
        "triggerOn": "specificWorkflow",
        "workflowId": "main-workflow-id"
      },
      "name": "Error Trigger",
      "type": "n8n-nodes-base.errorTrigger"
    }
  ],
  "connections": {
    "Error Trigger": {
      "main": [[{"node": "Log Error", "type": "main", "index": 0}]]
    }
  }
}
```

---

### 6. Loop Pattern (Process Array Items)

**Pattern**:
```
[Fetch Items] → [Split Out] → [Process Each] → [Aggregate] → [Summary]
```

**Example**:
```
[Schedule] → [Get Orders] → [Split Out] → [Process Order] → [Aggregate Results] → [Send Summary]
```

**JSON**:
```json
{
  "connections": {
    "Schedule": {
      "main": [[{"node": "Get Orders", "type": "main", "index": 0}]]
    },
    "Get Orders": {
      "main": [[{"node": "Split Out", "type": "main", "index": 0}]]
    },
    "Split Out": {
      "main": [[{"node": "Process Order", "type": "main", "index": 0}]]
    },
    "Process Order": {
      "main": [[{"node": "Aggregate Results", "type": "main", "index": 0}]]
    },
    "Aggregate Results": {
      "main": [[{"node": "Send Summary", "type": "main", "index": 0}]]
    }
  }
}
```

**Split Out Node**:
```json
{
  "parameters": {
    "fieldName": "orders",
    "options": {}
  },
  "name": "Split Out",
  "type": "n8n-nodes-base.splitOut"
}
```

---

### 7. Data Enrichment Pattern

**Pattern**:
```
[Trigger] → [Base Data]
              ├─ [Fetch Detail A] ──┐
              ├─ [Fetch Detail B] ──┤
              └─ [Fetch Detail C] ──┴─ [Merge] → [Combined Data]
```

**Example**:
```
[Webhook] → [Validate]
              ├─ [Get User Profile] ──┐
              ├─ [Get Order History] ──┤
              └─ [Get Preferences] ────┴─ [Merge] → [Send Personalized Email]
```

**JSON**:
```json
{
  "connections": {
    "Webhook": {
      "main": [[{"node": "Validate", "type": "main", "index": 0}]]
    },
    "Validate": {
      "main": [[
        {"node": "Get User Profile", "type": "main", "index": 0},
        {"node": "Get Order History", "type": "main", "index": 0},
        {"node": "Get Preferences", "type": "main", "index": 0}
      ]]
    },
    "Get User Profile": {
      "main": [[{"node": "Merge", "type": "main", "index": 0}]]
    },
    "Get Order History": {
      "main": [[{"node": "Merge", "type": "main", "index": 0}]]
    },
    "Get Preferences": {
      "main": [[{"node": "Merge", "type": "main", "index": 0}]]
    },
    "Merge": {
      "main": [[{"node": "Send Personalized Email", "type": "main", "index": 0}]]
    }
  }
}
```

---

### 8. Retry with Fallback Pattern

**Pattern**:
```
[Try Primary] → Success → [Continue]
              → Fail → [Try Secondary] → Success → [Continue]
                                       → Fail → [Manual Review]
```

**Example**:
```
[Webhook] → [Try Slack API] → [Success Path]
                             → [Error] → [Try Email] → [Success Path]
                                                     → [Error] → [Log for Manual Follow-up]
```

**Implementation**:
Using IF nodes to check for errors:

```json
{
  "connections": {
    "Webhook": {
      "main": [[{"node": "Try Slack API", "type": "main", "index": 0}]]
    },
    "Try Slack API": {
      "main": [[{"node": "Check Slack Success", "type": "main", "index": 0}]]
    },
    "Check Slack Success": {
      "main": [
        [{"node": "Success Path", "type": "main", "index": 0}],
        [{"node": "Try Email", "type": "main", "index": 0}]
      ]
    },
    "Try Email": {
      "main": [[{"node": "Check Email Success", "type": "main", "index": 0}]]
    },
    "Check Email Success": {
      "main": [
        [{"node": "Success Path", "type": "main", "index": 0}],
        [{"node": "Log for Manual Follow-up", "type": "main", "index": 0}]
      ]
    }
  }
}
```

---

## Data Flow Best Practices

### 1. Preserve Original Data

Use Set node with `duplicateItem: false` to preserve original data:

```json
{
  "parameters": {
    "mode": "manual",
    "duplicateItem": false,
    "assignments": {
      "assignments": [
        {
          "name": "enrichedField",
          "value": "={{$json[\"newData\"]}}",
          "type": "string"
        }
      ]
    }
  }
}
```

### 2. Clear Data Transformation Points

Add descriptive Set nodes at key transformation points:

```
[Raw Input] → [Parse JSON] → [Validate Format] → [Transform to Schema] → [Enrich Data]
```

Each node clearly labeled with its transformation purpose.

### 3. Minimize Data Passing

Only pass required fields to reduce payload size:

```json
{
  "parameters": {
    "assignments": {
      "assignments": [
        {
          "name": "userId",
          "value": "={{$json[\"userId\"]}}",
          "type": "string"
        },
        {
          "name": "email",
          "value": "={{$json[\"email\"]}}",
          "type": "string"
        }
      ]
    },
    "options": {
      "dotNotation": false,
      "includeOtherFields": false
    }
  }
}
```

### 4. Use Merge Strategically

Choose appropriate merge mode:

- **Append**: Sequential combination (fastest)
- **Merge by Key**: Combine related data
- **Merge by Index**: Position-based matching

```json
{
  "parameters": {
    "mode": "mergeByKey",
    "propertyName1": "userId",
    "propertyName2": "userId"
  }
}
```

---

## Connection Complexity Guidelines

### Simple Workflows (1-5 nodes)
```
Linear: A → B → C → D
```

- Single path
- No branching
- Straightforward data flow

### Medium Workflows (6-15 nodes)
```
Branched: A → IF → B → D
                 → C → D
```

- Conditional routing
- Some parallel execution
- Error handling

### Complex Workflows (16+ nodes)
```
Multi-path:
  A → Split → B → Merge → E
            → C →       → F
            → D →
```

- Multiple branching
- Parallel processing
- Sub-workflow calls
- Comprehensive error handling

**Recommendation**: Split workflows >20 nodes into sub-workflows

---

## Common Anti-Patterns to Avoid

### ❌ Excessive Nesting
```
IF → IF → IF → IF (too deep)
```

**Solution**: Use Switch node or restructure logic

### ❌ Circular Dependencies
```
A → B → C → A (infinite loop)
```

**Solution**: Add exit conditions or redesign flow

### ❌ Unmerged Parallel Branches
```
A → B → (no continuation)
  → C → (no continuation)
```

**Solution**: Use Merge node or separate workflows

### ❌ Missing Error Paths
```
[API Call] → [Process] (no error handling)
```

**Solution**: Add IF checks or Error Trigger workflow

---

## Connection Testing Checklist

Before finalizing connections:

- [ ] All nodes connected (no orphaned nodes)
- [ ] IF/Switch nodes have all outputs connected
- [ ] Parallel branches properly merged (if needed)
- [ ] Error paths defined
- [ ] Data flow validated (each node receives expected data)
- [ ] No circular dependencies
- [ ] Webhook workflows have response nodes
- [ ] Credentials assigned where needed
