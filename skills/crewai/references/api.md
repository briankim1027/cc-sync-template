# Crewai - Api

**Pages:** 8

---

## GET /inputs

**URL:** llms-txt#get-/inputs

Source: https://docs.crewai.com/en/api-reference/inputs

enterprise-api.en.yaml get /inputs
Get required inputs for your crew

---

## GET /status/{kickoff_id}

**URL:** llms-txt#get-/status/{kickoff_id}

Source: https://docs.crewai.com/en/api-reference/status

enterprise-api.en.yaml get /status/{kickoff_id}
Get execution status

---

## POST /kickoff

**URL:** llms-txt#post-/kickoff

Source: https://docs.crewai.com/en/api-reference/kickoff

enterprise-api.en.yaml post /kickoff
Start a crew execution

---

## POST /resume

**URL:** llms-txt#post-/resume

Source: https://docs.crewai.com/en/api-reference/resume

enterprise-api.en.yaml post /resume
Resume crew execution with human feedback

---

## With explicit reference context

**URL:** llms-txt#with-explicit-reference-context

**Contents:**
  - Adding to Tasks

context_guardrail = HallucinationGuardrail(
    context="AI helps with various tasks including analysis and generation.",
    llm=LLM(model="gpt-4o-mini")
)
python  theme={null}
from crewai import Task

**Examples:**

Example 1 (unknown):
```unknown
### Adding to Tasks
```

---

## ❌ Wrong - replaces dict reference

**URL:** llms-txt#❌-wrong---replaces-dict-reference

**Contents:**
- Registration Methods
  - 1. Global Hook Registration
  - 2. Decorator-Based Registration
  - 3. Crew-Scoped Hooks
- Common Use Cases
  - 1. Safety Guardrails
  - 2. Human Approval Gate
  - 3. Input Validation and Sanitization
  - 4. Result Sanitization
  - 5. Tool Usage Analytics

def wrong_approach(context: ToolCallHookContext) -> None:
    context.tool_input = {'query': 'new query'}
python  theme={null}
from crewai.hooks import register_before_tool_call_hook, register_after_tool_call_hook

def log_tool_call(context):
    print(f"Tool: {context.tool_name}")
    print(f"Input: {context.tool_input}")
    return None  # Allow execution

register_before_tool_call_hook(log_tool_call)
python  theme={null}
from crewai.hooks import before_tool_call, after_tool_call

@before_tool_call
def block_dangerous_tools(context):
    dangerous_tools = ['delete_database', 'drop_table', 'rm_rf']
    if context.tool_name in dangerous_tools:
        print(f"⛔ Blocked dangerous tool: {context.tool_name}")
        return False  # Block execution
    return None

@after_tool_call
def sanitize_results(context):
    if context.tool_result and "password" in context.tool_result.lower():
        return context.tool_result.replace("password", "[REDACTED]")
    return None
python  theme={null}
@CrewBase
class MyProjCrew:
    @before_tool_call_crew
    def validate_tool_inputs(self, context):
        # Only applies to this crew
        if context.tool_name == "web_search":
            if not context.tool_input.get('query'):
                print("❌ Invalid search query")
                return False
        return None

@after_tool_call_crew
    def log_tool_results(self, context):
        # Crew-specific tool logging
        print(f"✅ {context.tool_name} completed")
        return None

@crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
python  theme={null}
@before_tool_call
def safety_check(context: ToolCallHookContext) -> bool | None:
    # Block tools that could cause harm
    destructive_tools = [
        'delete_file',
        'drop_table',
        'remove_user',
        'system_shutdown'
    ]

if context.tool_name in destructive_tools:
        print(f"🛑 Blocked destructive tool: {context.tool_name}")
        return False

# Warn on sensitive operations
    sensitive_tools = ['send_email', 'post_to_social_media', 'charge_payment']
    if context.tool_name in sensitive_tools:
        print(f"⚠️  Executing sensitive tool: {context.tool_name}")

return None
python  theme={null}
@before_tool_call
def require_approval_for_actions(context: ToolCallHookContext) -> bool | None:
    approval_required = [
        'send_email',
        'make_purchase',
        'delete_file',
        'post_message'
    ]

