# Error Handling and Recovery Strategies

## Overview

This document describes comprehensive error handling strategies for the n8n-workflow-generator pipeline, covering detection, recovery, and prevention patterns.

## Error Categories

### Phase 1 Errors (Prompt Enhancement)

#### Incomplete Input Error

**Description**: User request lacks sufficient detail for enhancement

**Detection**:
```python
def validate_input_completeness(request: str) -> bool:
    required_elements = ['action', 'trigger', 'data_source']
    detected = [elem for elem in required_elements if elem in request.lower()]
    return len(detected) >= 2  # At least 2 elements required
```

**Recovery Strategy**:
- Generate clarifying questions
- Provide example inputs
- Suggest input improvements

**Error Message**:
```
Error: Insufficient detail in automation request

Your request: "email automation"

Please provide:
- What triggers the automation? (schedule, webhook, form submission)
- What data is being processed?
- What action should be performed?

Example: "Send email daily at 9am with database report to team@company.com"
```

#### Ambiguous Requirements Error

**Description**: Request can be interpreted multiple ways

**Detection**:
```python
def detect_ambiguity(request: str) -> List[str]:
    ambiguous_terms = {
        'notification': ['email', 'slack', 'sms', 'webhook'],
        'process': ['transform', 'validate', 'enrich', 'filter'],
        'schedule': ['daily', 'weekly', 'hourly', 'on-demand']
    }

    ambiguities = []
    for term, options in ambiguous_terms.items():
        if term in request.lower():
            ambiguities.append(f"{term} could mean: {', '.join(options)}")

    return ambiguities
```

**Recovery Strategy**:
- Present alternatives with examples
- Ask user to clarify specific terms
- Provide default interpretation with option to override

### Phase 2 Errors (Architecture Design)

#### Complexity Threshold Exceeded

**Description**: Workflow design exceeds recommended complexity limits

**Detection**:
```python
def calculate_complexity_score(node_count: int, branch_count: int, depth: int) -> int:
    score = (node_count * 2) + (branch_count * 5) + (depth * 3)
    return score

# Thresholds
SIMPLE = 30      # < 30: Simple workflow
MEDIUM = 60      # 30-60: Medium complexity
COMPLEX = 100    # 60-100: Complex workflow
TOO_COMPLEX = 100  # > 100: Recommend splitting
```

**Recovery Strategy**:
- Suggest workflow splitting
- Identify sub-workflow boundaries
- Provide optimization recommendations

**Error Message**:
```
Warning: High Complexity Detected

Complexity Score: 125/100 (Threshold exceeded)
- Node Count: 25 (contribution: 50)
- Branch Count: 8 (contribution: 40)
- Nesting Depth: 5 (contribution: 15)

Recommendation:
Split into 3 sub-workflows:
1. Data Collection Workflow (8 nodes)
2. Processing & Enrichment Workflow (10 nodes)
3. Notification & Logging Workflow (7 nodes)
```

#### Invalid Node Type Error

**Description**: Requested functionality not supported by n8n nodes

**Detection**:
```python
SUPPORTED_NODE_TYPES = [
    'webhook', 'http-request', 'if', 'switch', 'set', 'function',
    'slack', 'gmail', 'sheets', 'mysql', 'postgres', 'redis',
    'schedule-trigger', 'error-trigger', 'respond-to-webhook'
]

def validate_node_types(architecture: Dict) -> List[str]:
    invalid_nodes = []
    for node in architecture['nodes']:
        if node['type'] not in SUPPORTED_NODE_TYPES:
            invalid_nodes.append(node['type'])
    return invalid_nodes
```

**Recovery Strategy**:
- Suggest alternative n8n nodes
- Provide workaround implementations
- Recommend custom node development if critical

#### Connection Pattern Error

**Description**: Invalid or impossible node connections

**Detection**:
```python
def validate_connections(architecture: Dict) -> List[str]:
    errors = []

    # Check for orphaned nodes
    connected_nodes = set()
    for source, targets in architecture['connections'].items():
        connected_nodes.add(source)
        for target in targets:
            connected_nodes.add(target['node'])

    all_nodes = {node['name'] for node in architecture['nodes']}
    orphaned = all_nodes - connected_nodes

    if orphaned and len(orphaned) > 1:  # Trigger can be orphaned (only input)
        errors.append(f"Orphaned nodes detected: {', '.join(orphaned)}")

    return errors
```

**Recovery Strategy**:
- Auto-connect orphaned nodes to nearest logical parent
- Suggest connection points
- Validate against connection patterns library

### Phase 3 Errors (JSON Generation)

#### JSON Syntax Error

**Description**: Generated JSON contains syntax errors

**Detection**:
```python
import json

def validate_json_syntax(json_str: str) -> Tuple[bool, Optional[str]]:
    try:
        json.loads(json_str)
        return True, None
    except json.JSONDecodeError as e:
        return False, f"JSON syntax error at line {e.lineno}: {e.msg}"
```

