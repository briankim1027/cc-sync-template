---
name: n8n-workflow-architect
description: Transform enhanced n8n workflow prompts into production-ready technical implementations. Takes structured workflow requirements from n8n-prompt-enhancer and generates comprehensive architecture documentation, node-by-node implementation guides, importable n8n JSON workflows, and validated deployment plans. Use when you have a detailed workflow specification and need to create actual n8n workflow implementations with complete technical architecture.
---

# N8N Workflow Architect

## Overview

This skill transforms detailed workflow specifications into production-ready n8n workflow implementations. It bridges the gap between business requirements (from `n8n_prompt_enhancer`) and technical execution by generating complete workflow architectures, implementation guides, and importable n8n JSON files.

## When to Use This Skill

Activate this skill when:
- You have a detailed workflow specification (typically from `n8n_prompt_enhancer`)
- You need to design the technical architecture for an n8n workflow
- You want to generate importable n8n workflow JSON files
- You require step-by-step implementation instructions
- You need to validate workflow architecture before implementation

**Do NOT use** for:
- Vague workflow requests (use `n8n_prompt_enhancer` first)
- Non-n8n automation platforms
- General programming tasks unrelated to workflows

## Architecture Workflow

### Phase 1: Requirements Analysis

**Input**: Enhanced workflow prompt with sections:
- Workflow Objective
- Trigger Configuration
- Node Sequence & Logic
- Data Transformation
- Error Handling
- Testing Checklist

**Process**:
1. Parse the enhanced prompt to extract key requirements
2. Identify all required n8n nodes and their types
3. Map data flow between nodes
4. Determine credential requirements
5. Identify error handling strategies

**Output**: Structured requirements document with:
- Complete node inventory
- Data flow map
- Credential dependencies
- Error handling requirements

### Phase 2: Architecture Design

**Reference**: Use `references/connection_patterns.md` and `references/workflow_organization.md`

**Process**:
1. Design workflow topology (linear, branching, parallel)
2. Define node connections and data passing
3. Plan conditional routing (IF/Switch nodes)
4. Design error handling paths
5. Structure sub-workflows if needed

**Output**: Architecture diagram using template from `assets/architecture_template.md`:

```
[Trigger Node] → [Validation Node] → [IF Valid?]
                                       ├─ Yes → [Processing Branch]
                                       │         ├─ [Transform Data]
                                       │         ├─ [External API Call]
                                       │         └─ [Store Result] → [Success Response]
                                       └─ No → [Error Handler] → [Error Response]
                                                └─ [Log Error]
```

**Include**:
- Visual/textual workflow diagram
- Node connection specifications
- Data flow annotations
- Error path routing
- Parallel execution paths (if applicable)

### Phase 3: Node-by-Node Implementation Guide

**Reference**: Use `references/n8n_node_specs.md` for node configurations

**Process**:
For each node in the workflow, create detailed implementation instructions using template from `assets/implementation_guide_template.md`.

**Output Format**:
```markdown
### Node 1: [Node Name]
**Type**: [n8n node type, e.g., "n8n-nodes-base.webhook"]
**Purpose**: [What this node does in the workflow]

**Configuration**:
- Parameter 1: [Value or expression]
- Parameter 2: [Value or expression]
- [All required parameters]

**Credentials**: [If required]
- Credential Type: [e.g., "slackApi", "gmailOAuth2"]
- Setup Instructions: [How to configure]

**Expressions**: [If using n8n expressions]
- Field: `{{$json["fieldName"]}}`
- Transformation: `{{$json["field"].toLowerCase()}}`

**Output Data**:
```json
{
  "field1": "description",
  "field2": "description"
}
```

**Common Issues**:
- [Potential problem 1 and solution]
- [Potential problem 2 and solution]

**Testing**:
- [ ] Test step 1
- [ ] Test step 2
```

Repeat for all nodes in sequence.

### Phase 4: Generate n8n Workflow JSON

**Reference**: Use `references/n8n_node_specs.md` for JSON structure

