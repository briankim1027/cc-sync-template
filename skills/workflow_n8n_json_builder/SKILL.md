---
name: n8n-workflow-json-builder
description: Transform workflow architecture documents into production-ready, executable n8n JSON files. Takes detailed design specifications from n8n-workflow-architect and generates valid, importable n8n workflow JSON with complete node configurations, connections, and credential references. Performs validation and feasibility checks to ensure complex workflows execute correctly. Use when you have architecture documentation and need to create actual n8n workflow JSON files ready for import.
---

# N8N Workflow JSON Builder

## Overview

This skill transforms workflow architecture documents into executable n8n JSON files. It bridges the final gap between design (from `n8n_workflow_architect`) and deployment by generating production-ready JSON that can be directly imported into n8n.

## When to Use This Skill

Activate this skill when:
- You have complete workflow architecture documentation
- You need to generate importable n8n JSON files
- You want to validate JSON structure and feasibility
- You need to convert node specifications to actual JSON

**Input Requirements**:
- Architecture design document
- Node-by-node implementation guide
- OR: Structured workflow specification

**Do NOT use** for:
- Creating architecture designs (use `n8n_workflow_architect`)
- Enhancing vague requirements (use `n8n_prompt_enhancer`)
- Non-n8n platforms

## JSON Building Workflow

### Phase 1: Parse Architecture Documents

**Input**: Architecture documentation (markdown or structured format)

**Process**:
1. Extract workflow metadata (name, tags, settings)
2. Parse node inventory and specifications
3. Extract connection mappings
4. Identify credential requirements
5. Collect configuration parameters

**Output**: Structured workflow specification object with `metadata`, `nodes`, `connections`, and `credentials` fields.

### Phase 2: Generate Node JSON

**Reference**: See `references/node_generation_rules.md` for detailed rules and examples.

**Process**: For each node in specification:

1. **Select Node Template** - Match type to template library (see `references/node_templates.md`)
2. **Configure Parameters** - Map specification parameters to JSON fields, apply expressions
3. **Assign Position** - Calculate canvas position from flow topology with standard spacing
4. **Generate IDs** - Create unique UUIDs for node and webhook IDs
5. **Add Credentials** - Map credential references with proper types

### Phase 3: Build Connection Map

**Reference**: See `references/connection_mapping.md` for connection generation logic and examples.

**Process**:

1. **Parse Connection Specifications** - Extract node-to-node mappings, branching paths
2. **Generate Connection Objects** - Create entries for each source node with output indices
3. **Validate Connection Integrity** - Ensure no orphaned nodes, verify all outputs connected

### Phase 4: Add Workflow Metadata

**Process**:

1. **Workflow Settings** - Execution order (v1), manual execution saving, error workflow
2. **Tags** - Environment tags (production, staging, dev) and category tags
3. **Timestamps** - Creation/update timestamps, version ID
4. **Static Data** - Initialize static data storage (usually null)

```json
{
  "name": "Customer Signup Notifications",
  "settings": {
    "executionOrder": "v1",
    "saveManualExecutions": true,
    "callerPolicy": "workflowsFromSameOwner"
  },
  "tags": [{"id": "tag-id-1", "name": "production"}],
  "pinData": {},
  "staticData": null,
  "triggerCount": 1
}
```

### Phase 5: Validate JSON Structure

**Reference**: Use `scripts/validate_json.py`

**Validation Checks**:

| Category | Checks |
|----------|--------|
| JSON Syntax | Valid format, no errors, proper escaping |
| Required Fields | Nodes have id/name/type/typeVersion/position/parameters |
| Node Types | All types exist in n8n, correct typeVersion |
| Connections | All referenced nodes exist, proper indices, no orphans |
| Credentials | Correct type for node, valid structure |
| Expressions | Valid `{{ }}` format, proper field references |

**Output**: Validation report with passed checks, warnings, errors, and metrics (node/connection/expression counts). Status: Ready/Not Ready for import.

### Phase 6: Feasibility & Complexity Analysis

**Reference**: See `references/feasibility_checks.md` for detailed analysis guidelines.

**Analysis Points**:
- **Complexity**: Node count (simple <10, medium 10-20, complex >20), nesting depth, parallel branches
- **Performance**: Expected execution time, API call count, database operations
- **Resources**: Memory, CPU, network, database connections
- **Risks**: Timeouts, rate limiting, memory constraints, circular dependencies
- **Recommendations**: Optimization opportunities, batch processing, sub-workflow splitting

### Phase 7: Generate Complete JSON File

**Process**:
1. Combine all components (nodes, connections, metadata)
2. Format with proper indentation (2 spaces)
3. Validate final structure
4. Save to file: `workflow_[name].json`

## Usage Examples

### Example 1: Simple Workflow

**Input** (Architecture excerpt):
```markdown
## Node Inventory
1. Webhook Trigger (POST /signup)
2. Validate Email (IF node)
3. Send Slack Message
4. Respond Success
```

**Command**:
```bash
python scripts/build_workflow.py \
  --input architecture_signup.md \
  --output workflow_signup.json
```

### Example 2: Complex Workflow with Validation

```bash
python scripts/build_workflow.py \
  --input architecture_order_processing.md \
  --output workflow_order_processing.json \
  --validate \
  --feasibility
```

## Resources

### Scripts

| Script | Purpose |
|--------|---------|
| `build_workflow.py` | Main JSON builder - parses, generates, validates |
| `validate_json.py` | JSON structure validator |
| `test_workflow.py` | Workflow testing utilities |

### References

| File | Contents |
|------|----------|
| `node_generation_rules.md` | Node type mapping, parameter transformation, expressions |
| `node_templates.md` | Complete library of n8n node JSON templates |
| `connection_mapping.md` | Connection syntax, branching, parallel execution |
| `feasibility_checks.md` | Complexity metrics, resource estimation, optimization |
| `expression_syntax.md` | N8N expression syntax reference and validation |
| `advanced_features.md` | Incremental building, templates, batch processing, diff/merge |

### Assets

- **workflow_templates/**: Pre-built JSON templates (webhook_process_respond, schedule_fetch_export, etc.)
- **sample_workflows/**: Complete example workflows

## Integration with Previous Skills

```
User Requirement → [n8n_prompt_enhancer] → Enhanced Specification
→ [n8n_workflow_architect] → Architecture Documentation
→ [n8n_workflow_json_builder] ← THIS SKILL → Executable n8n JSON → Deploy
```

## Quality Standards

All generated JSON must meet:
- Valid JSON syntax (parseable without errors)
- Complete node configurations (no missing required fields)
- Proper connection structure (all nodes connected)
- Valid credential references and expression syntax
- Unique node IDs, proper workflow metadata
- Importable to n8n without errors

## Performance & Testing

**For Large Workflows** (>20 nodes): Use batch processing, parallel generation, cached templates. See `references/advanced_features.md`.

**Testing Strategy**: Syntax validation → Import test → Execution test → Error path test → Performance test

## Export Formats

- `workflow_[name].json` - Main importable workflow
- `validation_report_[name].md` - Validation results
- `feasibility_report_[name].md` - Feasibility analysis
- `test_data_[name].json` - Sample test payloads

---

**Build Time Estimate**: 1-5 minutes per workflow
**Complexity Support**: Simple to Complex (unlimited nodes)
**Success Rate**: >99% for valid architecture documents
