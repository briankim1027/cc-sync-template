#!/usr/bin/env python3
"""
N8N Workflow JSON Builder

Builds executable n8n workflow JSON from architecture documents.

Usage:
    python build_workflow.py --input architecture.md --output workflow.json
    python build_workflow.py --input arch.md --output wf.json --validate --feasibility
"""

import json
import uuid
import re
import sys
import argparse
from datetime import datetime


def generate_uuid():
    """Generate unique UUID"""
    return str(uuid.uuid4())


def parse_architecture(content):
    """Parse architecture document to extract workflow specification"""
    spec = {
        "metadata": {"name": "Workflow", "tags": []},
        "nodes": [],
        "connections": {},
        "settings": {}
    }

    # Extract workflow name
    name_match = re.search(r'#\s+(?:Workflow:\s+)?(.+)', content)
    if name_match:
        spec["metadata"]["name"] = name_match.group(1).strip()

    # Extract node inventory (simplified parsing)
    node_section = re.search(r'##\s+Node Inventory(.+?)##', content, re.DOTALL)
    if node_section:
        node_text = node_section.group(1)
        node_lines = re.findall(r'(?:\d+\.|\-)\s+(.+)', node_text)

        for i, line in enumerate(node_lines):
            # Parse node line (format: "Node Name (Type)")
            match = re.search(r'(.+?)\s*\((.+?)\)', line)
            if match:
                node_name = match.group(1).strip()
                node_type = match.group(2).strip().lower()

                spec["nodes"].append({
                    "name": node_name,
                    "type": map_node_type(node_type),
                    "index": i
                })

    # Extract connections (simplified)
    conn_section = re.search(r'##\s+(?:Connection|Data Flow)(.+?)##', content, re.DOTALL)
    if conn_section:
        conn_text = conn_section.group(1)
        # Parse connections like "A → B"
        connections = re.findall(r'(\w+(?:\s+\w+)*)\s*(?:→|->)\s*(\w+(?:\s+\w+)*)', conn_text)

        for source, target in connections:
            source = source.strip()
            target = target.strip()

            if source not in spec["connections"]:
                spec["connections"][source] = []
            spec["connections"][source].append(target)

    return spec


def map_node_type(type_str):
    """Map simplified type to full n8n node type"""
    type_map = {
        "webhook": "n8n-nodes-base.webhook",
        "http": "n8n-nodes-base.webhook",
        "schedule": "n8n-nodes-base.scheduleTrigger",
        "manual": "n8n-nodes-base.manualTrigger",
        "if": "n8n-nodes-base.if",
        "switch": "n8n-nodes-base.switch",
        "set": "n8n-nodes-base.set",
        "transform": "n8n-nodes-base.set",
        "code": "n8n-nodes-base.code",
        "function": "n8n-nodes-base.code",
        "http request": "n8n-nodes-base.httpRequest",
        "api": "n8n-nodes-base.httpRequest",
        "slack": "n8n-nodes-base.slack",
        "gmail": "n8n-nodes-base.gmail",
        "email": "n8n-nodes-base.gmail",
        "postgres": "n8n-nodes-base.postgres",
        "database": "n8n-nodes-base.postgres",
        "sheets": "n8n-nodes-base.googleSheets",
        "respond": "n8n-nodes-base.respondToWebhook",
        "wait": "n8n-nodes-base.wait",
        "merge": "n8n-nodes-base.merge"
    }

    return type_map.get(type_str.lower(), "n8n-nodes-base.set")


def build_node_json(node_spec, index):
    """Build node JSON from specification"""
    node_type = node_spec["type"]
    node_name = node_spec["name"]

    # Calculate position
    x = 250 + (index * 200)
    y = 300

    # Base node structure
    node = {
        "parameters": {},
        "id": generate_uuid(),
        "name": node_name,
        "type": node_type,
        "typeVersion": get_type_version(node_type),
        "position": [x, y]
    }

    # Add type-specific parameters
    if "webhook" in node_type:
        node["parameters"] = {
            "httpMethod": "POST",
            "path": "webhook-path",
            "responseMode": "onReceived",
            "options": {}
        }
        node["webhookId"] = generate_uuid()

    elif "if" in node_type:
        node["parameters"] = {
            "conditions": {
                "string": [{
                    "value1": "={{$json[\"field\"]}}",
                    "operation": "isNotEmpty"
                }]
            }
        }

    elif "set" in node_type:
        node["parameters"] = {
            "mode": "manual",
            "duplicateItem": False,
            "assignments": {
                "assignments": [{
                    "name": "field",
                    "value": "={{$json[\"value\"]}}",
                    "type": "string"
                }]
            },
            "options": {}
        }

    elif "httpRequest" in node_type:
        node["parameters"] = {
            "method": "POST",
            "url": "https://api.example.com",
            "options": {}
        }

    elif "respondToWebhook" in node_type:
        node["parameters"] = {
            "options": {
                "responseCode": 200,
                "responseData": "noData"
            }
        }

    return node