**Recovery Strategy**:
- Auto-correct common JSON errors
- Re-generate problematic sections
- Validate against JSON schema

#### Invalid Expression Syntax

**Description**: n8n expressions contain syntax errors

**Detection**:
```python
import re

def validate_expression_syntax(expression: str) -> Tuple[bool, Optional[str]]:
    # Check n8n expression format: ={{...}}
    if not re.match(r'^={{.*}}$', expression):
        return False, "Expression must be wrapped in ={{...}}"

    # Check for common syntax errors
    inner = expression[3:-2]  # Extract content between ={{ and }}

    # Check balanced brackets
    if inner.count('[') != inner.count(']'):
        return False, "Unbalanced square brackets"
    if inner.count('(') != inner.count(')'):
        return False, "Unbalanced parentheses"

    return True, None
```

**Recovery Strategy**:
- Auto-fix expression syntax
- Validate against n8n expression grammar
- Provide corrected expression with explanation

#### Missing Required Fields

**Description**: Generated nodes missing required fields

**Detection**:
```python
REQUIRED_FIELDS = {
    'webhook': ['httpMethod', 'path', 'responseMode'],
    'if': ['conditions'],
    'http-request': ['url', 'method'],
    'set': ['mode', 'assignments'],
    'slack': ['channel', 'text']
}

def validate_required_fields(node: Dict) -> List[str]:
    node_type = node['type'].split('.')[-1]
    required = REQUIRED_FIELDS.get(node_type, [])

    missing = []
    for field in required:
        if field not in node.get('parameters', {}):
            missing.append(field)

    return missing
```

**Recovery Strategy**:
- Add missing fields with sensible defaults
- Prompt for required configuration
- Use template values with warnings

## Error Prevention Strategies

### Input Validation

**Pre-Flight Checks**:
```python
class InputValidator:
    def validate(self, request: str) -> ValidationResult:
        checks = [
            self.check_length(request),
            self.check_clarity(request),
            self.check_completeness(request),
            self.check_feasibility(request)
        ]

        return ValidationResult(
            passed=all(c.passed for c in checks),
            checks=checks,
            score=sum(c.score for c in checks) / len(checks)
        )

    def check_length(self, request: str) -> Check:
        length = len(request.split())
        return Check(
            name='length',
            passed=length >= 5,
            score=min(100, length * 10),
            message=f"Request length: {length} words (minimum 5)"
        )

    def check_clarity(self, request: str) -> Check:
        clarity_keywords = ['send', 'create', 'update', 'monitor', 'notify']
        has_clear_action = any(kw in request.lower() for kw in clarity_keywords)
        return Check(
            name='clarity',
            passed=has_clear_action,
            score=100 if has_clear_action else 50,
            message="Clear action verb detected" if has_clear_action else "Add action verb (send, create, update, etc.)"
        )
```

### Progressive Enhancement

**Step-by-Step Validation**:
```python
def progressive_pipeline_execution(request: str):
    # Validate before each phase

    # Pre-Phase 1 validation
    if not validate_input(request):
        return enhance_input_with_guidance(request)

    phase1_result = execute_phase1(request)

    # Pre-Phase 2 validation
    if not validate_enhanced_prompt(phase1_result):
        return refine_enhancement(phase1_result)

    phase2_result = execute_phase2(phase1_result)

    # Pre-Phase 3 validation
    if not validate_architecture(phase2_result):
        return simplify_architecture(phase2_result)

    phase3_result = execute_phase3(phase2_result)

    return phase3_result
```

### Quality Gates

**Validation Gates Between Phases**:
```python
class QualityGate:
    def __init__(self, threshold: float = 0.8):
        self.threshold = threshold

    def check(self, output: Dict, metrics: Dict) -> bool:
        score = metrics.get('quality_score', 0)

        if score < self.threshold:
            self.log_failure(output, score)
            return False

        return True

    def log_failure(self, output: Dict, score: float):
        print(f"Quality gate failed: {score} < {self.threshold}")
        print("Suggestions:", output.get('suggestions', []))
```

## Error Reporting

### User-Friendly Error Messages

**Error Message Template**:
```
┌─────────────────────────────────────────┐
│ Error in Phase {phase_number}           │
├─────────────────────────────────────────┤
│ What happened:                          │
│ {clear_explanation}                     │
│                                         │
│ Why it happened:                        │
│ {root_cause}                            │
│                                         │
│ How to fix:                             │
│ {actionable_steps}                      │
│                                         │
│ Example:                                │
│ {example_solution}                      │
└─────────────────────────────────────────┘
```

