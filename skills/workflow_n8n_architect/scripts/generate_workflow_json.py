#!/usr/bin/env python3
"""
N8N Workflow JSON Generator

Generates n8n workflow JSON from architecture specifications.
Handles node creation, connection mapping, and proper ID generation.

Usage:
    python generate_workflow_json.py --name "Workflow Name" --nodes nodes.json --output workflow.json
"""

import json
import uuid
import sys
import argparse
from datetime import datetime


def generate_uuid():
    """Generate UUID for nodes and connections"""
    return str(uuid.uuid4())


def create_webhook_node(name, path, method="POST", position=None):
    """Create a webhook trigger node"""
    if position is None:
        position = [250, 300]

    return {
        "parameters": {
            "httpMethod": method,
            "path": path,
            "responseMode": "onReceived",
            "options": {}
        },
        "id": generate_uuid(),
        "name": name,
        "type": "n8n-nodes-base.webhook",
        "typeVersion": 1,
        "position": position,
        "webhookId": generate_uuid()
    }


def create_if_node(name, conditions, position=None):
    """Create an IF conditional node"""
    if position is None:
        position = [450, 300]

    return {
        "parameters": {
            "conditions": conditions,
            "combineOperation": "all"
        },
        "id": generate_uuid(),
        "name": name,
        "type": "n8n-nodes-base.if",
        "typeVersion": 1,
        "position": position
    }


def create_set_node(name, assignments, position=None, include_other_fields=True):
    """Create a Set node for data transformation"""
    if position is None:
        position = [650, 300]

    return {
        "parameters": {
            "mode": "manual",
            "duplicateItem": False,
            "assignments": {
                "assignments": assignments
            },
            "options": {
                "includeOtherFields": include_other_fields
            }
        },
        "id": generate_uuid(),
        "name": name,
        "type": "n8n-nodes-base.set",
        "typeVersion": 3,
        "position": position
    }


def create_http_request_node(name, url, method="POST", position=None, credential_id=None):
    """Create an HTTP Request node"""
    if position is None:
        position = [850, 300]

    node = {
        "parameters": {
            "method": method,
            "url": url,
            "authentication": "predefinedCredentialType",
            "nodeCredentialType": "httpHeaderAuth",
            "options": {
                "timeout": 30000
            }
        },
        "id": generate_uuid(),
        "name": name,
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4,
        "position": position
    }

    if credential_id:
        node["credentials"] = {
            "httpHeaderAuth": {
                "id": credential_id,
                "name": "API Credential"
            }
        }

    return node


def create_respond_webhook_node(name, response_code=200, position=None):
    """Create a Respond to Webhook node"""
    if position is None:
        position = [1050, 300]

    response_body = {
        "status": "success" if response_code == 200 else "error",
        "timestamp": "new Date().toISOString()"
    }

    return {
        "parameters": {
            "options": {
                "responseCode": response_code,
                "responseBody": "={{" + json.dumps(response_body) + "}}",
                "responseData": "noData"
            }
        },
        "id": generate_uuid(),
        "name": name,
        "type": "n8n-nodes-base.respondToWebhook",
        "typeVersion": 1,
        "position": position
    }


def create_connection(from_node, to_node, output_index=0):
    """Create a connection between two nodes"""
    return {
        "node": to_node,
        "type": "main",
        "index": output_index
    }


def build_connections(nodes_config):
    """Build connections object from node configuration"""
    connections = {}

    for node_name, node_info in nodes_config.items():
        if "connections" in node_info:
            node_connections = {"main": []}

            for output_index, targets in enumerate(node_info["connections"]):
                connection_list = []
                for target in targets:
                    connection_list.append(create_connection(node_name, target))
                node_connections["main"].append(connection_list)

            connections[node_name] = node_connections

    return connections


def generate_workflow(workflow_name, nodes, connections):
    """Generate complete workflow JSON"""
    return {
        "name": workflow_name,
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


def main():
    parser = argparse.ArgumentParser(description="Generate n8n workflow JSON")
    parser.add_argument("--name", required=True, help="Workflow name")
    parser.add_argument("--nodes", required=True, help="Nodes configuration JSON file")
    parser.add_argument("--output", required=True, help="Output workflow JSON file")

    args = parser.parse_args()

    # Load nodes configuration
    try:
        with open(args.nodes, 'r') as f:
            nodes_config = json.load(f)
    except FileNotFoundError:
        print(f"Error: Nodes file not found: {args.nodes}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in nodes file: {args.nodes}")
        sys.exit(1)

    # Generate nodes
    nodes = []
    for node_name, node_spec in nodes_config.items():
        node_type = node_spec.get("type")

        if node_type == "webhook":
            node = create_webhook_node(
                node_name,
                node_spec.get("path", "webhook"),
                node_spec.get("method", "POST"),
                node_spec.get("position")
            )
        elif node_type == "if":
            node = create_if_node(
                node_name,
                node_spec.get("conditions", {}),
                node_spec.get("position")
            )
        elif node_type == "set":
            node = create_set_node(
                node_name,
                node_spec.get("assignments", []),
                node_spec.get("position")
            )
        elif node_type == "httpRequest":
            node = create_http_request_node(
                node_name,
                node_spec.get("url", "https://api.example.com"),
                node_spec.get("method", "POST"),
                node_spec.get("position"),
                node_spec.get("credential_id")
            )
        elif node_type == "respondToWebhook":
            node = create_respond_webhook_node(
                node_name,
                node_spec.get("responseCode", 200),
                node_spec.get("position")
            )
        else:
            print(f"Warning: Unknown node type '{node_type}' for node '{node_name}'")
            continue

        nodes.append(node)

    # Build connections
    connections = build_connections(nodes_config)

    # Generate workflow
    workflow = generate_workflow(args.name, nodes, connections)

    # Write output
    try:
        with open(args.output, 'w') as f:
            json.dump(workflow, f, indent=2)
        print(f"✅ Workflow JSON generated: {args.output}")
        print(f"   Nodes: {len(nodes)}")
        print(f"   Connections: {len(connections)}")
    except IOError as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