if context.tool_name in approval_required:
        response = context.request_human_input(
            prompt=f"Approve {context.tool_name}?",
            default_message=f"Input: {context.tool_input}\nType 'yes' to approve:"
        )

if response.lower() != 'yes':
            print(f"❌ Tool execution denied: {context.tool_name}")
            return False

return None
python  theme={null}
@before_tool_call
def validate_and_sanitize_inputs(context: ToolCallHookContext) -> bool | None:
    # Validate search queries
    if context.tool_name == 'web_search':
        query = context.tool_input.get('query', '')
        if len(query) < 3:
            print("❌ Search query too short")
            return False

# Sanitize query
        context.tool_input['query'] = query.strip().lower()

# Validate file paths
    if context.tool_name == 'read_file':
        path = context.tool_input.get('path', '')
        if '..' in path or path.startswith('/'):
            print("❌ Invalid file path")
            return False

return None
python  theme={null}
@after_tool_call
def sanitize_sensitive_data(context: ToolCallHookContext) -> str | None:
    if not context.tool_result:
        return None

import re
    result = context.tool_result

# Remove API keys
    result = re.sub(
        r'(api[_-]?key|token)["\']?\s*[:=]\s*["\']?[\w-]+',
        r'\1: [REDACTED]',
        result,
        flags=re.IGNORECASE
    )

# Remove email addresses
    result = re.sub(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        '[EMAIL-REDACTED]',
        result
    )

# Remove credit card numbers
    result = re.sub(
        r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b',
        '[CARD-REDACTED]',
        result
    )

return result
python  theme={null}
import time
from collections import defaultdict

tool_stats = defaultdict(lambda: {'count': 0, 'total_time': 0, 'failures': 0})

@before_tool_call
def start_timer(context: ToolCallHookContext) -> None:
    context.tool_input['_start_time'] = time.time()
    return None

@after_tool_call
def track_tool_usage(context: ToolCallHookContext) -> None:
    start_time = context.tool_input.get('_start_time', time.time())
    duration = time.time() - start_time

tool_stats[context.tool_name]['count'] += 1
    tool_stats[context.tool_name]['total_time'] += duration

if not context.tool_result or 'error' in context.tool_result.lower():
        tool_stats[context.tool_name]['failures'] += 1

print(f"""
    📊 Tool Stats for {context.tool_name}:
    - Executions: {tool_stats[context.tool_name]['count']}
    - Avg Time: {tool_stats[context.tool_name]['total_time'] / tool_stats[context.tool_name]['count']:.2f}s
    - Failures: {tool_stats[context.tool_name]['failures']}
    """)

return None
python  theme={null}
from collections import defaultdict
from datetime import datetime, timedelta

tool_call_history = defaultdict(list)

@before_tool_call
def rate_limit_tools(context: ToolCallHookContext) -> bool | None:
    tool_name = context.tool_name
    now = datetime.now()

# Clean old entries (older than 1 minute)
    tool_call_history[tool_name] = [
        call_time for call_time in tool_call_history[tool_name]
        if now - call_time < timedelta(minutes=1)
    ]

# Check rate limit (max 10 calls per minute)
    if len(tool_call_history[tool_name]) >= 10:
        print(f"🚫 Rate limit exceeded for {tool_name}")
        return False

# Record this call
    tool_call_history[tool_name].append(now)
    return None
python  theme={null}
import hashlib
import json

def cache_key(tool_name: str, tool_input: dict) -> str:
    """Generate cache key from tool name and input."""
    input_str = json.dumps(tool_input, sort_keys=True)
    return hashlib.md5(f"{tool_name}:{input_str}".encode()).hexdigest()

@before_tool_call
def check_cache(context: ToolCallHookContext) -> bool | None:
    key = cache_key(context.tool_name, context.tool_input)
    if key in tool_cache:
        print(f"💾 Cache hit for {context.tool_name}")
        # Note: Can't return cached result from before hook
        # Would need to implement this differently
    return None

@after_tool_call
def cache_result(context: ToolCallHookContext) -> None:
    if context.tool_result:
        key = cache_key(context.tool_name, context.tool_input)
        tool_cache[key] = context.tool_result
        print(f"💾 Cached result for {context.tool_name}")
    return None