**Process**:
1. Use `scripts/generate_workflow_json.py` to create base structure
2. Define workflow metadata (name, tags, version)
3. Generate node configurations with proper IDs and positions
4. Create connection objects linking nodes
5. Add credential references
6. Include settings and metadata

**Output**: Complete n8n workflow JSON file

```json
{
  "name": "Workflow Name",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook-path",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "node-id-1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "uuid"
    },
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
      },
      "id": "node-id-2",
      "name": "Validate Email",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [450, 300]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Validate Email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Validate Email": {
      "main": [
        [
          {
            "node": "Process Data",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Error Handler",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": [],
  "triggerCount": 1,
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "versionId": "uuid"
}
```

**File Naming**: `workflow_[workflow-name].json`

### Phase 5: Implementation Checklist

**Process**:
Create ordered task list for implementing the workflow

**Output**:
```markdown
## Implementation Checklist

### Pre-Implementation
- [ ] Review architecture design
- [ ] Verify n8n version compatibility (requires n8n v1.x+)
- [ ] Prepare required credentials
- [ ] Review security requirements

### Credential Setup
- [ ] Create [Credential Type 1] in n8n
  - Instructions: [Specific setup steps]
- [ ] Create [Credential Type 2] in n8n
  - Instructions: [Specific setup steps]

### Workflow Import
- [ ] Download workflow JSON file: `workflow_[name].json`
- [ ] Open n8n instance
- [ ] Navigate to Workflows → Import from File
- [ ] Select the downloaded JSON file
- [ ] Verify all nodes imported successfully

### Node Configuration
- [ ] Configure Node 1: [Node Name]
  - Set parameter X to [value]
  - Assign credential [name]
  - Test node execution
- [ ] Configure Node 2: [Node Name]
  - [Configuration steps]

### Testing
- [ ] Unit Tests
  - [ ] Test trigger with sample payload
  - [ ] Verify validation logic
  - [ ] Test success path end-to-end
  - [ ] Test error path
- [ ] Integration Tests
  - [ ] Verify external API connections
  - [ ] Test with production-like data
  - [ ] Validate error handling
  - [ ] Check credential authentication

### Deployment
- [ ] Review production deployment checklist (references/production_deployment.md)
- [ ] Configure environment variables
- [ ] Set up monitoring and logging
- [ ] Enable workflow
- [ ] Test webhook endpoint (if applicable)
- [ ] Monitor initial executions

### Post-Deployment
- [ ] Document workflow URL/webhook endpoint
- [ ] Set up alerting for failures
- [ ] Schedule first monitoring review
- [ ] Update team documentation
```

### Phase 6: Validation & Quality Checks

**Reference**: Use `scripts/validate_workflow.py`

**Process**:
1. Verify all required nodes are present
2. Check node connections are complete
3. Validate credential references
4. Review error handling coverage
5. Check for best practice violations
6. Verify data flow integrity

**Output**: Validation report

```markdown
## Workflow Validation Report

### ✅ Passed Checks
- All required nodes present (8/8)
- Node connections complete
- Credentials properly referenced
- Error handling configured
- Webhook authentication enabled

### ⚠️ Warnings
- Consider adding retry logic to HTTP Request node
- Slack notification lacks fallback channel
- No rate limiting configured for API calls

### ❌ Critical Issues
None found

### 📊 Metrics
- Total Nodes: 8
- Trigger Nodes: 1
- Error Handlers: 2
- External Integrations: 3
- Estimated Complexity: Medium

### 💡 Recommendations
1. Add exponential backoff retry for external API calls
2. Implement circuit breaker for frequently failing services
3. Consider splitting workflow if complexity grows beyond 15 nodes
4. Add monitoring for execution time and success rate
```

## Complete Output Package

When this skill completes, it provides:

1. **Architecture Design Document** (`architecture_[workflow-name].md`)
   - Visual workflow diagram
   - Node inventory
   - Data flow specifications
   - Design decisions and rationale

