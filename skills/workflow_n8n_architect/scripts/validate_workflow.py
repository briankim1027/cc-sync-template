#!/usr/bin/env python3
"""
N8N Workflow Validator

Validates n8n workflow JSON for completeness, best practices, and potential issues.
Provides detailed validation reports with recommendations.

Usage:
    python validate_workflow.py workflow.json
    python validate_workflow.py workflow.json --verbose
"""

import json
import sys
import argparse
from collections import defaultdict


class WorkflowValidator:
    def __init__(self, workflow):
        self.workflow = workflow
        self.nodes = {node["name"]: node for node in workflow.get("nodes", [])}
        self.connections = workflow.get("connections", {})
        self.errors = []
        self.warnings = []
        self.recommendations = []

    def validate_all(self):
        """Run all validation checks"""
        self.check_basic_structure()
        self.check_node_configuration()
        self.check_connections()
        self.check_error_handling()
        self.check_credentials()
        self.check_best_practices()
        return self.generate_report()

    def check_basic_structure(self):
        """Validate basic workflow structure"""
        if not self.workflow.get("name"):
            self.errors.append("Workflow name is missing")

        if not self.workflow.get("nodes"):
            self.errors.append("Workflow has no nodes")
            return

        if len(self.workflow["nodes"]) < 1:
            self.errors.append("Workflow must have at least one node")

        # Check for trigger node
        trigger_types = ["webhook", "scheduleTrigger", "manualTrigger"]
        has_trigger = any(
            node.get("type", "").split(".")[-1] in trigger_types
            for node in self.workflow["nodes"]
        )
        if not has_trigger:
            self.warnings.append("No trigger node found (webhook, schedule, or manual)")

    def check_node_configuration(self):
        """Validate individual node configurations"""
        for node in self.workflow["nodes"]:
            node_name = node.get("name", "Unknown")
            node_type = node.get("type", "")

            # Check required fields
            if not node.get("id"):
                self.errors.append(f"Node '{node_name}' missing ID")

            if not node.get("type"):
                self.errors.append(f"Node '{node_name}' missing type")

            if not node.get("position"):
                self.warnings.append(f"Node '{node_name}' missing position")

            # Check node-specific configurations
            if "webhook" in node_type:
                self._validate_webhook_node(node)
            elif "if" in node_type or "switch" in node_type:
                self._validate_conditional_node(node)
            elif "httpRequest" in node_type:
                self._validate_http_node(node)

    def _validate_webhook_node(self, node):
        """Validate webhook node configuration"""
        params = node.get("parameters", {})

        if not params.get("path"):
            self.errors.append(f"Webhook node '{node['name']}' missing path")

        if params.get("authentication") == "none":
            self.warnings.append(
                f"Webhook '{node['name']}' has no authentication - security risk"
            )

    def _validate_conditional_node(self, node):
        """Validate IF/Switch node configuration"""
        params = node.get("parameters", {})

        if "if" in node.get("type", ""):
            conditions = params.get("conditions", {})
            if not any(conditions.values()):
                self.warnings.append(
                    f"IF node '{node['name']}' has no conditions defined"
                )

    def _validate_http_node(self, node):
        """Validate HTTP Request node configuration"""
        params = node.get("parameters", {})

        if not params.get("url"):
            self.errors.append(f"HTTP node '{node['name']}' missing URL")

        if params.get("authentication") == "none":
            self.recommendations.append(
                f"HTTP node '{node['name']}' has no authentication - consider using credentials"
            )

        timeout = params.get("options", {}).get("timeout", 10000)
        if timeout > 60000:
            self.warnings.append(
                f"HTTP node '{node['name']}' has very long timeout ({timeout}ms)"
            )

    def check_connections(self):
        """Validate node connections"""
        # Check all nodes are connected
        connected_nodes = set()
        connected_nodes.add(self.workflow["nodes"][0]["name"])  # Trigger is always connected

        for source_node, connections in self.connections.items():
            connected_nodes.add(source_node)
            for output_branch in connections.get("main", []):
                for connection in output_branch:
                    connected_nodes.add(connection["node"])

        orphaned = set(self.nodes.keys()) - connected_nodes
        for node_name in orphaned:
            self.warnings.append(f"Node '{node_name}' is not connected")

        # Check IF/Switch nodes have both outputs connected
        for node in self.workflow["nodes"]:
            if "if" in node.get("type", ""):
                node_name = node["name"]
                if node_name in self.connections:
                    outputs = self.connections[node_name].get("main", [])
                    if len(outputs) < 2:
                        self.warnings.append(
                            f"IF node '{node_name}' missing FALSE branch connection"
                        )
                    elif not outputs[0] or not outputs[1]:
                        self.warnings.append(
                            f"IF node '{node_name}' has empty output branch"
                        )

    def check_error_handling(self):
        """Check for error handling implementation"""
        has_error_workflow = self.workflow.get("settings", {}).get("errorWorkflow")

        # Check for error trigger in connections or nodes
        has_error_handling = False
        for node in self.workflow["nodes"]:
            if "error" in node.get("type", "").lower():
                has_error_handling = True
                break

        if not has_error_workflow and not has_error_handling:
            self.recommendations.append(
                "No error handling configured - consider adding error workflow"
            )

        # Check for retry logic on HTTP nodes
        for node in self.workflow["nodes"]:
            if "httpRequest" in node.get("type", ""):
                params = node.get("parameters", {})
                retry_config = params.get("options", {}).get("retry", {})
                if not retry_config:
                    self.recommendations.append(
                        f"HTTP node '{node['name']}' has no retry logic configured"
                    )

    def check_credentials(self):
        """Validate credential configuration"""
        nodes_with_creds = []

        for node in self.workflow["nodes"]:
            if node.get("credentials"):
                nodes_with_creds.append(node["name"])

                for cred_type, cred_info in node["credentials"].items():
                    if not cred_info.get("id"):
                        self.warnings.append(
                            f"Node '{node['name']}' credential '{cred_type}' missing ID"
                        )

        if not nodes_with_creds:
            self.recommendations.append(
                "No credentials configured - ensure external service authentication is set up"
            )

    def check_best_practices(self):
        """Check adherence to best practices"""
        node_count = len(self.workflow["nodes"])

        # Workflow complexity
        if node_count > 20:
            self.recommendations.append(
                f"Workflow has {node_count} nodes - consider breaking into sub-workflows"
            )
        elif node_count > 15:
            self.recommendations.append(
                f"Workflow complexity is high ({node_count} nodes) - monitor for maintainability"
            )

        # Check for webhook response
        has_webhook = any(
            "webhook" in node.get("type", "")
            for node in self.workflow["nodes"]
        )
        has_respond = any(
            "respondToWebhook" in node.get("type", "")
            for node in self.workflow["nodes"]
        )

        if has_webhook and not has_respond:
            self.warnings.append(
                "Webhook workflow should include 'Respond to Webhook' node"
            )

        # Check for logging
        has_logging = any(
            "postgres" in node.get("type", "") or
            "googleSheets" in node.get("type", "")
            for node in self.workflow["nodes"]
        )

        if not has_logging and node_count > 5:
            self.recommendations.append(
                "Consider adding logging node to track workflow executions"
            )

    def generate_report(self):
        """Generate validation report"""
        passed_checks = []

        if not self.errors:
            passed_checks.append("Basic structure valid")

        if not any("authentication" in w for w in self.warnings):
            passed_checks.append("Authentication configured")

        if not any("connected" in w for w in self.warnings):
            passed_checks.append("All nodes connected")

        return {
            "passed": passed_checks,
            "errors": self.errors,
            "warnings": self.warnings,
            "recommendations": self.recommendations,
            "metrics": {
                "total_nodes": len(self.workflow.get("nodes", [])),
                "trigger_nodes": sum(
                    1 for node in self.workflow.get("nodes", [])
                    if any(t in node.get("type", "") for t in ["webhook", "trigger"])
                ),
                "external_integrations": sum(
                    1 for node in self.workflow.get("nodes", [])
                    if any(t in node.get("type", "") for t in ["http", "slack", "gmail", "postgres"])
                ),
                "error_handlers": sum(
                    1 for node in self.workflow.get("nodes", [])
                    if "error" in node.get("type", "").lower()
                )
            }
        }