python  theme={null}
@before_tool_call
def debug_tool_call(context: ToolCallHookContext) -> None:
    print(f"""
    🔍 Tool Call Debug:
    - Tool: {context.tool_name}
    - Agent: {context.agent.role if context.agent else 'Unknown'}
    - Task: {context.task.description[:50] if context.task else 'Unknown'}...
    - Input: {context.tool_input}
    """)
    return None

@after_tool_call
def debug_tool_result(context: ToolCallHookContext) -> None:
    if context.tool_result:
        result_preview = context.tool_result[:200]
        print(f"✅ Result Preview: {result_preview}...")
    else:
        print("⚠️  No result returned")
    return None
python  theme={null}
from crewai.hooks import (
    unregister_before_tool_call_hook,
    unregister_after_tool_call_hook
)

**Examples:**

Example 1 (unknown):
```unknown
## Registration Methods

### 1. Global Hook Registration

Register hooks that apply to all tool calls across all crews:
```

Example 2 (unknown):
```unknown
### 2. Decorator-Based Registration

Use decorators for cleaner syntax:
```

Example 3 (unknown):
```unknown
### 3. Crew-Scoped Hooks

Register hooks for a specific crew instance:
```

Example 4 (unknown):
```unknown
## Common Use Cases

### 1. Safety Guardrails
```

---

## ❌ Wrong - replaces list reference

**URL:** llms-txt#❌-wrong---replaces-list-reference

**Contents:**
- Registration Methods
  - 1. Global Hook Registration
  - 2. Decorator-Based Registration
  - 3. Crew-Scoped Hooks
- Common Use Cases
  - 1. Iteration Limiting
  - 2. Human Approval Gate
  - 3. Adding System Context
  - 4. Response Sanitization
  - 5. Cost Tracking

def wrong_approach(context: LLMCallHookContext) -> None:
    context.messages = [{"role": "system", "content": "Be concise"}]
python  theme={null}
from crewai.hooks import register_before_llm_call_hook, register_after_llm_call_hook

def log_llm_call(context):
    print(f"LLM call by {context.agent.role} at iteration {context.iterations}")
    return None  # Allow execution

register_before_llm_call_hook(log_llm_call)
python  theme={null}
from crewai.hooks import before_llm_call, after_llm_call

@before_llm_call
def validate_iteration_count(context):
    if context.iterations > 10:
        print("⚠️ Exceeded maximum iterations")
        return False  # Block execution
    return None

@after_llm_call
def sanitize_response(context):
    if context.response and "API_KEY" in context.response:
        return context.response.replace("API_KEY", "[REDACTED]")
    return None
python  theme={null}
@CrewBase
class MyProjCrew:
    @before_llm_call_crew
    def validate_inputs(self, context):
        # Only applies to this crew
        if context.iterations == 0:
            print(f"Starting task: {context.task.description}")
        return None

@after_llm_call_crew
    def log_responses(self, context):
        # Crew-specific response logging
        print(f"Response length: {len(context.response)}")
        return None

@crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
python  theme={null}
@before_llm_call
def limit_iterations(context: LLMCallHookContext) -> bool | None:
    max_iterations = 15
    if context.iterations > max_iterations:
        print(f"⛔ Blocked: Exceeded {max_iterations} iterations")
        return False  # Block execution
    return None
python  theme={null}
@before_llm_call
def require_approval(context: LLMCallHookContext) -> bool | None:
    if context.iterations > 5:
        response = context.request_human_input(
            prompt=f"Iteration {context.iterations}: Approve LLM call?",
            default_message="Press Enter to approve, or type 'no' to block:"
        )
        if response.lower() == "no":
            print("🚫 LLM call blocked by user")
            return False
    return None
python  theme={null}
@before_llm_call
def add_guardrails(context: LLMCallHookContext) -> None:
    # Add safety guidelines to every LLM call
    context.messages.append({
        "role": "system",
        "content": "Ensure responses are factual and cite sources when possible."
    })
    return None
python  theme={null}
@after_llm_call
def sanitize_sensitive_data(context: LLMCallHookContext) -> str | None:
    if not context.response:
        return None