**Example Error Report**:
```
┌─────────────────────────────────────────┐
│ Error in Phase 2: Architecture Design   │
├─────────────────────────────────────────┤
│ What happened:                          │
│ Workflow complexity exceeds limits      │
│ (35 nodes detected, limit is 30)       │
│                                         │
│ Why it happened:                        │
│ Your automation request involves many   │
│ different actions and data sources      │
│                                         │
│ How to fix:                             │
│ 1. Split into smaller workflows         │
│ 2. Identify logical boundaries          │
│ 3. Use sub-workflows for modularity     │
│                                         │
│ Example:                                │
│ Instead of one large workflow:          │
│   "Collect data, process, enrich,       │
│    validate, send to 5 destinations"    │
│                                         │
│ Create 2 workflows:                     │
│   Workflow 1: "Data collection &        │
│                processing"              │
│   Workflow 2: "Distribution to all      │
│                destinations"            │
└─────────────────────────────────────────┘
```

### Detailed Error Logs

**Log Structure**:
```python
class ErrorLog:
    def __init__(self):
        self.errors = []

    def log(self, error: Exception, context: Dict):
        entry = {
            'timestamp': datetime.now().isoformat(),
            'error_type': type(error).__name__,
            'message': str(error),
            'phase': context.get('phase'),
            'stack_trace': traceback.format_exc(),
            'context': context
        }
        self.errors.append(entry)

        # Write to file
        with open('pipeline_errors.log', 'a') as f:
            json.dump(entry, f)
            f.write('\n')
```

## Recovery Mechanisms

### Automatic Retry

**Retry Strategy**:
```python
from functools import wraps
import time

def retry_on_failure(max_attempts=3, delay=1, backoff=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            current_delay = delay

            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except RetryableError as e:
                    if attempt == max_attempts:
                        raise

                    print(f"Attempt {attempt} failed: {e}")
                    print(f"Retrying in {current_delay}s...")
                    time.sleep(current_delay)

                    attempt += 1
                    current_delay *= backoff

        return wrapper
    return decorator

@retry_on_failure(max_attempts=3, delay=2, backoff=2)
def execute_phase_with_retry(phase_func, *args, **kwargs):
    return phase_func(*args, **kwargs)
```

### Fallback Strategies

**Graceful Degradation**:
```python
def execute_with_fallback(primary_func, fallback_func, *args, **kwargs):
    try:
        return primary_func(*args, **kwargs)
    except Exception as e:
        print(f"Primary execution failed: {e}")
        print("Attempting fallback strategy...")
        return fallback_func(*args, **kwargs)

# Example usage
result = execute_with_fallback(
    primary_func=generate_complex_architecture,
    fallback_func=generate_simple_architecture,
    specification=spec
)
```

### Checkpoint and Resume

**Checkpoint System**:
```python
class CheckpointManager:
    def __init__(self, checkpoint_dir='checkpoints'):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(exist_ok=True)

    def save(self, phase: str, data: Dict):
        checkpoint_file = self.checkpoint_dir / f"{phase}.json"
        with open(checkpoint_file, 'w') as f:
            json.dump(data, f, indent=2)

    def load(self, phase: str) -> Optional[Dict]:
        checkpoint_file = self.checkpoint_dir / f"{phase}.json"
        if checkpoint_file.exists():
            with open(checkpoint_file, 'r') as f:
                return json.load(f)
        return None

    def resume_from(self, last_successful_phase: str):
        # Load checkpoint and skip completed phases
        checkpoint_data = self.load(last_successful_phase)
        return checkpoint_data
```

## Monitoring and Alerting

### Error Rate Monitoring

**Track Error Metrics**:
```python
class ErrorMetrics:
    def __init__(self):
        self.error_counts = defaultdict(int)
        self.phase_errors = defaultdict(list)

    def record_error(self, phase: str, error: Exception):
        self.error_counts[type(error).__name__] += 1
        self.phase_errors[phase].append({
            'type': type(error).__name__,
            'message': str(error),
            'timestamp': datetime.now().isoformat()
        })

    def get_error_rate(self, phase: str) -> float:
        total_executions = self.get_total_executions(phase)
        error_count = len(self.phase_errors[phase])
        return error_count / total_executions if total_executions > 0 else 0

    def alert_if_threshold_exceeded(self, threshold=0.1):
        for phase, errors in self.phase_errors.items():
            error_rate = self.get_error_rate(phase)
            if error_rate > threshold:
                self.send_alert(phase, error_rate)
```

## Best Practices

1. **Fail Fast**: Validate early and often
2. **Clear Messages**: Provide actionable error messages
3. **Log Everything**: Comprehensive error logging for debugging
4. **Graceful Degradation**: Fallback to simpler implementations
5. **User Guidance**: Help users fix issues themselves
6. **Monitoring**: Track error patterns and rates
7. **Prevention**: Validate inputs before processing
8. **Recovery**: Automatic retry with exponential backoff
9. **Transparency**: Show users what went wrong and why
10. **Documentation**: Document common errors and solutions
