# Connection Mapping Rules

Rules for generating connection JSON from architecture specifications.

## Connection Structure

```json
{
  "connections": {
    "Source Node Name": {
      "main": [
        [
          {
            "node": "Target Node Name",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

## Parsing Connection Specifications

### Format 1: Arrow Notation

**Spec**: `Node A → Node B`
**Generated**:
```json
{
  "Node A": {
    "main": [[{"node": "Node B", "type": "main", "index": 0}]]
  }
}
```

### Format 2: List Format

**Spec**:
```markdown
Connections:
- Webhook → Validate
- Validate → Process
```

**Generated**: Sequential connections for each pair

### Format 3: Branching Format

**Spec**:
```markdown
IF Node:
  - TRUE → Success Path
  - FALSE → Error Path
```

**Generated**:
```json
{
  "IF Node": {
    "main": [
      [{"node": "Success Path", "type": "main", "index": 0}],
      [{"node": "Error Path", "type": "main", "index": 0}]
    ]
  }
}
```

## Branch Index Rules

**IF Node Outputs**:
- Output 0 (index 0): TRUE branch
- Output 1 (index 1): FALSE branch

**Switch Node Outputs**:
- Output 0: First rule match
- Output 1: Second rule match
- Output N: Nth rule or fallback

## Parallel Execution

**Spec**:
```markdown
Node A connects to:
- Node B
- Node C
- Node D
```

**Generated**:
```json
{
  "Node A": {
    "main": [[
      {"node": "Node B", "type": "main", "index": 0},
      {"node": "Node C", "type": "main", "index": 0},
      {"node": "Node D", "type": "main", "index": 0}
    ]]
  }
}
```

## Merge Connections

**Spec**:
```markdown
Node B → Merge
Node C → Merge
Node D → Merge
```

**Generated**: Each source node connects to Merge independently

## Validation Rules

✅ All target nodes must exist
✅ Source node must exist
✅ Output index must match node type
✅ No circular dependencies
✅ IF/Switch nodes must have all outputs connected
✅ No orphaned nodes (except trigger)

## Common Patterns

### Linear Flow
```json
{
  "A": {"main": [[{"node": "B", "type": "main", "index": 0}]]},
  "B": {"main": [[{"node": "C", "type": "main", "index": 0}]]}
}
```

### Conditional Branch
```json
{
  "IF": {
    "main": [
      [{"node": "True Path", "type": "main", "index": 0}],
      [{"node": "False Path", "type": "main", "index": 0}]
    ]
  }
}
```

### Multiple Outputs
```json
{
  "Split": {
    "main": [[
      {"node": "Process A", "type": "main", "index": 0},
      {"node": "Process B", "type": "main", "index": 0}
    ]]
  }
}
```