# Remove sensitive patterns
    import re
    sanitized = context.response
    sanitized = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[SSN-REDACTED]', sanitized)
    sanitized = re.sub(r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b', '[CARD-REDACTED]', sanitized)

return sanitized
python  theme={null}
import tiktoken

@before_llm_call
def track_token_usage(context: LLMCallHookContext) -> None:
    encoding = tiktoken.get_encoding("cl100k_base")
    total_tokens = sum(
        len(encoding.encode(msg.get("content", "")))
        for msg in context.messages
    )
    print(f"📊 Input tokens: ~{total_tokens}")
    return None

@after_llm_call
def track_response_tokens(context: LLMCallHookContext) -> None:
    if context.response:
        encoding = tiktoken.get_encoding("cl100k_base")
        tokens = len(encoding.encode(context.response))
        print(f"📊 Response tokens: ~{tokens}")
    return None
python  theme={null}
@before_llm_call
def debug_request(context: LLMCallHookContext) -> None:
    print(f"""
    🔍 LLM Call Debug:
    - Agent: {context.agent.role}
    - Task: {context.task.description[:50]}...
    - Iteration: {context.iterations}
    - Message Count: {len(context.messages)}
    - Last Message: {context.messages[-1] if context.messages else 'None'}
    """)
    return None

@after_llm_call
def debug_response(context: LLMCallHookContext) -> None:
    if context.response:
        print(f"✅ Response Preview: {context.response[:100]}...")
    return None
python  theme={null}
from crewai.hooks import (
    unregister_before_llm_call_hook,
    unregister_after_llm_call_hook
)

**Examples:**

Example 1 (unknown):
```unknown
## Registration Methods

### 1. Global Hook Registration

Register hooks that apply to all LLM calls across all crews:
```

Example 2 (unknown):
```unknown
### 2. Decorator-Based Registration

Use decorators for cleaner syntax:
```

Example 3 (unknown):
```unknown
### 3. Crew-Scoped Hooks

Register hooks for a specific crew instance:
```

Example 4 (unknown):
```unknown
## Common Use Cases

### 1. Iteration Limiting
```

---

## ❌ Wrong - replaces reference

**URL:** llms-txt#❌-wrong---replaces-reference

**Contents:**
  - 4. Use Type Hints
  - 5. Clean Up in Tests
- When to Use Which Hook
  - Use LLM Hooks When:
  - Use Tool Hooks When:
  - Use Both When:
- Alternative Registration Methods
  - Programmatic Registration (Advanced)

@before_llm_call
def wrong_approach(context):
    context.messages = [{"role": "system", "content": "Be concise"}]
python  theme={null}
from crewai.hooks import LLMCallHookContext, ToolCallHookContext

def my_llm_hook(context: LLMCallHookContext) -> bool | None:
    # IDE autocomplete and type checking
    return None

def my_tool_hook(context: ToolCallHookContext) -> str | None:
    return None
python  theme={null}
import pytest
from crewai.hooks import clear_all_global_hooks

@pytest.fixture(autouse=True)
def clean_hooks():
    """Reset hooks before each test."""
    yield
    clear_all_global_hooks()
python  theme={null}
from crewai.hooks import (
    register_before_llm_call_hook,
    register_after_tool_call_hook
)

def my_hook(context):
    return None

**Examples:**

Example 1 (unknown):
```unknown
### 4. Use Type Hints
```

Example 2 (unknown):
```unknown
### 5. Clean Up in Tests
```

Example 3 (unknown):
```unknown
## When to Use Which Hook

### Use LLM Hooks When:

* Implementing iteration limits
* Adding context or safety guidelines to prompts
* Tracking token usage and costs
* Sanitizing or transforming responses
* Implementing approval gates for LLM calls
* Debugging prompt/response interactions

### Use Tool Hooks When:

* Blocking dangerous or destructive operations
* Validating tool inputs before execution
* Implementing approval gates for sensitive actions
* Caching tool results
* Tracking tool usage and performance
* Sanitizing tool outputs
* Rate limiting tool calls

### Use Both When:

Building comprehensive observability, safety, or approval systems that need to monitor all agent operations.

## Alternative Registration Methods

### Programmatic Registration (Advanced)

For dynamic hook registration or when you need to register hooks programmatically:
```

---
