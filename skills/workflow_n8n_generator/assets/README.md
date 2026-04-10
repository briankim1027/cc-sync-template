# N8N Workflow Generator - Sample Assets

This directory contains sample automation requests and example outputs to help you understand how to use the n8n-workflow-generator skill effectively.

## Sample Requests

### 1. Email Automation
**File**: `sample_request_email_automation.txt`

**Description**: Automated welcome email workflow for new customer signups

**Complexity**: Simple (6-8 nodes)

**Key Features**:
- Webhook trigger
- Email sending with personalization
- Logging to Google Sheets

**Use Case**: Customer onboarding automation

### 2. Slack Monitoring
**File**: `sample_request_slack_monitoring.txt`

**Description**: API health monitoring with Slack alerts

**Complexity**: Simple-Medium (8-10 nodes)

**Key Features**:
- Scheduled trigger (cron)
- HTTP health check
- Conditional alerting
- Retry logic

**Use Case**: Production monitoring and alerting

### 3. Data Synchronization
**File**: `sample_request_data_sync.txt`

**Description**: Daily database to spreadsheet sync workflow

**Complexity**: Medium (10-12 nodes)

**Key Features**:
- Scheduled trigger
- Database queries
- Data transformation
- Multi-destination output

**Use Case**: Sales team data access automation

## How to Use These Samples

### Method 1: Command Line

```bash
python scripts/generate_complete_workflow.py \
  --input assets/sample_request_email_automation.txt \
  --output workflow_email_automation/
```

### Method 2: Programmatic Usage

```python
from scripts.generate_complete_workflow import WorkflowGeneratorPipeline

# Read sample request
with open('assets/sample_request_email_automation.txt', 'r') as f:
    request = f.read()

# Generate workflow
pipeline = WorkflowGeneratorPipeline(output_dir='workflow_email_automation')
result = pipeline.execute_pipeline(request)

print(f"Workflow generated: {result['output_directory']}")
```

### Method 3: Interactive Mode

```bash
# Run the pipeline interactively
python scripts/generate_complete_workflow.py

# When prompted, paste content from sample request file
# Or provide your own automation request
```

## Expected Output

For each sample request, the pipeline generates:

1. **Enhanced Prompt** (`1_enhanced_prompt.md`)
   - Structured workflow specification
   - All required sections filled

2. **Architecture Design** (`2_architecture_[name].md`)
   - Visual workflow diagram
   - Node inventory and specifications

3. **Implementation Guide** (`3_implementation_guide_[name].md`)
   - Node-by-node configuration instructions
   - Credential setup steps

4. **Deployment Checklist** (`4_deployment_checklist_[name].md`)
   - Step-by-step deployment tasks
   - Testing procedures

5. **Validation Report** (`5_validation_[name].md`)
   - Quality checks and metrics
   - Recommendations

6. **Workflow JSON** (`workflow_[name].json`)
   - Importable n8n workflow file
   - Ready for deployment

7. **Validation Report** (`validation_report_[name].md`)
   - JSON validation results
   - Feasibility analysis

8. **Pipeline Summary** (`00_PIPELINE_SUMMARY.md`)
   - Complete execution summary
   - Next steps guidance

## Customizing Samples

You can modify the sample requests to match your specific needs:

### Add More Detail
- Specify exact field names
- Define data formats
- Include error handling requirements
- Add specific timing requirements

### Change Services
- Replace Gmail with SendGrid
- Use different database (MySQL, MongoDB)
- Change from Slack to Discord or Teams
- Use different spreadsheet service

### Adjust Complexity
- Add more processing steps
- Include data enrichment from APIs
- Add conditional routing
- Implement parallel execution paths

## Best Practices from Samples

### Email Automation Sample
- **Good**: Clear trigger type (webhook)
- **Good**: Specifies email service and fields
- **Good**: Includes logging requirement
- **Lesson**: Always specify data sources and destinations

### Slack Monitoring Sample
- **Good**: Specific timing (every 5 minutes)
- **Good**: Clear success criteria (status code, response time)
- **Good**: Includes retry logic
- **Lesson**: Define thresholds and error handling upfront

### Data Sync Sample
- **Good**: Schedule clearly defined (daily at 9am)
- **Good**: Specifies data fields to sync
- **Good**: Includes notification requirement
- **Lesson**: Comprehensive requirements lead to better workflows

## Common Patterns in Samples

### Pattern 1: Trigger → Validate → Process → Action
Used in: Email Automation

### Pattern 2: Trigger → Check → Conditional → Alert
Used in: Slack Monitoring

### Pattern 3: Trigger → Fetch → Transform → Store → Notify
Used in: Data Synchronization

## Getting Help

If you're unsure how to structure your automation request:

1. **Start with a sample**: Choose the closest sample to your use case
2. **Modify incrementally**: Change one aspect at a time
3. **Test early**: Generate workflow from modified sample
4. **Iterate**: Refine based on output quality

## Contributing Samples

To add your own sample requests:

1. Create a new `.txt` file in this directory
2. Follow the structure of existing samples
3. Include clear requirements and specifications
4. Test the sample to ensure quality output
5. Document any special considerations

---

**Last Updated**: 2024-01-15
**Samples Count**: 3
**Complexity Range**: Simple to Medium