2. **Implementation Guide** (`implementation_guide_[workflow-name].md`)
   - Node-by-node configuration instructions
   - Credential setup steps
   - Expression syntax examples
   - Troubleshooting tips

3. **Workflow JSON** (`workflow_[workflow-name].json`)
   - Importable n8n workflow file
   - Pre-configured nodes and connections
   - Ready for credential assignment

4. **Implementation Checklist** (`checklist_[workflow-name].md`)
   - Ordered deployment tasks
   - Testing procedures
   - Validation steps

5. **Validation Report** (`validation_[workflow-name].md`)
   - Quality check results
   - Best practice compliance
   - Recommendations for improvement

## Example Usage Flow

### Input (from n8n_prompt_enhancer):
```markdown
# N8N Workflow: Customer Signup Notifications

## Workflow Objective
Send Slack notifications when new customers sign up

## Trigger Configuration
- Type: Webhook
- Method: POST
- Payload: {userId, email, name, plan}

## Node Sequence
1. Webhook Trigger
2. Validate Data
3. Format Message
4. Send to Slack
5. Log Result

[... complete enhanced prompt ...]
```

### Process:
```
1. Analyze requirements → Extract 5 nodes, identify Slack credential need
2. Design architecture → Linear flow with error branch
3. Generate implementation guide → Detail each node configuration
4. Create workflow JSON → Generate importable file
5. Build checklist → 15 implementation steps
6. Validate → Pass all checks, 2 warnings
```

### Output Files:
```
architecture_customer-signup-notifications.md
implementation_guide_customer-signup-notifications.md
workflow_customer-signup-notifications.json
checklist_customer-signup-notifications.md
validation_customer-signup-notifications.md
```

## Resources

### Scripts

**generate_workflow_json.py**:
Python script to generate n8n workflow JSON from architecture specifications. Handles node creation, connection mapping, and proper ID generation.

**validate_workflow.py**:
Validation script that checks workflow completeness, best practices compliance, and potential issues. Provides detailed validation reports.

### References

**n8n_node_specs.md**: Complete specifications for n8n node types including parameters, JSON structure, and configuration examples.

**connection_patterns.md**: Common node connection patterns, data flow strategies, and topology best practices.

**credential_setup.md**: Instructions for configuring credentials in n8n for various services (Slack, Gmail, APIs, databases).

**workflow_organization.md**: Best practices for structuring workflows, using sub-workflows, and organizing complex automations.

**production_deployment.md**: Production deployment guidelines including monitoring, logging, security, and operational best practices.

### Assets

**architecture_template.md**: Template for creating workflow architecture diagrams and design documentation.

**implementation_guide_template.md**: Template for node-by-node implementation instructions.

**workflow_json_template.json**: Base n8n workflow JSON structure with proper format and required fields.

## Integration with n8n_prompt_enhancer

This skill works as the second step after `n8n_prompt_enhancer`:

```
User Request
    ↓
[n8n_prompt_enhancer]
    ↓
Enhanced Workflow Prompt
    ↓
[n8n_workflow_architect] ← THIS SKILL
    ↓
Production-Ready Implementation Package
```

**Workflow**:
1. User provides vague request: "I need email automation"
2. `n8n_prompt_enhancer` creates structured specification
3. `n8n_workflow_architect` generates complete technical implementation
4. User imports JSON to n8n and follows implementation guide

## Quality Standards

All generated architectures must include:
- ✅ Complete node specifications with all required parameters
- ✅ Valid n8n workflow JSON (importable without errors)
- ✅ Comprehensive implementation guide (node-by-node)
- ✅ Error handling for all external operations
- ✅ Credential setup instructions
- ✅ Testing procedures
- ✅ Validation report with quality metrics

Avoid:
- ❌ Incomplete node configurations
- ❌ Invalid JSON syntax
- ❌ Missing error handling
- ❌ Undefined credential references
- ❌ Untested workflow designs
- ❌ Missing implementation steps
