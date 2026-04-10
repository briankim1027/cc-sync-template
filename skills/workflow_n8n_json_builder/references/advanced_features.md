# Advanced Features

## 1. Incremental Building

Build workflow in stages:
```bash
# Stage 1: Generate nodes only
python scripts/build_workflow.py --nodes-only

# Stage 2: Add connections
python scripts/build_workflow.py --connections-only

# Stage 3: Finalize
python scripts/build_workflow.py --finalize
```

## 2. Template-Based Generation

Use pre-built templates:
```bash
python scripts/build_workflow.py \
  --template webhook_process_respond \
  --customize config.json
```

## 3. Batch Processing

Generate multiple workflows:
```bash
python scripts/build_workflow.py \
  --batch architectures/ \
  --output-dir workflows/
```

## 4. Diff and Merge

Compare workflow versions:
```bash
python scripts/diff_workflows.py \
  workflow_v1.json \
  workflow_v2.json
```

## 5. Interactive Builder

Step-by-step guided building:
```bash
python scripts/interactive_builder.py
```

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| "Invalid node type" | Node type not recognized | Check spelling, verify n8n version |
| "Connection target not found" | Referenced node missing | Verify node names match exactly |
| "Invalid expression syntax" | Malformed `{{ }}` expression | Validate syntax, escape special chars |
| "Import fails in n8n" | JSON incompatible with version | Check n8n version, update typeVersions |