def print_report(report, verbose=False):
    """Print validation report to console"""
    print("\n" + "="*60)
    print("N8N Workflow Validation Report")
    print("="*60)

    # Passed checks
    if report["passed"]:
        print("\n✅ Passed Checks:")
        for check in report["passed"]:
            print(f"   - {check}")

    # Errors
    if report["errors"]:
        print("\n❌ Critical Issues:")
        for error in report["errors"]:
            print(f"   - {error}")
    else:
        print("\n✅ No critical issues found")

    # Warnings
    if report["warnings"]:
        print("\n⚠️  Warnings:")
        for warning in report["warnings"]:
            print(f"   - {warning}")

    # Recommendations
    if report["recommendations"]:
        print("\n💡 Recommendations:")
        for rec in report["recommendations"]:
            print(f"   - {rec}")

    # Metrics
    print("\n📊 Workflow Metrics:")
    for metric, value in report["metrics"].items():
        print(f"   - {metric.replace('_', ' ').title()}: {value}")

    # Summary
    print("\n" + "="*60)
    if not report["errors"]:
        if not report["warnings"]:
            print("✅ Workflow is production-ready!")
        else:
            print(f"⚠️  Workflow is valid but has {len(report['warnings'])} warnings")
    else:
        print(f"❌ Workflow has {len(report['errors'])} critical issues")
    print("="*60 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Validate n8n workflow JSON")
    parser.add_argument("workflow", help="Path to workflow JSON file")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    # Load workflow
    try:
        with open(args.workflow, 'r') as f:
            workflow = json.load(f)
    except FileNotFoundError:
        print(f"Error: Workflow file not found: {args.workflow}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in workflow file: {e}")
        sys.exit(1)

    # Validate
    validator = WorkflowValidator(workflow)
    report = validator.validate_all()

    # Output
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_report(report, args.verbose)

    # Exit code
    sys.exit(1 if report["errors"] else 0)


if __name__ == "__main__":
    main()
