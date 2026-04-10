#!/usr/bin/env python3
"""
N8N Workflow JSON Validator

Validates n8n workflow JSON structure and syntax.

Usage:
    python validate_json.py workflow.json
    python validate_json.py workflow.json --strict
"""

import json
import sys
import argparse


def validate_workflow_json(workflow):
    """Validate workflow JSON structure"""
    errors = []
    warnings = []
    passed = []

    # Required top-level fields
    required_fields = ["name", "nodes", "connections"]
    for field in required_fields:
        if field in workflow:
            passed.append(f"Has required field: {field}")
        else:
            errors.append(f"Missing required field: {field}")

    # Validate nodes
    if "nodes" in workflow:
        if not isinstance(workflow["nodes"], list):
            errors.append("'nodes' must be an array")
        elif len(workflow["nodes"]) == 0:
            warnings.append("Workflow has no nodes")
        else:
            for i, node in enumerate(workflow["nodes"]):
                validate_node(node, i, errors, warnings, passed)

    # Validate connections
    if "connections" in workflow:
        if not isinstance(workflow["connections"], dict):
            errors.append("'connections' must be an object")
        else:
            node_names = {n["name"] for n in workflow.get("nodes", [])}
            validate_connections(workflow["connections"], node_names, errors, warnings)

    return {
        "passed": passed,
        "errors": errors,
        "warnings": warnings,
        "metrics": {
            "nodes": len(workflow.get("nodes", [])),
            "connections": len(workflow.get("connections", {}))
        }
    }


def validate_node(node, index, errors, warnings, passed):
    """Validate individual node"""
    required = ["id", "name", "type", "typeVersion", "position", "parameters"]

    for field in required:
        if field not in node:
            errors.append(f"Node {index} ({node.get('name', 'unknown')}) missing '{field}'")

    # Validate position
    if "position" in node:
        if not isinstance(node["position"], list) or len(node["position"]) != 2:
            errors.append(f"Node '{node.get('name')}' position must be [x, y] array")

    # Validate node type
    if "type" in node:
        if not node["type"].startswith("n8n-nodes-"):
            warnings.append(f"Node '{node.get('name')}' has non-standard type")


def validate_connections(connections, node_names, errors, warnings):
    """Validate connections"""
    for source, conn in connections.items():
        if source not in node_names:
            errors.append(f"Connection source '{source}' not found in nodes")

        if not isinstance(conn, dict) or "main" not in conn:
            errors.append(f"Connection '{source}' missing 'main' field")
            continue

        for branch in conn.get("main", []):
            if not isinstance(branch, list):
                errors.append(f"Connection branch must be array")
                continue

            for target in branch:
                if not isinstance(target, dict):
                    errors.append("Connection target must be object")
                    continue

                if "node" not in target:
                    errors.append("Connection target missing 'node' field")
                elif target["node"] not in node_names:
                    errors.append(f"Connection target '{target['node']}' not found")


def print_report(report):
    """Print validation report"""
    print("\n" + "="*60)
    print("N8N Workflow JSON Validation Report")
    print("="*60)

    if report["passed"]:
        print("\n✅ Passed Checks:")
        for check in report["passed"][:5]:  # Show first 5
            print(f"   - {check}")
        if len(report["passed"]) > 5:
            print(f"   ... and {len(report['passed']) - 5} more")

    if report["errors"]:
        print("\n❌ Errors:")
        for error in report["errors"]:
            print(f"   - {error}")

    if report["warnings"]:
        print("\n⚠️  Warnings:")
        for warning in report["warnings"]:
            print(f"   - {warning}")

    print("\n📊 Metrics:")
    for key, value in report["metrics"].items():
        print(f"   - {key.title()}: {value}")

    print("\n" + "="*60)
    if not report["errors"]:
        print("✅ Validation PASSED")
    else:
        print(f"❌ Validation FAILED ({len(report['errors'])} errors)")
    print("="*60 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Validate n8n workflow JSON")
    parser.add_argument("workflow", help="Workflow JSON file to validate")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")

    args = parser.parse_args()

    # Load workflow
    try:
        with open(args.workflow, 'r', encoding='utf-8') as f:
            workflow = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: File not found: {args.workflow}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON: {e}")
        sys.exit(1)

    # Validate
    report = validate_workflow_json(workflow)
    print_report(report)

    # Exit code
    has_errors = bool(report["errors"])
    has_warnings = bool(report["warnings"])

    if has_errors or (args.strict and has_warnings):
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