def get_type_version(node_type):
    """Get appropriate typeVersion for node type"""
    versions = {
        "n8n-nodes-base.set": 3,
        "n8n-nodes-base.code": 2,
        "n8n-nodes-base.httpRequest": 4,
        "n8n-nodes-base.slack": 2,
        "n8n-nodes-base.gmail": 2,
        "n8n-nodes-base.postgres": 2,
        "n8n-nodes-base.googleSheets": 4,
        "n8n-nodes-base.merge": 2
    }
    return versions.get(node_type, 1)


def build_connections(spec):
    """Build connections JSON from specification"""
    connections = {}
    node_names = {node["name"]: node for node in spec["nodes"]}

    for source, targets in spec["connections"].items():
        if source in node_names:
            connections[source] = {
                "main": [[{
                    "node": target,
                    "type": "main",
                    "index": 0
                } for target in targets if target in node_names]]
            }

    return connections


def build_workflow(spec):
    """Build complete workflow JSON"""
    # Build nodes
    nodes = []
    for node_spec in spec["nodes"]:
        node = build_node_json(node_spec, node_spec["index"])
        nodes.append(node)

    # Build connections
    connections = build_connections(spec)

    # Build complete workflow
    workflow = {
        "name": spec["metadata"]["name"],
        "nodes": nodes,
        "connections": connections,
        "pinData": {},
        "settings": {
            "executionOrder": "v1",
            "saveManualExecutions": True,
            "callerPolicy": "workflowsFromSameOwner"
        },
        "staticData": None,
        "tags": [],
        "triggerCount": 1,
        "updatedAt": datetime.now().isoformat() + "Z",
        "versionId": generate_uuid()
    }

    return workflow


def validate_workflow(workflow):
    """Basic validation of workflow JSON"""
    errors = []
    warnings = []

    # Check required fields
    if not workflow.get("name"):
        errors.append("Workflow name missing")

    if not workflow.get("nodes"):
        errors.append("No nodes in workflow")

    # Validate nodes
    for node in workflow.get("nodes", []):
        if not node.get("id"):
            errors.append(f"Node '{node.get('name')}' missing ID")
        if not node.get("type"):
            errors.append(f"Node '{node.get('name')}' missing type")

    # Check connections
    node_names = {n["name"] for n in workflow.get("nodes", [])}
    for source, conn in workflow.get("connections", {}).items():
        if source not in node_names:
            errors.append(f"Connection source '{source}' not found in nodes")

        for branch in conn.get("main", []):
            for target in branch:
                if target["node"] not in node_names:
                    errors.append(f"Connection target '{target['node']}' not found")

    return {"errors": errors, "warnings": warnings}


def main():
    parser = argparse.ArgumentParser(description="Build n8n workflow JSON")
    parser.add_argument("--input", required=True, help="Input architecture file")
    parser.add_argument("--output", required=True, help="Output workflow JSON file")
    parser.add_argument("--validate", action="store_true", help="Validate generated JSON")
    parser.add_argument("--feasibility", action="store_true", help="Run feasibility check")

    args = parser.parse_args()

    # Read architecture document
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Input file not found: {args.input}")
        sys.exit(1)

    print(f"✅ Parsing architecture document...")
    spec = parse_architecture(content)

    print(f"✅ Generating {len(spec['nodes'])} nodes...")
    workflow = build_workflow(spec)

    print(f"✅ Building {len(spec['connections'])} connections...")

    # Validate if requested
    if args.validate:
        print("✅ Validating workflow JSON...")
        validation = validate_workflow(workflow)

        if validation["errors"]:
            print(f"❌ Validation errors:")
            for error in validation["errors"]:
                print(f"   - {error}")
            sys.exit(1)

        if validation["warnings"]:
            print(f"⚠️  Warnings:")
            for warning in validation["warnings"]:
                print(f"   - {warning}")

    # Feasibility check if requested
    if args.feasibility:
        node_count = len(workflow["nodes"])
        complexity = "Simple" if node_count < 10 else "Medium" if node_count < 20 else "High"
        print(f"✅ Feasibility check: {complexity} complexity ({node_count} nodes)")

    # Write output
    try:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(workflow, f, indent=2, ensure_ascii=False)
        print(f"✅ Workflow JSON created: {args.output}")
        print(f"\n🎉 Ready to import to n8n!")
    except IOError as e:
        print(f"❌ Error writing output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
