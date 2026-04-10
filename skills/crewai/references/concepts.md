# Crewai - Concepts

**Pages:** 254

---

## Accessing the type-safe output

**URL:** llms-txt#accessing-the-type-safe-output

**Contents:**
  - Note:
  - Workflow in Action
- Advanced Features
  - Task Delegation
  - Asynchronous Execution
  - Memory and Caching
  - Callbacks
  - Usage Metrics
- Best Practices for Sequential Processes

task_output: TaskOutput = result.tasks[0].output
crew_output: CrewOutput = result.output
```

Each task in a sequential process **must** have an agent assigned. Ensure that every `Task` includes an `agent` parameter.

### Workflow in Action

1. **Initial Task**: In a sequential process, the first agent completes their task and signals completion.
2. **Subsequent Tasks**: Agents pick up their tasks based on the process type, with outcomes of preceding tasks or directives guiding their execution.
3. **Completion**: The process concludes once the final task is executed, leading to project completion.

In sequential processes, if an agent has `allow_delegation` set to `True`, they can delegate tasks to other agents in the crew.
This feature is automatically set up when there are multiple agents in the crew.

### Asynchronous Execution

Tasks can be executed asynchronously, allowing for parallel processing when appropriate.
To create an asynchronous task, set `async_execution=True` when defining the task.

### Memory and Caching

CrewAI supports both memory and caching features:

* **Memory**: Enable by setting `memory=True` when creating the Crew. This allows agents to retain information across tasks.
* **Caching**: By default, caching is enabled. Set `cache=False` to disable it.

You can set callbacks at both the task and step level:

* `task_callback`: Executed after each task completion.
* `step_callback`: Executed after each step in an agent's execution.

CrewAI tracks token usage across all tasks and agents. You can access these metrics after execution.

## Best Practices for Sequential Processes

1. **Order Matters**: Arrange tasks in a logical sequence where each task builds upon the previous one.
2. **Clear Task Descriptions**: Provide detailed descriptions for each task to guide the agents effectively.
3. **Appropriate Agent Selection**: Match agents' skills and roles to the requirements of each task.
4. **Use Context**: Leverage the context from previous tasks to inform subsequent ones.

This updated documentation ensures that details accurately reflect the latest changes in the codebase and clearly describes how to leverage new features and configurations.
The content is kept simple and direct to ensure easy understanding.

---

## Access final result

**URL:** llms-txt#access-final-result

**Contents:**
  - Using the CLI

result = streaming.result
shell  theme={null}
crewai run
shell  theme={null}
crewai flow kickoff
```

However, the `crewai run` command is now the preferred method as it works for both crews and flows.

**Examples:**

Example 1 (unknown):
```unknown
Learn more about streaming in the [Streaming Flow Execution](/en/learn/streaming-flow-execution) guide.

### Using the CLI

Starting from version 0.103.0, you can run flows using the `crewai run` command:
```

Example 2 (unknown):
```unknown
This command automatically detects if your project is a flow (based on the `type = "flow"` setting in your pyproject.toml) and runs it accordingly. This is the recommended way to run flows from the command line.

For backward compatibility, you can also use:
```

---

## Access the crew's usage metrics

**URL:** llms-txt#access-the-crew's-usage-metrics

**Contents:**
- Crew Execution Process
  - Kicking Off a Crew

crew = Crew(agents=[agent1, agent2], tasks=[task1, task2])
crew.kickoff()
print(crew.usage_metrics)
python Code theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## Crew Execution Process

* **Sequential Process**: Tasks are executed one after another, allowing for a linear flow of work.
* **Hierarchical Process**: A manager agent coordinates the crew, delegating tasks and validating outcomes before proceeding. **Note**: A `manager_llm` or `manager_agent` is required for this process and it's essential for validating the process flow.

### Kicking Off a Crew

Once your crew is assembled, initiate the workflow with the `kickoff()` method. This starts the execution process according to the defined process flow.
```

---

## Add to your agent

**URL:** llms-txt#add-to-your-agent

**Contents:**
- **Integration Benefits**

agent = Agent(
    role="Automation Specialist",
    tools=[apify_automation, platform_integration, browser_automation],
    goal="Automate workflows and integrate systems"
)
```

## **Integration Benefits**

* **Efficiency**: Reduce manual work through automation
* **Scalability**: Handle increased workloads automatically
* **Reliability**: Consistent execution of workflows
* **Connectivity**: Bridge different systems and platforms
* **Productivity**: Focus on high-value tasks while automation handles routine work

---

## Agents

**URL:** llms-txt#agents

**Contents:**
- Overview of an Agent
- Agent Attributes
- Creating Agents
  - YAML Configuration (Recommended)

Source: https://docs.crewai.com/en/concepts/agents

Detailed guide on creating and managing agents within the CrewAI framework.

## Overview of an Agent

In the CrewAI framework, an `Agent` is an autonomous unit that can:

* Perform specific tasks
* Make decisions based on its role and goal
* Use tools to accomplish objectives
* Communicate and collaborate with other agents
* Maintain memory of interactions
* Delegate tasks when allowed

<Tip>
  Think of an agent as a specialized team member with specific skills, expertise, and responsibilities. For example, a `Researcher` agent might excel at gathering and analyzing information, while a `Writer` agent might be better at creating content.
</Tip>

<Note type="info" title="Enterprise Enhancement: Visual Agent Builder">
  CrewAI AOP includes a Visual Agent Builder that simplifies agent creation and configuration without writing code. Design your agents visually and test them in real-time.

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c4f5428b111816273b3b53d9cef14fad" alt="Visual Agent Builder Screenshot" data-og-width="2654" width="2654" data-og-height="1710" height="1710" data-path="images/enterprise/crew-studio-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=35ea9140f0b9e57da5f45adbc7e2f166 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ae6f0c18ef3679b5466177710fbc4a94 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6c3e2fe013ab4826da90c937a9855635 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7f1474dd7f983532dc910363b96f783a 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f1a6d7e744e6862af5e72dce4deb0fd1 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=74aeb1ccd8e2c8f84d4247b8d0259737 2500w" />

The Visual Agent Builder enables:

* Intuitive agent configuration with form-based interfaces
  * Real-time testing and validation
  * Template library with pre-configured agent types
  * Easy customization of agent attributes and behaviors
</Note>

| Attribute                               | Parameter                | Type                                  | Description                                                                                              |
| :-------------------------------------- | :----------------------- | :------------------------------------ | :------------------------------------------------------------------------------------------------------- |
| **Role**                                | `role`                   | `str`                                 | Defines the agent's function and expertise within the crew.                                              |
| **Goal**                                | `goal`                   | `str`                                 | The individual objective that guides the agent's decision-making.                                        |
| **Backstory**                           | `backstory`              | `str`                                 | Provides context and personality to the agent, enriching interactions.                                   |
| **LLM** *(optional)*                    | `llm`                    | `Union[str, LLM, Any]`                | Language model that powers the agent. Defaults to the model specified in `OPENAI_MODEL_NAME` or "gpt-4". |
| **Tools** *(optional)*                  | `tools`                  | `List[BaseTool]`                      | Capabilities or functions available to the agent. Defaults to an empty list.                             |
| **Function Calling LLM** *(optional)*   | `function_calling_llm`   | `Optional[Any]`                       | Language model for tool calling, overrides crew's LLM if specified.                                      |
| **Max Iterations** *(optional)*         | `max_iter`               | `int`                                 | Maximum iterations before the agent must provide its best answer. Default is 20.                         |
| **Max RPM** *(optional)*                | `max_rpm`                | `Optional[int]`                       | Maximum requests per minute to avoid rate limits.                                                        |
| **Max Execution Time** *(optional)*     | `max_execution_time`     | `Optional[int]`                       | Maximum time (in seconds) for task execution.                                                            |
| **Verbose** *(optional)*                | `verbose`                | `bool`                                | Enable detailed execution logs for debugging. Default is False.                                          |
| **Allow Delegation** *(optional)*       | `allow_delegation`       | `bool`                                | Allow the agent to delegate tasks to other agents. Default is False.                                     |
| **Step Callback** *(optional)*          | `step_callback`          | `Optional[Any]`                       | Function called after each agent step, overrides crew callback.                                          |
| **Cache** *(optional)*                  | `cache`                  | `bool`                                | Enable caching for tool usage. Default is True.                                                          |
| **System Template** *(optional)*        | `system_template`        | `Optional[str]`                       | Custom system prompt template for the agent.                                                             |
| **Prompt Template** *(optional)*        | `prompt_template`        | `Optional[str]`                       | Custom prompt template for the agent.                                                                    |
| **Response Template** *(optional)*      | `response_template`      | `Optional[str]`                       | Custom response template for the agent.                                                                  |
| **Allow Code Execution** *(optional)*   | `allow_code_execution`   | `Optional[bool]`                      | Enable code execution for the agent. Default is False.                                                   |
| **Max Retry Limit** *(optional)*        | `max_retry_limit`        | `int`                                 | Maximum number of retries when an error occurs. Default is 2.                                            |
| **Respect Context Window** *(optional)* | `respect_context_window` | `bool`                                | Keep messages under context window size by summarizing. Default is True.                                 |
| **Code Execution Mode** *(optional)*    | `code_execution_mode`    | `Literal["safe", "unsafe"]`           | Mode for code execution: 'safe' (using Docker) or 'unsafe' (direct). Default is 'safe'.                  |
| **Multimodal** *(optional)*             | `multimodal`             | `bool`                                | Whether the agent supports multimodal capabilities. Default is False.                                    |
| **Inject Date** *(optional)*            | `inject_date`            | `bool`                                | Whether to automatically inject the current date into tasks. Default is False.                           |
| **Date Format** *(optional)*            | `date_format`            | `str`                                 | Format string for date when inject\_date is enabled. Default is "%Y-%m-%d" (ISO format).                 |
| **Reasoning** *(optional)*              | `reasoning`              | `bool`                                | Whether the agent should reflect and create a plan before executing a task. Default is False.            |
| **Max Reasoning Attempts** *(optional)* | `max_reasoning_attempts` | `Optional[int]`                       | Maximum number of reasoning attempts before executing the task. If None, will try until ready.           |
| **Embedder** *(optional)*               | `embedder`               | `Optional[Dict[str, Any]]`            | Configuration for the embedder used by the agent.                                                        |
| **Knowledge Sources** *(optional)*      | `knowledge_sources`      | `Optional[List[BaseKnowledgeSource]]` | Knowledge sources available to the agent.                                                                |
| **Use System Prompt** *(optional)*      | `use_system_prompt`      | `Optional[bool]`                      | Whether to use system prompt (for o1 model support). Default is True.                                    |

There are two ways to create agents in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define agents. We strongly recommend using this approach in your CrewAI projects.

After creating your CrewAI project as outlined in the [Installation](/en/installation) section, navigate to the `src/latest_ai_development/config/agents.yaml` file and modify the template to match your requirements.

<Note>
  Variables in your YAML files (like `{topic}`) will be replaced with values from your inputs when running the crew:

Here's an example of how to configure agents using YAML:

```yaml agents.yaml theme={null}

**Examples:**

Example 1 (unknown):
```unknown
</Note>

Here's an example of how to configure agents using YAML:
```

---

## Agents are defined with attributes for backstory, cache, and verbose mode

**URL:** llms-txt#agents-are-defined-with-attributes-for-backstory,-cache,-and-verbose-mode

researcher = Agent(
    role='Researcher',
    goal='Conduct in-depth analysis',
    backstory='Experienced data analyst with a knack for uncovering hidden trends.',
)
writer = Agent(
    role='Writer',
    goal='Create engaging content',
    backstory='Creative writer passionate about storytelling in technical domains.',
)

---

## Agents can now collaborate automatically

**URL:** llms-txt#agents-can-now-collaborate-automatically

**Contents:**
- How Agent Collaboration Works
  - 1. **Delegate Work Tool**

crew = Crew(
    agents=[researcher, writer],
    tasks=[...],
    verbose=True
)
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## How Agent Collaboration Works

When `allow_delegation=True`, CrewAI automatically provides agents with two powerful tools:

### 1. **Delegate Work Tool**

Allows agents to assign tasks to teammates with specific expertise.
```

---

## Allow agents to search within any XML file's content

**URL:** llms-txt#allow-agents-to-search-within-any-xml-file's-content

#as it learns about their paths during execution
tool = XMLSearchTool()

---

## All knowledge will now be stored in ./my_project_storage/knowledge/

**URL:** llms-txt#all-knowledge-will-now-be-stored-in-./my_project_storage/knowledge/

crew = Crew(
    agents=[...],
    tasks=[...],
    knowledge_sources=[...]
)
python  theme={null}
from crewai.knowledge.storage.knowledge_storage import KnowledgeStorage
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

**Examples:**

Example 1 (unknown):
```unknown
#### Option 2: Custom Knowledge Storage
```

---

## All memory and knowledge will now be stored in ./my_project_storage/

**URL:** llms-txt#all-memory-and-knowledge-will-now-be-stored-in-./my_project_storage/

crew = Crew(
    agents=[...],
    tasks=[...],
    memory=True
)
python  theme={null}
import os
from crewai import Crew
from crewai.memory import LongTermMemory
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage

**Examples:**

Example 1 (unknown):
```unknown
#### Option 2: Custom Storage Paths
```

---

## Alternative: Break tasks into smaller pieces

**URL:** llms-txt#alternative:-break-tasks-into-smaller-pieces

---

## Asana Integration

**URL:** llms-txt#asana-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Asana Integration
  - 1. Connect Your Asana Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Asana Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/asana

Team task and project coordination with Asana integration for CrewAI.

Enable your agents to manage tasks, projects, and team coordination through Asana. Create tasks, update project status, manage assignments, and streamline your team's workflow with AI-powered automation.

Before using the Asana integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* An Asana account with appropriate permissions
* Connected your Asana account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Asana Integration

### 1. Connect Your Asana Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Asana** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for task and project management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="asana/create_comment">
    **Description:** Create a comment in Asana.

* `task` (string, required): Task ID - The ID of the Task the comment will be added to. The comment will be authored by the currently authenticated user.
    * `text` (string, required): Text (example: "This is a comment.").
  </Accordion>

<Accordion title="asana/create_project">
    **Description:** Create a project in Asana.

* `name` (string, required): Name (example: "Stuff to buy").
    * `workspace` (string, required): Workspace - Use Connect Portal Workflow Settings to allow users to select which Workspace to create Projects in. Defaults to the user's first Workspace if left blank.
    * `team` (string, optional): Team - Use Connect Portal Workflow Settings to allow users to select which Team to share this Project with. Defaults to the user's first Team if left blank.
    * `notes` (string, optional): Notes (example: "These are things we need to purchase.").
  </Accordion>

<Accordion title="asana/get_projects">
    **Description:** Get a list of projects in Asana.

* `archived` (string, optional): Archived - Choose "true" to show archived projects, "false" to display only active projects, or "default" to show both archived and active projects.
      * Options: `default`, `true`, `false`
  </Accordion>

<Accordion title="asana/get_project_by_id">
    **Description:** Get a project by ID in Asana.

* `projectFilterId` (string, required): Project ID.
  </Accordion>

<Accordion title="asana/create_task">
    **Description:** Create a task in Asana.

* `name` (string, required): Name (example: "Task Name").
    * `workspace` (string, optional): Workspace - Use Connect Portal Workflow Settings to allow users to select which Workspace to create Tasks in. Defaults to the user's first Workspace if left blank..
    * `project` (string, optional): Project - Use Connect Portal Workflow Settings to allow users to select which Project to create this Task in.
    * `notes` (string, optional): Notes.
    * `dueOnDate` (string, optional): Due On - The date on which this task is due. Cannot be used together with Due At. (example: "YYYY-MM-DD").
    * `dueAtDate` (string, optional): Due At - The date and time (ISO timestamp) at which this task is due. Cannot be used together with Due On. (example: "2019-09-15T02:06:58.147Z").
    * `assignee` (string, optional): Assignee - The ID of the Asana user this task will be assigned to. Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `gid` (string, optional): External ID - An ID from your application to associate this task with. You can use this ID to sync updates to this task later.
  </Accordion>

<Accordion title="asana/update_task">
    **Description:** Update a task in Asana.

* `taskId` (string, required): Task ID - The ID of the Task that will be updated.
    * `completeStatus` (string, optional): Completed Status.
      * Options: `true`, `false`
    * `name` (string, optional): Name (example: "Task Name").
    * `notes` (string, optional): Notes.
    * `dueOnDate` (string, optional): Due On - The date on which this task is due. Cannot be used together with Due At. (example: "YYYY-MM-DD").
    * `dueAtDate` (string, optional): Due At - The date and time (ISO timestamp) at which this task is due. Cannot be used together with Due On. (example: "2019-09-15T02:06:58.147Z").
    * `assignee` (string, optional): Assignee - The ID of the Asana user this task will be assigned to. Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `gid` (string, optional): External ID - An ID from your application to associate this task with. You can use this ID to sync updates to this task later.
  </Accordion>

<Accordion title="asana/get_tasks">
    **Description:** Get a list of tasks in Asana.

* `workspace` (string, optional): Workspace - The ID of the Workspace to filter tasks on. Use Connect Portal Workflow Settings to allow users to select a Workspace.
    * `project` (string, optional): Project - The ID of the Project to filter tasks on. Use Connect Portal Workflow Settings to allow users to select a Project.
    * `assignee` (string, optional): Assignee - The ID of the assignee to filter tasks on. Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `completedSince` (string, optional): Completed since - Only return tasks that are either incomplete or that have been completed since this time (ISO or Unix timestamp). (example: "2014-04-25T16:15:47-04:00").
  </Accordion>

<Accordion title="asana/get_tasks_by_id">
    **Description:** Get a list of tasks by ID in Asana.

* `taskId` (string, required): Task ID.
  </Accordion>

<Accordion title="asana/get_task_by_external_id">
    **Description:** Get a task by external ID in Asana.

* `gid` (string, required): External ID - The ID that this task is associated or synced with, from your application.
  </Accordion>

<Accordion title="asana/add_task_to_section">
    **Description:** Add a task to a section in Asana.

* `sectionId` (string, required): Section ID - The ID of the section to add this task to.
    * `taskId` (string, required): Task ID - The ID of the task. (example: "1204619611402340").
    * `beforeTaskId` (string, optional): Before Task ID - The ID of a task in this section that this task will be inserted before. Cannot be used with After Task ID. (example: "1204619611402340").
    * `afterTaskId` (string, optional): After Task ID - The ID of a task in this section that this task will be inserted after. Cannot be used with Before Task ID. (example: "1204619611402340").
  </Accordion>

<Accordion title="asana/get_teams">
    **Description:** Get a list of teams in Asana.

* `workspace` (string, required): Workspace - Returns the teams in this workspace visible to the authorized user.
  </Accordion>

<Accordion title="asana/get_workspaces">
    **Description:** Get a list of workspaces in Asana.

**Parameters:** None required.
  </Accordion>
</AccordionGroup>

### Basic Asana Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="asana/create_comment">
    **Description:** Create a comment in Asana.

    **Parameters:**

    * `task` (string, required): Task ID - The ID of the Task the comment will be added to. The comment will be authored by the currently authenticated user.
    * `text` (string, required): Text (example: "This is a comment.").
  </Accordion>

  <Accordion title="asana/create_project">
    **Description:** Create a project in Asana.

    **Parameters:**

    * `name` (string, required): Name (example: "Stuff to buy").
    * `workspace` (string, required): Workspace - Use Connect Portal Workflow Settings to allow users to select which Workspace to create Projects in. Defaults to the user's first Workspace if left blank.
    * `team` (string, optional): Team - Use Connect Portal Workflow Settings to allow users to select which Team to share this Project with. Defaults to the user's first Team if left blank.
    * `notes` (string, optional): Notes (example: "These are things we need to purchase.").
  </Accordion>

  <Accordion title="asana/get_projects">
    **Description:** Get a list of projects in Asana.

    **Parameters:**

    * `archived` (string, optional): Archived - Choose "true" to show archived projects, "false" to display only active projects, or "default" to show both archived and active projects.
      * Options: `default`, `true`, `false`
  </Accordion>

  <Accordion title="asana/get_project_by_id">
    **Description:** Get a project by ID in Asana.

    **Parameters:**

    * `projectFilterId` (string, required): Project ID.
  </Accordion>

  <Accordion title="asana/create_task">
    **Description:** Create a task in Asana.

    **Parameters:**

    * `name` (string, required): Name (example: "Task Name").
    * `workspace` (string, optional): Workspace - Use Connect Portal Workflow Settings to allow users to select which Workspace to create Tasks in. Defaults to the user's first Workspace if left blank..
    * `project` (string, optional): Project - Use Connect Portal Workflow Settings to allow users to select which Project to create this Task in.
    * `notes` (string, optional): Notes.
    * `dueOnDate` (string, optional): Due On - The date on which this task is due. Cannot be used together with Due At. (example: "YYYY-MM-DD").
    * `dueAtDate` (string, optional): Due At - The date and time (ISO timestamp) at which this task is due. Cannot be used together with Due On. (example: "2019-09-15T02:06:58.147Z").
    * `assignee` (string, optional): Assignee - The ID of the Asana user this task will be assigned to. Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `gid` (string, optional): External ID - An ID from your application to associate this task with. You can use this ID to sync updates to this task later.
  </Accordion>

  <Accordion title="asana/update_task">
    **Description:** Update a task in Asana.

    **Parameters:**

    * `taskId` (string, required): Task ID - The ID of the Task that will be updated.
    * `completeStatus` (string, optional): Completed Status.
      * Options: `true`, `false`
    * `name` (string, optional): Name (example: "Task Name").
    * `notes` (string, optional): Notes.
    * `dueOnDate` (string, optional): Due On - The date on which this task is due. Cannot be used together with Due At. (example: "YYYY-MM-DD").
    * `dueAtDate` (string, optional): Due At - The date and time (ISO timestamp) at which this task is due. Cannot be used together with Due On. (example: "2019-09-15T02:06:58.147Z").
    * `assignee` (string, optional): Assignee - The ID of the Asana user this task will be assigned to. Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `gid` (string, optional): External ID - An ID from your application to associate this task with. You can use this ID to sync updates to this task later.
  </Accordion>

  <Accordion title="asana/get_tasks">
    **Description:** Get a list of tasks in Asana.

    **Parameters:**

    * `workspace` (string, optional): Workspace - The ID of the Workspace to filter tasks on. Use Connect Portal Workflow Settings to allow users to select a Workspace.
    * `project` (string, optional): Project - The ID of the Project to filter tasks on. Use Connect Portal Workflow Settings to allow users to select a Project.
    * `assignee` (string, optional): Assignee - The ID of the assignee to filter tasks on. Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `completedSince` (string, optional): Completed since - Only return tasks that are either incomplete or that have been completed since this time (ISO or Unix timestamp). (example: "2014-04-25T16:15:47-04:00").
  </Accordion>

  <Accordion title="asana/get_tasks_by_id">
    **Description:** Get a list of tasks by ID in Asana.

    **Parameters:**

    * `taskId` (string, required): Task ID.
  </Accordion>

  <Accordion title="asana/get_task_by_external_id">
    **Description:** Get a task by external ID in Asana.

    **Parameters:**

    * `gid` (string, required): External ID - The ID that this task is associated or synced with, from your application.
  </Accordion>

  <Accordion title="asana/add_task_to_section">
    **Description:** Add a task to a section in Asana.

    **Parameters:**

    * `sectionId` (string, required): Section ID - The ID of the section to add this task to.
    * `taskId` (string, required): Task ID - The ID of the task. (example: "1204619611402340").
    * `beforeTaskId` (string, optional): Before Task ID - The ID of a task in this section that this task will be inserted before. Cannot be used with After Task ID. (example: "1204619611402340").
    * `afterTaskId` (string, optional): After Task ID - The ID of a task in this section that this task will be inserted after. Cannot be used with Before Task ID. (example: "1204619611402340").
  </Accordion>

  <Accordion title="asana/get_teams">
    **Description:** Get a list of teams in Asana.

    **Parameters:**

    * `workspace` (string, required): Workspace - Returns the teams in this workspace visible to the authorized user.
  </Accordion>

  <Accordion title="asana/get_workspaces">
    **Description:** Get a list of workspaces in Asana.

    **Parameters:** None required.
  </Accordion>
</AccordionGroup>

## Usage Examples

### Basic Asana Agent Setup
```

---

## Assemble a crew with planning enabled

**URL:** llms-txt#assemble-a-crew-with-planning-enabled

crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write],
    verbose=True,
    planning=True,  # Enable planning feature
)

---

## Async function to kickoff multiple crews asynchronously and wait for all to finish

**URL:** llms-txt#async-function-to-kickoff-multiple-crews-asynchronously-and-wait-for-all-to-finish

async def async_multiple_crews():
    # Create coroutines for concurrent execution
    result_1 = crew_1.kickoff_async(inputs={"ages": [25, 30, 35, 40, 45]})
    result_2 = crew_2.kickoff_async(inputs={"ages": [20, 22, 24, 28, 30]})

# Wait for both crews to finish
    results = await asyncio.gather(result_1, result_2)

for i, result in enumerate(results, 1):
        print(f"Crew {i} Result:", result)

---

## Basic OpenAI configuration (uses environment OPENAI_API_KEY)

**URL:** llms-txt#basic-openai-configuration-(uses-environment-openai_api_key)

crew = Crew(
    agents=[...],
    tasks=[...],
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "model_name": "text-embedding-3-small"  # or "text-embedding-3-large"
        }
    }
)

---

## `BedrockInvokeAgentTool`

**URL:** llms-txt#`bedrockinvokeagenttool`

**Contents:**
- Installation
- Requirements
- Usage

The `BedrockInvokeAgentTool` enables CrewAI agents to invoke Amazon Bedrock Agents and leverage their capabilities within your workflows.

* AWS credentials configured (either through environment variables or AWS CLI)
* `boto3` and `python-dotenv` packages
* Access to Amazon Bedrock Agents

Here's how to use the tool with a CrewAI agent:

```python {2, 4-8} theme={null}
from crewai import Agent, Task, Crew
from crewai_tools.aws.bedrock.agents.invoke_agent_tool import BedrockInvokeAgentTool

**Examples:**

Example 1 (unknown):
```unknown
## Requirements

* AWS credentials configured (either through environment variables or AWS CLI)
* `boto3` and `python-dotenv` packages
* Access to Amazon Bedrock Agents

## Usage

Here's how to use the tool with a CrewAI agent:
```

---

## Bedrock Invoke Agent Tool

**URL:** llms-txt#bedrock-invoke-agent-tool

Source: https://docs.crewai.com/en/tools/integration/bedrockinvokeagenttool

Enables CrewAI agents to invoke Amazon Bedrock Agents and leverage their capabilities within your workflows

---

## Build Crew

**URL:** llms-txt#build-crew

**Contents:**
- Overview
- Getting Started
  - Installation and Setup
  - Building Your Crew
- Support and Resources

Source: https://docs.crewai.com/en/enterprise/guides/build-crew

A Crew is a group of agents that work together to complete a task.

[CrewAI AOP](https://app.crewai.com) streamlines the process of **creating**, **deploying**, and **managing** your AI agents in production environments.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/-kSOTtYzgEw" title="Building crews with the CrewAI CLI" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

### Installation and Setup

<Card title="Follow Standard Installation" icon="wrench" href="/en/installation">
  Follow our standard installation guide to set up CrewAI CLI and create your first project.
</Card>

### Building Your Crew

<Card title="Quickstart Tutorial" icon="rocket" href="/en/quickstart">
  Follow our quickstart guide to create your first agent crew using YAML configuration.
</Card>

## Support and Resources

For Enterprise-specific support or questions, contact our dedicated support team at [support@crewai.com](mailto:support@crewai.com).

<Card title="Schedule a Demo" icon="calendar" href="mailto:support@crewai.com">
  Book time with our team to learn more about Enterprise features and how they can benefit your organization.
</Card>

---

## Build Your First Crew

**URL:** llms-txt#build-your-first-crew

**Contents:**
- Unleashing the Power of Collaborative AI
  - What You'll Build and Learn
  - Prerequisites
- Step 1: Create a New CrewAI Project
- Step 2: Explore the Project Structure
- Step 3: Configure Your Agents

Source: https://docs.crewai.com/en/guides/crews/first-crew

Step-by-step tutorial to create a collaborative AI team that works together to solve complex problems.

## Unleashing the Power of Collaborative AI

Imagine having a team of specialized AI agents working together seamlessly to solve complex problems, each contributing their unique skills to achieve a common goal. This is the power of CrewAI - a framework that enables you to create collaborative AI systems that can accomplish tasks far beyond what a single AI could achieve alone.

In this guide, we'll walk through creating a research crew that will help us research and analyze a topic, then create a comprehensive report. This practical example demonstrates how AI agents can collaborate to accomplish complex tasks, but it's just the beginning of what's possible with CrewAI.

### What You'll Build and Learn

By the end of this guide, you'll have:

1. **Created a specialized AI research team** with distinct roles and responsibilities
2. **Orchestrated collaboration** between multiple AI agents
3. **Automated a complex workflow** that involves gathering information, analysis, and report generation
4. **Built foundational skills** that you can apply to more ambitious projects

While we're building a simple research crew in this guide, the same patterns and techniques can be applied to create much more sophisticated teams for tasks like:

* Multi-stage content creation with specialized writers, editors, and fact-checkers
* Complex customer service systems with tiered support agents
* Autonomous business analysts that gather data, create visualizations, and generate insights
* Product development teams that ideate, design, and plan implementation

Let's get started building your first crew!

Before starting, make sure you have:

1. Installed CrewAI following the [installation guide](/en/installation)
2. Set up your LLM API key in your environment, following the [LLM setup
   guide](/en/concepts/llms#setting-up-your-llm)
3. Basic understanding of Python

## Step 1: Create a New CrewAI Project

First, let's create a new CrewAI project using the CLI. This command will set up a complete project structure with all the necessary files, allowing you to focus on defining your agents and their tasks rather than setting up boilerplate code.

This will generate a project with the basic structure needed for your crew. The CLI automatically creates:

* A project directory with the necessary files
* Configuration files for agents and tasks
* A basic crew implementation
* A main script to run the crew

<Frame caption="CrewAI Framework Overview">
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=514fd0b06e4128e62f10728d44601975" alt="CrewAI Framework Overview" data-og-width="634" width="634" data-og-height="473" height="473" data-path="images/crews.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=279c5c26c77fc9acc8411677716fa5ee 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=92b76be34b84b36771e0a8eed8976966 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3ef573e6215967af1bb2975a58d0d859 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1af6e6a337b70ca2ce238d8e40f49218 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c5da01705f1373446f8582ac582ff244 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=96464aab7bb5efe4213a7b80f58038aa 2500w" />
</Frame>

## Step 2: Explore the Project Structure

Let's take a moment to understand the project structure created by the CLI. CrewAI follows best practices for Python projects, making it easy to maintain and extend your code as your crews become more complex.

This structure follows best practices for Python projects and makes it easy to organize your code. The separation of configuration files (in YAML) from implementation code (in Python) makes it easy to modify your crew's behavior without changing the underlying code.

## Step 3: Configure Your Agents

Now comes the fun part - defining your AI agents! In CrewAI, agents are specialized entities with specific roles, goals, and backstories that shape their behavior. Think of them as characters in a play, each with their own personality and purpose.

For our research crew, we'll create two agents:

1. A **researcher** who excels at finding and organizing information
2. An **analyst** who can interpret research findings and create insightful reports

Let's modify the `agents.yaml` file to define these specialized agents. Be sure
to set `llm` to the provider you are using.

```yaml  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
This will generate a project with the basic structure needed for your crew. The CLI automatically creates:

* A project directory with the necessary files
* Configuration files for agents and tasks
* A basic crew implementation
* A main script to run the crew

<Frame caption="CrewAI Framework Overview">
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=514fd0b06e4128e62f10728d44601975" alt="CrewAI Framework Overview" data-og-width="634" width="634" data-og-height="473" height="473" data-path="images/crews.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=279c5c26c77fc9acc8411677716fa5ee 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=92b76be34b84b36771e0a8eed8976966 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3ef573e6215967af1bb2975a58d0d859 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1af6e6a337b70ca2ce238d8e40f49218 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c5da01705f1373446f8582ac582ff244 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=96464aab7bb5efe4213a7b80f58038aa 2500w" />
</Frame>

## Step 2: Explore the Project Structure

Let's take a moment to understand the project structure created by the CLI. CrewAI follows best practices for Python projects, making it easy to maintain and extend your code as your crews become more complex.
```

Example 2 (unknown):
```unknown
This structure follows best practices for Python projects and makes it easy to organize your code. The separation of configuration files (in YAML) from implementation code (in Python) makes it easy to modify your crew's behavior without changing the underlying code.

## Step 3: Configure Your Agents

Now comes the fun part - defining your AI agents! In CrewAI, agents are specialized entities with specific roles, goals, and backstories that shape their behavior. Think of them as characters in a play, each with their own personality and purpose.

For our research crew, we'll create two agents:

1. A **researcher** who excels at finding and organizing information
2. An **analyst** who can interpret research findings and create insightful reports

Let's modify the `agents.yaml` file to define these specialized agents. Be sure
to set `llm` to the provider you are using.
```

---

## Build Your First Flow

**URL:** llms-txt#build-your-first-flow

**Contents:**
- Taking Control of AI Workflows with Flows
  - What Makes Flows Powerful
  - What You'll Build and Learn
- Prerequisites
- Step 1: Create a New CrewAI Flow Project
- Step 2: Understanding the Project Structure
- Step 3: Add a Content Writer Crew
- Step 4: Configure the Content Writer Crew

Source: https://docs.crewai.com/en/guides/flows/first-flow

Learn how to create structured, event-driven workflows with precise control over execution.

## Taking Control of AI Workflows with Flows

CrewAI Flows represent the next level in AI orchestration - combining the collaborative power of AI agent crews with the precision and flexibility of procedural programming. While crews excel at agent collaboration, flows give you fine-grained control over exactly how and when different components of your AI system interact.

In this guide, we'll walk through creating a powerful CrewAI Flow that generates a comprehensive learning guide on any topic. This tutorial will demonstrate how Flows provide structured, event-driven control over your AI workflows by combining regular code, direct LLM calls, and crew-based processing.

### What Makes Flows Powerful

1. **Combine different AI interaction patterns** - Use crews for complex collaborative tasks, direct LLM calls for simpler operations, and regular code for procedural logic
2. **Build event-driven systems** - Define how components respond to specific events and data changes
3. **Maintain state across components** - Share and transform data between different parts of your application
4. **Integrate with external systems** - Seamlessly connect your AI workflow with databases, APIs, and user interfaces
5. **Create complex execution paths** - Design conditional branches, parallel processing, and dynamic workflows

### What You'll Build and Learn

By the end of this guide, you'll have:

1. **Created a sophisticated content generation system** that combines user input, AI planning, and multi-agent content creation
2. **Orchestrated the flow of information** between different components of your system
3. **Implemented event-driven architecture** where each step responds to the completion of previous steps
4. **Built a foundation for more complex AI applications** that you can expand and customize

This guide creator flow demonstrates fundamental patterns that can be applied to create much more advanced applications, such as:

* Interactive AI assistants that combine multiple specialized subsystems
* Complex data processing pipelines with AI-enhanced transformations
* Autonomous agents that integrate with external services and APIs
* Multi-stage decision-making systems with human-in-the-loop processes

Let's dive in and build your first flow!

Before starting, make sure you have:

1. Installed CrewAI following the [installation guide](/en/installation)
2. Set up your LLM API key in your environment, following the [LLM setup
   guide](/en/concepts/llms#setting-up-your-llm)
3. Basic understanding of Python

## Step 1: Create a New CrewAI Flow Project

First, let's create a new CrewAI Flow project using the CLI. This command sets up a scaffolded project with all the necessary directories and template files for your flow.

This will generate a project with the basic structure needed for your flow.

<Frame caption="CrewAI Framework Overview">
  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=82ea168de2f004553dcea21410cd7d8a" alt="CrewAI Framework Overview" data-og-width="669" width="669" data-og-height="464" height="464" data-path="images/flows.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=4a6177acae3789dd8e4467b791c8966e 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=7900e4cdad93fd37bbcd2f1f2f38b40b 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a83fa78165e93bc1d988a30ebc33889a 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=540eb3d8d8f256d6d703aa5e6111a4cd 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=04fbb8e23728b87efa78a0a776e2d194 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=ff06d73f5d4aa911154c66becf14d732 2500w" />
</Frame>

## Step 2: Understanding the Project Structure

The generated project has the following structure. Take a moment to familiarize yourself with it, as understanding this structure will help you create more complex flows in the future.

This structure provides a clear separation between different components of your flow:

* The main flow logic in the `main.py` file
* Specialized crews in the `crews` directory
* Custom tools in the `tools` directory

We'll modify this structure to create our guide creator flow, which will orchestrate the process of generating comprehensive learning guides.

## Step 3: Add a Content Writer Crew

Our flow will need a specialized crew to handle the content creation process. Let's use the CrewAI CLI to add a content writer crew:

This command automatically creates the necessary directories and template files for your crew. The content writer crew will be responsible for writing and reviewing sections of our guide, working within the overall flow orchestrated by our main application.

## Step 4: Configure the Content Writer Crew

Now, let's modify the generated files for the content writer crew. We'll set up two specialized agents - a writer and a reviewer - that will collaborate to create high-quality content for our guide.

1. First, update the agents configuration file to define our content creation team:

Remember to set `llm` to the provider you are using.

```yaml  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
This will generate a project with the basic structure needed for your flow.

<Frame caption="CrewAI Framework Overview">
  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=82ea168de2f004553dcea21410cd7d8a" alt="CrewAI Framework Overview" data-og-width="669" width="669" data-og-height="464" height="464" data-path="images/flows.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=4a6177acae3789dd8e4467b791c8966e 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=7900e4cdad93fd37bbcd2f1f2f38b40b 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a83fa78165e93bc1d988a30ebc33889a 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=540eb3d8d8f256d6d703aa5e6111a4cd 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=04fbb8e23728b87efa78a0a776e2d194 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=ff06d73f5d4aa911154c66becf14d732 2500w" />
</Frame>

## Step 2: Understanding the Project Structure

The generated project has the following structure. Take a moment to familiarize yourself with it, as understanding this structure will help you create more complex flows in the future.
```

Example 2 (unknown):
```unknown
This structure provides a clear separation between different components of your flow:

* The main flow logic in the `main.py` file
* Specialized crews in the `crews` directory
* Custom tools in the `tools` directory

We'll modify this structure to create our guide creator flow, which will orchestrate the process of generating comprehensive learning guides.

## Step 3: Add a Content Writer Crew

Our flow will need a specialized crew to handle the content creation process. Let's use the CrewAI CLI to add a content writer crew:
```

Example 3 (unknown):
```unknown
This command automatically creates the necessary directories and template files for your crew. The content writer crew will be responsible for writing and reviewing sections of our guide, working within the overall flow orchestrated by our main application.

## Step 4: Configure the Content Writer Crew

Now, let's modify the generated files for the content writer crew. We'll set up two specialized agents - a writer and a reviewer - that will collaborate to create high-quality content for our guide.

1. First, update the agents configuration file to define our content creation team:

   Remember to set `llm` to the provider you are using.
```

---

## Check if API keys are set

**URL:** llms-txt#check-if-api-keys-are-set

required_keys = ["OPENAI_API_KEY", "GOOGLE_API_KEY", "COHERE_API_KEY"]
for key in required_keys:
    if os.getenv(key):
        print(f"✅ {key} is set")
    else:
        print(f"❌ {key} is not set")
python  theme={null}
import time

def test_embedding_performance(embedder_config, test_text="This is a test document"):
    start_time = time.time()

crew = Crew(
        agents=[...],
        tasks=[...],
        memory=True,
        embedder=embedder_config
    )

# Simulate memory operation
    crew.kickoff()

end_time = time.time()
    return end_time - start_time

**Examples:**

Example 1 (unknown):
```unknown
**Performance comparison:**
```

---

## ClickUp Integration

**URL:** llms-txt#clickup-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up ClickUp Integration
  - 1. Connect Your ClickUp Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic ClickUp Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/clickup

Task and productivity management with ClickUp integration for CrewAI.

Enable your agents to manage tasks, projects, and productivity workflows through ClickUp. Create and update tasks, organize projects, manage team assignments, and streamline your productivity management with AI-powered automation.

Before using the ClickUp integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A ClickUp account with appropriate permissions
* Connected your ClickUp account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up ClickUp Integration

### 1. Connect Your ClickUp Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **ClickUp** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for task and project management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="clickup/search_tasks">
    **Description:** Search for tasks in ClickUp using advanced filters.

* `taskFilterFormula` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
      
      Available fields: `space_ids%5B%5D`, `project_ids%5B%5D`, `list_ids%5B%5D`, `statuses%5B%5D`, `include_closed`, `assignees%5B%5D`, `tags%5B%5D`, `due_date_gt`, `due_date_lt`, `date_created_gt`, `date_created_lt`, `date_updated_gt`, `date_updated_lt`
  </Accordion>

<Accordion title="clickup/get_task_in_list">
    **Description:** Get tasks in a specific list in ClickUp.

* `listId` (string, required): List - Select a List to get tasks from. Use Connect Portal User Settings to allow users to select a ClickUp List.
    * `taskFilterFormula` (string, optional): Search for tasks that match specified filters. For example: name=task1.
  </Accordion>

<Accordion title="clickup/create_task">
    **Description:** Create a task in ClickUp.

* `listId` (string, required): List - Select a List to create this task in. Use Connect Portal User Settings to allow users to select a ClickUp List.
    * `name` (string, required): Name - The task name.
    * `description` (string, optional): Description - Task description.
    * `status` (string, optional): Status - Select a Status for this task. Use Connect Portal User Settings to allow users to select a ClickUp Status.
    * `assignees` (string, optional): Assignees - Select a Member (or an array of member IDs) to be assigned to this task. Use Connect Portal User Settings to allow users to select a ClickUp Member.
    * `dueDate` (string, optional): Due Date - Specify a date for this task to be due on.
    * `additionalFields` (string, optional): Additional Fields - Specify additional fields to include on this task as JSON.
  </Accordion>

<Accordion title="clickup/update_task">
    **Description:** Update a task in ClickUp.

* `taskId` (string, required): Task ID - The ID of the task to update.
    * `listId` (string, required): List - Select a List to create this task in. Use Connect Portal User Settings to allow users to select a ClickUp List.
    * `name` (string, optional): Name - The task name.
    * `description` (string, optional): Description - Task description.
    * `status` (string, optional): Status - Select a Status for this task. Use Connect Portal User Settings to allow users to select a ClickUp Status.
    * `assignees` (string, optional): Assignees - Select a Member (or an array of member IDs) to be assigned to this task. Use Connect Portal User Settings to allow users to select a ClickUp Member.
    * `dueDate` (string, optional): Due Date - Specify a date for this task to be due on.
    * `additionalFields` (string, optional): Additional Fields - Specify additional fields to include on this task as JSON.
  </Accordion>

<Accordion title="clickup/delete_task">
    **Description:** Delete a task in ClickUp.

* `taskId` (string, required): Task ID - The ID of the task to delete.
  </Accordion>

<Accordion title="clickup/get_list">
    **Description:** Get List information in ClickUp.

* `spaceId` (string, required): Space ID - The ID of the space containing the lists.
  </Accordion>

<Accordion title="clickup/get_custom_fields_in_list">
    **Description:** Get Custom Fields in a List in ClickUp.

* `listId` (string, required): List ID - The ID of the list to get custom fields from.
  </Accordion>

<Accordion title="clickup/get_all_fields_in_list">
    **Description:** Get All Fields in a List in ClickUp.

* `listId` (string, required): List ID - The ID of the list to get all fields from.
  </Accordion>

<Accordion title="clickup/get_space">
    **Description:** Get Space information in ClickUp.

* `spaceId` (string, optional): Space ID - The ID of the space to retrieve.
  </Accordion>

<Accordion title="clickup/get_folders">
    **Description:** Get Folders in ClickUp.

* `spaceId` (string, required): Space ID - The ID of the space containing the folders.
  </Accordion>

<Accordion title="clickup/get_member">
    **Description:** Get Member information in ClickUp.

**Parameters:** None required.
  </Accordion>
</AccordionGroup>

### Basic ClickUp Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="clickup/search_tasks">
    **Description:** Search for tasks in ClickUp using advanced filters.

    **Parameters:**

    * `taskFilterFormula` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
```

Example 4 (unknown):
```unknown
Available fields: `space_ids%5B%5D`, `project_ids%5B%5D`, `list_ids%5B%5D`, `statuses%5B%5D`, `include_closed`, `assignees%5B%5D`, `tags%5B%5D`, `due_date_gt`, `due_date_lt`, `date_created_gt`, `date_created_lt`, `date_updated_gt`, `date_updated_lt`
  </Accordion>

  <Accordion title="clickup/get_task_in_list">
    **Description:** Get tasks in a specific list in ClickUp.

    **Parameters:**

    * `listId` (string, required): List - Select a List to get tasks from. Use Connect Portal User Settings to allow users to select a ClickUp List.
    * `taskFilterFormula` (string, optional): Search for tasks that match specified filters. For example: name=task1.
  </Accordion>

  <Accordion title="clickup/create_task">
    **Description:** Create a task in ClickUp.

    **Parameters:**

    * `listId` (string, required): List - Select a List to create this task in. Use Connect Portal User Settings to allow users to select a ClickUp List.
    * `name` (string, required): Name - The task name.
    * `description` (string, optional): Description - Task description.
    * `status` (string, optional): Status - Select a Status for this task. Use Connect Portal User Settings to allow users to select a ClickUp Status.
    * `assignees` (string, optional): Assignees - Select a Member (or an array of member IDs) to be assigned to this task. Use Connect Portal User Settings to allow users to select a ClickUp Member.
    * `dueDate` (string, optional): Due Date - Specify a date for this task to be due on.
    * `additionalFields` (string, optional): Additional Fields - Specify additional fields to include on this task as JSON.
  </Accordion>

  <Accordion title="clickup/update_task">
    **Description:** Update a task in ClickUp.

    **Parameters:**

    * `taskId` (string, required): Task ID - The ID of the task to update.
    * `listId` (string, required): List - Select a List to create this task in. Use Connect Portal User Settings to allow users to select a ClickUp List.
    * `name` (string, optional): Name - The task name.
    * `description` (string, optional): Description - Task description.
    * `status` (string, optional): Status - Select a Status for this task. Use Connect Portal User Settings to allow users to select a ClickUp Status.
    * `assignees` (string, optional): Assignees - Select a Member (or an array of member IDs) to be assigned to this task. Use Connect Portal User Settings to allow users to select a ClickUp Member.
    * `dueDate` (string, optional): Due Date - Specify a date for this task to be due on.
    * `additionalFields` (string, optional): Additional Fields - Specify additional fields to include on this task as JSON.
  </Accordion>

  <Accordion title="clickup/delete_task">
    **Description:** Delete a task in ClickUp.

    **Parameters:**

    * `taskId` (string, required): Task ID - The ID of the task to delete.
  </Accordion>

  <Accordion title="clickup/get_list">
    **Description:** Get List information in ClickUp.

    **Parameters:**

    * `spaceId` (string, required): Space ID - The ID of the space containing the lists.
  </Accordion>

  <Accordion title="clickup/get_custom_fields_in_list">
    **Description:** Get Custom Fields in a List in ClickUp.

    **Parameters:**

    * `listId` (string, required): List ID - The ID of the list to get custom fields from.
  </Accordion>

  <Accordion title="clickup/get_all_fields_in_list">
    **Description:** Get All Fields in a List in ClickUp.

    **Parameters:**

    * `listId` (string, required): List ID - The ID of the list to get all fields from.
  </Accordion>

  <Accordion title="clickup/get_space">
    **Description:** Get Space information in ClickUp.

    **Parameters:**

    * `spaceId` (string, optional): Space ID - The ID of the space to retrieve.
  </Accordion>

  <Accordion title="clickup/get_folders">
    **Description:** Get Folders in ClickUp.

    **Parameters:**

    * `spaceId` (string, required): Space ID - The ID of the space containing the folders.
  </Accordion>

  <Accordion title="clickup/get_member">
    **Description:** Get Member information in ClickUp.

    **Parameters:** None required.
  </Accordion>
</AccordionGroup>

## Usage Examples

### Basic ClickUp Agent Setup
```

---

## Coding Agents

**URL:** llms-txt#coding-agents

**Contents:**
- Introduction
- Enabling Code Execution
- Important Considerations
- Code Execution Process
- Example Usage

Source: https://docs.crewai.com/en/learn/coding-agents

Learn how to enable your CrewAI Agents to write and execute code, and explore advanced features for enhanced functionality.

CrewAI Agents now have the powerful ability to write and execute code, significantly enhancing their problem-solving capabilities. This feature is particularly useful for tasks that require computational or programmatic solutions.

## Enabling Code Execution

To enable code execution for an agent, set the `allow_code_execution` parameter to `True` when creating the agent.

<Note>
  Note that `allow_code_execution` parameter defaults to `False`.
</Note>

## Important Considerations

1. **Model Selection**: It is strongly recommended to use more capable models like Claude 3.5 Sonnet and GPT-4 when enabling code execution.
   These models have a better understanding of programming concepts and are more likely to generate correct and efficient code.

2. **Error Handling**: The code execution feature includes error handling. If executed code raises an exception, the agent will receive the error message and can attempt to correct the code or
   provide alternative solutions. The `max_retry_limit` parameter, which defaults to 2, controls the maximum number of retries for a task.

3. **Dependencies**: To use the code execution feature, you need to install the `crewai_tools` package. If not installed, the agent will log an info message:
   "Coding tools not available. Install crewai\_tools."

## Code Execution Process

When an agent with code execution enabled encounters a task requiring programming:

<Steps>
  <Step title="Task Analysis">
    The agent analyzes the task and determines that code execution is necessary.
  </Step>

<Step title="Code Formulation">
    It formulates the Python code needed to solve the problem.
  </Step>

<Step title="Code Execution">
    The code is sent to the internal code execution tool (`CodeInterpreterTool`).
  </Step>

<Step title="Result Interpretation">
    The agent interprets the result and incorporates it into its response or uses it for further problem-solving.
  </Step>
</Steps>

Here's a detailed example of creating an agent with code execution capabilities and using it in a task:

```python Code theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
<Note>
  Note that `allow_code_execution` parameter defaults to `False`.
</Note>

## Important Considerations

1. **Model Selection**: It is strongly recommended to use more capable models like Claude 3.5 Sonnet and GPT-4 when enabling code execution.
   These models have a better understanding of programming concepts and are more likely to generate correct and efficient code.

2. **Error Handling**: The code execution feature includes error handling. If executed code raises an exception, the agent will receive the error message and can attempt to correct the code or
   provide alternative solutions. The `max_retry_limit` parameter, which defaults to 2, controls the maximum number of retries for a task.

3. **Dependencies**: To use the code execution feature, you need to install the `crewai_tools` package. If not installed, the agent will log an info message:
   "Coding tools not available. Install crewai\_tools."

## Code Execution Process

When an agent with code execution enabled encounters a task requiring programming:

<Steps>
  <Step title="Task Analysis">
    The agent analyzes the task and determines that code execution is necessary.
  </Step>

  <Step title="Code Formulation">
    It formulates the Python code needed to solve the problem.
  </Step>

  <Step title="Code Execution">
    The code is sent to the internal code execution tool (`CodeInterpreterTool`).
  </Step>

  <Step title="Result Interpretation">
    The agent interprets the result and incorporates it into its response or uses it for further problem-solving.
  </Step>
</Steps>

## Example Usage

Here's a detailed example of creating an agent with code execution capabilities and using it in a task:
```

---

## Collaboration

**URL:** llms-txt#collaboration

**Contents:**
- Overview
- Quick Start: Enable Collaboration

Source: https://docs.crewai.com/en/concepts/collaboration

How to enable agents to work together, delegate tasks, and communicate effectively within CrewAI teams.

Collaboration in CrewAI enables agents to work together as a team by delegating tasks and asking questions to leverage each other's expertise. When `allow_delegation=True`, agents automatically gain access to powerful collaboration tools.

## Quick Start: Enable Collaboration

```python  theme={null}
from crewai import Agent, Crew, Task

---

## Complex communication automation task

**URL:** llms-txt#complex-communication-automation-task

**Contents:**
- Troubleshooting
  - Common Issues
  - Getting Help

automation_task = Task(
    description="""
    1. List all workspace users and identify team roles
    2. Get specific user information for project stakeholders
    3. Create automated status update comments on key project pages
    4. Facilitate team communication through targeted comments
    """,
    agent=communication_automator,
    expected_output="Automated communication workflow completed with user management and comments"
)

crew = Crew(
    agents=[communication_automator],
    tasks=[automation_task]
)

**Permission Errors**

* Ensure your Notion account has appropriate permissions to read user information
* Verify that the OAuth connection includes required scopes for user access and comment creation
* Check that you have permissions to comment on the target pages or discussions

**User Access Issues**

* Ensure you have workspace admin permissions to list all users
* Verify that user IDs are correct and users exist in the workspace
* Check that the workspace allows API access to user information

**Comment Creation Issues**

* Verify that page IDs or discussion IDs are correct and accessible
* Ensure that rich text content follows Notion's API format specifications
* Check that you have comment permissions on the target pages or discussions

* Be mindful of Notion's API rate limits when making multiple requests
* Implement appropriate delays between requests if needed
* Consider pagination for large user lists

**Parent Object Specification**

* Ensure parent object type is correctly specified (page\_id or discussion\_id)
* Verify that the parent page or discussion exists and is accessible
* Check that the parent object ID format is correct

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Notion integration setup or troubleshooting.
</Card>

---

## Complex task involving analytics and reporting

**URL:** llms-txt#complex-task-involving-analytics-and-reporting

analytics_task = Task(
    description="""
    1. Search for all open tickets from the last 30 days
    2. Analyze ticket resolution times and customer satisfaction
    3. Identify common issues and support patterns
    4. Generate weekly support performance report
    """,
    agent=support_analyst,
    expected_output="Comprehensive support analytics report with performance insights and recommendations"
)

crew = Crew(
    agents=[support_analyst],
    tasks=[analytics_task]
)

---

## Complex task involving financial analysis

**URL:** llms-txt#complex-task-involving-financial-analysis

**Contents:**
- Subscription Status Reference
- Metadata Usage

analytics_task = Task(
    description="""
    1. Retrieve balance transactions for the current month
    2. Analyze customer payment patterns and subscription trends
    3. Identify high-value customers and subscription performance
    4. Generate monthly financial performance report
    """,
    agent=financial_analyst,
    expected_output="Comprehensive financial analysis with payment insights and recommendations"
)

crew = Crew(
    agents=[financial_analyst],
    tasks=[analytics_task]
)

crew.kickoff()
json  theme={null}
{
  "customer_segment": "enterprise",
  "acquisition_source": "google_ads",
  "lifetime_value": "high",
  "custom_field_1": "value1"
}
```

This integration enables comprehensive payment and subscription management automation, allowing your AI agents to handle billing operations seamlessly within your Stripe ecosystem.

**Examples:**

Example 1 (unknown):
```unknown
## Subscription Status Reference

Understanding subscription statuses:

* **incomplete** - Subscription requires payment method or payment confirmation
* **incomplete\_expired** - Subscription expired before payment was confirmed
* **trialing** - Subscription is in trial period
* **active** - Subscription is active and current
* **past\_due** - Payment failed but subscription is still active
* **canceled** - Subscription has been canceled
* **unpaid** - Payment failed and subscription is no longer active

## Metadata Usage

Metadata allows you to store additional information about customers, subscriptions, and products:
```

---

## Complex task involving multiple Asana operations

**URL:** llms-txt#complex-task-involving-multiple-asana-operations

coordination_task = Task(
    description="""
    1. Get all active projects in the workspace
    2. For each project, get the list of incomplete tasks
    3. Create a summary report task in the 'Management Reports' project
    4. Add comments to overdue tasks to request status updates
    """,
    agent=project_coordinator,
    expected_output="Summary report created and status update requests sent for overdue tasks"
)

crew = Crew(
    agents=[project_coordinator],
    tasks=[coordination_task]
)

---

## Complex task involving multiple Box operations

**URL:** llms-txt#complex-task-involving-multiple-box-operations

management_task = Task(
    description="""
    1. List all files in the root folder
    2. Create monthly archive folders for the current year
    3. Move old files to appropriate archive folders
    4. Generate a summary report of the file organization
    """,
    agent=file_manager,
    expected_output="Files organized into archive structure with summary report"
)

crew = Crew(
    agents=[file_manager],
    tasks=[management_task]
)

---

## Complex task involving multiple ClickUp operations

**URL:** llms-txt#complex-task-involving-multiple-clickup-operations

**Contents:**
  - Task Search and Management

project_coordination = Task(
    description="""
    1. Get all open tasks in the current space
    2. Identify overdue tasks and update their status
    3. Create a weekly report task summarizing project progress
    4. Assign the report task to the team lead
    """,
    agent=project_manager,
    expected_output="Project status updated and weekly report task created and assigned"
)

crew = Crew(
    agents=[project_manager],
    tasks=[project_coordination]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

task_analyst = Agent(
    role="Task Analyst",
    goal="Analyze task patterns and optimize team productivity",
    backstory="An AI assistant that analyzes task data to improve team efficiency.",
    apps=['clickup']
)

**Examples:**

Example 1 (unknown):
```unknown
### Task Search and Management
```

---

## Complex task involving multiple GitHub operations

**URL:** llms-txt#complex-task-involving-multiple-github-operations

**Contents:**
  - Getting Help

coordination_task = Task(
    description="""
    1. Search for all open issues assigned to the current milestone
    2. Identify overdue issues and update their priority labels
    3. Create a weekly progress report issue
    4. Lock resolved issues that have been inactive for 30 days
    """,
    agent=project_coordinator,
    expected_output="Project coordination completed with progress report and issue management"
)

crew = Crew(
    agents=[project_coordinator],
    tasks=[coordination_task]
)

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with GitHub integration setup or troubleshooting.
</Card>

---

## Complex task involving multiple operations

**URL:** llms-txt#complex-task-involving-multiple-operations

**Contents:**
  - Getting Help

analytics_task = Task(
    description="""
    1. Retrieve recent customer data and order history
    2. Identify abandoned carts from the last 7 days
    3. Analyze product performance and inventory levels
    4. Generate recommendations for customer retention
    """,
    agent=analytics_agent,
    expected_output="Comprehensive e-commerce analytics report with actionable insights"
)

crew = Crew(
    agents=[analytics_agent],
    tasks=[analytics_task]
)

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Shopify integration setup or troubleshooting.
</Card>

---

## Complex task involving search and analysis

**URL:** llms-txt#complex-task-involving-search-and-analysis

**Contents:**
- Contact Support

analysis_task = Task(
    description="""
    1. Search for recent project-related messages across all channels
    2. Find users by email to identify team members
    3. Analyze communication patterns and response times
    4. Generate weekly team communication summary
    """,
    agent=analytics_agent,
    expected_output="Comprehensive communication analysis with team insights and recommendations"
)

crew = Crew(
    agents=[analytics_agent],
    tasks=[analysis_task]
)

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Slack integration setup or troubleshooting.
</Card>

---

## Complex task involving SOQL queries and data analysis

**URL:** llms-txt#complex-task-involving-soql-queries-and-data-analysis

**Contents:**
  - Getting Help

analysis_task = Task(
    description="""
    1. Execute a SOQL query to find all opportunities closing this quarter
    2. Search for contacts at companies with opportunities over $100K
    3. Create a summary report of the sales pipeline status
    4. Update high-value opportunities with next steps
    """,
    agent=data_analyst,
    expected_output="Comprehensive sales pipeline analysis with actionable insights"
)

crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task]
)

This comprehensive documentation covers all the Salesforce tools organized by functionality, making it easy for users to find the specific operations they need for their CRM automation tasks.

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Salesforce integration setup or troubleshooting.
</Card>

---

## Complex workflow task

**URL:** llms-txt#complex-workflow-task

**Contents:**
- Troubleshooting
  - Common Issues
  - Getting Help

workflow_task = Task(
    description="""
    1. Get all customer data from the main customer spreadsheet
    2. Create a new monthly summary spreadsheet
    3. Append summary data to the new spreadsheet
    4. Update customer status based on activity metrics
    5. Generate reports with proper formatting
    """,
    agent=workflow_manager,
    expected_output="Monthly customer workflow completed with new spreadsheet and updated data"
)

crew = Crew(
    agents=[workflow_manager],
    tasks=[workflow_task]
)

**Permission Errors**

* Ensure your Google account has edit access to the target spreadsheets
* Verify that the OAuth connection includes required scopes for Google Sheets API
* Check that spreadsheets are shared with the authenticated account

**Spreadsheet Structure Issues**

* Ensure worksheets have proper column headers before creating or updating rows
* Verify that range notation (A1 format) is correct for the target cells
* Check that the specified spreadsheet ID exists and is accessible

**Data Type and Format Issues**

* Ensure data values match the expected format for each column
* Use proper date formats for date columns (ISO format recommended)
* Verify that numeric values are properly formatted for number columns

**Range and Cell Reference Issues**

* Use proper A1 notation for ranges (e.g., "A1:C10", "Sheet1!A1:B5")
* Ensure range references don't exceed the actual spreadsheet dimensions
* Verify that sheet names in range references match actual sheet names

**Value Input and Rendering Options**

* Choose appropriate `valueInputOption` (RAW vs USER\_ENTERED) for your data
* Select proper `valueRenderOption` based on how you want data formatted
* Consider `dateTimeRenderOption` for consistent date/time handling

**Spreadsheet Creation Issues**

* Ensure spreadsheet titles are unique and follow naming conventions
* Verify that sheet properties are properly structured when creating sheets
* Check that you have permissions to create new spreadsheets in your account

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Google Sheets integration setup or troubleshooting.
</Card>

---

## Conditional Tasks

**URL:** llms-txt#conditional-tasks

**Contents:**
- Introduction
- Example Usage

Source: https://docs.crewai.com/en/learn/conditional-tasks

Learn how to use conditional tasks in a crewAI kickoff

Conditional Tasks in crewAI allow for dynamic workflow adaptation based on the outcomes of previous tasks.
This powerful feature enables crews to make decisions and execute tasks selectively, enhancing the flexibility and efficiency of your AI-driven processes.

```python Code theme={null}
from typing import List
from pydantic import BaseModel
from crewai import Agent, Crew
from crewai.tasks.conditional_task import ConditionalTask
from crewai.tasks.task_output import TaskOutput
from crewai.task import Task
from crewai_tools import SerperDevTool

---

## Configure and run the crew

**URL:** llms-txt#configure-and-run-the-crew

**Contents:**
- Viewing Your Traces
- Troubleshooting
  - Common Issues
- Resources

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)

try:
    result = crew.kickoff()
finally:
    maxim.cleanup()  # Ensure cleanup happens even if errors occur
python  theme={null}
  instrument_crewai(logger, debug=True)
  python  theme={null}
  agent = CrewAgent(..., verbose=True)
  ```
* Double-check that `instrument_crewai()` is called **before** creating or executing agents. This might be obvious, but it's a common oversight.

<CardGroup cols="3">
  <Card title="CrewAI Docs" icon="book" href="https://docs.crewai.com/">
    Official CrewAI documentation
  </Card>

<Card title="Maxim Docs" icon="book" href="https://getmaxim.ai/docs">
    Official Maxim documentation
  </Card>

<Card title="Maxim Github" icon="github" href="https://github.com/maximhq">
    Maxim Github
  </Card>
</CardGroup>

**Examples:**

Example 1 (unknown):
```unknown
That's it! All your CrewAI agent interactions will now be logged and available in your Maxim dashboard.

Check this Google Colab Notebook for a quick reference - [Notebook](https://colab.research.google.com/drive/1ZKIZWsmgQQ46n8TH9zLsT1negKkJA6K8?usp=sharing)

## Viewing Your Traces

After running your CrewAI application:

1. Log in to your [Maxim Dashboard](https://app.getmaxim.ai/login)
2. Navigate to your repository
3. View detailed agent traces, including:

   * Agent conversations
   * Tool usage patterns
   * Performance metrics
   * Cost analytics

   <img src="https://raw.githubusercontent.com/akmadan/crewAI/docs_maxim_observability/docs/images/crewai_traces.gif" />

## Troubleshooting

### Common Issues

* **No traces appearing**: Ensure your API key and repository ID are correct
* Ensure you've **`called instrument_crewai()`** ***before*** running your crew. This initializes logging hooks correctly.
* Set `debug=True` in your `instrument_crewai()` call to surface any internal errors:
```

Example 2 (unknown):
```unknown
* Configure your agents with `verbose=True` to capture detailed logs:
```

---

## Continue with additional focused tasks...

**URL:** llms-txt#continue-with-additional-focused-tasks...

**Contents:**
  - 3. Misaligned Description and Expected Output
  - 4. Not Understanding the Process Yourself
  - 5. Premature Use of Hierarchical Structures
  - 6. Vague or Generic Agent Definitions
- Advanced Agent Design Strategies
  - Designing for Collaboration

yaml  theme={null}
analysis_task:
  description: "Analyze customer feedback to find areas of improvement."
  expected_output: "A marketing plan for the next quarter."
yaml  theme={null}
analysis_task:
  description: "Analyze customer feedback to identify the top 3 areas for product improvement."
  expected_output: "A report listing the 3 priority improvement areas with supporting customer quotes and data points."
yaml  theme={null}
agent:
  role: "Business Analyst"
  goal: "Analyze business data"
  backstory: "You are good at business analysis."
yaml  theme={null}
agent:
  role: "SaaS Metrics Specialist focusing on growth-stage startups"
  goal: "Identify actionable insights from business data that can directly impact customer retention and revenue growth"
  backstory: "With 10+ years analyzing SaaS business models, you've developed a keen eye for the metrics that truly matter for sustainable growth. You've helped numerous companies identify the leverage points that turned around their business trajectory. You believe in connecting data to specific, actionable recommendations rather than general observations."
yaml  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
### 3. Misaligned Description and Expected Output

**Problem:** The task description asks for one thing while the expected output specifies something different.

**Example of Poor Design:**
```

Example 2 (unknown):
```unknown
**Improved Version:**
```

Example 3 (unknown):
```unknown
### 4. Not Understanding the Process Yourself

**Problem:** Asking agents to execute tasks that you yourself don't fully understand.

**Solution:**

1. Try to perform the task manually first
2. Document your process, decision points, and information sources
3. Use this documentation as the basis for your task description

### 5. Premature Use of Hierarchical Structures

**Problem:** Creating unnecessarily complex agent hierarchies where sequential processes would work better.

**Solution:** Start with sequential processes and only move to hierarchical models when the workflow complexity truly requires it.

### 6. Vague or Generic Agent Definitions

**Problem:** Generic agent definitions lead to generic outputs.

**Example of Poor Design:**
```

Example 4 (unknown):
```unknown
**Improved Version:**
```

---

## Crafting Effective Agents

**URL:** llms-txt#crafting-effective-agents

**Contents:**
- The Art and Science of Agent Design
  - Why Agent Design Matters
- The 80/20 Rule: Focus on Tasks Over Agents
- Core Principles of Effective Agent Design
  - 1. The Role-Goal-Backstory Framework
  - 2. Specialists Over Generalists
  - 3. Balancing Specialization and Versatility
  - 4. Setting Appropriate Expertise Levels
- Practical Examples: Before and After
  - Example 1: Content Creation Agent

Source: https://docs.crewai.com/en/guides/agents/crafting-effective-agents

Learn best practices for designing powerful, specialized AI agents that collaborate effectively to solve complex problems.

## The Art and Science of Agent Design

At the heart of CrewAI lies the agent - a specialized AI entity designed to perform specific roles within a collaborative framework. While creating basic agents is simple, crafting truly effective agents that produce exceptional results requires understanding key design principles and best practices.

This guide will help you master the art of agent design, enabling you to create specialized AI personas that collaborate effectively, think critically, and produce high-quality outputs tailored to your specific needs.

### Why Agent Design Matters

The way you define your agents significantly impacts:

1. **Output quality**: Well-designed agents produce more relevant, high-quality results
2. **Collaboration effectiveness**: Agents with complementary skills work together more efficiently
3. **Task performance**: Agents with clear roles and goals execute tasks more effectively
4. **System scalability**: Thoughtfully designed agents can be reused across multiple crews and contexts

Let's explore best practices for creating agents that excel in these dimensions.

## The 80/20 Rule: Focus on Tasks Over Agents

When building effective AI systems, remember this crucial principle: **80% of your effort should go into designing tasks, and only 20% into defining agents**.

Why? Because even the most perfectly defined agent will fail with poorly designed tasks, but well-designed tasks can elevate even a simple agent. This means:

* Spend most of your time writing clear task instructions
* Define detailed inputs and expected outputs
* Add examples and context to guide execution
* Dedicate the remaining time to agent role, goal, and backstory

This doesn't mean agent design isn't important - it absolutely is. But task design is where most execution failures occur, so prioritize accordingly.

## Core Principles of Effective Agent Design

### 1. The Role-Goal-Backstory Framework

The most powerful agents in CrewAI are built on a strong foundation of three key elements:

#### Role: The Agent's Specialized Function

The role defines what the agent does and their area of expertise. When crafting roles:

* **Be specific and specialized**: Instead of "Writer," use "Technical Documentation Specialist" or "Creative Storyteller"
* **Align with real-world professions**: Base roles on recognizable professional archetypes
* **Include domain expertise**: Specify the agent's field of knowledge (e.g., "Financial Analyst specializing in market trends")

**Examples of effective roles:**

#### Goal: The Agent's Purpose and Motivation

The goal directs the agent's efforts and shapes their decision-making process. Effective goals should:

* **Be clear and outcome-focused**: Define what the agent is trying to achieve
* **Emphasize quality standards**: Include expectations about the quality of work
* **Incorporate success criteria**: Help the agent understand what "good" looks like

**Examples of effective goals:**

#### Backstory: The Agent's Experience and Perspective

The backstory gives depth to the agent, influencing how they approach problems and interact with others. Good backstories:

* **Establish expertise and experience**: Explain how the agent gained their skills
* **Define working style and values**: Describe how the agent approaches their work
* **Create a cohesive persona**: Ensure all elements of the backstory align with the role and goal

**Examples of effective backstories:**

### 2. Specialists Over Generalists

Agents perform significantly better when given specialized roles rather than general ones. A highly focused agent delivers more precise, relevant outputs:

**Generic (Less Effective):**

**Specialized (More Effective):**

**Specialist Benefits:**

* Clearer understanding of expected output
* More consistent performance
* Better alignment with specific tasks
* Improved ability to make domain-specific judgments

### 3. Balancing Specialization and Versatility

Effective agents strike the right balance between specialization (doing one thing extremely well) and versatility (being adaptable to various situations):

* **Specialize in role, versatile in application**: Create agents with specialized skills that can be applied across multiple contexts
* **Avoid overly narrow definitions**: Ensure agents can handle variations within their domain of expertise
* **Consider the collaborative context**: Design agents whose specializations complement the other agents they'll work with

### 4. Setting Appropriate Expertise Levels

The expertise level you assign to your agent shapes how they approach tasks:

* **Novice agents**: Good for straightforward tasks, brainstorming, or initial drafts
* **Intermediate agents**: Suitable for most standard tasks with reliable execution
* **Expert agents**: Best for complex, specialized tasks requiring depth and nuance
* **World-class agents**: Reserved for critical tasks where exceptional quality is needed

Choose the appropriate expertise level based on task complexity and quality requirements. For most collaborative crews, a mix of expertise levels often works best, with higher expertise assigned to core specialized functions.

## Practical Examples: Before and After

Let's look at some examples of agent definitions before and after applying these best practices:

### Example 1: Content Creation Agent

### Example 2: Research Agent

## Crafting Effective Tasks for Your Agents

While agent design is important, task design is critical for successful execution. Here are best practices for designing tasks that set your agents up for success:

### The Anatomy of an Effective Task

A well-designed task has two key components that serve different purposes:

#### Task Description: The Process

The description should focus on what to do and how to do it, including:

* Detailed instructions for execution
* Context and background information
* Scope and constraints
* Process steps to follow

#### Expected Output: The Deliverable

The expected output should define what the final result should look like:

* Format specifications (markdown, JSON, etc.)
* Structure requirements
* Quality criteria
* Examples of good outputs (when possible)

### Task Design Best Practices

#### 1. Single Purpose, Single Output

Tasks perform best when focused on one clear objective:

**Bad Example (Too Broad):**

**Good Example (Focused):**

```yaml  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
#### Goal: The Agent's Purpose and Motivation

The goal directs the agent's efforts and shapes their decision-making process. Effective goals should:

* **Be clear and outcome-focused**: Define what the agent is trying to achieve
* **Emphasize quality standards**: Include expectations about the quality of work
* **Incorporate success criteria**: Help the agent understand what "good" looks like

**Examples of effective goals:**
```

Example 2 (unknown):
```unknown
#### Backstory: The Agent's Experience and Perspective

The backstory gives depth to the agent, influencing how they approach problems and interact with others. Good backstories:

* **Establish expertise and experience**: Explain how the agent gained their skills
* **Define working style and values**: Describe how the agent approaches their work
* **Create a cohesive persona**: Ensure all elements of the backstory align with the role and goal

**Examples of effective backstories:**
```

Example 3 (unknown):
```unknown
### 2. Specialists Over Generalists

Agents perform significantly better when given specialized roles rather than general ones. A highly focused agent delivers more precise, relevant outputs:

**Generic (Less Effective):**
```

Example 4 (unknown):
```unknown
**Specialized (More Effective):**
```

---

## Create agents

**URL:** llms-txt#create-agents

researcher = Agent(
    role='Research Analyst',
    goal='Conduct detailed market research',
    backstory='Expert market analyst with attention to detail',
    llm=llm,
    verbose=True
)

writer = Agent(
    role='Content Writer', 
    goal='Create comprehensive reports',
    backstory='Experienced technical writer',
    llm=llm,
    verbose=True
)

---

## Create agents and tasks as normal

**URL:** llms-txt#create-agents-and-tasks-as-normal

researcher = Agent(
    role="Research Specialist",
    goal="Find information on quantum computing",
    backstory="You are a quantum physics expert",
    verbose=True
)

research_task = Task(
    description="Research quantum computing applications",
    expected_output="A summary of practical applications",
    agent=researcher
)

---

## Create agents for different stages

**URL:** llms-txt#create-agents-for-different-stages

researcher = Agent(
    role='AWS Service Researcher',
    goal='Gather information about AWS services',
    backstory='I am specialized in finding detailed AWS service information.',
    tools=[initial_tool]
)

analyst = Agent(
    role='Service Compatibility Analyst',
    goal='Analyze service compatibility and requirements',
    backstory='I analyze AWS services for compatibility and integration possibilities.',
    tools=[followup_tool]
)

summarizer = Agent(
    role='Technical Documentation Writer',
    goal='Create clear technical summaries',
    backstory='I specialize in creating clear, concise technical documentation.',
    tools=[final_tool]
)

---

## Create and execute a task with custom parameters

**URL:** llms-txt#create-and-execute-a-task-with-custom-parameters

**Contents:**
  - Multi-Stage Automation Workflow

research_task = Task(
    description="Conduct market research on AI tools market for 2024 in North America with detailed format",
    agent=research_agent,
    expected_output="Comprehensive market research report"
)

crew = Crew(
    agents=[research_agent],
    tasks=[research_task]
)

result = crew.kickoff()
python {2, 4-35} theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import InvokeCrewAIAutomationTool

**Examples:**

Example 1 (unknown):
```unknown
### Multi-Stage Automation Workflow
```

---

## Create and execute crew

**URL:** llms-txt#create-and-execute-crew

**Contents:**
  - Observability and Governance
- Tracing

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

result = crew.kickoff()
bash  theme={null}
pip install traceloop-sdk
python  theme={null}
from traceloop.sdk import Traceloop

**Examples:**

Example 1 (unknown):
```unknown
### Observability and Governance

Monitor your CrewAI agents through TrueFoundry's metrics tab:
<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=33755ff848cb457e162e806c20c98216" alt="TrueFoundry metrics" data-og-width="3840" width="3840" data-og-height="1984" height="1984" data-path="images/gateway-metrics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=49a01b5e5bcc0429efd529860c020c10 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=3f47f171146339690e3516a892020626 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=857541d282cce3557f796ade097be01c 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=2f2b883b00e823ceb25ae1b747c656a4 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=9ddee789557bdbaacec42fd405180458 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=e9097f84b482e5c4da153d2d0271e6bf 2500w" />

With Truefoundry's AI gateway, you can monitor and analyze:

* **Performance Metrics**: Track key latency metrics like Request Latency, Time to First Token (TTFS), and Inter-Token Latency (ITL) with P99, P90, and P50 percentiles
* **Cost and Token Usage**: Gain visibility into your application's costs with detailed breakdowns of input/output tokens and the associated expenses for each model
* **Usage Patterns**: Understand how your application is being used with detailed analytics on user activity, model distribution, and team-based usage
* **Rate limit and Load balancing**: You can set up rate limiting, load balancing and fallback for your models

## Tracing

For a more detailed understanding on tracing, please see [getting-started-tracing](https://docs.truefoundry.com/docs/tracing/tracing-getting-started).For tracing, you can add the Traceloop SDK:
For tracing, you can add the Traceloop SDK:
```

Example 2 (unknown):
```unknown

```

---

## Create and execute tasks

**URL:** llms-txt#create-and-execute-tasks

**Contents:**
- Required Methods
  - Constructor: `__init__()`
  - Abstract Method: `call()`
  - Optional Methods
- Common Patterns
  - Error Handling
  - Custom Authentication
  - Stop Words Support
- Function Calling
- Troubleshooting

task = Task(
    description="Research the latest developments in AI",
    expected_output="A comprehensive summary",
    agent=agent
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
python  theme={null}
def __init__(self, model: str, api_key: str, temperature: Optional[float] = None):
    # REQUIRED: Call parent constructor with model and temperature
    super().__init__(model=model, temperature=temperature)
    
    # Your custom initialization
    self.api_key = api_key
python  theme={null}
def supports_function_calling(self) -> bool:
    """Return True if your LLM supports function calling."""
    return True  # Default is True

def supports_stop_words(self) -> bool:
    """Return True if your LLM supports stop sequences."""
    return True  # Default is True

def get_context_window_size(self) -> int:
    """Return the context window size."""
    return 4096  # Default is 4096
python  theme={null}
import requests

def call(self, messages, tools=None, callbacks=None, available_functions=None):
    try:
        response = requests.post(
            self.endpoint,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
        
    except requests.Timeout:
        raise TimeoutError("LLM request timed out")
    except requests.RequestException as e:
        raise RuntimeError(f"LLM request failed: {str(e)}")
    except (KeyError, IndexError) as e:
        raise ValueError(f"Invalid response format: {str(e)}")
python  theme={null}
from crewai import BaseLLM
from typing import Optional

class CustomAuthLLM(BaseLLM):
    def __init__(self, model: str, auth_token: str, endpoint: str, temperature: Optional[float] = None):
        super().__init__(model=model, temperature=temperature)
        self.auth_token = auth_token
        self.endpoint = endpoint
    
    def call(self, messages, tools=None, callbacks=None, available_functions=None):
        headers = {
            "Authorization": f"Custom {self.auth_token}",  # Custom auth format
            "Content-Type": "application/json"
        }
        # Rest of implementation...
python  theme={null}
def call(self, messages, tools=None, callbacks=None, available_functions=None):
    payload = {
        "model": self.model,
        "messages": messages,
        "stop": self.stop  # Include stop words in API call
    }
    # Make API call...

def supports_stop_words(self) -> bool:
    return True  # Your LLM supports stop sequences
python  theme={null}
def call(self, messages, tools=None, callbacks=None, available_functions=None):
    response = self._make_api_call(messages, tools)
    content = response["choices"][0]["message"]["content"]
    
    # Manually truncate at stop words
    if self.stop:
        for stop_word in self.stop:
            if stop_word in content:
                content = content.split(stop_word)[0]
                break
    
    return content

def supports_stop_words(self) -> bool:
    return False  # Tell CrewAI we handle stop words manually
python  theme={null}
import json

def call(self, messages, tools=None, callbacks=None, available_functions=None):
    # Convert string to message format
    if isinstance(messages, str):
        messages = [{"role": "user", "content": messages}]
    
    # Make API call
    response = self._make_api_call(messages, tools)
    message = response["choices"][0]["message"]
    
    # Check for function calls
    if "tool_calls" in message and available_functions:
        return self._handle_function_calls(
            message["tool_calls"], messages, tools, available_functions
        )
    
    return message["content"]

def _handle_function_calls(self, tool_calls, messages, tools, available_functions):
    """Handle function calling with proper message flow."""
    for tool_call in tool_calls:
        function_name = tool_call["function"]["name"]
        
        if function_name in available_functions:
            # Parse and execute function
            function_args = json.loads(tool_call["function"]["arguments"])
            function_result = available_functions[function_name](**function_args)
            
            # Add function call and result to message history
            messages.append({
                "role": "assistant",
                "content": None,
                "tool_calls": [tool_call]
            })
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "name": function_name,
                "content": str(function_result)
            })
            
            # Call LLM again with updated context
            return self.call(messages, tools, None, available_functions)
    
    return "Function call failed"
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## Required Methods

### Constructor: `__init__()`

**Critical**: You must call `super().__init__(model, temperature)` with the required parameters:
```

Example 2 (unknown):
```unknown
### Abstract Method: `call()`

The `call()` method is the heart of your LLM implementation. It must:

* Accept messages (string or list of dicts with 'role' and 'content')
* Return a string response
* Handle tools and function calling if supported
* Raise appropriate exceptions for errors

### Optional Methods
```

Example 3 (unknown):
```unknown
## Common Patterns

### Error Handling
```

Example 4 (unknown):
```unknown
### Custom Authentication
```

---

## Create and run crew

**URL:** llms-txt#create-and-run-crew

**Contents:**
- MCP Reference Formats
  - String-Based References
  - Structured Configurations
  - Mixed References
  - Tool Filtering

crew = Crew(agents=[research_agent], tasks=[research_task])
result = crew.kickoff()
python  theme={null}
mcps=[
    # Full server - get all available tools
    "https://mcp.example.com/api",

# Specific tool from server using # syntax
    "https://api.weather.com/mcp#get_current_weather",

# Server with authentication parameters
    "https://mcp.exa.ai/mcp?api_key=your_key&profile=your_profile"
]
python  theme={null}
mcps=[
    # Full AMP MCP service - get all available tools
    "crewai-amp:financial-data",

# Specific tool from AMP service using # syntax
    "crewai-amp:research-tools#pubmed_search",

# Multiple AMP services
    "crewai-amp:weather-service",
    "crewai-amp:market-analysis"
]
python  theme={null}
from crewai.mcp import MCPServerStdio
from crewai.mcp.filters import create_static_tool_filter

mcps=[
    MCPServerStdio(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem"],
        env={"API_KEY": "your_key"},
        tool_filter=create_static_tool_filter(
            allowed_tool_names=["read_file", "write_file"]
        ),
        cache_tools_list=True,
    ),
    # Python-based server
    MCPServerStdio(
        command="python",
        args=["path/to/server.py"],
        env={"UV_PYTHON": "3.12", "API_KEY": "your_key"},
    ),
]
python  theme={null}
from crewai.mcp import MCPServerHTTP

mcps=[
    # Streamable HTTP (default)
    MCPServerHTTP(
        url="https://api.example.com/mcp",
        headers={"Authorization": "Bearer your_token"},
        streamable=True,
        cache_tools_list=True,
    ),
    # Standard HTTP
    MCPServerHTTP(
        url="https://api.example.com/mcp",
        headers={"Authorization": "Bearer your_token"},
        streamable=False,
    ),
]
python  theme={null}
from crewai.mcp import MCPServerSSE

mcps=[
    MCPServerSSE(
        url="https://stream.example.com/mcp/sse",
        headers={"Authorization": "Bearer your_token"},
        cache_tools_list=True,
    ),
]
python  theme={null}
from crewai.mcp import MCPServerStdio, MCPServerHTTP

mcps=[
    # String references
    "https://external-api.com/mcp",              # External server
    "crewai-amp:financial-insights",             # AMP service

# Structured configurations
    MCPServerStdio(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem"],
    ),
    MCPServerHTTP(
        url="https://api.example.com/mcp",
        headers={"Authorization": "Bearer token"},
    ),
]
python  theme={null}
from crewai.mcp import MCPServerStdio
from crewai.mcp.filters import create_static_tool_filter, create_dynamic_tool_filter, ToolFilterContext

**Examples:**

Example 1 (unknown):
```unknown
That's it! The MCP tools are automatically discovered and available to your agent.

## MCP Reference Formats

The `mcps` field supports both **string references** (for quick setup) and **structured configurations** (for full control). You can mix both formats in the same list.

### String-Based References

#### External MCP Servers
```

Example 2 (unknown):
```unknown
#### CrewAI AOP Marketplace
```

Example 3 (unknown):
```unknown
### Structured Configurations

#### Stdio Transport (Local Servers)

Perfect for local MCP servers that run as processes:
```

Example 4 (unknown):
```unknown
#### HTTP/Streamable HTTP Transport (Remote Servers)

For remote MCP servers over HTTP/HTTPS:
```

---

## Create and run the crew

**URL:** llms-txt#create-and-run-the-crew

**Contents:**
- Parameters
- Usage

crew = Crew(agents=[browser_agent], tasks=[browse_task])
result = crew.kickoff()
python Code theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## Parameters

The `MultiOnTool` accepts the following parameters during initialization:

* **api\_key**: Optional. Specifies the MultiOn API key. If not provided, it will look for the `MULTION_API_KEY` environment variable.
* **local**: Optional. Set to `True` to run the agent locally on your browser. Make sure the MultiOn browser extension is installed and API Enabled is checked. Default is `False`.
* **max\_steps**: Optional. Sets the maximum number of steps the MultiOn agent can take for a command. Default is `3`.

## Usage

When using the `MultiOnTool`, the agent will provide natural language instructions that the tool translates into web browsing actions. The tool returns the results of the browsing session along with a status.
```

---

## Create and run the flow with tracing enabled

**URL:** llms-txt#create-and-run-the-flow-with-tracing-enabled

**Contents:**
  - Step 5: View Traces in the CrewAI AOP Dashboard
  - Alternative: Environment Variable Configuration
- Viewing Your Traces
  - Access the CrewAI AOP Dashboard
  - What You'll See in Traces
  - Trace Features
  - Authentication Issues
  - Traces Not Appearing

flow = ExampleFlow(tracing=True)
result = flow.kickoff()
bash  theme={null}
export CREWAI_TRACING_ENABLED=true
env  theme={null}
CREWAI_TRACING_ENABLED=true
```

When this environment variable is set, all Crews and Flows will automatically have tracing enabled, even without explicitly setting `tracing=True`.

## Viewing Your Traces

### Access the CrewAI AOP Dashboard

1. Visit [app.crewai.com](https://app.crewai.com) and log in to your account
2. Navigate to your project dashboard
3. Click on the **Traces** tab to view execution details

### What You'll See in Traces

CrewAI tracing provides comprehensive visibility into:

* **Agent Decisions**: See how agents reason through tasks and make decisions
* **Task Execution Timeline**: Visual representation of task sequences and dependencies
* **Tool Usage**: Monitor which tools are called and their results
* **LLM Calls**: Track all language model interactions, including prompts and responses
* **Performance Metrics**: Execution times, token usage, and costs
* **Error Tracking**: Detailed error information and stack traces

* **Execution Timeline**: Click through different stages of execution
* **Detailed Logs**: Access comprehensive logs for debugging
* **Performance Analytics**: Analyze execution patterns and optimize performance
* **Export Capabilities**: Download traces for further analysis

### Authentication Issues

If you encounter authentication problems:

1. Ensure you're logged in: `crewai login`
2. Check your internet connection
3. Verify your account at [app.crewai.com](https://app.crewai.com)

### Traces Not Appearing

If traces aren't showing up in the dashboard:

1. Confirm `tracing=True` is set in your Crew/Flow
2. Check that `CREWAI_TRACING_ENABLED=true` if using environment variables
3. Ensure you're authenticated with `crewai login`
4. Verify your crew/flow is actually executing

**Examples:**

Example 1 (unknown):
```unknown
### Step 5: View Traces in the CrewAI AOP Dashboard

After running the crew or flow, you can view the traces generated by your CrewAI application in the CrewAI AOP dashboard. You should see detailed steps of the agent interactions, tool usages, and LLM calls.
Just click on the link below to view the traces or head over to the traces tab in the dashboard [here](https://app.crewai.com/crewai_plus/trace_batches)
<img src="https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=72981ddafcda030270c059f08b98db03" alt="CrewAI Tracing Interface" data-og-width="3272" width="3272" data-og-height="162" height="162" data-path="images/view-traces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=280&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=ccd01161e9258840e74ef1c451f84269 280w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=560&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=d8feaccbddc300723769a977ca3e0ff9 560w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=840&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=2b404956f27d32dd38b0a5d4bf48ab58 840w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=1100&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=8bc1f5f99f4289ee1dd7ebe2e60bb189 1100w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=1650&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=1ab7e96c4017cf1cbab719c695884969 1650w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=2500&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=3ab9ea0309e81741969db86307657b90 2500w" />

### Alternative: Environment Variable Configuration

You can also enable tracing globally by setting an environment variable:
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

---

## Create an agent with the knowledge store

**URL:** llms-txt#create-an-agent-with-the-knowledge-store

**Contents:**
- Supported Knowledge Sources
  - Text File Knowledge Source
  - PDF Knowledge Source
  - CSV Knowledge Source
  - Excel Knowledge Source
  - JSON Knowledge Source
- Agent vs Crew Knowledge: Complete Guide
  - How Knowledge Initialization Actually Works

agent = Agent(
    role="About papers",
    goal="You know everything about the papers.",
    backstory="You are a master at understanding papers and their content.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Answer the following questions about the papers: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[content_source],
)

result = crew.kickoff(
    inputs={"question": "What is the reward hacking paper about? Be sure to provide sources."}
)
python  theme={null}
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

text_source = TextFileKnowledgeSource(
    file_paths=["document.txt", "another.txt"]
)
python  theme={null}
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

pdf_source = PDFKnowledgeSource(
    file_paths=["document.pdf", "another.pdf"]
)
python  theme={null}
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource

csv_source = CSVKnowledgeSource(
    file_paths=["data.csv"]
)
python  theme={null}
from crewai.knowledge.source.excel_knowledge_source import ExcelKnowledgeSource

excel_source = ExcelKnowledgeSource(
    file_paths=["spreadsheet.xlsx"]
)
python  theme={null}
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource

json_source = JSONKnowledgeSource(
    file_paths=["data.json"]
)
python  theme={null}
from crewai import Agent, Task, Crew
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

**Examples:**

Example 1 (unknown):
```unknown
## Supported Knowledge Sources

CrewAI supports various types of knowledge sources out of the box:

<CardGroup cols={2}>
  <Card title="Text Sources" icon="text">
    * Raw strings
    * Text files (.txt)
    * PDF documents
  </Card>

  <Card title="Structured Data" icon="table">
    * CSV files
    * Excel spreadsheets
    * JSON documents
  </Card>
</CardGroup>

### Text File Knowledge Source
```

Example 2 (unknown):
```unknown
### PDF Knowledge Source
```

Example 3 (unknown):
```unknown
### CSV Knowledge Source
```

Example 4 (unknown):
```unknown
### Excel Knowledge Source
```

---

## Create a CrewAI agent that uses the tool

**URL:** llms-txt#create-a-crewai-agent-that-uses-the-tool

automation_coordinator = Agent(
    role='Automation Coordinator',
    goal='Coordinate and execute automated crew tasks',
    backstory='I am an expert at leveraging automation tools to execute complex workflows.',
    tools=[automation_tool],
    verbose=True
)

---

## Create a crew and add the task

**URL:** llms-txt#create-a-crew-and-add-the-task

analysis_crew = Crew(
    agents=[coding_agent],
    tasks=[data_analysis_task],
    verbose=True,
    memory=False
)

datasets = [
  { "ages": [25, 30, 35, 40, 45] },
  { "ages": [20, 25, 30, 35, 40] },
  { "ages": [30, 35, 40, 45, 50] }
]

---

## Create a crew and run the task

**URL:** llms-txt#create-a-crew-and-run-the-task

**Contents:**
- Error Handling

crew = Crew(agents=[analyst], tasks=[analysis_task])
result = crew.kickoff()

print(result)
python  theme={null}
from crewai import Agent, Task
import logging

**Examples:**

Example 1 (unknown):
```unknown
## Error Handling

The reasoning process is designed to be robust, with error handling built in. If an error occurs during reasoning, the agent will proceed with executing the task without the reasoning plan. This ensures that tasks can still be executed even if the reasoning process fails.

Here's how to handle potential errors in your code:
```

---

## Create a Crew for the task

**URL:** llms-txt#create-a-crew-for-the-task

llama_crew = Crew(
    agents=[principal_engineer],
    tasks=[engineering_task],
    process=Process.sequential,
    verbose=True
)

---

## Create a crew with sequential processing

**URL:** llms-txt#create-a-crew-with-sequential-processing

**Contents:**
- Use Cases
  - Distributed Crew Orchestration
  - Cross-Platform Integration
  - Enterprise Automation Pipelines
  - Dynamic Workflow Composition
  - Specialized Domain Processing
- Custom Input Schema
- Error Handling
- API Endpoints
- Notes

crew = Crew(
    agents=[data_collector, data_analyst, report_generator],
    tasks=[collection_task, analysis_task, reporting_task],
    process=Process.sequential,
    verbose=2
)

result = crew.kickoff()
python  theme={null}
from pydantic import Field

crew_inputs = {
    "required_param": Field(..., description="This parameter is required"),
    "optional_param": Field(default="default_value", description="This parameter is optional"),
    "typed_param": Field(..., description="Integer parameter", ge=1, le=100)  # With validation
}
```

The tool provides comprehensive error handling for common scenarios:

* **API Connection Errors**: Network connectivity issues with CrewAI Platform
* **Authentication Errors**: Invalid or expired bearer tokens
* **Timeout Errors**: Tasks that exceed the maximum polling time
* **Task Failures**: Crew automations that fail during execution
* **Input Validation Errors**: Invalid parameters passed to automation endpoints

The tool interacts with two main API endpoints:

* `POST {crew_api_url}/kickoff`: Starts a new crew automation task
* `GET {crew_api_url}/status/{crew_id}`: Checks the status of a running task

* The tool automatically polls the status endpoint every second until completion or timeout
* Successful tasks return the result directly, while failed tasks return error information
* Bearer tokens should be kept secure and not hardcoded in production environments
* Consider using environment variables for sensitive configuration like bearer tokens
* Custom input schemas must be compatible with the target crew automation's expected parameters

**Examples:**

Example 1 (unknown):
```unknown
## Use Cases

### Distributed Crew Orchestration

* Coordinate multiple specialized crew automations to handle complex, multi-stage workflows
* Enable seamless handoffs between different automation services for comprehensive task execution
* Scale processing by distributing workloads across multiple CrewAI Platform automations

### Cross-Platform Integration

* Bridge CrewAI agents with CrewAI Platform automations for hybrid local-cloud workflows
* Leverage specialized automations while maintaining local control and orchestration
* Enable secure collaboration between local agents and cloud-based automation services

### Enterprise Automation Pipelines

* Create enterprise-grade automation pipelines that combine local intelligence with cloud processing power
* Implement complex business workflows that span multiple automation services
* Enable scalable, repeatable processes for data analysis, reporting, and decision-making

### Dynamic Workflow Composition

* Dynamically compose workflows by chaining different automation services based on task requirements
* Enable adaptive processing where the choice of automation depends on data characteristics or business rules
* Create flexible, reusable automation components that can be combined in various ways

### Specialized Domain Processing

* Access domain-specific automations (financial analysis, legal research, technical documentation) from general-purpose agents
* Leverage pre-built, specialized crew automations without rebuilding complex domain logic
* Enable agents to access expert-level capabilities through targeted automation services

## Custom Input Schema

When defining `crew_inputs`, use Pydantic Field objects to specify the input parameters:
```

---

## Create a crew with the agents and tasks

**URL:** llms-txt#create-a-crew-with-the-agents-and-tasks

crew = Crew(
    agents=[researcher, analyst, summarizer],
    tasks=[research_task, analysis_task, summary_task],
    process=Process.sequential,
    verbose=2
)

---

## Create a crew with the agent

**URL:** llms-txt#create-a-crew-with-the-agent

crew = Crew(
    agents=[automation_coordinator],
    tasks=[analysis_task],
    verbose=2
)

---

## Create a crew with the tasks

**URL:** llms-txt#create-a-crew-with-the-tasks

crew = Crew(
    agents=[data_fetcher_agent, data_processor_agent, summary_generator_agent],
    tasks=[task1, conditional_task, task3],
    verbose=True,
    planning=True
)

---

## Create a crew with your custom prompt file

**URL:** llms-txt#create-a-crew-with-your-custom-prompt-file

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    prompt_file="path/to/custom_prompts.json",
    verbose=True
)

---

## Create collaborative agents

**URL:** llms-txt#create-collaborative-agents

researcher = Agent(
    role="Research Specialist",
    goal="Find accurate, up-to-date information on any topic",
    backstory="""You're a meticulous researcher with expertise in finding 
    reliable sources and fact-checking information across various domains.""",
    allow_delegation=True,
    verbose=True
)

writer = Agent(
    role="Content Writer",
    goal="Create engaging, well-structured content",
    backstory="""You're a skilled content writer who excels at transforming 
    research into compelling, readable content for different audiences.""",
    allow_delegation=True,
    verbose=True
)

editor = Agent(
    role="Content Editor",
    goal="Ensure content quality and consistency",
    backstory="""You're an experienced editor with an eye for detail, 
    ensuring content meets high standards for clarity and accuracy.""",
    allow_delegation=True,
    verbose=True
)

---

## Create collaborative crew

**URL:** llms-txt#create-collaborative-crew

**Contents:**
- Collaboration Patterns
  - Pattern 1: Research → Write → Edit
  - Pattern 2: Collaborative Single Task
- Hierarchical Collaboration

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[article_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()
python  theme={null}
research_task = Task(
    description="Research the latest developments in quantum computing",
    expected_output="Comprehensive research summary with key findings and sources",
    agent=researcher
)

writing_task = Task(
    description="Write an article based on the research findings",
    expected_output="Engaging 800-word article about quantum computing",
    agent=writer,
    context=[research_task]  # Gets research output as context
)

editing_task = Task(
    description="Edit and polish the article for publication",
    expected_output="Publication-ready article with improved clarity and flow",
    agent=editor,
    context=[writing_task]  # Gets article draft as context
)
python  theme={null}
collaborative_task = Task(
    description="""Create a marketing strategy for a new AI product.
    
    Writer: Focus on messaging and content strategy
    Researcher: Provide market analysis and competitor insights
    
    Work together to create a comprehensive strategy.""",
    expected_output="Complete marketing strategy with research backing",
    agent=writer  # Lead agent, but can delegate to researcher
)
python  theme={null}
from crewai import Agent, Crew, Task, Process

**Examples:**

Example 1 (unknown):
```unknown
## Collaboration Patterns

### Pattern 1: Research → Write → Edit
```

Example 2 (unknown):
```unknown
### Pattern 2: Collaborative Single Task
```

Example 3 (unknown):
```unknown
## Hierarchical Collaboration

For complex projects, use a hierarchical process with a manager agent:
```

---

## Create components - fingerprints are automatically generated

**URL:** llms-txt#create-components---fingerprints-are-automatically-generated

agent = Agent(
    role="Data Scientist",
    goal="Analyze data",
    backstory="Expert in data analysis"
)

crew = Crew(
    agents=[agent],
    tasks=[]
)

task = Task(
    description="Analyze customer data",
    expected_output="Insights from data analysis",
    agent=agent
)

---

## Create CrewAI agents

**URL:** llms-txt#create-crewai-agents

search_agent = Agent(
    role="Senior Semantic Search Agent",
    goal="Find and analyze documents based on semantic search",
    backstory="""You are an expert research assistant who can find relevant
    information using semantic search in a Qdrant database.""",
    tools=[qdrant_tool],
    verbose=True
)

answer_agent = Agent(
    role="Senior Answer Assistant",
    goal="Generate answers to questions based on the context provided",
    backstory="""You are an expert answer assistant who can generate
    answers to questions based on the context provided.""",
    tools=[qdrant_tool],
    verbose=True
)

---

## Create sequential tasks

**URL:** llms-txt#create-sequential-tasks

collection_task = Task(
    description="Collect market data for Q4 2024 analysis",
    agent=data_collector
)

analysis_task = Task(
    description="Analyze collected data to identify trends and patterns",
    agent=data_analyst
)

reporting_task = Task(
    description="Generate executive summary report with key insights and recommendations",
    agent=report_generator
)

---

## Create specialized agents

**URL:** llms-txt#create-specialized-agents

data_collector = Agent(
    role='Data Collection Specialist',
    goal='Gather and preprocess data from various sources',
    backstory='I specialize in collecting and cleaning data from multiple sources.',
    tools=[data_collection_tool]
)

data_analyst = Agent(
    role='Data Analysis Expert',
    goal='Perform advanced analysis on collected data',
    backstory='I am an expert in statistical analysis and machine learning.',
    tools=[analysis_tool]
)

report_generator = Agent(
    role='Report Generation Specialist',
    goal='Create comprehensive reports and visualizations',
    backstory='I excel at creating clear, actionable reports from complex data.',
    tools=[reporting_tool]
)

---

## Create tasks

**URL:** llms-txt#create-tasks

research_task = Task(
    description="Find all available AWS services in us-west-2 region.",
    agent=researcher
)

analysis_task = Task(
    description="Analyze which services support IPv6 and their implementation requirements.",
    agent=analyst
)

summary_task = Task(
    description="Create a summary of IPv6-compatible services and their key features.",
    agent=summarizer
)

---

## Create tasks for your agents

**URL:** llms-txt#create-tasks-for-your-agents

research_task = Task(
    description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
    Identify key trends, breakthrough technologies, and potential industry impacts.""",
    expected_output="Full analysis report in bullet points",
    agent=researcher,
)

writing_task = Task(
    description="""Using the insights provided, develop an engaging blog
    post that highlights the most significant AI advancements.
    Your post should be informative yet accessible, catering to a tech-savvy audience.""",
    expected_output="Full blog post of at least 4 paragraphs",
    agent=writer,
)

---

## Create tasks that require code execution

**URL:** llms-txt#create-tasks-that-require-code-execution

task_1 = Task(
    description="Analyze the first dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent,
    expected_output="The average age of the participants."
)

task_2 = Task(
    description="Analyze the second dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent,
    expected_output="The average age of the participants."
)

---

## Create the crew

**URL:** llms-txt#create-the-crew

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

---

## Create two crews and add tasks

**URL:** llms-txt#create-two-crews-and-add-tasks

crew_1 = Crew(agents=[coding_agent], tasks=[task_1])
crew_2 = Crew(agents=[coding_agent], tasks=[task_2])

---

## Creating a CrewAI Project

**URL:** llms-txt#creating-a-crewai-project

**Contents:**
- Enterprise Installation Options
- Next Steps

We recommend using the `YAML` template scaffolding for a structured approach to defining agents and tasks. Here's how to get started:

<Steps>
  <Step title="Generate Project Scaffolding">
    * Run the `crewai` CLI command:

* This creates a new project with the following structure:
      
  </Step>

<Step title="Customize Your Project">
    * Your project will contain these essential files:
      | File          | Purpose                                  |
      | ------------- | ---------------------------------------- |
      | `agents.yaml` | Define your AI agents and their roles    |
      | `tasks.yaml`  | Set up agent tasks and workflows         |
      | `.env`        | Store API keys and environment variables |
      | `main.py`     | Project entry point and execution flow   |
      | `crew.py`     | Crew orchestration and coordination      |
      | `tools/`      | Directory for custom agent tools         |
      | `knowledge/`  | Directory for knowledge base             |

* Start by editing `agents.yaml` and `tasks.yaml` to define your crew's behavior.

* Keep sensitive information like API keys in `.env`.
  </Step>

<Step title="Run your Crew">
    * Before you run your crew, make sure to run:
      
    * If you need to install additional packages, use:
      
    * To run your crew, execute the following command in the root of your project:
      
  </Step>
</Steps>

## Enterprise Installation Options

<Note type="info">
  For teams and organizations, CrewAI offers enterprise deployment options that eliminate setup complexity:

### CrewAI AOP (SaaS)

* Zero installation required - just sign up for free at [app.crewai.com](https://app.crewai.com)
  * Automatic updates and maintenance
  * Managed infrastructure and scaling
  * Build Crews with no Code

### CrewAI Factory (Self-hosted)

* Containerized deployment for your infrastructure
  * Supports any hyperscaler including on prem deployments
  * Integration with your existing security systems

<Card title="Explore Enterprise Options" icon="building" href="https://crewai.com/enterprise">
    Learn about CrewAI's enterprise offerings and schedule a demo
  </Card>
</Note>

<CardGroup cols={2}>
  <Card title="Build Your First Agent" icon="code" href="/en/quickstart">
    Follow our quickstart guide to create your first CrewAI agent and get hands-on experience.
  </Card>

<Card title="Join the Community" icon="comments" href="https://community.crewai.com">
    Connect with other developers, get help, and share your CrewAI experiences.
  </Card>
</CardGroup>

**Examples:**

Example 1 (unknown):
```unknown
* This creates a new project with the following structure:
```

Example 2 (unknown):
```unknown
</Step>

  <Step title="Customize Your Project">
    * Your project will contain these essential files:
      | File          | Purpose                                  |
      | ------------- | ---------------------------------------- |
      | `agents.yaml` | Define your AI agents and their roles    |
      | `tasks.yaml`  | Set up agent tasks and workflows         |
      | `.env`        | Store API keys and environment variables |
      | `main.py`     | Project entry point and execution flow   |
      | `crew.py`     | Crew orchestration and coordination      |
      | `tools/`      | Directory for custom agent tools         |
      | `knowledge/`  | Directory for knowledge base             |

    * Start by editing `agents.yaml` and `tasks.yaml` to define your crew's behavior.

    * Keep sensitive information like API keys in `.env`.
  </Step>

  <Step title="Run your Crew">
    * Before you run your crew, make sure to run:
```

Example 3 (unknown):
```unknown
* If you need to install additional packages, use:
```

Example 4 (unknown):
```unknown
* To run your crew, execute the following command in the root of your project:
```

---

## CrewAI AOP

**URL:** llms-txt#crewai-aop

**Contents:**
- Introduction
- Key Features
- Deployment Options
- Getting Started

Source: https://docs.crewai.com/en/enterprise/introduction

Deploy, monitor, and scale your AI agent workflows

CrewAI AOP(Agent Operations Platform) provides a platform for deploying, monitoring, and scaling your crews and agents in a production environment.

<Frame>
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f3c686c946a4843a9093f21c0d1a420f" alt="CrewAI AOP Dashboard" data-og-width="3648" width="3648" data-og-height="2248" height="2248" data-path="images/enterprise/crewai-enterprise-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a58dd6da8e1de0056bc26152476114c9 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3cbeb2e4972fe106a8fdf256539c965a 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c81d9773136e4d33a8853457690bc14d 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=d5a21be80d159c6041ebfeb51f948b5e 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=326a6f4e11c1091dca20d98384eeb0ad 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crewai-enterprise-dashboard.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=2d799c4a99363505252df6a3553fc248 2500w" />
</Frame>

CrewAI AOP extends the power of the open-source framework with features designed for production deployments, collaboration, and scalability. Deploy your crews to a managed infrastructure and monitor their execution in real-time.

<CardGroup cols={2}>
  <Card title="Crew Deployments" icon="rocket">
    Deploy your crews to a managed infrastructure with a few clicks
  </Card>

<Card title="API Access" icon="code">
    Access your deployed crews via REST API for integration with existing systems
  </Card>

<Card title="Observability" icon="chart-line">
    Monitor your crews with detailed execution traces and logs
  </Card>

<Card title="Tool Repository" icon="toolbox">
    Publish and install tools to enhance your crews' capabilities
  </Card>

<Card title="Webhook Streaming" icon="webhook">
    Stream real-time events and updates to your systems
  </Card>

<Card title="Crew Studio" icon="paintbrush">
    Create and customize crews using a no-code/low-code interface
  </Card>
</CardGroup>

## Deployment Options

<CardGroup cols={3}>
  <Card title="GitHub Integration" icon="github">
    Connect directly to your GitHub repositories to deploy code
  </Card>

<Card title="Crew Studio" icon="palette">
    Deploy crews created through the no-code Crew Studio interface
  </Card>

<Card title="CLI Deployment" icon="terminal">
    Use the CrewAI CLI for more advanced deployment workflows
  </Card>
</CardGroup>

<Steps>
  <Step title="Sign up for an account">
    Create your account at [app.crewai.com](https://app.crewai.com)

<Card title="Sign Up" icon="user" href="https://app.crewai.com/signup">
      Sign Up
    </Card>
  </Step>

<Step title="Build your first crew">
    Use code or Crew Studio to build your crew

<Card title="Build Crew" icon="paintbrush" href="/en/enterprise/guides/build-crew">
      Build Crew
    </Card>
  </Step>

<Step title="Deploy your crew">
    Deploy your crew to the Enterprise platform

<Card title="Deploy Crew" icon="rocket" href="/en/enterprise/guides/deploy-crew">
      Deploy Crew
    </Card>
  </Step>

<Step title="Access your crew">
    Integrate with your crew via the generated API endpoints

<Card title="API Access" icon="code" href="/en/enterprise/guides/kickoff-crew">
      Use the Crew API
    </Card>
  </Step>
</Steps>

For detailed instructions, check out our [deployment guide](/en/enterprise/guides/deploy-crew) or click the button below to get started.

---

## CrewAI AOP API

**URL:** llms-txt#crewai-aop-api

**Contents:**
- Quick Start
- Authentication
  - Token Types
- Base URL
- Typical Workflow
- Error Handling
- Interactive Testing
  - **To Test Your Actual API:**
- Need Help?

Welcome to the CrewAI AOP API reference. This API allows you to programmatically interact with your deployed crews, enabling integration with your applications, workflows, and services.

<Steps>
  <Step title="Get Your API Credentials">
    Navigate to your crew's detail page in the CrewAI AOP dashboard and copy your Bearer Token from the Status tab.
  </Step>

<Step title="Discover Required Inputs">
    Use the `GET /inputs` endpoint to see what parameters your crew expects.
  </Step>

<Step title="Start a Crew Execution">
    Call `POST /kickoff` with your inputs to start the crew execution and receive a `kickoff_id`.
  </Step>

<Step title="Monitor Progress">
    Use `GET /status/{kickoff_id}` to check execution status and retrieve results.
  </Step>
</Steps>

All API requests require authentication using a Bearer token. Include your token in the `Authorization` header:

| Token Type            | Scope                     | Use Case                                                     |
| :-------------------- | :------------------------ | :----------------------------------------------------------- |
| **Bearer Token**      | Organization-level access | Full crew operations, ideal for server-to-server integration |
| **User Bearer Token** | User-scoped access        | Limited permissions, suitable for user-specific operations   |

<Tip>
  You can find both token types in the Status tab of your crew's detail page in the CrewAI AOP dashboard.
</Tip>

Each deployed crew has its own unique API endpoint:

Replace `your-crew-name` with your actual crew's URL from the dashboard.

1. **Discovery**: Call `GET /inputs` to understand what your crew needs
2. **Execution**: Submit inputs via `POST /kickoff` to start processing
3. **Monitoring**: Poll `GET /status/{kickoff_id}` until completion
4. **Results**: Extract the final output from the completed response

The API uses standard HTTP status codes:

| Code  | Meaning                                    |
| ----- | :----------------------------------------- |
| `200` | Success                                    |
| `400` | Bad Request - Invalid input format         |
| `401` | Unauthorized - Invalid bearer token        |
| `404` | Not Found - Resource doesn't exist         |
| `422` | Validation Error - Missing required inputs |
| `500` | Server Error - Contact support             |

## Interactive Testing

<Info>
  **Why no "Send" button?** Since each CrewAI AOP user has their own unique crew URL, we use **reference mode** instead of an interactive playground to avoid confusion. This shows you exactly what the requests should look like without non-functional send buttons.
</Info>

Each endpoint page shows you:

* ✅ **Exact request format** with all parameters
* ✅ **Response examples** for success and error cases
* ✅ **Code samples** in multiple languages (cURL, Python, JavaScript, etc.)
* ✅ **Authentication examples** with proper Bearer token format

### **To Test Your Actual API:**

<CardGroup cols={2}>
  <Card title="Copy cURL Examples" icon="terminal">
    Copy the cURL examples and replace the URL + token with your real values
  </Card>

<Card title="Use Postman/Insomnia" icon="play">
    Import the examples into your preferred API testing tool
  </Card>
</CardGroup>

**Example workflow:**

1. **Copy this cURL example** from any endpoint page
2. **Replace `your-actual-crew-name.crewai.com`** with your real crew URL
3. **Replace the Bearer token** with your real token from the dashboard
4. **Run the request** in your terminal or API client

<CardGroup cols={2}>
  <Card title="Enterprise Support" icon="headset" href="mailto:support@crewai.com">
    Get help with API integration and troubleshooting
  </Card>

<Card title="Enterprise Dashboard" icon="chart-line" href="https://app.crewai.com">
    Manage your crews and view execution logs
  </Card>
</CardGroup>

**Examples:**

Example 1 (unknown):
```unknown
### Token Types

| Token Type            | Scope                     | Use Case                                                     |
| :-------------------- | :------------------------ | :----------------------------------------------------------- |
| **Bearer Token**      | Organization-level access | Full crew operations, ideal for server-to-server integration |
| **User Bearer Token** | User-scoped access        | Limited permissions, suitable for user-specific operations   |

<Tip>
  You can find both token types in the Status tab of your crew's detail page in the CrewAI AOP dashboard.
</Tip>

## Base URL

Each deployed crew has its own unique API endpoint:
```

---

## CrewAI Built-in Tracing

**URL:** llms-txt#crewai-built-in-tracing

**Contents:**
- Prerequisites
- Setup Instructions
  - Step 1: Create Your CrewAI AOP Account
  - Step 2: Install CrewAI CLI and Authenticate
  - Step 3: Enable Tracing in Your Crew

CrewAI provides built-in tracing capabilities that allow you to monitor and debug your Crews and Flows in real-time. This guide demonstrates how to enable tracing for both **Crews** and **Flows** using CrewAI's integrated observability platform.

> **What is CrewAI Tracing?** CrewAI's built-in tracing provides comprehensive observability for your AI agents, including agent decisions, task execution timelines, tool usage, and LLM calls - all accessible through the [CrewAI AOP platform](https://app.crewai.com).

<img src="https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=b7e95a8f56ed3c459699acf641b4ae5a" alt="CrewAI Tracing Interface" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/crewai-tracing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=280&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=432b91fbee9d71f0c152a097c1b87773 280w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=560&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=62b6417d4f5289617124df196c0a9c94 560w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=840&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=fb115418f8fb1c0bb79e9ac647158996 840w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=1100&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=bb955f30c027461597f15dbe436fc068 1100w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=1650&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=d891852f83abfd576cc6b2c3eb83749c 1650w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=2500&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=67cbde03f418d19d66d4273df9427db2 2500w" />

Before you can use CrewAI tracing, you need:

1. **CrewAI AOP Account**: Sign up for a free account at [app.crewai.com](https://app.crewai.com)
2. **CLI Authentication**: Use the CrewAI CLI to authenticate your local environment

## Setup Instructions

### Step 1: Create Your CrewAI AOP Account

Visit [app.crewai.com](https://app.crewai.com) and create your free account. This will give you access to the CrewAI AOP platform where you can view traces, metrics, and manage your crews.

### Step 2: Install CrewAI CLI and Authenticate

If you haven't already, install CrewAI with the CLI tools:

Then authenticate your CLI with your CrewAI AOP account:

1. Open your browser to the authentication page
2. Prompt you to enter a device code
3. Authenticate your local environment with your CrewAI AOP account
4. Enable tracing capabilities for your local development

### Step 3: Enable Tracing in Your Crew

You can enable tracing for your Crew by setting the `tracing` parameter to `True`:

```python  theme={null}
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool

**Examples:**

Example 1 (unknown):
```unknown
## Setup Instructions

### Step 1: Create Your CrewAI AOP Account

Visit [app.crewai.com](https://app.crewai.com) and create your free account. This will give you access to the CrewAI AOP platform where you can view traces, metrics, and manage your crews.

### Step 2: Install CrewAI CLI and Authenticate

If you haven't already, install CrewAI with the CLI tools:
```

Example 2 (unknown):
```unknown
Then authenticate your CLI with your CrewAI AOP account:
```

Example 3 (unknown):
```unknown
This command will:

1. Open your browser to the authentication page
2. Prompt you to enter a device code
3. Authenticate your local environment with your CrewAI AOP account
4. Enable tracing capabilities for your local development

### Step 3: Enable Tracing in Your Crew

You can enable tracing for your Crew by setting the `tracing` parameter to `True`:
```

---

## CrewAI Cookbooks

**URL:** llms-txt#crewai-cookbooks

**Contents:**
- Quickstarts & Demos

Source: https://docs.crewai.com/en/examples/cookbooks

Feature-focused quickstarts and notebooks for learning patterns fast.

## Quickstarts & Demos

<CardGroup cols={3}>
  <Card title="Collaboration" icon="people-arrows" href="https://github.com/crewAIInc/crewAI-quickstarts/blob/main/Collaboration/crewai_collaboration.ipynb">
    Coordinate multiple agents on shared tasks. Includes notebook with end-to-end collaboration pattern.
  </Card>

<Card title="Planning" icon="timeline" href="https://github.com/crewAIInc/crewAI-quickstarts/blob/main/Planning/crewai_planning.ipynb">
    Teach agents to reason about multi-step plans before execution using the planning toolkit.
  </Card>

<Card title="Reasoning" icon="lightbulb" href="https://github.com/crewAIInc/crewAI-quickstarts/blob/main/Reasoning/crewai_reasoning.ipynb">
    Explore self-reflection loops, critique prompts, and structured thinking patterns.
  </Card>
</CardGroup>

<CardGroup cols={3}>
  <Card title="Structured Guardrails" icon="shield-check" href="https://github.com/crewAIInc/crewAI-quickstarts/blob/main/Guardrails/task_guardrails.ipynb">
    Apply task-level guardrails with retries, validation functions, and safe fallbacks.
  </Card>

<Card title="Gemini Search & Grounding" icon="magnifying-glass" href="https://github.com/crewAIInc/crewAI-quickstarts/blob/main/Custom%20LLM/gemini_search_grounding_crewai.ipynb">
    Connect CrewAI to Gemini with search grounding for factual, citation-rich outputs.
  </Card>

<Card title="Gemini Video Summaries" icon="video" href="https://github.com/crewAIInc/crewAI-quickstarts/blob/main/Custom%20LLM/summarize_video_gemini_crewai.ipynb">
    Generate video recaps using Gemini multimodal LLM and CrewAI orchestration.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Browse Quickstarts" icon="bolt" href="https://github.com/crewAIInc/crewAI-quickstarts">
    View all notebooks and feature demos showcasing specific CrewAI capabilities.
  </Card>

<Card title="Request a cookbook" icon="message-plus" href="https://community.crewai.com">
    Missing a pattern? Drop a request in the community forum and we’ll expand the library.
  </Card>
</CardGroup>

<Tip>
  Use Cookbooks to learn a pattern quickly, then jump to Full Examples for production‑grade implementations.
</Tip>

---

## CrewAI Documentation

**URL:** llms-txt#crewai-documentation

**Contents:**
- Get started
- Build the basics
- Enterprise journey
- What’s new
- Stay connected

Source: https://docs.crewai.com/index

Build collaborative AI agents, crews, and flows — production ready from day one.

<div
  style={{
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  gap: 20,
  textAlign: 'center',
  padding: '48px 24px',
  borderRadius: 16,
  background: 'linear-gradient(180deg, rgba(235,102,88,0.12) 0%, rgba(201,76,60,0.08) 100%)',
  border: '1px solid rgba(235,102,88,0.18)'
}}
>
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f" alt="CrewAI" width="250" height="100" data-og-width="375" data-og-height="114" data-path="images/crew_only_logo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ea0aa43c49a743b0e50cdc8e453f9150 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3025604ad4e1a40cda55cbb4ec726f14 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=26b82b135ed2768dbb95a4f0ba4cd871 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=77d06e853a60d4a862cbceecf1dd3e93 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=da76ce1913c6086278df262cd9ad684a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7b7cb283aa3588d52cdf6ed4c2e09d30 2500w" />

<div style={{ maxWidth: 720 }}>
    <h1 style={{ marginBottom: 12 }}>Ship multi‑agent systems with confidence</h1>

<p style={{ color: 'var(--mint-text-2)' }}>
      Design agents, orchestrate crews, and automate flows with guardrails, memory, knowledge, and observability baked in.
    </p>
  </div>

<div style={{ display: 'flex', flexWrap: 'wrap', gap: 12, justifyContent: 'center' }}>
    <a className="button button-primary" href="/en/quickstart">Get started</a>
    <a className="button" href="/en/changelog">View changelog</a>
    <a className="button" href="/en/api-reference/introduction">API Reference</a>
  </div>
</div>

<div style={{ marginTop: 32 }} />

<CardGroup cols={3}>
  <Card title="Introduction" href="/en/introduction" icon="sparkles">
    Overview of CrewAI concepts, architecture, and what you can build with agents, crews, and flows.
  </Card>

<Card title="Installation" href="/en/installation" icon="wrench">
    Install via `uv`, configure API keys, and set up the CLI for local development.
  </Card>

<Card title="Quickstart" href="/en/quickstart" icon="rocket">
    Spin up your first crew in minutes. Learn the core runtime, project layout, and dev loop.
  </Card>
</CardGroup>

<CardGroup cols={3}>
  <Card title="Agents" href="/en/concepts/agents" icon="users">
    Compose agents with tools, memory, knowledge, and structured outputs using Pydantic. Includes templates and best practices.
  </Card>

<Card title="Flows" href="/en/concepts/flows" icon="arrow-progress">
    Orchestrate start/listen/router steps, manage state, persist execution, and resume long-running workflows.
  </Card>

<Card title="Tasks & Processes" href="/en/concepts/tasks" icon="check">
    Define sequential, hierarchical, or hybrid processes with guardrails, callbacks, and human-in-the-loop triggers.
  </Card>
</CardGroup>

## Enterprise journey

<CardGroup cols={3}>
  <Card title="Deploy automations" href="/en/enterprise/features/automations" icon="server">
    Manage environments, redeploy safely, and monitor live runs directly from the Enterprise console.
  </Card>

<Card title="Triggers & Flows" href="/en/enterprise/guides/automation-triggers" icon="bolt">
    Connect Gmail, Slack, Salesforce, and more. Pass trigger payloads into crews and flows automatically.
  </Card>

<Card title="Team management" href="/en/enterprise/guides/team-management" icon="users-gear">
    Invite teammates, configure RBAC, and control access to production automations.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Triggers overview" href="/en/enterprise/guides/automation-triggers" icon="sparkles">
    Unified overview for Gmail, Drive, Outlook, Teams, OneDrive, HubSpot, and more — now with sample payloads and crews.
  </Card>

<Card title="Integration tools" href="/en/tools/integration/overview" icon="plug">
    Call existing CrewAI automations or Amazon Bedrock Agents directly from your crews using the updated integration toolkit.
  </Card>
</CardGroup>

<Callout title="Explore real-world patterns" icon="github">
  Browse the <a href="/en/examples/cookbooks">examples and cookbooks</a> for end-to-end reference implementations across agents, flows, and enterprise automations.
</Callout>

<CardGroup cols={2}>
  <Card title="Star us on GitHub" href="https://github.com/crewAIInc/crewAI" icon="star">
    If CrewAI helps you ship faster, give us a star and share your builds with the community.
  </Card>

<Card title="Join the community" href="https://community.crewai.com" icon="comments">
    Ask questions, showcase workflows, and request features alongside other builders.
  </Card>
</CardGroup>

---

## CrewAI Examples

**URL:** llms-txt#crewai-examples

**Contents:**
- Crews
- Flows
- Integrations
- Notebooks

Source: https://docs.crewai.com/en/examples/example

Explore curated examples organized by Crews, Flows, Integrations, and Notebooks.

<CardGroup cols={3}>
  <Card title="Marketing Strategy" icon="bullhorn" href="https://github.com/crewAIInc/crewAI-examples/tree/main/crews/marketing_strategy">
    Multi‑agent marketing campaign planning.
  </Card>

<Card title="Surprise Trip" icon="plane" href="https://github.com/crewAIInc/crewAI-examples/tree/main/crews/surprise_trip">
    Personalized surprise travel planning.
  </Card>

<Card title="Match Profile to Positions" icon="id-card" href="https://github.com/crewAIInc/crewAI-examples/tree/main/crews/match_profile_to_positions">
    CV‑to‑job matching with vector search.
  </Card>

<Card title="Job Posting" icon="newspaper" href="https://github.com/crewAIInc/crewAI-examples/tree/main/crews/job-posting">
    Automated job description creation.
  </Card>

<Card title="Game Builder Crew" icon="gamepad" href="https://github.com/crewAIInc/crewAI-examples/tree/main/crews/game-builder-crew">
    Multi‑agent team that designs and builds Python games.
  </Card>

<Card title="Recruitment" icon="user-group" href="https://github.com/crewAIInc/crewAI-examples/tree/main/crews/recruitment">
    Candidate sourcing and evaluation.
  </Card>

<Card title="Browse all Crews" icon="users" href="https://github.com/crewAIInc/crewAI-examples/tree/main/crews">
    See the full list of crew examples.
  </Card>
</CardGroup>

<CardGroup cols={3}>
  <Card title="Content Creator Flow" icon="pen" href="https://github.com/crewAIInc/crewAI-examples/tree/main/flows/content_creator_flow">
    Multi‑crew content generation with routing.
  </Card>

<Card title="Email Auto Responder" icon="envelope" href="https://github.com/crewAIInc/crewAI-examples/tree/main/flows/email_auto_responder_flow">
    Automated email monitoring and replies.
  </Card>

<Card title="Lead Score Flow" icon="chart-line" href="https://github.com/crewAIInc/crewAI-examples/tree/main/flows/lead_score_flow">
    Lead qualification with human‑in‑the‑loop.
  </Card>

<Card title="Meeting Assistant Flow" icon="calendar" href="https://github.com/crewAIInc/crewAI-examples/tree/main/flows/meeting_assistant_flow">
    Notes processing with integrations.
  </Card>

<Card title="Self Evaluation Loop" icon="rotate" href="https://github.com/crewAIInc/crewAI-examples/tree/main/flows/self_evaluation_loop_flow">
    Iterative self‑improvement workflows.
  </Card>

<Card title="Write a Book (Flows)" icon="book" href="https://github.com/crewAIInc/crewAI-examples/tree/main/flows/write_a_book_with_flows">
    Parallel chapter generation.
  </Card>

<Card title="Browse all Flows" icon="diagram-project" href="https://github.com/crewAIInc/crewAI-examples/tree/main/flows">
    See the full list of flow examples.
  </Card>
</CardGroup>

<CardGroup cols={3}>
  <Card title="CrewAI ↔ LangGraph" icon="link" href="https://github.com/crewAIInc/crewAI-examples/tree/main/integrations/crewai-langgraph">
    Integration with LangGraph framework.
  </Card>

<Card title="Azure OpenAI" icon="cloud" href="https://github.com/crewAIInc/crewAI-examples/tree/main/integrations/azure_model">
    Using CrewAI with Azure OpenAI.
  </Card>

<Card title="NVIDIA Models" icon="microchip" href="https://github.com/crewAIInc/crewAI-examples/tree/main/integrations/nvidia_models">
    NVIDIA ecosystem integrations.
  </Card>

<Card title="Browse Integrations" icon="puzzle-piece" href="https://github.com/crewAIInc/crewAI-examples/tree/main/integrations">
    See all integration examples.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Simple QA Crew + Flow" icon="book" href="https://github.com/crewAIInc/crewAI-examples/tree/main/Notebooks/Simple%20QA%20Crew%20%2B%20Flow">
    Simple QA Crew + Flow.
  </Card>

<Card title="All Notebooks" icon="book" href="https://github.com/crewAIInc/crewAI-examples/tree/main/Notebooks">
    Interactive examples for learning and experimentation.
  </Card>
</CardGroup>

---

## CrewAI Run Automation Tool

**URL:** llms-txt#crewai-run-automation-tool

Source: https://docs.crewai.com/en/tools/integration/crewaiautomationtool

Enables CrewAI agents to invoke CrewAI Platform automations and leverage external crew services within your workflows.

---

## CrewAI Tracing

**URL:** llms-txt#crewai-tracing

Source: https://docs.crewai.com/en/observability/tracing

Built-in tracing for CrewAI Crews and Flows with the CrewAI AOP platform

---

## Crews

**URL:** llms-txt#crews

**Contents:**
- Overview
- Crew Attributes
- Creating Crews
  - YAML Configuration (Recommended)
  - Direct Code Definition (Alternative)
- Crew Output
  - Crew Output Attributes
  - Crew Output Methods and Properties
  - Accessing Crew Outputs

Source: https://docs.crewai.com/en/concepts/crews

Understanding and utilizing crews in the crewAI framework with comprehensive attributes and functionalities.

A crew in crewAI represents a collaborative group of agents working together to achieve a set of tasks. Each crew defines the strategy for task execution, agent collaboration, and the overall workflow.

| Attribute                             | Parameters             | Description                                                                                                                                                                                           |   |
| :------------------------------------ | :--------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - |
| **Tasks**                             | `tasks`                | A list of tasks assigned to the crew.                                                                                                                                                                 |   |
| **Agents**                            | `agents`               | A list of agents that are part of the crew.                                                                                                                                                           |   |
| **Process** *(optional)*              | `process`              | The process flow (e.g., sequential, hierarchical) the crew follows. Default is `sequential`.                                                                                                          |   |
| **Verbose** *(optional)*              | `verbose`              | The verbosity level for logging during execution. Defaults to `False`.                                                                                                                                |   |
| **Manager LLM** *(optional)*          | `manager_llm`          | The language model used by the manager agent in a hierarchical process. **Required when using a hierarchical process.**                                                                               |   |
| **Function Calling LLM** *(optional)* | `function_calling_llm` | If passed, the crew will use this LLM to do function calling for tools for all agents in the crew. Each agent can have its own LLM, which overrides the crew's LLM for function calling.              |   |
| **Config** *(optional)*               | `config`               | Optional configuration settings for the crew, in `Json` or `Dict[str, Any]` format.                                                                                                                   |   |
| **Max RPM** *(optional)*              | `max_rpm`              | Maximum requests per minute the crew adheres to during execution. Defaults to `None`.                                                                                                                 |   |
| **Memory** *(optional)*               | `memory`               | Utilized for storing execution memories (short-term, long-term, entity memory).                                                                                                                       |   |
| **Cache** *(optional)*                | `cache`                | Specifies whether to use a cache for storing the results of tools' execution. Defaults to `True`.                                                                                                     |   |
| **Embedder** *(optional)*             | `embedder`             | Configuration for the embedder to be used by the crew. Mostly used by memory for now. Default is `{"provider": "openai"}`.                                                                            |   |
| **Step Callback** *(optional)*        | `step_callback`        | A function that is called after each step of every agent. This can be used to log the agent's actions or to perform other operations; it won't override the agent-specific `step_callback`.           |   |
| **Task Callback** *(optional)*        | `task_callback`        | A function that is called after the completion of each task. Useful for monitoring or additional operations post-task execution.                                                                      |   |
| **Share Crew** *(optional)*           | `share_crew`           | Whether you want to share the complete crew information and execution with the crewAI team to make the library better, and allow us to train models.                                                  |   |
| **Output Log File** *(optional)*      | `output_log_file`      | Set to True to save logs as logs.txt in the current directory or provide a file path. Logs will be in JSON format if the filename ends in .json, otherwise .txt. Defaults to `None`.                  |   |
| **Manager Agent** *(optional)*        | `manager_agent`        | `manager` sets a custom agent that will be used as a manager.                                                                                                                                         |   |
| **Prompt File** *(optional)*          | `prompt_file`          | Path to the prompt JSON file to be used for the crew.                                                                                                                                                 |   |
| **Planning** *(optional)*             | `planning`             | Adds planning ability to the Crew. When activated before each Crew iteration, all Crew data is sent to an AgentPlanner that will plan the tasks and this plan will be added to each task description. |   |
| **Planning LLM** *(optional)*         | `planning_llm`         | The language model used by the AgentPlanner in a planning process.                                                                                                                                    |   |
| **Knowledge Sources** *(optional)*    | `knowledge_sources`    | Knowledge sources available at the crew level, accessible to all the agents.                                                                                                                          |   |
| **Stream** *(optional)*               | `stream`               | Enable streaming output to receive real-time updates during crew execution. Returns a `CrewStreamingOutput` object that can be iterated for chunks. Defaults to `False`.                              |   |

<Tip>
  **Crew Max RPM**: The `max_rpm` attribute sets the maximum number of requests per minute the crew can perform to avoid rate limits and will override individual agents' `max_rpm` settings if you set it.
</Tip>

There are two ways to create crews in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define crews and is consistent with how agents and tasks are defined in CrewAI projects.

After creating your CrewAI project as outlined in the [Installation](/en/installation) section, you can define your crew in a class that inherits from `CrewBase` and uses decorators to define agents, tasks, and the crew itself.

#### Example Crew Class with Decorators

How to run the above code:

<Note>
  Tasks will be executed in the order they are defined.
</Note>

The `CrewBase` class, along with these decorators, automates the collection of agents and tasks, reducing the need for manual management.

#### Decorators overview from `annotations.py`

CrewAI provides several decorators in the `annotations.py` file that are used to mark methods within your crew class for special handling:

* `@CrewBase`: Marks the class as a crew base class.
* `@agent`: Denotes a method that returns an `Agent` object.
* `@task`: Denotes a method that returns a `Task` object.
* `@crew`: Denotes the method that returns the `Crew` object.
* `@before_kickoff`: (Optional) Marks a method to be executed before the crew starts.
* `@after_kickoff`: (Optional) Marks a method to be executed after the crew finishes.

These decorators help in organizing your crew's structure and automatically collecting agents and tasks without manually listing them.

### Direct Code Definition (Alternative)

Alternatively, you can define the crew directly in code without using YAML configuration files.

How to run the above code:

* Agents and tasks are defined directly within the class without decorators.
* We manually create and manage the list of agents and tasks.
* This approach provides more control but can be less maintainable for larger projects.

The output of a crew in the CrewAI framework is encapsulated within the `CrewOutput` class.
This class provides a structured way to access results of the crew's execution, including various formats such as raw strings, JSON, and Pydantic models.
The `CrewOutput` includes the results from the final task output, token usage, and individual task outputs.

### Crew Output Attributes

| Attribute        | Parameters     | Type                       | Description                                                                                          |
| :--------------- | :------------- | :------------------------- | :--------------------------------------------------------------------------------------------------- |
| **Raw**          | `raw`          | `str`                      | The raw output of the crew. This is the default format for the output.                               |
| **Pydantic**     | `pydantic`     | `Optional[BaseModel]`      | A Pydantic model object representing the structured output of the crew.                              |
| **JSON Dict**    | `json_dict`    | `Optional[Dict[str, Any]]` | A dictionary representing the JSON output of the crew.                                               |
| **Tasks Output** | `tasks_output` | `List[TaskOutput]`         | A list of `TaskOutput` objects, each representing the output of a task in the crew.                  |
| **Token Usage**  | `token_usage`  | `Dict[str, Any]`           | A summary of token usage, providing insights into the language model's performance during execution. |

### Crew Output Methods and Properties

| Method/Property | Description                                                                                       |
| :-------------- | :------------------------------------------------------------------------------------------------ |
| **json**        | Returns the JSON string representation of the crew output if the output format is JSON.           |
| **to\_dict**    | Converts the JSON and Pydantic outputs to a dictionary.                                           |
| \***\*str\*\*** | Returns the string representation of the crew output, prioritizing Pydantic, then JSON, then raw. |

### Accessing Crew Outputs

Once a crew has been executed, its output can be accessed through the `output` attribute of the `Crew` object. The `CrewOutput` class provides various ways to interact with and present this output.

```python Code theme={null}

**Examples:**

Example 1 (unknown):
```unknown
How to run the above code:
```

Example 2 (unknown):
```unknown
<Note>
  Tasks will be executed in the order they are defined.
</Note>

The `CrewBase` class, along with these decorators, automates the collection of agents and tasks, reducing the need for manual management.

#### Decorators overview from `annotations.py`

CrewAI provides several decorators in the `annotations.py` file that are used to mark methods within your crew class for special handling:

* `@CrewBase`: Marks the class as a crew base class.
* `@agent`: Denotes a method that returns an `Agent` object.
* `@task`: Denotes a method that returns a `Task` object.
* `@crew`: Denotes the method that returns the `Crew` object.
* `@before_kickoff`: (Optional) Marks a method to be executed before the crew starts.
* `@after_kickoff`: (Optional) Marks a method to be executed after the crew finishes.

These decorators help in organizing your crew's structure and automatically collecting agents and tasks without manually listing them.

### Direct Code Definition (Alternative)

Alternatively, you can define the crew directly in code without using YAML configuration files.
```

Example 3 (unknown):
```unknown
How to run the above code:
```

Example 4 (unknown):
```unknown
In this example:

* Agents and tasks are defined directly within the class without decorators.
* We manually create and manage the list of agents and tasks.
* This approach provides more control but can be less maintainable for larger projects.

## Crew Output

The output of a crew in the CrewAI framework is encapsulated within the `CrewOutput` class.
This class provides a structured way to access results of the crew's execution, including various formats such as raw strings, JSON, and Pydantic models.
The `CrewOutput` includes the results from the final task output, token usage, and individual task outputs.

### Crew Output Attributes

| Attribute        | Parameters     | Type                       | Description                                                                                          |
| :--------------- | :------------- | :------------------------- | :--------------------------------------------------------------------------------------------------- |
| **Raw**          | `raw`          | `str`                      | The raw output of the crew. This is the default format for the output.                               |
| **Pydantic**     | `pydantic`     | `Optional[BaseModel]`      | A Pydantic model object representing the structured output of the crew.                              |
| **JSON Dict**    | `json_dict`    | `Optional[Dict[str, Any]]` | A dictionary representing the JSON output of the crew.                                               |
| **Tasks Output** | `tasks_output` | `List[TaskOutput]`         | A list of `TaskOutput` objects, each representing the output of a task in the crew.                  |
| **Token Usage**  | `token_usage`  | `Dict[str, Any]`           | A summary of token usage, providing insights into the language model's performance during execution. |

### Crew Output Methods and Properties

| Method/Property | Description                                                                                       |
| :-------------- | :------------------------------------------------------------------------------------------------ |
| **json**        | Returns the JSON string representation of the crew output if the output format is JSON.           |
| **to\_dict**    | Converts the JSON and Pydantic outputs to a dictionary.                                           |
| \***\*str\*\*** | Returns the string representation of the crew output, prioritizing Pydantic, then JSON, then raw. |

### Accessing Crew Outputs

Once a crew has been executed, its output can be accessed through the `output` attribute of the `Crew` object. The `CrewOutput` class provides various ways to interact with and present this output.

#### Example
```

---

## Crew-wide knowledge (shared by all agents)

**URL:** llms-txt#crew-wide-knowledge-(shared-by-all-agents)

crew_knowledge = StringKnowledgeSource(
    content="Company policies and general information for all agents"
)

---

## Customize Agents

**URL:** llms-txt#customize-agents

**Contents:**
- Customizable Attributes
  - Key Attributes for Customization
- Advanced Customization Options
  - Language Model Customization
- Performance and Debugging Settings
  - Verbose Mode and RPM Limit
  - Maximum Iterations for Task Execution
- Customizing Agents and Tools
  - Example: Assigning Tools to an Agent

Source: https://docs.crewai.com/en/learn/customizing-agents

A comprehensive guide to tailoring agents for specific roles, tasks, and advanced customizations within the CrewAI framework.

## Customizable Attributes

Crafting an efficient CrewAI team hinges on the ability to dynamically tailor your AI agents to meet the unique requirements of any project. This section covers the foundational attributes you can customize.

### Key Attributes for Customization

| Attribute                           | Description                                                                                                         |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| **Role**                            | Specifies the agent's job within the crew, such as 'Analyst' or 'Customer Service Rep'.                             |
| **Goal**                            | Defines the agent’s objectives, aligned with its role and the crew’s overarching mission.                           |
| **Backstory**                       | Provides depth to the agent's persona, enhancing motivations and engagements within the crew.                       |
| **Tools** *(Optional)*              | Represents the capabilities or methods the agent uses for tasks, from simple functions to complex integrations.     |
| **Cache** *(Optional)*              | Determines if the agent should use a cache for tool usage.                                                          |
| **Max RPM**                         | Sets the maximum requests per minute (`max_rpm`). Can be set to `None` for unlimited requests to external services. |
| **Verbose** *(Optional)*            | Enables detailed logging for debugging and optimization, providing insights into execution processes.               |
| **Allow Delegation** *(Optional)*   | Controls task delegation to other agents, default is `False`.                                                       |
| **Max Iter** *(Optional)*           | Limits the maximum number of iterations (`max_iter`) for a task to prevent infinite loops, with a default of 25.    |
| **Max Execution Time** *(Optional)* | Sets the maximum time allowed for an agent to complete a task.                                                      |
| **System Template** *(Optional)*    | Defines the system format for the agent.                                                                            |
| **Prompt Template** *(Optional)*    | Defines the prompt format for the agent.                                                                            |
| **Response Template** *(Optional)*  | Defines the response format for the agent.                                                                          |
| **Use System Prompt** *(Optional)*  | Controls whether the agent will use a system prompt during task execution.                                          |
| **Respect Context Window**          | Enables a sliding context window by default, maintaining context size.                                              |
| **Max Retry Limit**                 | Sets the maximum number of retries (`max_retry_limit`) for an agent in case of errors.                              |

## Advanced Customization Options

Beyond the basic attributes, CrewAI allows for deeper customization to enhance an agent's behavior and capabilities significantly.

### Language Model Customization

Agents can be customized with specific language models (`llm`) and function-calling language models (`function_calling_llm`), offering advanced control over their processing and decision-making abilities.
It's important to note that setting the `function_calling_llm` allows for overriding the default crew function-calling language model, providing a greater degree of customization.

## Performance and Debugging Settings

Adjusting an agent's performance and monitoring its operations are crucial for efficient task execution.

### Verbose Mode and RPM Limit

* **Verbose Mode**: Enables detailed logging of an agent's actions, useful for debugging and optimization. Specifically, it provides insights into agent execution processes, aiding in the optimization of performance.
* **RPM Limit**: Sets the maximum number of requests per minute (`max_rpm`). This attribute is optional and can be set to `None` for no limit, allowing for unlimited queries to external services if needed.

### Maximum Iterations for Task Execution

The `max_iter` attribute allows users to define the maximum number of iterations an agent can perform for a single task, preventing infinite loops or excessively long executions.
The default value is set to 25, providing a balance between thoroughness and efficiency. Once the agent approaches this number, it will try its best to give a good answer.

## Customizing Agents and Tools

Agents are customized by defining their attributes and tools during initialization. Tools are critical for an agent's functionality, enabling them to perform specialized tasks.
The `tools` attribute should be an array of tools the agent can utilize, and it's initialized as an empty list by default. Tools can be added or modified post-agent initialization to adapt to new requirements.

### Example: Assigning Tools to an Agent

```python Code theme={null}
import os
from crewai import Agent
from crewai_tools import SerperDevTool

**Examples:**

Example 1 (unknown):
```unknown
### Example: Assigning Tools to an Agent
```

---

## Define tasks

**URL:** llms-txt#define-tasks

search_task = Task(
    description="""Search for relevant documents about the {query}.
    Your final answer should include:
    - The relevant information found
    - The similarity scores of the results
    - The metadata of the relevant documents""",
    agent=search_agent
)

answer_task = Task(
    description="""Given the context and metadata of relevant documents,
    generate a final answer based on the context.""",
    agent=answer_agent
)

---

## Define their tasks

**URL:** llms-txt#define-their-tasks

research_task = Task(
    description="Research the current market landscape for AI-powered healthcare solutions",
    expected_output="Comprehensive market data including key players, market size, and growth trends",
    agent=researcher
)

analysis_task = Task(
    description="Analyze the market data and identify the top 3 investment opportunities",
    expected_output="Analysis report with 3 recommended investment opportunities and rationale",
    agent=analyst,
    context=[research_task]
)

---

## Define the agents

**URL:** llms-txt#define-the-agents

data_fetcher_agent = Agent(
    role="Data Fetcher",
    goal="Fetch data online using Serper tool",
    backstory="Backstory 1",
    verbose=True,
    tools=[SerperDevTool()]
)

data_processor_agent = Agent(
    role="Data Processor",
    goal="Process fetched data",
    backstory="Backstory 2",
    verbose=True
)

summary_generator_agent = Agent(
    role="Summary Generator",
    goal="Generate summary from fetched data",
    backstory="Backstory 3",
    verbose=True
)

class EventOutput(BaseModel):
    events: List[str]

task1 = Task(
    description="Fetch data about events in San Francisco using Serper tool",
    expected_output="List of 10 things to do in SF this week",
    agent=data_fetcher_agent,
    output_pydantic=EventOutput,
)

conditional_task = ConditionalTask(
    description="""
        Check if data is missing. If we have less than 10 events,
        fetch more events using Serper tool so that
        we have a total of 10 events in SF this week..
        """,
    expected_output="List of 10 Things to do in SF this week",
    condition=is_data_missing,
    agent=data_processor_agent,
)

task3 = Task(
    description="Generate summary of events in San Francisco from fetched data",
    expected_output="A complete report on the customer and their customers and competitors, including their demographics, preferences, market positioning and audience engagement.",
    agent=summary_generator_agent,
)

---

## Define your agents

**URL:** llms-txt#define-your-agents

researcher = Agent(
    role="Senior Research Analyst",
    goal="Uncover cutting-edge developments in AI and data science",
    backstory="""You work at a leading tech think tank.
    Your expertise lies in identifying emerging trends.
    You have a knack for dissecting complex data and presenting actionable insights.""",
    verbose=True,
    tools=[SerperDevTool()],
)

writer = Agent(
    role="Tech Content Strategist",
    goal="Craft compelling content on tech advancements",
    backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
    You transform complex concepts into compelling narratives.""",
    verbose=True,
)

---

## Define your agents with roles and goals

**URL:** llms-txt#define-your-agents-with-roles-and-goals

researcher = Agent(
    role="Senior Research Analyst",
    goal="Uncover cutting-edge developments in AI and data science",
    backstory="""You work at a leading tech think tank.
    Your expertise lies in identifying emerging trends.
    You have a knack for dissecting complex data and presenting actionable insights.""",
    verbose=True,
    allow_delegation=False,
    # You can pass an optional llm attribute specifying what model you wanna use.
    # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7),
    tools=[search_tool],
)
writer = Agent(
    role="Tech Content Strategist",
    goal="Craft compelling content on tech advancements",
    backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
    You transform complex concepts into compelling narratives.""",
    verbose=True,
    allow_delegation=True,
)

---

## Define your agents with roles, goals, tools, and additional attributes

**URL:** llms-txt#define-your-agents-with-roles,-goals,-tools,-and-additional-attributes

researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in AI and data science',
    backstory=(
        "You are a Senior Research Analyst at a leading tech think tank. "
        "Your expertise lies in identifying emerging trends and technologies in AI and data science. "
        "You have a knack for dissecting complex data and presenting actionable insights."
    ),
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)
writer = Agent(
    role='Tech Content Strategist',
    goal='Craft compelling content on tech advancements',
    backstory=(
        "You are a renowned Tech Content Strategist, known for your insightful and engaging articles on technology and innovation. "
        "With a deep understanding of the tech industry, you transform complex concepts into compelling narratives."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[search_tool],
    cache=False,  # Disable cache for this agent
)

---

## Define your tasks

**URL:** llms-txt#define-your-tasks

research_task = Task(
  description='Gather relevant data...', 
  agent=researcher, 
  expected_output='Raw Data'
)
analysis_task = Task(
  description='Analyze the data...', 
  agent=analyst, 
  expected_output='Data Insights'
)
writing_task = Task(
  description='Compose the report...', 
  agent=writer, 
  expected_output='Final Report'
)

---

## Different knowledge for different agents

**URL:** llms-txt#different-knowledge-for-different-agents

sales_knowledge = StringKnowledgeSource(content="Sales procedures and pricing")
tech_knowledge = StringKnowledgeSource(content="Technical documentation")
support_knowledge = StringKnowledgeSource(content="Support procedures")

sales_agent = Agent(
    role="Sales Representative",
    knowledge_sources=[sales_knowledge],
    embedder={"provider": "openai", "config": {"model": "text-embedding-3-small"}}
)

tech_agent = Agent(
    role="Technical Expert", 
    knowledge_sources=[tech_knowledge],
    embedder={"provider": "ollama", "config": {"model": "mxbai-embed-large"}}
)

support_agent = Agent(
    role="Support Specialist",
    knowledge_sources=[support_knowledge]
    # Will use crew embedder as fallback
)

crew = Crew(
    agents=[sales_agent, tech_agent, support_agent],
    tasks=[...],
    embedder={  # Fallback embedder for agents without their own
        "provider": "google-generativeai",
        "config": {"model_name": "gemini-embedding-001"}
    }
)

---

## Enable basic memory system

**URL:** llms-txt#enable-basic-memory-system

**Contents:**
  - How It Works
- Storage Location Transparency
  - Where CrewAI Stores Files
  - Finding Your Storage Location

crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,  # Enables short-term, long-term, and entity memory
    verbose=True
)

~/Library/Application Support/CrewAI/{project_name}/
├── knowledge/           # Knowledge base ChromaDB files
├── short_term_memory/   # Short-term memory ChromaDB files
├── long_term_memory/    # Long-term memory ChromaDB files
├── entities/            # Entity memory ChromaDB files
└── long_term_memory_storage.db  # SQLite database

~/.local/share/CrewAI/{project_name}/
├── knowledge/
├── short_term_memory/
├── long_term_memory/
├── entities/
└── long_term_memory_storage.db

C:\Users\{username}\AppData\Local\CrewAI\{project_name}\
├── knowledge\
├── short_term_memory\
├── long_term_memory\
├── entities\
└── long_term_memory_storage.db
python  theme={null}
from crewai.utilities.paths import db_storage_path
import os

**Examples:**

Example 1 (unknown):
```unknown
### How It Works

* **Short-Term Memory**: Uses ChromaDB with RAG for current context
* **Long-Term Memory**: Uses SQLite3 to store task results across sessions
* **Entity Memory**: Uses RAG to track entities (people, places, concepts)
* **Storage Location**: Platform-specific location via `appdirs` package
* **Custom Storage Directory**: Set `CREWAI_STORAGE_DIR` environment variable

## Storage Location Transparency

<Info>
  **Understanding Storage Locations**: CrewAI uses platform-specific directories to store memory and knowledge files following OS conventions. Understanding these locations helps with production deployments, backups, and debugging.
</Info>

### Where CrewAI Stores Files

By default, CrewAI uses the `appdirs` library to determine storage locations following platform conventions. Here's exactly where your files are stored:

#### Default Storage Locations by Platform

**macOS:**
```

Example 2 (unknown):
```unknown
**Linux:**
```

Example 3 (unknown):
```unknown
**Windows:**
```

Example 4 (unknown):
```unknown
### Finding Your Storage Location

To see exactly where CrewAI is storing files on your system:
```

---

## Enable collaboration for agents

**URL:** llms-txt#enable-collaboration-for-agents

researcher = Agent(
    role="Research Specialist",
    goal="Conduct thorough research on any topic",
    backstory="Expert researcher with access to various sources",
    allow_delegation=True,  # 🔑 Key setting for collaboration
    verbose=True
)

writer = Agent(
    role="Content Writer", 
    goal="Create engaging content based on research",
    backstory="Skilled writer who transforms research into compelling content",
    allow_delegation=True,  # 🔑 Enables asking questions to other agents
    verbose=True
)

---

## Enable streaming

**URL:** llms-txt#enable-streaming

crew = Crew(
    agents=[researcher],
    tasks=[task],
    stream=True
)

---

## Enable tracing in your crew

**URL:** llms-txt#enable-tracing-in-your-crew

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    tracing=True,  # Enable built-in tracing
    verbose=True
)

---

## Ensure to provide a manager_llm or manager_agent

**URL:** llms-txt#ensure-to-provide-a-manager_llm-or-manager_agent

**Contents:**
- Sequential Process
- Hierarchical Process
- Process Class: Detailed Overview
- Conclusion

crew = Crew(
    agents=my_agents,
    tasks=my_tasks,
    process=Process.hierarchical,
    manager_llm="gpt-4o"
    # or
    # manager_agent=my_manager_agent
)
```

**Note:** Ensure `my_agents` and `my_tasks` are defined prior to creating a `Crew` object, and for the hierarchical process, either `manager_llm` or `manager_agent` is also required.

## Sequential Process

This method mirrors dynamic team workflows, progressing through tasks in a thoughtful and systematic manner. Task execution follows the predefined order in the task list, with the output of one task serving as context for the next.

To customize task context, utilize the `context` parameter in the `Task` class to specify outputs that should be used as context for subsequent tasks.

## Hierarchical Process

Emulates a corporate hierarchy, CrewAI allows specifying a custom manager agent or automatically creates one, requiring the specification of a manager language model (`manager_llm`). This agent oversees task execution, including planning, delegation, and validation. Tasks are not pre-assigned; the manager allocates tasks to agents based on their capabilities, reviews outputs, and assesses task completion.

## Process Class: Detailed Overview

The `Process` class is implemented as an enumeration (`Enum`), ensuring type safety and restricting process values to the defined types (`sequential`, `hierarchical`). The consensual process is planned for future inclusion, emphasizing our commitment to continuous development and innovation.

The structured collaboration facilitated by processes within CrewAI is crucial for enabling systematic teamwork among agents.
This documentation has been updated to reflect the latest features, enhancements, and the planned integration of the Consensual Process, ensuring users have access to the most current and comprehensive information.

---

## Establishing the crew with a hierarchical process and additional configurations

**URL:** llms-txt#establishing-the-crew-with-a-hierarchical-process-and-additional-configurations

**Contents:**
  - Using a Custom Manager Agent

project_crew = Crew(
    tasks=[...],  # Tasks to be delegated and executed under the manager's supervision
    agents=[researcher, writer],
    manager_llm="gpt-4o",  # Specify which LLM the manager should use
    process=Process.hierarchical,  
    planning=True, 
)
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
### Using a Custom Manager Agent

Alternatively, you can create a custom manager agent with specific attributes tailored to your project's management needs. This gives you more control over the manager's behavior and capabilities.
```

---

## Evaluating Use Cases for CrewAI

**URL:** llms-txt#evaluating-use-cases-for-crewai

**Contents:**
- Understanding the Decision Framework
- The Complexity-Precision Matrix Explained
  - What is Complexity?
  - What is Precision?
  - The Four Quadrants
- Choosing Between Crews and Flows
  - When to Choose Crews

Source: https://docs.crewai.com/en/guides/concepts/evaluating-use-cases

Learn how to assess your AI application needs and choose the right approach between Crews and Flows based on complexity and precision requirements.

## Understanding the Decision Framework

When building AI applications with CrewAI, one of the most important decisions you'll make is choosing the right approach for your specific use case. Should you use a Crew? A Flow? A combination of both? This guide will help you evaluate your requirements and make informed architectural decisions.

At the heart of this decision is understanding the relationship between **complexity** and **precision** in your application:

<Frame caption="Complexity vs. Precision Matrix for CrewAI Applications">
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/complexity_precision.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ba6f265da6ac72075285b5008735be82" alt="Complexity vs. Precision Matrix" data-og-width="615" width="615" data-og-height="392" height="392" data-path="images/complexity_precision.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/complexity_precision.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=48c8a451aaef57f3f152ccb921dac715 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/complexity_precision.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=780bae03e53c2fcfd4dce5e3c8672372 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/complexity_precision.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=364f719dfe67f2ae8a54ffce0a7544a8 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/complexity_precision.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=535a75d70cd4109123adf1d34e1316a0 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/complexity_precision.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4f42346c0b66928bf27b3c3a78a3a6ff 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/complexity_precision.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=832ce0a91bf333433801bca1d1832527 2500w" />
</Frame>

This matrix helps visualize how different approaches align with varying requirements for complexity and precision. Let's explore what each quadrant means and how it guides your architectural choices.

## The Complexity-Precision Matrix Explained

### What is Complexity?

In the context of CrewAI applications, **complexity** refers to:

* The number of distinct steps or operations required
* The diversity of tasks that need to be performed
* The interdependencies between different components
* The need for conditional logic and branching
* The sophistication of the overall workflow

### What is Precision?

**Precision** in this context refers to:

* The accuracy required in the final output
* The need for structured, predictable results
* The importance of reproducibility
* The level of control needed over each step
* The tolerance for variation in outputs

### The Four Quadrants

#### 1. Low Complexity, Low Precision

* Simple, straightforward tasks
* Tolerance for some variation in outputs
* Limited number of steps
* Creative or exploratory applications

**Recommended Approach:** Simple Crews with minimal agents

**Example Use Cases:**

* Basic content generation
* Idea brainstorming
* Simple summarization tasks
* Creative writing assistance

#### 2. Low Complexity, High Precision

* Simple workflows that require exact, structured outputs
* Need for reproducible results
* Limited steps but high accuracy requirements
* Often involves data processing or transformation

**Recommended Approach:** Flows with direct LLM calls or simple Crews with structured outputs

**Example Use Cases:**

* Data extraction and transformation
* Form filling and validation
* Structured content generation (JSON, XML)
* Simple classification tasks

#### 3. High Complexity, Low Precision

* Multi-stage processes with many steps
* Creative or exploratory outputs
* Complex interactions between components
* Tolerance for variation in final results

**Recommended Approach:** Complex Crews with multiple specialized agents

**Example Use Cases:**

* Research and analysis
* Content creation pipelines
* Exploratory data analysis
* Creative problem-solving

#### 4. High Complexity, High Precision

* Complex workflows requiring structured outputs
* Multiple interdependent steps with strict accuracy requirements
* Need for both sophisticated processing and precise results
* Often mission-critical applications

**Recommended Approach:** Flows orchestrating multiple Crews with validation steps

**Example Use Cases:**

* Enterprise decision support systems
* Complex data processing pipelines
* Multi-stage document processing
* Regulated industry applications

## Choosing Between Crews and Flows

### When to Choose Crews

Crews are ideal when:

1. **You need collaborative intelligence** - Multiple agents with different specializations need to work together
2. **The problem requires emergent thinking** - The solution benefits from different perspectives and approaches
3. **The task is primarily creative or analytical** - The work involves research, content creation, or analysis
4. **You value adaptability over strict structure** - The workflow can benefit from agent autonomy
5. **The output format can be somewhat flexible** - Some variation in output structure is acceptable

```python  theme={null}

---

## Example: Content Production Pipeline combining Crews and Flows

**URL:** llms-txt#example:-content-production-pipeline-combining-crews-and-flows

from crewai.flow.flow import Flow, listen, start
from crewai import Agent, Crew, Process, Task
from pydantic import BaseModel
from typing import List, Dict

class ContentState(BaseModel):
    topic: str = ""
    target_audience: str = ""
    content_type: str = ""
    outline: Dict = {}
    draft_content: str = ""
    final_content: str = ""
    seo_score: int = 0

class ContentProductionFlow(Flow[ContentState]):
    @start()
    def initialize_project(self):
        # Set initial parameters
        self.state.topic = "Sustainable Investing"
        self.state.target_audience = "Millennial Investors"
        self.state.content_type = "Blog Post"
        return "Project initialized"

@listen(initialize_project)
    def create_outline(self, _):
        # Use a research crew to create an outline
        researcher = Agent(
            role="Content Researcher",
            goal=f"Research {self.state.topic} for {self.state.target_audience}",
            backstory="You are an expert researcher with deep knowledge of content creation."
        )

outliner = Agent(
            role="Content Strategist",
            goal=f"Create an engaging outline for a {self.state.content_type}",
            backstory="You excel at structuring content for maximum engagement."
        )

research_task = Task(
            description=f"Research {self.state.topic} focusing on what would interest {self.state.target_audience}",
            expected_output="Comprehensive research notes with key points and statistics",
            agent=researcher
        )

outline_task = Task(
            description=f"Create an outline for a {self.state.content_type} about {self.state.topic}",
            expected_output="Detailed content outline with sections and key points",
            agent=outliner,
            context=[research_task]
        )

outline_crew = Crew(
            agents=[researcher, outliner],
            tasks=[research_task, outline_task],
            process=Process.sequential,
            verbose=True
        )

# Run the crew and store the result
        result = outline_crew.kickoff()

# Parse the outline (in a real app, you might use a more robust parsing approach)
        import json
        try:
            self.state.outline = json.loads(result.raw)
        except:
            # Fallback if not valid JSON
            self.state.outline = {"sections": result.raw}

return "Outline created"

@listen(create_outline)
    def write_content(self, _):
        # Use a writing crew to create the content
        writer = Agent(
            role="Content Writer",
            goal=f"Write engaging content for {self.state.target_audience}",
            backstory="You are a skilled writer who creates compelling content."
        )

editor = Agent(
            role="Content Editor",
            goal="Ensure content is polished, accurate, and engaging",
            backstory="You have a keen eye for detail and a talent for improving content."
        )

writing_task = Task(
            description=f"Write a {self.state.content_type} about {self.state.topic} following this outline: {self.state.outline}",
            expected_output="Complete draft content in markdown format",
            agent=writer
        )

editing_task = Task(
            description="Edit and improve the draft content for clarity, engagement, and accuracy",
            expected_output="Polished final content in markdown format",
            agent=editor,
            context=[writing_task]
        )

writing_crew = Crew(
            agents=[writer, editor],
            tasks=[writing_task, editing_task],
            process=Process.sequential,
            verbose=True
        )

# Run the crew and store the result
        result = writing_crew.kickoff()
        self.state.final_content = result.raw

return "Content created"

@listen(write_content)
    def optimize_for_seo(self, _):
        # Use a direct LLM call for SEO optimization
        from crewai import LLM
        llm = LLM(model="openai/gpt-4o-mini")

prompt = f"""
        Analyze this content for SEO effectiveness for the keyword "{self.state.topic}".
        Rate it on a scale of 1-100 and provide 3 specific recommendations for improvement.

Content: {self.state.final_content[:1000]}... (truncated for brevity)

Format your response as JSON with the following structure:
        {{
            "score": 85,
            "recommendations": [
                "Recommendation 1",
                "Recommendation 2",
                "Recommendation 3"
            ]
        }}
        """

seo_analysis = llm.call(prompt)

# Parse the SEO analysis
        import json
        try:
            analysis = json.loads(seo_analysis)
            self.state.seo_score = analysis.get("score", 0)
            return analysis
        except:
            self.state.seo_score = 50
            return {"score": 50, "recommendations": ["Unable to parse SEO analysis"]}

---

## Example: Creating a crew with a sequential process

**URL:** llms-txt#example:-creating-a-crew-with-a-sequential-process

crew = Crew(
    agents=my_agents,
    tasks=my_tasks,
    process=Process.sequential
)

---

## Example crew execution

**URL:** llms-txt#example-crew-execution

crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, write_article_task],
    verbose=True
)

crew_output = crew.kickoff()

---

## Example of initiating tool that agents can use

**URL:** llms-txt#example-of-initiating-tool-that-agents-can-use

---

## Execute tasks

**URL:** llms-txt#execute-tasks

**Contents:**
- Available CrewAI Tools
- Creating your own Tools
  - Subclassing `BaseTool`
- Asynchronous Tool Support
  - Creating Async Tools
  - Using Async Tools

crew.kickoff()
python Code theme={null}
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class MyToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = "What this tool does. It's vital for effective utilization."
    args_schema: Type[BaseModel] = MyToolInput

def _run(self, argument: str) -> str:
        # Your tool's logic here
        return "Tool's result"
python Code theme={null}
from crewai.tools import tool

@tool("fetch_data_async")
async def fetch_data_async(query: str) -> str:
    """Asynchronously fetch data based on the query."""
    # Simulate async operation
    await asyncio.sleep(1)
    return f"Data retrieved for {query}"
python Code theme={null}
from crewai.tools import BaseTool

class AsyncCustomTool(BaseTool):
    name: str = "async_custom_tool"
    description: str = "An asynchronous custom tool"

async def _run(self, query: str = "") -> str:
        """Asynchronously run the tool"""
        # Your async implementation here
        await asyncio.sleep(1)
        return f"Processed {query} asynchronously"
python Code theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## Available CrewAI Tools

* **Error Handling**: All tools are built with error handling capabilities, allowing agents to gracefully manage exceptions and continue their tasks.
* **Caching Mechanism**: All tools support caching, enabling agents to efficiently reuse previously obtained results, reducing the load on external resources and speeding up the execution time. You can also define finer control over the caching mechanism using the `cache_function` attribute on the tool.

Here is a list of the available tools and their descriptions:

| Tool                             | Description                                                                                    |
| :------------------------------- | :--------------------------------------------------------------------------------------------- |
| **ApifyActorsTool**              | A tool that integrates Apify Actors with your workflows for web scraping and automation tasks. |
| **BrowserbaseLoadTool**          | A tool for interacting with and extracting data from web browsers.                             |
| **CodeDocsSearchTool**           | A RAG tool optimized for searching through code documentation and related technical documents. |
| **CodeInterpreterTool**          | A tool for interpreting python code.                                                           |
| **ComposioTool**                 | Enables use of Composio tools.                                                                 |
| **CSVSearchTool**                | A RAG tool designed for searching within CSV files, tailored to handle structured data.        |
| **DALL-E Tool**                  | A tool for generating images using the DALL-E API.                                             |
| **DirectorySearchTool**          | A RAG tool for searching within directories, useful for navigating through file systems.       |
| **DOCXSearchTool**               | A RAG tool aimed at searching within DOCX documents, ideal for processing Word files.          |
| **DirectoryReadTool**            | Facilitates reading and processing of directory structures and their contents.                 |
| **EXASearchTool**                | A tool designed for performing exhaustive searches across various data sources.                |
| **FileReadTool**                 | Enables reading and extracting data from files, supporting various file formats.               |
| **FirecrawlSearchTool**          | A tool to search webpages using Firecrawl and return the results.                              |
| **FirecrawlCrawlWebsiteTool**    | A tool for crawling webpages using Firecrawl.                                                  |
| **FirecrawlScrapeWebsiteTool**   | A tool for scraping webpages URL using Firecrawl and returning its contents.                   |
| **GithubSearchTool**             | A RAG tool for searching within GitHub repositories, useful for code and documentation search. |
| **SerperDevTool**                | A specialized tool for development purposes, with specific functionalities under development.  |
| **TXTSearchTool**                | A RAG tool focused on searching within text (.txt) files, suitable for unstructured data.      |
| **JSONSearchTool**               | A RAG tool designed for searching within JSON files, catering to structured data handling.     |
| **LlamaIndexTool**               | Enables the use of LlamaIndex tools.                                                           |
| **MDXSearchTool**                | A RAG tool tailored for searching within Markdown (MDX) files, useful for documentation.       |
| **PDFSearchTool**                | A RAG tool aimed at searching within PDF documents, ideal for processing scanned documents.    |
| **PGSearchTool**                 | A RAG tool optimized for searching within PostgreSQL databases, suitable for database queries. |
| **Vision Tool**                  | A tool for generating images using the DALL-E API.                                             |
| **RagTool**                      | A general-purpose RAG tool capable of handling various data sources and types.                 |
| **ScrapeElementFromWebsiteTool** | Enables scraping specific elements from websites, useful for targeted data extraction.         |
| **ScrapeWebsiteTool**            | Facilitates scraping entire websites, ideal for comprehensive data collection.                 |
| **WebsiteSearchTool**            | A RAG tool for searching website content, optimized for web data extraction.                   |
| **XMLSearchTool**                | A RAG tool designed for searching within XML files, suitable for structured data formats.      |
| **YoutubeChannelSearchTool**     | A RAG tool for searching within YouTube channels, useful for video content analysis.           |
| **YoutubeVideoSearchTool**       | A RAG tool aimed at searching within YouTube videos, ideal for video data extraction.          |

## Creating your own Tools

<Tip>
  Developers can craft `custom tools` tailored for their agent's needs or
  utilize pre-built options.
</Tip>

There are two main ways for one to create a CrewAI tool:

### Subclassing `BaseTool`
```

Example 2 (unknown):
```unknown
## Asynchronous Tool Support

CrewAI supports asynchronous tools, allowing you to implement tools that perform non-blocking operations like network requests, file I/O, or other async operations without blocking the main execution thread.

### Creating Async Tools

You can create async tools in two ways:

#### 1. Using the `tool` Decorator with Async Functions
```

Example 3 (unknown):
```unknown
#### 2. Implementing Async Methods in Custom Tool Classes
```

Example 4 (unknown):
```unknown
### Using Async Tools

Async tools work seamlessly in both standard Crew workflows and Flow-based workflows:
```

---

## FAQs

**URL:** llms-txt#faqs

Source: https://docs.crewai.com/en/enterprise/resources/frequently-asked-questions

Frequently asked questions about CrewAI AOP

<AccordionGroup>
  <Accordion title="How is task execution handled in the hierarchical process?">
    In the hierarchical process, a manager agent is automatically created and coordinates the workflow, delegating tasks and validating outcomes for streamlined and effective execution. The manager agent utilizes tools to facilitate task delegation and execution by agents under the manager's guidance. The manager LLM is crucial for the hierarchical process and must be set up correctly for proper function.
  </Accordion>

<Accordion title="Where can I get the latest CrewAI documentation?">
    The most up-to-date documentation for CrewAI is available on our official documentation website: [https://docs.crewai.com/](https://docs.crewai.com/)
    <Card href="https://docs.crewai.com/" icon="books">CrewAI Docs</Card>
  </Accordion>

<Accordion title="What are the key differences between Hierarchical and Sequential Processes in CrewAI?">
    #### Hierarchical Process:

* Tasks are delegated and executed based on a structured chain of command
    * A manager language model (`manager_llm`) must be specified for the manager agent
    * Manager agent oversees task execution, planning, delegation, and validation
    * Tasks are not pre-assigned; the manager allocates tasks to agents based on their capabilities

#### Sequential Process:

* Tasks are executed one after another, ensuring tasks are completed in an orderly progression
    * Output of one task serves as context for the next
    * Task execution follows the predefined order in the task list

#### Which Process is Better for Complex Projects?

The hierarchical process is better suited for complex projects because it allows for:

* **Dynamic task allocation and delegation**: Manager agent can assign tasks based on agent capabilities
    * **Structured validation and oversight**: Manager agent reviews task outputs and ensures completion
    * **Complex task management**: Precise control over tool availability at the agent level
  </Accordion>

<Accordion title="What are the benefits of using memory in the CrewAI framework?">
    * **Adaptive Learning**: Crews become more efficient over time, adapting to new information and refining their approach to tasks
    * **Enhanced Personalization**: Memory enables agents to remember user preferences and historical interactions, leading to personalized experiences
    * **Improved Problem Solving**: Access to a rich memory store aids agents in making more informed decisions, drawing on past learnings and contextual insights
  </Accordion>

<Accordion title="What is the purpose of setting a maximum RPM limit for an agent?">
    Setting a maximum RPM limit for an agent prevents the agent from making too many requests to external services, which can help to avoid rate limits and improve performance.
  </Accordion>

<Accordion title="What role does human input play in the execution of tasks within a CrewAI crew?">
    Human input allows agents to request additional information or clarification when necessary. This feature is crucial in complex decision-making processes or when agents require more details to complete a task effectively.

To integrate human input into agent execution, set the `human_input` flag in the task definition. When enabled, the agent prompts the user for input before delivering its final answer. This input can provide extra context, clarify ambiguities, or validate the agent's output.

For detailed implementation guidance, see our [Human-in-the-Loop guide](/en/enterprise/guides/human-in-the-loop).
  </Accordion>

<Accordion title="What advanced customization options are available for tailoring and enhancing agent behavior and capabilities in CrewAI?">
    CrewAI provides a range of advanced customization options:

* **Language Model Customization**: Agents can be customized with specific language models (`llm`) and function-calling language models (`function_calling_llm`)
    * **Performance and Debugging Settings**: Adjust an agent's performance and monitor its operations
    * **Verbose Mode**: Enables detailed logging of an agent's actions, useful for debugging and optimization
    * **RPM Limit**: Sets the maximum number of requests per minute (`max_rpm`)
    * **Maximum Iterations**: The `max_iter` attribute allows users to define the maximum number of iterations an agent can perform for a single task
    * **Delegation and Autonomy**: Control an agent's ability to delegate or ask questions with the `allow_delegation` attribute (default: True)
    * **Human Input Integration**: Agents can request additional information or clarification when necessary
  </Accordion>

<Accordion title="In what scenarios is human input particularly useful in agent execution?">
    Human input is particularly useful when:

* **Agents require additional information or clarification**: When agents encounter ambiguity or incomplete data
    * **Agents need to make complex or sensitive decisions**: Human input can assist in ethical or nuanced decision-making
    * **Oversight and validation of agent output**: Human input can help validate results and prevent errors
    * **Customizing agent behavior**: Human input can provide feedback to refine agent responses over time
    * **Identifying and resolving errors or limitations**: Human input helps address agent capability gaps
  </Accordion>

<Accordion title="What are the different types of memory that are available in crewAI?">
    The different types of memory available in CrewAI are:

* **Short-term memory**: Temporary storage for immediate context
    * **Long-term memory**: Persistent storage for learned patterns and information
    * **Entity memory**: Focused storage for specific entities and their attributes
    * **Contextual memory**: Memory that maintains context across interactions

Learn more about the different types of memory:
    <Card href="https://docs.crewai.com/concepts/memory" icon="brain">CrewAI Memory</Card>
  </Accordion>

<Accordion title="How do I use Output Pydantic in a Task?">
    To use Output Pydantic in a task, you need to define the expected output of the task as a Pydantic model. Here's a quick example:

<Steps>
      <Step title="Define a Pydantic model">
        
      </Step>

<Step title="Create a task with Output Pydantic">
        
      </Step>

<Step title="Set the output_pydantic attribute in your agent">
        
      </Step>
    </Steps>

Here's a tutorial on how to consistently get structured outputs from your agents:

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/dNpKQk5uxHw" title="Structured outputs in CrewAI" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
  </Accordion>

<Accordion title="How can I create custom tools for my CrewAI agents?">
    You can create custom tools by subclassing the `BaseTool` class provided by CrewAI or by using the tool decorator. Subclassing involves defining a new class that inherits from `BaseTool`, specifying the name, description, and the `_run` method for operational logic. The tool decorator allows you to create a `Tool` object directly with the required attributes and a functional logic.

<Card href="/en/learn/create-custom-tools" icon="code">CrewAI Tools Guide</Card>
  </Accordion>

<Accordion title="How can you control the maximum number of requests per minute that the entire crew can perform?">
    The `max_rpm` attribute sets the maximum number of requests per minute the crew can perform to avoid rate limits and will override individual agents' `max_rpm` settings if you set it.
  </Accordion>
</AccordionGroup>

**Examples:**

Example 1 (unknown):
```unknown
</Step>

      <Step title="Create a task with Output Pydantic">
```

Example 2 (unknown):
```unknown
</Step>

      <Step title="Set the output_pydantic attribute in your agent">
```

---

## Flows

**URL:** llms-txt#flows

**Contents:**
- Overview
- Getting Started
  - @start()
  - @listen()
  - Flow Output
- Flow State Management
  - Unstructured State Management
  - Structured State Management
  - Choosing Between Unstructured and Structured State Management
- Flow Persistence

Source: https://docs.crewai.com/en/concepts/flows

Learn how to create and manage AI workflows using CrewAI Flows.

CrewAI Flows is a powerful feature designed to streamline the creation and management of AI workflows. Flows allow developers to combine and coordinate coding tasks and Crews efficiently, providing a robust framework for building sophisticated AI automations.

Flows allow you to create structured, event-driven workflows. They provide a seamless way to connect multiple tasks, manage state, and control the flow of execution in your AI applications. With Flows, you can easily design and implement multi-step processes that leverage the full potential of CrewAI's capabilities.

1. **Simplified Workflow Creation**: Easily chain together multiple Crews and tasks to create complex AI workflows.

2. **State Management**: Flows make it super easy to manage and share state between different tasks in your workflow.

3. **Event-Driven Architecture**: Built on an event-driven model, allowing for dynamic and responsive workflows.

4. **Flexible Control Flow**: Implement conditional logic, loops, and branching within your workflows.

Let's create a simple Flow where you will use OpenAI to generate a random city in one task and then use that city to generate a fun fact in another task.

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=18b381277b7b017abf7cb19bc5e03923" alt="Flow Visual image" data-og-width="1913" width="1913" data-og-height="989" height="989" data-path="images/crewai-flow-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=78864d97e0fc7f225a5313c9fb650900 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d87938c680e7aa201798075fe19dcf8 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=36448790f7ca45e69ffdd3ceb2b2e713 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4d10a3f4f9ea1c9b0428fbb66f0fca17 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=928a75232235b73e9308d4d9cfeaf0e8 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=fa7022034285d0022ff07f97f6b675f7 2500w" />
In the above example, we have created a simple Flow that generates a random city using OpenAI and then generates a fun fact about that city. The Flow consists of two tasks: `generate_city` and `generate_fun_fact`. The `generate_city` task is the starting point of the Flow, and the `generate_fun_fact` task listens for the output of the `generate_city` task.

Each Flow instance automatically receives a unique identifier (UUID) in its state, which helps track and manage flow executions. The state can also store additional data (like the generated city and fun fact) that persists throughout the flow's execution.

When you run the Flow, it will:

1. Generate a unique ID for the flow state
2. Generate a random city and store it in the state
3. Generate a fun fact about that city and store it in the state
4. Print the results to the console

The state's unique ID and stored data can be useful for tracking flow executions and maintaining context between tasks.

**Note:** Ensure you have set up your `.env` file to store your `OPENAI_API_KEY`. This key is necessary for authenticating requests to the OpenAI API.

The `@start()` decorator marks entry points for a Flow. You can:

* Declare multiple unconditional starts: `@start()`
* Gate a start on a prior method or router label: `@start("method_or_label")`
* Provide a callable condition to control when a start should fire

All satisfied `@start()` methods will execute (often in parallel) when the Flow begins or resumes.

The `@listen()` decorator is used to mark a method as a listener for the output of another task in the Flow. The method decorated with `@listen()` will be executed when the specified task emits an output. The method can access the output of the task it is listening to as an argument.

The `@listen()` decorator can be used in several ways:

1. **Listening to a Method by Name**: You can pass the name of the method you want to listen to as a string. When that method completes, the listener method will be triggered.

2. **Listening to a Method Directly**: You can pass the method itself. When that method completes, the listener method will be triggered.

Accessing and handling the output of a Flow is essential for integrating your AI workflows into larger applications or systems. CrewAI Flows provide straightforward mechanisms to retrieve the final output, access intermediate results, and manage the overall state of your Flow.

#### Retrieving the Final Output

When you run a Flow, the final output is determined by the last method that completes. The `kickoff()` method returns the output of this final method.

Here's how you can access the final output:

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d987994d2c99a06a3cf149c71831fd5" alt="Flow Visual image" data-og-width="2015" width="2015" data-og-height="1040" height="1040" data-path="images/crewai-flow-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e6b4e913cd2d4bf4dc67bdcb2e59cceb 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=245303e4f6e5bc30819aa9357561e7b3 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=32155410f336267e29c64407e22ae57e 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5dc414bc338e0475ae40aa3eedea0bd8 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cfdf47937eb1f0a1f7e9ffdaab866e5a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ef7d71c39b8ea4ad865c514420df28d1 2500w" />

In this example, the `second_method` is the last method to complete, so its output will be the final output of the Flow.
The `kickoff()` method will return the final output, which is then printed to the console. The `plot()` method will generate the HTML file, which will help you understand the flow.

#### Accessing and Updating State

In addition to retrieving the final output, you can also access and update the state within your Flow. The state can be used to store and share data between different methods in the Flow. After the Flow has run, you can access the state to retrieve any information that was added or updated during the execution.

Here's an example of how to update and access the state:

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d987994d2c99a06a3cf149c71831fd5" alt="Flow Visual image" data-og-width="2015" width="2015" data-og-height="1040" height="1040" data-path="images/crewai-flow-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e6b4e913cd2d4bf4dc67bdcb2e59cceb 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=245303e4f6e5bc30819aa9357561e7b3 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=32155410f336267e29c64407e22ae57e 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5dc414bc338e0475ae40aa3eedea0bd8 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cfdf47937eb1f0a1f7e9ffdaab866e5a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ef7d71c39b8ea4ad865c514420df28d1 2500w" />

In this example, the state is updated by both `first_method` and `second_method`.
After the Flow has run, you can access the final state to see the updates made by these methods.

By ensuring that the final method's output is returned and providing access to the state, CrewAI Flows make it easy to integrate the results of your AI workflows into larger applications or systems,
while also maintaining and accessing the state throughout the Flow's execution.

## Flow State Management

Managing state effectively is crucial for building reliable and maintainable AI workflows. CrewAI Flows provides robust mechanisms for both unstructured and structured state management,
allowing developers to choose the approach that best fits their application's needs.

### Unstructured State Management

In unstructured state management, all state is stored in the `state` attribute of the `Flow` class.
This approach offers flexibility, enabling developers to add or modify state attributes on the fly without defining a strict schema.
Even with unstructured states, CrewAI Flows automatically generates and maintains a unique identifier (UUID) for each state instance.

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1d64a80a490430f29b7fa1085a3062c4" alt="Flow Visual image" data-og-width="1974" width="1974" data-og-height="1058" height="1058" data-path="images/crewai-flow-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=192f7a8605d3a5c12b6b61aa4a23917f 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f41cbc9a268ba4bbb466fa2e2a1c2c1e 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4d2315a6e69d8125e7e144f04180529f 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=02eb5ffde3ef5936b2cf172160c72f72 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3fc5bb51802a4a5d641834e19d24e565 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=85414106ada4d15dcb7bccc086194b84 2500w" />

**Note:** The `id` field is automatically generated and preserved throughout the flow's execution. You don't need to manage or set it manually, and it will be maintained even when updating the state with new data.

* **Flexibility:** You can dynamically add attributes to `self.state` without predefined constraints.
* **Simplicity:** Ideal for straightforward workflows where state structure is minimal or varies significantly.

### Structured State Management

Structured state management leverages predefined schemas to ensure consistency and type safety across the workflow.
By using models like Pydantic's `BaseModel`, developers can define the exact shape of the state, enabling better validation and auto-completion in development environments.

Each state in CrewAI Flows automatically receives a unique identifier (UUID) to help track and manage state instances. This ID is automatically generated and managed by the Flow system.

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1d64a80a490430f29b7fa1085a3062c4" alt="Flow Visual image" data-og-width="1974" width="1974" data-og-height="1058" height="1058" data-path="images/crewai-flow-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=192f7a8605d3a5c12b6b61aa4a23917f 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f41cbc9a268ba4bbb466fa2e2a1c2c1e 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4d2315a6e69d8125e7e144f04180529f 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=02eb5ffde3ef5936b2cf172160c72f72 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3fc5bb51802a4a5d641834e19d24e565 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=85414106ada4d15dcb7bccc086194b84 2500w" />

* **Defined Schema:** `ExampleState` clearly outlines the state structure, enhancing code readability and maintainability.
* **Type Safety:** Leveraging Pydantic ensures that state attributes adhere to the specified types, reducing runtime errors.
* **Auto-Completion:** IDEs can provide better auto-completion and error checking based on the defined state model.

### Choosing Between Unstructured and Structured State Management

* **Use Unstructured State Management when:**

* The workflow's state is simple or highly dynamic.
  * Flexibility is prioritized over strict state definitions.
  * Rapid prototyping is required without the overhead of defining schemas.

* **Use Structured State Management when:**
  * The workflow requires a well-defined and consistent state structure.
  * Type safety and validation are important for your application's reliability.
  * You want to leverage IDE features like auto-completion and type checking for better developer experience.

By providing both unstructured and structured state management options, CrewAI Flows empowers developers to build AI workflows that are both flexible and robust, catering to a wide range of application requirements.

The @persist decorator enables automatic state persistence in CrewAI Flows, allowing you to maintain flow state across restarts or different workflow executions. This decorator can be applied at either the class level or method level, providing flexibility in how you manage state persistence.

### Class-Level Persistence

When applied at the class level, the @persist decorator automatically persists all flow method states:

### Method-Level Persistence

For more granular control, you can apply @persist to specific methods:

1. **Unique State Identification**
   * Each flow state automatically receives a unique UUID
   * The ID is preserved across state updates and method calls
   * Supports both structured (Pydantic BaseModel) and unstructured (dictionary) states

2. **Default SQLite Backend**
   * SQLiteFlowPersistence is the default storage backend
   * States are automatically saved to a local SQLite database
   * Robust error handling ensures clear messages if database operations fail

3. **Error Handling**
   * Comprehensive error messages for database operations
   * Automatic state validation during save and load
   * Clear feedback when persistence operations encounter issues

### Important Considerations

* **State Types**: Both structured (Pydantic BaseModel) and unstructured (dictionary) states are supported
* **Automatic ID**: The `id` field is automatically added if not present
* **State Recovery**: Failed or restarted flows can automatically reload their previous state
* **Custom Implementation**: You can provide your own FlowPersistence implementation for specialized storage needs

### Technical Advantages

1. **Precise Control Through Low-Level Access**
   * Direct access to persistence operations for advanced use cases
   * Fine-grained control via method-level persistence decorators
   * Built-in state inspection and debugging capabilities
   * Full visibility into state changes and persistence operations

2. **Enhanced Reliability**
   * Automatic state recovery after system failures or restarts
   * Transaction-based state updates for data integrity
   * Comprehensive error handling with clear error messages
   * Robust validation during state save and load operations

3. **Extensible Architecture**
   * Customizable persistence backend through FlowPersistence interface
   * Support for specialized storage solutions beyond SQLite
   * Compatible with both structured (Pydantic) and unstructured (dict) states
   * Seamless integration with existing CrewAI flow patterns

The persistence system's architecture emphasizes technical precision and customization options, allowing developers to maintain full control over state management while benefiting from built-in reliability features.

### Conditional Logic: `or`

The `or_` function in Flows allows you to listen to multiple methods and trigger the listener method when any of the specified methods emit an output.

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=88ce9c9f10781b835f170847bc541a13" alt="Flow Visual image" data-og-width="2026" width="2026" data-og-height="1016" height="1016" data-path="images/crewai-flow-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=796ce622251faa461b481eb5d7cdcf70 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=260fcd89a5b3a6a42a25dd4f41e7c5c6 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b9268adb3abef93c7cce693a424a78ba 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=75f3ad392bfd6b72bd29d701675899d6 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=dd771250338648e1f22c1463cb8e2ff0 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b8e6fd63ec2ba23d9fa4f1dc2fd87143 2500w" />

When you run this Flow, the `logger` method will be triggered by the output of either the `start_method` or the `second_method`.
The `or_` function is used to listen to multiple methods and trigger the listener method when any of the specified methods emit an output.

### Conditional Logic: `and`

The `and_` function in Flows allows you to listen to multiple methods and trigger the listener method only when all the specified methods emit an output.

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=104318219be9d3502ac57ebb513aded7" alt="Flow Visual image" data-og-width="2062" width="2062" data-og-height="987" height="987" data-path="images/crewai-flow-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6e9cb9d2b1ec2cb2aee2df008d3696c9 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=07cbcc6de6e8c8ae5da6c02a6fe4b457 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=afc6aad8f7276be4918527e553b5aa81 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e026919d9dff7ce0b0e592f4f2c0c4fd 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=03ea50c8681de2b8ea8cada6c0150e2c 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=61f9c7b0aceb69df6346ab2af321b779 2500w" />

When you run this Flow, the `logger` method will be triggered only when both the `start_method` and the `second_method` emit an output.
The `and_` function is used to listen to multiple methods and trigger the listener method only when all the specified methods emit an output.

The `@router()` decorator in Flows allows you to define conditional routing logic based on the output of a method.
You can specify different routes based on the output of the method, allowing you to control the flow of execution dynamically.

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f8cad73f073b4e936ef68d88545f1777" alt="Flow Visual image" data-og-width="1951" width="1951" data-og-height="1101" height="1101" data-path="images/crewai-flow-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9a8462f42a9d9e14748d35312553ec6c 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=78e66eabae15099e2ef1d0c314d3cb04 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a144377de810ed24f1d1aed1ba54d2d7 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=2b17ebb2dd4eee4d086a8d0126a36c0d 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4536b83aa7ff7e897f1193709ace944f 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3b89cff817f7b4d05338f4a3a028f974 2500w" />

In the above example, the `start_method` generates a random boolean value and sets it in the state.
The `second_method` uses the `@router()` decorator to define conditional routing logic based on the value of the boolean.
If the boolean is `True`, the method returns `"success"`, and if it is `False`, the method returns `"failed"`.
The `third_method` and `fourth_method` listen to the output of the `second_method` and execute based on the returned value.

When you run this Flow, the output will change based on the random boolean value generated by the `start_method`.

## Adding Agents to Flows

Agents can be seamlessly integrated into your flows, providing a lightweight alternative to full Crews when you need simpler, focused task execution. Here's an example of how to use an Agent within a flow to perform market research:

```python  theme={null}
import asyncio
from typing import Any, Dict, List

from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field

from crewai.agent import Agent
from crewai.flow.flow import Flow, listen, start

**Examples:**

Example 1 (unknown):
```unknown
<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=18b381277b7b017abf7cb19bc5e03923" alt="Flow Visual image" data-og-width="1913" width="1913" data-og-height="989" height="989" data-path="images/crewai-flow-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=78864d97e0fc7f225a5313c9fb650900 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d87938c680e7aa201798075fe19dcf8 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=36448790f7ca45e69ffdd3ceb2b2e713 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4d10a3f4f9ea1c9b0428fbb66f0fca17 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=928a75232235b73e9308d4d9cfeaf0e8 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=fa7022034285d0022ff07f97f6b675f7 2500w" />
In the above example, we have created a simple Flow that generates a random city using OpenAI and then generates a fun fact about that city. The Flow consists of two tasks: `generate_city` and `generate_fun_fact`. The `generate_city` task is the starting point of the Flow, and the `generate_fun_fact` task listens for the output of the `generate_city` task.

Each Flow instance automatically receives a unique identifier (UUID) in its state, which helps track and manage flow executions. The state can also store additional data (like the generated city and fun fact) that persists throughout the flow's execution.

When you run the Flow, it will:

1. Generate a unique ID for the flow state
2. Generate a random city and store it in the state
3. Generate a fun fact about that city and store it in the state
4. Print the results to the console

The state's unique ID and stored data can be useful for tracking flow executions and maintaining context between tasks.

**Note:** Ensure you have set up your `.env` file to store your `OPENAI_API_KEY`. This key is necessary for authenticating requests to the OpenAI API.

### @start()

The `@start()` decorator marks entry points for a Flow. You can:

* Declare multiple unconditional starts: `@start()`
* Gate a start on a prior method or router label: `@start("method_or_label")`
* Provide a callable condition to control when a start should fire

All satisfied `@start()` methods will execute (often in parallel) when the Flow begins or resumes.

### @listen()

The `@listen()` decorator is used to mark a method as a listener for the output of another task in the Flow. The method decorated with `@listen()` will be executed when the specified task emits an output. The method can access the output of the task it is listening to as an argument.

#### Usage

The `@listen()` decorator can be used in several ways:

1. **Listening to a Method by Name**: You can pass the name of the method you want to listen to as a string. When that method completes, the listener method will be triggered.
```

Example 2 (unknown):
```unknown
2. **Listening to a Method Directly**: You can pass the method itself. When that method completes, the listener method will be triggered.
```

Example 3 (unknown):
```unknown
### Flow Output

Accessing and handling the output of a Flow is essential for integrating your AI workflows into larger applications or systems. CrewAI Flows provide straightforward mechanisms to retrieve the final output, access intermediate results, and manage the overall state of your Flow.

#### Retrieving the Final Output

When you run a Flow, the final output is determined by the last method that completes. The `kickoff()` method returns the output of this final method.

Here's how you can access the final output:

<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## Form the crew and kick it off

**URL:** llms-txt#form-the-crew-and-kick-it-off

**Contents:**
- Configuration Options
- Advanced Usage

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=2
)

result = crew.kickoff()
print(result)
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## Configuration Options

The `TavilySearchTool` accepts the following arguments during initialization or when calling the `run` method:

* `query` (str): **Required**. The search query string.
* `search_depth` (Literal\["basic", "advanced"], optional): The depth of the search. Defaults to `"basic"`.
* `topic` (Literal\["general", "news", "finance"], optional): The topic to focus the search on. Defaults to `"general"`.
* `time_range` (Literal\["day", "week", "month", "year"], optional): The time range for the search. Defaults to `None`.
* `days` (int, optional): The number of days to search back. Relevant if `time_range` is not set. Defaults to `7`.
* `max_results` (int, optional): The maximum number of search results to return. Defaults to `5`.
* `include_domains` (Sequence\[str], optional): A list of domains to prioritize in the search. Defaults to `None`.
* `exclude_domains` (Sequence\[str], optional): A list of domains to exclude from the search. Defaults to `None`.
* `include_answer` (Union\[bool, Literal\["basic", "advanced"]], optional): Whether to include a direct answer synthesized from the search results. Defaults to `False`.
* `include_raw_content` (bool, optional): Whether to include the raw HTML content of the searched pages. Defaults to `False`.
* `include_images` (bool, optional): Whether to include image results. Defaults to `False`.
* `timeout` (int, optional): The request timeout in seconds. Defaults to `60`.

## Advanced Usage

You can configure the tool with custom parameters:
```

---

## Form the crew with a sequential process

**URL:** llms-txt#form-the-crew-with-a-sequential-process

report_crew = Crew(
  agents=[researcher, analyst, writer],
  tasks=[research_task, analysis_task, writing_task],
  process=Process.sequential
)

---

## For complex reasoning tasks

**URL:** llms-txt#for-complex-reasoning-tasks

analyst:
  role: "Data Insights Analyst"
  goal: "..."
  backstory: "..."
  llm: openai/gpt-4o

---

## Google Calendar Integration

**URL:** llms-txt#google-calendar-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Google Calendar Integration
  - 1. Connect Your Google Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Calendar Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/google_calendar

Event and schedule management with Google Calendar integration for CrewAI.

Enable your agents to manage calendar events, schedules, and availability through Google Calendar. Create and update events, manage attendees, check availability, and streamline your scheduling workflows with AI-powered automation.

Before using the Google Calendar integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Google account with Google Calendar access
* Connected your Google account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Google Calendar Integration

### 1. Connect Your Google Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Google Calendar** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for calendar access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="google_calendar/get_availability">
    **Description:** Get calendar availability (free/busy information).

* `timeMin` (string, required): Start time (RFC3339 format)
    * `timeMax` (string, required): End time (RFC3339 format)
    * `items` (array, required): Calendar IDs to check
      
    * `timeZone` (string, optional): Time zone used in the response. The default is UTC.
    * `groupExpansionMax` (integer, optional): Maximal number of calendar identifiers to be provided for a single group. Maximum: 100
    * `calendarExpansionMax` (integer, optional): Maximal number of calendars for which FreeBusy information is to be provided. Maximum: 50
  </Accordion>

<Accordion title="google_calendar/create_event">
    **Description:** Create a new event in the specified calendar.

* `calendarId` (string, required): Calendar ID (use 'primary' for main calendar)
    * `summary` (string, required): Event title/summary
    * `start_dateTime` (string, required): Start time in RFC3339 format (e.g., 2024-01-20T10:00:00-07:00)
    * `end_dateTime` (string, required): End time in RFC3339 format
    * `description` (string, optional): Event description
    * `timeZone` (string, optional): Time zone (e.g., America/Los\_Angeles)
    * `location` (string, optional): Geographic location of the event as free-form text.
    * `attendees` (array, optional): List of attendees for the event.
      
    * `reminders` (object, optional): Information about the event's reminders.
      
    * `conferenceData` (object, optional): The conference-related information, such as details of a Google Meet conference.
      
    * `visibility` (string, optional): Visibility of the event. Options: default, public, private, confidential. Default: default
    * `transparency` (string, optional): Whether the event blocks time on the calendar. Options: opaque, transparent. Default: opaque
  </Accordion>

<Accordion title="google_calendar/view_events">
    **Description:** Retrieve events for the specified calendar.

* `calendarId` (string, required): Calendar ID (use 'primary' for main calendar)
    * `timeMin` (string, optional): Lower bound for events (RFC3339)
    * `timeMax` (string, optional): Upper bound for events (RFC3339)
    * `maxResults` (integer, optional): Maximum number of events (default 10). Minimum: 1, Maximum: 2500
    * `orderBy` (string, optional): The order of the events returned in the result. Options: startTime, updated. Default: startTime
    * `singleEvents` (boolean, optional): Whether to expand recurring events into instances and only return single one-off events and instances of recurring events. Default: true
    * `showDeleted` (boolean, optional): Whether to include deleted events (with status equals cancelled) in the result. Default: false
    * `showHiddenInvitations` (boolean, optional): Whether to include hidden invitations in the result. Default: false
    * `q` (string, optional): Free text search terms to find events that match these terms in any field.
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `timeZone` (string, optional): Time zone used in the response.
    * `updatedMin` (string, optional): Lower bound for an event's last modification time (RFC3339) to filter by.
    * `iCalUID` (string, optional): Specifies an event ID in the iCalendar format to be provided in the response.
  </Accordion>

<Accordion title="google_calendar/update_event">
    **Description:** Update an existing event.

* `calendarId` (string, required): Calendar ID
    * `eventId` (string, required): Event ID to update
    * `summary` (string, optional): Updated event title
    * `description` (string, optional): Updated event description
    * `start_dateTime` (string, optional): Updated start time
    * `end_dateTime` (string, optional): Updated end time
  </Accordion>

<Accordion title="google_calendar/delete_event">
    **Description:** Delete a specified event.

* `calendarId` (string, required): Calendar ID
    * `eventId` (string, required): Event ID to delete
  </Accordion>

<Accordion title="google_calendar/view_calendar_list">
    **Description:** Retrieve user's calendar list.

* `maxResults` (integer, optional): Maximum number of entries returned on one result page. Minimum: 1
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `showDeleted` (boolean, optional): Whether to include deleted calendar list entries in the result. Default: false
    * `showHidden` (boolean, optional): Whether to show hidden entries. Default: false
    * `minAccessRole` (string, optional): The minimum access role for the user in the returned entries. Options: freeBusyReader, owner, reader, writer
  </Accordion>
</AccordionGroup>

### Basic Calendar Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="google_calendar/get_availability">
    **Description:** Get calendar availability (free/busy information).

    **Parameters:**

    * `timeMin` (string, required): Start time (RFC3339 format)
    * `timeMax` (string, required): End time (RFC3339 format)
    * `items` (array, required): Calendar IDs to check
```

Example 4 (unknown):
```unknown
* `timeZone` (string, optional): Time zone used in the response. The default is UTC.
    * `groupExpansionMax` (integer, optional): Maximal number of calendar identifiers to be provided for a single group. Maximum: 100
    * `calendarExpansionMax` (integer, optional): Maximal number of calendars for which FreeBusy information is to be provided. Maximum: 50
  </Accordion>

  <Accordion title="google_calendar/create_event">
    **Description:** Create a new event in the specified calendar.

    **Parameters:**

    * `calendarId` (string, required): Calendar ID (use 'primary' for main calendar)
    * `summary` (string, required): Event title/summary
    * `start_dateTime` (string, required): Start time in RFC3339 format (e.g., 2024-01-20T10:00:00-07:00)
    * `end_dateTime` (string, required): End time in RFC3339 format
    * `description` (string, optional): Event description
    * `timeZone` (string, optional): Time zone (e.g., America/Los\_Angeles)
    * `location` (string, optional): Geographic location of the event as free-form text.
    * `attendees` (array, optional): List of attendees for the event.
```

---

## Google Docs Integration

**URL:** llms-txt#google-docs-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Google Docs Integration
  - 1. Connect Your Google Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Google Docs Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/google_docs

Document creation and editing with Google Docs integration for CrewAI.

Enable your agents to create, edit, and manage Google Docs documents with text manipulation and formatting. Automate document creation, insert and replace text, manage content ranges, and streamline your document workflows with AI-powered automation.

Before using the Google Docs integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Google account with Google Docs access
* Connected your Google account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Google Docs Integration

### 1. Connect Your Google Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Google Docs** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for document access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="google_docs/create_document">
    **Description:** Create a new Google Document.

* `title` (string, optional): The title for the new document.
  </Accordion>

<Accordion title="google_docs/get_document">
    **Description:** Get the contents and metadata of a Google Document.

* `documentId` (string, required): The ID of the document to retrieve.
    * `includeTabsContent` (boolean, optional): Whether to include tab content. Default is `false`.
    * `suggestionsViewMode` (string, optional): The suggestions view mode to apply to the document. Enum: `DEFAULT_FOR_CURRENT_ACCESS`, `PREVIEW_SUGGESTIONS_ACCEPTED`, `PREVIEW_WITHOUT_SUGGESTIONS`. Default is `DEFAULT_FOR_CURRENT_ACCESS`.
  </Accordion>

<Accordion title="google_docs/batch_update">
    **Description:** Apply one or more updates to a Google Document.

* `documentId` (string, required): The ID of the document to update.
    * `requests` (array, required): A list of updates to apply to the document. Each item is an object representing a request.
    * `writeControl` (object, optional): Provides control over how write requests are executed. Contains `requiredRevisionId` (string) and `targetRevisionId` (string).
  </Accordion>

<Accordion title="google_docs/insert_text">
    **Description:** Insert text into a Google Document at a specific location.

* `documentId` (string, required): The ID of the document to update.
    * `text` (string, required): The text to insert.
    * `index` (integer, optional): The zero-based index where to insert the text. Default is `1`.
  </Accordion>

<Accordion title="google_docs/replace_text">
    **Description:** Replace all instances of text in a Google Document.

* `documentId` (string, required): The ID of the document to update.
    * `containsText` (string, required): The text to find and replace.
    * `replaceText` (string, required): The text to replace it with.
    * `matchCase` (boolean, optional): Whether the search should respect case. Default is `false`.
  </Accordion>

<Accordion title="google_docs/delete_content_range">
    **Description:** Delete content from a specific range in a Google Document.

* `documentId` (string, required): The ID of the document to update.
    * `startIndex` (integer, required): The start index of the range to delete.
    * `endIndex` (integer, required): The end index of the range to delete.
  </Accordion>

<Accordion title="google_docs/insert_page_break">
    **Description:** Insert a page break at a specific location in a Google Document.

* `documentId` (string, required): The ID of the document to update.
    * `index` (integer, optional): The zero-based index where to insert the page break. Default is `1`.
  </Accordion>

<Accordion title="google_docs/create_named_range">
    **Description:** Create a named range in a Google Document.

* `documentId` (string, required): The ID of the document to update.
    * `name` (string, required): The name for the named range.
    * `startIndex` (integer, required): The start index of the range.
    * `endIndex` (integer, required): The end index of the range.
  </Accordion>
</AccordionGroup>

### Basic Google Docs Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="google_docs/create_document">
    **Description:** Create a new Google Document.

    **Parameters:**

    * `title` (string, optional): The title for the new document.
  </Accordion>

  <Accordion title="google_docs/get_document">
    **Description:** Get the contents and metadata of a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to retrieve.
    * `includeTabsContent` (boolean, optional): Whether to include tab content. Default is `false`.
    * `suggestionsViewMode` (string, optional): The suggestions view mode to apply to the document. Enum: `DEFAULT_FOR_CURRENT_ACCESS`, `PREVIEW_SUGGESTIONS_ACCEPTED`, `PREVIEW_WITHOUT_SUGGESTIONS`. Default is `DEFAULT_FOR_CURRENT_ACCESS`.
  </Accordion>

  <Accordion title="google_docs/batch_update">
    **Description:** Apply one or more updates to a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `requests` (array, required): A list of updates to apply to the document. Each item is an object representing a request.
    * `writeControl` (object, optional): Provides control over how write requests are executed. Contains `requiredRevisionId` (string) and `targetRevisionId` (string).
  </Accordion>

  <Accordion title="google_docs/insert_text">
    **Description:** Insert text into a Google Document at a specific location.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `text` (string, required): The text to insert.
    * `index` (integer, optional): The zero-based index where to insert the text. Default is `1`.
  </Accordion>

  <Accordion title="google_docs/replace_text">
    **Description:** Replace all instances of text in a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `containsText` (string, required): The text to find and replace.
    * `replaceText` (string, required): The text to replace it with.
    * `matchCase` (boolean, optional): Whether the search should respect case. Default is `false`.
  </Accordion>

  <Accordion title="google_docs/delete_content_range">
    **Description:** Delete content from a specific range in a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `startIndex` (integer, required): The start index of the range to delete.
    * `endIndex` (integer, required): The end index of the range to delete.
  </Accordion>

  <Accordion title="google_docs/insert_page_break">
    **Description:** Insert a page break at a specific location in a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `index` (integer, optional): The zero-based index where to insert the page break. Default is `1`.
  </Accordion>

  <Accordion title="google_docs/create_named_range">
    **Description:** Create a named range in a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `name` (string, required): The name for the named range.
    * `startIndex` (integer, required): The start index of the range.
    * `endIndex` (integer, required): The end index of the range.
  </Accordion>
</AccordionGroup>

## Usage Examples

### Basic Google Docs Agent Setup
```

---

## Google Drive Integration

**URL:** llms-txt#google-drive-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Google Drive Integration
  - 1. Connect Your Google Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Google Drive Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/google_drive

File storage and management with Google Drive integration for CrewAI.

Enable your agents to manage files and folders through Google Drive. Upload, download, organize, and share files, create folders, and streamline your document management workflows with AI-powered automation.

Before using the Google Drive integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Google account with Google Drive access
* Connected your Google account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Google Drive Integration

### 1. Connect Your Google Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Google Drive** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for file and folder management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="google_drive/get_file">
    **Description:** Get a file by ID from Google Drive.

* `file_id` (string, required): The ID of the file to retrieve.
  </Accordion>

<Accordion title="google_drive/list_files">
    **Description:** List files in Google Drive.

* `q` (string, optional): Query string to filter files (example: "name contains 'report'").
    * `page_size` (integer, optional): Maximum number of files to return (default: 100, max: 1000).
    * `page_token` (string, optional): Token for retrieving the next page of results.
    * `order_by` (string, optional): Sort order (example: "name", "createdTime desc", "modifiedTime").
    * `spaces` (string, optional): Comma-separated list of spaces to query (drive, appDataFolder, photos).
  </Accordion>

<Accordion title="google_drive/upload_file">
    **Description:** Upload a file to Google Drive.

* `name` (string, required): Name of the file to create.
    * `content` (string, required): Content of the file to upload.
    * `mime_type` (string, optional): MIME type of the file (example: "text/plain", "application/pdf").
    * `parent_folder_id` (string, optional): ID of the parent folder where the file should be created.
    * `description` (string, optional): Description of the file.
  </Accordion>

<Accordion title="google_drive/download_file">
    **Description:** Download a file from Google Drive.

* `file_id` (string, required): The ID of the file to download.
    * `mime_type` (string, optional): MIME type for export (required for Google Workspace documents).
  </Accordion>

<Accordion title="google_drive/create_folder">
    **Description:** Create a new folder in Google Drive.

* `name` (string, required): Name of the folder to create.
    * `parent_folder_id` (string, optional): ID of the parent folder where the new folder should be created.
    * `description` (string, optional): Description of the folder.
  </Accordion>

<Accordion title="google_drive/delete_file">
    **Description:** Delete a file from Google Drive.

* `file_id` (string, required): The ID of the file to delete.
  </Accordion>

<Accordion title="google_drive/share_file">
    **Description:** Share a file in Google Drive with specific users or make it public.

* `file_id` (string, required): The ID of the file to share.
    * `role` (string, required): The role granted by this permission (reader, writer, commenter, owner).
    * `type` (string, required): The type of the grantee (user, group, domain, anyone).
    * `email_address` (string, optional): The email address of the user or group to share with (required for user/group types).
    * `domain` (string, optional): The domain to share with (required for domain type).
    * `send_notification_email` (boolean, optional): Whether to send a notification email (default: true).
    * `email_message` (string, optional): A plain text custom message to include in the notification email.
  </Accordion>

<Accordion title="google_drive/update_file">
    **Description:** Update an existing file in Google Drive.

* `file_id` (string, required): The ID of the file to update.
    * `name` (string, optional): New name for the file.
    * `content` (string, optional): New content for the file.
    * `mime_type` (string, optional): New MIME type for the file.
    * `description` (string, optional): New description for the file.
    * `add_parents` (string, optional): Comma-separated list of parent folder IDs to add.
    * `remove_parents` (string, optional): Comma-separated list of parent folder IDs to remove.
  </Accordion>
</AccordionGroup>

### Basic Google Drive Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="google_drive/get_file">
    **Description:** Get a file by ID from Google Drive.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to retrieve.
  </Accordion>

  <Accordion title="google_drive/list_files">
    **Description:** List files in Google Drive.

    **Parameters:**

    * `q` (string, optional): Query string to filter files (example: "name contains 'report'").
    * `page_size` (integer, optional): Maximum number of files to return (default: 100, max: 1000).
    * `page_token` (string, optional): Token for retrieving the next page of results.
    * `order_by` (string, optional): Sort order (example: "name", "createdTime desc", "modifiedTime").
    * `spaces` (string, optional): Comma-separated list of spaces to query (drive, appDataFolder, photos).
  </Accordion>

  <Accordion title="google_drive/upload_file">
    **Description:** Upload a file to Google Drive.

    **Parameters:**

    * `name` (string, required): Name of the file to create.
    * `content` (string, required): Content of the file to upload.
    * `mime_type` (string, optional): MIME type of the file (example: "text/plain", "application/pdf").
    * `parent_folder_id` (string, optional): ID of the parent folder where the file should be created.
    * `description` (string, optional): Description of the file.
  </Accordion>

  <Accordion title="google_drive/download_file">
    **Description:** Download a file from Google Drive.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to download.
    * `mime_type` (string, optional): MIME type for export (required for Google Workspace documents).
  </Accordion>

  <Accordion title="google_drive/create_folder">
    **Description:** Create a new folder in Google Drive.

    **Parameters:**

    * `name` (string, required): Name of the folder to create.
    * `parent_folder_id` (string, optional): ID of the parent folder where the new folder should be created.
    * `description` (string, optional): Description of the folder.
  </Accordion>

  <Accordion title="google_drive/delete_file">
    **Description:** Delete a file from Google Drive.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to delete.
  </Accordion>

  <Accordion title="google_drive/share_file">
    **Description:** Share a file in Google Drive with specific users or make it public.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to share.
    * `role` (string, required): The role granted by this permission (reader, writer, commenter, owner).
    * `type` (string, required): The type of the grantee (user, group, domain, anyone).
    * `email_address` (string, optional): The email address of the user or group to share with (required for user/group types).
    * `domain` (string, optional): The domain to share with (required for domain type).
    * `send_notification_email` (boolean, optional): Whether to send a notification email (default: true).
    * `email_message` (string, optional): A plain text custom message to include in the notification email.
  </Accordion>

  <Accordion title="google_drive/update_file">
    **Description:** Update an existing file in Google Drive.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to update.
    * `name` (string, optional): New name for the file.
    * `content` (string, optional): New content for the file.
    * `mime_type` (string, optional): New MIME type for the file.
    * `description` (string, optional): New description for the file.
    * `add_parents` (string, optional): Comma-separated list of parent folder IDs to add.
    * `remove_parents` (string, optional): Comma-separated list of parent folder IDs to remove.
  </Accordion>
</AccordionGroup>

## Usage Examples

### Basic Google Drive Agent Setup
```

---

## Google Drive Trigger

**URL:** llms-txt#google-drive-trigger

**Contents:**
- Overview
- Enabling the Google Drive Trigger
- Example: Summarize file activity
- Testing Locally

Source: https://docs.crewai.com/en/enterprise/guides/google-drive-trigger

Respond to Google Drive file events with automated crews

Trigger your automations when files are created, updated, or removed in Google Drive. Typical workflows include summarizing newly uploaded content, enforcing sharing policies, or notifying owners when critical files change.

<Tip>
  Connect Google Drive in **Tools & Integrations** and confirm the trigger is enabled for the automation you want to monitor.
</Tip>

## Enabling the Google Drive Trigger

1. Open your deployment in CrewAI AOP
2. Go to the **Triggers** tab
3. Locate **Google Drive** and switch the toggle to enable

<Frame>
  <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=caef65990821bbc38454b46ca8f7bc46" alt="Enable or disable triggers with toggle" data-og-width="2208" width="2208" data-og-height="1540" height="1540" data-path="images/enterprise/gdrive-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=26fc4c3542735f7ff2f8723a7bec0265 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=67b08f32c76c711734916902a4df35a3 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=5d0695c5d0f5ebd51d6413c0334a0ce6 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=6b2600ca253c042e06f2108c68d5cff3 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=62541a717c8dee05cee7310561882f58 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=ac92f2d61bf065c81a2ce6f02cac5d9d 2500w" />
</Frame>

## Example: Summarize file activity

The drive example crews parse the payload to extract file metadata, evaluate permissions, and publish a summary.

Test your Google Drive trigger integration locally using the CrewAI CLI:

```bash  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## Testing Locally

Test your Google Drive trigger integration locally using the CrewAI CLI:
```

---

## Google Sheets Integration

**URL:** llms-txt#google-sheets-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Google Sheets Integration
  - 1. Connect Your Google Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Google Sheets Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/google_sheets

Spreadsheet data synchronization with Google Sheets integration for CrewAI.

Enable your agents to manage spreadsheet data through Google Sheets. Read rows, create new entries, update existing data, and streamline your data management workflows with AI-powered automation. Perfect for data tracking, reporting, and collaborative data management.

Before using the Google Sheets integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Google account with Google Sheets access
* Connected your Google account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)
* Spreadsheets with proper column headers for data operations

## Setting Up Google Sheets Integration

### 1. Connect Your Google Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Google Sheets** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for spreadsheet access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="google_sheets/get_spreadsheet">
    **Description:** Retrieve properties and data of a spreadsheet.

* `spreadsheetId` (string, required): The ID of the spreadsheet to retrieve.
    * `ranges` (array, optional): The ranges to retrieve from the spreadsheet.
    * `includeGridData` (boolean, optional): True if grid data should be returned. Default: false
    * `fields` (string, optional): The fields to include in the response. Use this to improve performance by only returning needed data.
  </Accordion>

<Accordion title="google_sheets/get_values">
    **Description:** Returns a range of values from a spreadsheet.

* `spreadsheetId` (string, required): The ID of the spreadsheet to retrieve data from.
    * `range` (string, required): The A1 notation or R1C1 notation of the range to retrieve values from.
    * `valueRenderOption` (string, optional): How values should be represented in the output. Options: FORMATTED\_VALUE, UNFORMATTED\_VALUE, FORMULA. Default: FORMATTED\_VALUE
    * `dateTimeRenderOption` (string, optional): How dates, times, and durations should be represented in the output. Options: SERIAL\_NUMBER, FORMATTED\_STRING. Default: SERIAL\_NUMBER
    * `majorDimension` (string, optional): The major dimension that results should use. Options: ROWS, COLUMNS. Default: ROWS
  </Accordion>

<Accordion title="google_sheets/update_values">
    **Description:** Sets values in a range of a spreadsheet.

* `spreadsheetId` (string, required): The ID of the spreadsheet to update.
    * `range` (string, required): The A1 notation of the range to update.
    * `values` (array, required): The data to be written. Each array represents a row.
      
    * `valueInputOption` (string, optional): How the input data should be interpreted. Options: RAW, USER\_ENTERED. Default: USER\_ENTERED
  </Accordion>

<Accordion title="google_sheets/append_values">
    **Description:** Appends values to a spreadsheet.

* `spreadsheetId` (string, required): The ID of the spreadsheet to update.
    * `range` (string, required): The A1 notation of a range to search for a logical table of data.
    * `values` (array, required): The data to append. Each array represents a row.
      
    * `valueInputOption` (string, optional): How the input data should be interpreted. Options: RAW, USER\_ENTERED. Default: USER\_ENTERED
    * `insertDataOption` (string, optional): How the input data should be inserted. Options: OVERWRITE, INSERT\_ROWS. Default: INSERT\_ROWS
  </Accordion>

<Accordion title="google_sheets/create_spreadsheet">
    **Description:** Creates a new spreadsheet.

* `title` (string, required): The title of the new spreadsheet.
    * `sheets` (array, optional): The sheets that are part of the spreadsheet.
      
  </Accordion>
</AccordionGroup>

### Basic Google Sheets Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="google_sheets/get_spreadsheet">
    **Description:** Retrieve properties and data of a spreadsheet.

    **Parameters:**

    * `spreadsheetId` (string, required): The ID of the spreadsheet to retrieve.
    * `ranges` (array, optional): The ranges to retrieve from the spreadsheet.
    * `includeGridData` (boolean, optional): True if grid data should be returned. Default: false
    * `fields` (string, optional): The fields to include in the response. Use this to improve performance by only returning needed data.
  </Accordion>

  <Accordion title="google_sheets/get_values">
    **Description:** Returns a range of values from a spreadsheet.

    **Parameters:**

    * `spreadsheetId` (string, required): The ID of the spreadsheet to retrieve data from.
    * `range` (string, required): The A1 notation or R1C1 notation of the range to retrieve values from.
    * `valueRenderOption` (string, optional): How values should be represented in the output. Options: FORMATTED\_VALUE, UNFORMATTED\_VALUE, FORMULA. Default: FORMATTED\_VALUE
    * `dateTimeRenderOption` (string, optional): How dates, times, and durations should be represented in the output. Options: SERIAL\_NUMBER, FORMATTED\_STRING. Default: SERIAL\_NUMBER
    * `majorDimension` (string, optional): The major dimension that results should use. Options: ROWS, COLUMNS. Default: ROWS
  </Accordion>

  <Accordion title="google_sheets/update_values">
    **Description:** Sets values in a range of a spreadsheet.

    **Parameters:**

    * `spreadsheetId` (string, required): The ID of the spreadsheet to update.
    * `range` (string, required): The A1 notation of the range to update.
    * `values` (array, required): The data to be written. Each array represents a row.
```

Example 4 (unknown):
```unknown
* `valueInputOption` (string, optional): How the input data should be interpreted. Options: RAW, USER\_ENTERED. Default: USER\_ENTERED
  </Accordion>

  <Accordion title="google_sheets/append_values">
    **Description:** Appends values to a spreadsheet.

    **Parameters:**

    * `spreadsheetId` (string, required): The ID of the spreadsheet to update.
    * `range` (string, required): The A1 notation of a range to search for a logical table of data.
    * `values` (array, required): The data to append. Each array represents a row.
```

---

## Google Slides Integration

**URL:** llms-txt#google-slides-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Google Slides Integration
  - 1. Connect Your Google Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Google Slides Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/google_slides

Presentation creation and management with Google Slides integration for CrewAI.

Enable your agents to create, edit, and manage Google Slides presentations. Create presentations, update content, import data from Google Sheets, manage pages and thumbnails, and streamline your presentation workflows with AI-powered automation.

Before using the Google Slides integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Google account with Google Slides access
* Connected your Google account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Google Slides Integration

### 1. Connect Your Google Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Google Slides** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for presentations, spreadsheets, and drive access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="google_slides/create_blank_presentation">
    **Description:** Creates a blank presentation with no content.

* `title` (string, required): The title of the presentation.
  </Accordion>

<Accordion title="google_slides/get_presentation">
    **Description:** Retrieves a presentation by ID.

* `presentationId` (string, required): The ID of the presentation to retrieve.
    * `fields` (string, optional): The fields to include in the response. Use this to improve performance by only returning needed data.
  </Accordion>

<Accordion title="google_slides/batch_update_presentation">
    **Description:** Applies updates, add content, or remove content from a presentation.

* `presentationId` (string, required): The ID of the presentation to update.
    * `requests` (array, required): A list of updates to apply to the presentation.
      
    * `writeControl` (object, optional): Provides control over how write requests are executed.
      
  </Accordion>

<Accordion title="google_slides/get_page">
    **Description:** Retrieves a specific page by its ID.

* `presentationId` (string, required): The ID of the presentation.
    * `pageObjectId` (string, required): The ID of the page to retrieve.
  </Accordion>

<Accordion title="google_slides/get_thumbnail">
    **Description:** Generates a page thumbnail.

* `presentationId` (string, required): The ID of the presentation.
    * `pageObjectId` (string, required): The ID of the page for thumbnail generation.
  </Accordion>

<Accordion title="google_slides/import_data_from_sheet">
    **Description:** Imports data from a Google Sheet into a presentation.

* `presentationId` (string, required): The ID of the presentation.
    * `sheetId` (string, required): The ID of the Google Sheet to import from.
    * `dataRange` (string, required): The range of data to import from the sheet.
  </Accordion>

<Accordion title="google_slides/upload_file_to_drive">
    **Description:** Uploads a file to Google Drive associated with the presentation.

* `file` (string, required): The file data to upload.
    * `presentationId` (string, required): The ID of the presentation to link the uploaded file.
  </Accordion>

<Accordion title="google_slides/link_file_to_presentation">
    **Description:** Links a file in Google Drive to a presentation.

* `presentationId` (string, required): The ID of the presentation.
    * `fileId` (string, required): The ID of the file to link.
  </Accordion>

<Accordion title="google_slides/get_all_presentations">
    **Description:** Lists all presentations accessible to the user.

* `pageSize` (integer, optional): The number of presentations to return per page.
    * `pageToken` (string, optional): A token for pagination.
  </Accordion>

<Accordion title="google_slides/delete_presentation">
    **Description:** Deletes a presentation by ID.

* `presentationId` (string, required): The ID of the presentation to delete.
  </Accordion>
</AccordionGroup>

### Basic Google Slides Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="google_slides/create_blank_presentation">
    **Description:** Creates a blank presentation with no content.

    **Parameters:**

    * `title` (string, required): The title of the presentation.
  </Accordion>

  <Accordion title="google_slides/get_presentation">
    **Description:** Retrieves a presentation by ID.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation to retrieve.
    * `fields` (string, optional): The fields to include in the response. Use this to improve performance by only returning needed data.
  </Accordion>

  <Accordion title="google_slides/batch_update_presentation">
    **Description:** Applies updates, add content, or remove content from a presentation.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation to update.
    * `requests` (array, required): A list of updates to apply to the presentation.
```

Example 4 (unknown):
```unknown
* `writeControl` (object, optional): Provides control over how write requests are executed.
```

---

## Hierarchical crew

**URL:** llms-txt#hierarchical-crew

**Contents:**
- Best Practices for Collaboration
  - 1. **Clear Role Definition**

crew = Crew(
    agents=[manager, researcher, writer],
    tasks=[project_task],
    process=Process.hierarchical,  # Manager coordinates everything
    manager_llm="gpt-4o",  # Specify LLM for manager
    verbose=True
)
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## Best Practices for Collaboration

### 1. **Clear Role Definition**
```

---

## HITL Workflows

**URL:** llms-txt#hitl-workflows

**Contents:**
- Setting Up HITL Workflows
- Best Practices
- Common Use Cases

Source: https://docs.crewai.com/en/enterprise/guides/human-in-the-loop

Learn how to implement Human-In-The-Loop workflows in CrewAI for enhanced decision-making

Human-In-The-Loop (HITL) is a powerful approach that combines artificial intelligence with human expertise to enhance decision-making and improve task outcomes. This guide shows you how to implement HITL within CrewAI.

## Setting Up HITL Workflows

<Steps>
  <Step title="Configure Your Task">
    Set up your task with human input enabled:

<Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cb2e2bab131e9eff86b0c51dceb16e11" alt="Crew Human Input" data-og-width="624" width="624" data-og-height="165" height="165" data-path="images/enterprise/crew-human-input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1bc2a85e5aa6e736a118fe2c91452dc6 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=137c8e9c09c9a93ba1b683ad3e247e0d 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=79c8be91790b117c1498568ca48f4287 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4da8411c0c26ee98c0dcdde6117353fe 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1b24b707df7ec697db2652d80ed3ff8f 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=39a7543043c397cf4ff84582216ddb65 2500w" />
    </Frame>
  </Step>

<Step title="Provide Webhook URL">
    When kicking off your crew, include a webhook URL for human input:

<Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f2d298c0b4c7b3a62e1dee4e2e6f1bb3" alt="Crew Webhook URL" data-og-width="624" width="624" data-og-height="259" height="259" data-path="images/enterprise/crew-webhook-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=80f52cbe2cd1c6a2a4cd3e2039c22971 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6496d6f5e1fe13fec8be8a406e635b26 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=27cfbbf1fecdab2540df4aeb7ddd15b6 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=57d3439e96917a0627189bfd188af4a0 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cad1f034d8fd4113f08df6bf1a58f3fa 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=fba10cd375c57bcd9b2a216067b5bd44 2500w" />
    </Frame>
  </Step>

<Step title="Receive Webhook Notification">
    Once the crew completes the task requiring human input, you'll receive a webhook notification containing:

* **Execution ID**
    * **Task ID**
    * **Task output**
  </Step>

<Step title="Review Task Output">
    The system will pause in the `Pending Human Input` state. Review the task output carefully.
  </Step>

<Step title="Submit Human Feedback">
    Call the resume endpoint of your crew with the following information:

<Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1e1c2ca22a2d674426f8e663fed33eca" alt="Crew Resume Endpoint" data-og-width="624" width="624" data-og-height="261" height="261" data-path="images/enterprise/crew-resume-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=09014207ae06e6522303b77e4648f0d4 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1ad53990ab04014e622b3acdb37ca604 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=afb11308edffa03de969712505cf95ab 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9bd69f0d75ec47ac2c6280f24a550bff 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f81e1ebcdc8a9348133503eb5eb4e37a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b12843fa2b80cc86580220766a1f4cc4 2500w" />
    </Frame>

<Warning>
      **Critical: Webhook URLs Must Be Provided Again**:
      You **must** provide the same webhook URLs (`taskWebhookUrl`, `stepWebhookUrl`, `crewWebhookUrl`) in the resume call that you used in the kickoff call. Webhook configurations are **NOT** automatically carried over from kickoff - they must be explicitly included in the resume request to continue receiving notifications for task completion, agent steps, and crew completion.
    </Warning>

Example resume call with webhooks:

<Warning>
      **Feedback Impact on Task Execution**:
      It's crucial to exercise care when providing feedback, as the entire feedback content will be incorporated as additional context for further task executions.
    </Warning>

* All information in your feedback becomes part of the task's context.
    * Irrelevant details may negatively influence it.
    * Concise, relevant feedback helps maintain task focus and efficiency.
    * Always review your feedback carefully before submission to ensure it contains only pertinent information that will positively guide the task's execution.
  </Step>

<Step title="Handle Negative Feedback">
    If you provide negative feedback:

* The crew will retry the task with added context from your feedback.
    * You'll receive another webhook notification for further review.
    * Repeat steps 4-6 until satisfied.
  </Step>

<Step title="Execution Continuation">
    When you submit positive feedback, the execution will proceed to the next steps.
  </Step>
</Steps>

* **Be Specific**: Provide clear, actionable feedback that directly addresses the task at hand
* **Stay Relevant**: Only include information that will help improve the task execution
* **Be Timely**: Respond to HITL prompts promptly to avoid workflow delays
* **Review Carefully**: Double-check your feedback before submitting to ensure accuracy

HITL workflows are particularly valuable for:

* Quality assurance and validation
* Complex decision-making scenarios
* Sensitive or high-stakes operations
* Creative tasks requiring human judgment
* Compliance and regulatory reviews

---

## HubSpot Integration

**URL:** llms-txt#hubspot-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up HubSpot Integration
  - 1. Connect Your HubSpot Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic HubSpot Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/hubspot

Manage companies and contacts in HubSpot with CrewAI.

Enable your agents to manage companies and contacts within HubSpot. Create new records and streamline your CRM processes with AI-powered automation.

Before using the HubSpot integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription.
* A HubSpot account with appropriate permissions.
* Connected your HubSpot account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors).

## Setting Up HubSpot Integration

### 1. Connect Your HubSpot Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors).
2. Find **HubSpot** in the Authentication Integrations section.
3. Click **Connect** and complete the OAuth flow.
4. Grant the necessary permissions for company and contact management.
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="hubspot/create_company">
    **Description:** Create a new company record in HubSpot.

* `name` (string, required): Name of the company.
    * `domain` (string, optional): Company Domain Name.
    * `industry` (string, optional): Industry. Must be one of the predefined values from HubSpot.
    * `phone` (string, optional): Phone Number.
    * `hubspot_owner_id` (string, optional): Company owner ID.
    * `type` (string, optional): Type of the company. Available values: `PROSPECT`, `PARTNER`, `RESELLER`, `VENDOR`, `OTHER`.
    * `city` (string, optional): City.
    * `state` (string, optional): State/Region.
    * `zip` (string, optional): Postal Code.
    * `numberofemployees` (number, optional): Number of Employees.
    * `annualrevenue` (number, optional): Annual Revenue.
    * `timezone` (string, optional): Time Zone.
    * `description` (string, optional): Description.
    * `linkedin_company_page` (string, optional): LinkedIn Company Page URL.
    * `company_email` (string, optional): Company Email.
    * `first_name` (string, optional): First Name of a contact at the company.
    * `last_name` (string, optional): Last Name of a contact at the company.
    * `about_us` (string, optional): About Us.
    * `hs_csm_sentiment` (string, optional): CSM Sentiment. Available values: `at_risk`, `neutral`, `healthy`.
    * `closedate` (string, optional): Close Date.
    * `hs_keywords` (string, optional): Company Keywords. Must be one of the predefined values.
    * `country` (string, optional): Country/Region.
    * `hs_country_code` (string, optional): Country/Region Code.
    * `hs_employee_range` (string, optional): Employee range.
    * `facebook_company_page` (string, optional): Facebook Company Page URL.
    * `facebookfans` (number, optional): Number of Facebook Fans.
    * `hs_gps_coordinates` (string, optional): GPS Coordinates.
    * `hs_gps_error` (string, optional): GPS Error.
    * `googleplus_page` (string, optional): Google Plus Page URL.
    * `owneremail` (string, optional): HubSpot Owner Email.
    * `ownername` (string, optional): HubSpot Owner Name.
    * `hs_ideal_customer_profile` (string, optional): Ideal Customer Profile Tier. Available values: `tier_1`, `tier_2`, `tier_3`.
    * `hs_industry_group` (string, optional): Industry group.
    * `is_public` (boolean, optional): Is Public.
    * `hs_last_metered_enrichment_timestamp` (string, optional): Last Metered Enrichment Timestamp.
    * `hs_lead_status` (string, optional): Lead Status. Available values: `NEW`, `OPEN`, `IN_PROGRESS`, `OPEN_DEAL`, `UNQUALIFIED`, `ATTEMPTED_TO_CONTACT`, `CONNECTED`, `BAD_TIMING`.
    * `lifecyclestage` (string, optional): Lifecycle Stage. Available values: `subscriber`, `lead`, `marketingqualifiedlead`, `salesqualifiedlead`, `opportunity`, `customer`, `evangelist`, `other`.
    * `linkedinbio` (string, optional): LinkedIn Bio.
    * `hs_linkedin_handle` (string, optional): LinkedIn handle.
    * `hs_live_enrichment_deadline` (string, optional): Live enrichment deadline.
    * `hs_logo_url` (string, optional): Logo URL.
    * `hs_analytics_source` (string, optional): Original Traffic Source.
    * `hs_pinned_engagement_id` (number, optional): Pinned Engagement ID.
    * `hs_quick_context` (string, optional): Quick context.
    * `hs_revenue_range` (string, optional): Revenue range.
    * `hs_state_code` (string, optional): State/Region Code.
    * `address` (string, optional): Street Address.
    * `address2` (string, optional): Street Address 2.
    * `hs_is_target_account` (boolean, optional): Target Account.
    * `hs_target_account` (string, optional): Target Account Tier. Available values: `tier_1`, `tier_2`, `tier_3`.
    * `hs_target_account_recommendation_snooze_time` (string, optional): Target Account Recommendation Snooze Time.
    * `hs_target_account_recommendation_state` (string, optional): Target Account Recommendation State. Available values: `DISMISSED`, `NONE`, `SNOOZED`.
    * `total_money_raised` (string, optional): Total Money Raised.
    * `twitterbio` (string, optional): Twitter Bio.
    * `twitterfollowers` (number, optional): Twitter Followers.
    * `twitterhandle` (string, optional): Twitter Handle.
    * `web_technologies` (string, optional): Web Technologies used. Must be one of the predefined values.
    * `website` (string, optional): Website URL.
    * `founded_year` (string, optional): Year Founded.
  </Accordion>

<Accordion title="hubspot/create_contact">
    **Description:** Create a new contact record in HubSpot.

* `email` (string, required): Email address of the contact.
    * `firstname` (string, optional): First Name.
    * `lastname` (string, optional): Last Name.
    * `phone` (string, optional): Phone Number.
    * `hubspot_owner_id` (string, optional): Contact owner.
    * `lifecyclestage` (string, optional): Lifecycle Stage. Available values: `subscriber`, `lead`, `marketingqualifiedlead`, `salesqualifiedlead`, `opportunity`, `customer`, `evangelist`, `other`.
    * `hs_lead_status` (string, optional): Lead Status. Available values: `NEW`, `OPEN`, `IN_PROGRESS`, `OPEN_DEAL`, `UNQUALIFIED`, `ATTEMPTED_TO_CONTACT`, `CONNECTED`, `BAD_TIMING`.
    * `annualrevenue` (string, optional): Annual Revenue.
    * `hs_buying_role` (string, optional): Buying Role.
    * `cc_emails` (string, optional): CC Emails.
    * `ch_customer_id` (string, optional): Chargify Customer ID.
    * `ch_customer_reference` (string, optional): Chargify Customer Reference.
    * `chargify_sites` (string, optional): Chargify Site(s).
    * `city` (string, optional): City.
    * `hs_facebook_ad_clicked` (boolean, optional): Clicked Facebook ad.
    * `hs_linkedin_ad_clicked` (string, optional): Clicked LinkedIn Ad.
    * `hs_clicked_linkedin_ad` (string, optional): Clicked on a LinkedIn Ad.
    * `closedate` (string, optional): Close Date.
    * `company` (string, optional): Company Name.
    * `company_size` (string, optional): Company size.
    * `country` (string, optional): Country/Region.
    * `hs_country_region_code` (string, optional): Country/Region Code.
    * `date_of_birth` (string, optional): Date of birth.
    * `degree` (string, optional): Degree.
    * `hs_email_customer_quarantined_reason` (string, optional): Email address quarantine reason.
    * `hs_role` (string, optional): Employment Role. Must be one of the predefined values.
    * `hs_seniority` (string, optional): Employment Seniority. Must be one of the predefined values.
    * `hs_sub_role` (string, optional): Employment Sub Role. Must be one of the predefined values.
    * `hs_employment_change_detected_date` (string, optional): Employment change detected date.
    * `hs_enriched_email_bounce_detected` (boolean, optional): Enriched Email Bounce Detected.
    * `hs_facebookid` (string, optional): Facebook ID.
    * `hs_facebook_click_id` (string, optional): Facebook click id.
    * `fax` (string, optional): Fax Number.
    * `field_of_study` (string, optional): Field of study.
    * `followercount` (number, optional): Follower Count.
    * `gender` (string, optional): Gender.
    * `hs_google_click_id` (string, optional): Google ad click id.
    * `graduation_date` (string, optional): Graduation date.
    * `owneremail` (string, optional): HubSpot Owner Email (legacy).
    * `ownername` (string, optional): HubSpot Owner Name (legacy).
    * `industry` (string, optional): Industry.
    * `hs_inferred_language_codes` (string, optional): Inferred Language Codes. Must be one of the predefined values.
    * `jobtitle` (string, optional): Job Title.
    * `hs_job_change_detected_date` (string, optional): Job change detected date.
    * `job_function` (string, optional): Job function.
    * `hs_journey_stage` (string, optional): Journey Stage. Must be one of the predefined values.
    * `kloutscoregeneral` (number, optional): Klout Score.
    * `hs_last_metered_enrichment_timestamp` (string, optional): Last Metered Enrichment Timestamp.
    * `hs_latest_source` (string, optional): Latest Traffic Source.
    * `hs_latest_source_timestamp` (string, optional): Latest Traffic Source Date.
    * `hs_legal_basis` (string, optional): Legal basis for processing contact's data.
    * `linkedinbio` (string, optional): LinkedIn Bio.
    * `linkedinconnections` (number, optional): LinkedIn Connections.
    * `hs_linkedin_url` (string, optional): LinkedIn URL.
    * `hs_linkedinid` (string, optional): Linkedin ID.
    * `hs_live_enrichment_deadline` (string, optional): Live enrichment deadline.
    * `marital_status` (string, optional): Marital Status.
    * `hs_content_membership_email` (string, optional): Member email.
    * `hs_content_membership_notes` (string, optional): Membership Notes.
    * `message` (string, optional): Message.
    * `military_status` (string, optional): Military status.
    * `mobilephone` (string, optional): Mobile Phone Number.
    * `numemployees` (string, optional): Number of Employees.
    * `hs_analytics_source` (string, optional): Original Traffic Source.
    * `photo` (string, optional): Photo.
    * `hs_pinned_engagement_id` (number, optional): Pinned engagement ID.
    * `zip` (string, optional): Postal Code.
    * `hs_language` (string, optional): Preferred language. Must be one of the predefined values.
    * `associatedcompanyid` (number, optional): Primary Associated Company ID.
    * `hs_email_optout_survey_reason` (string, optional): Reason for opting out of email.
    * `relationship_status` (string, optional): Relationship Status.
    * `hs_returning_to_office_detected_date` (string, optional): Returning to office detected date.
    * `salutation` (string, optional): Salutation.
    * `school` (string, optional): School.
    * `seniority` (string, optional): Seniority.
    * `hs_feedback_show_nps_web_survey` (boolean, optional): Should be shown an NPS web survey.
    * `start_date` (string, optional): Start date.
    * `state` (string, optional): State/Region.
    * `hs_state_code` (string, optional): State/Region Code.
    * `hs_content_membership_status` (string, optional): Status.
    * `address` (string, optional): Street Address.
    * `tax_exempt` (string, optional): Tax Exempt.
    * `hs_timezone` (string, optional): Time Zone. Must be one of the predefined values.
    * `twitterbio` (string, optional): Twitter Bio.
    * `hs_twitterid` (string, optional): Twitter ID.
    * `twitterprofilephoto` (string, optional): Twitter Profile Photo.
    * `twitterhandle` (string, optional): Twitter Username.
    * `vat_number` (string, optional): VAT Number.
    * `ch_verified` (string, optional): Verified for ACH/eCheck Payments.
    * `website` (string, optional): Website URL.
    * `hs_whatsapp_phone_number` (string, optional): WhatsApp Phone Number.
    * `work_email` (string, optional): Work email.
    * `hs_googleplusid` (string, optional): googleplus ID.
  </Accordion>

<Accordion title="hubspot/create_deal">
    **Description:** Create a new deal record in HubSpot.

* `dealname` (string, required): Name of the deal.
    * `amount` (number, optional): The value of the deal.
    * `dealstage` (string, optional): The pipeline stage of the deal.
    * `pipeline` (string, optional): The pipeline the deal belongs to.
    * `closedate` (string, optional): The date the deal is expected to close.
    * `hubspot_owner_id` (string, optional): The owner of the deal.
    * `dealtype` (string, optional): The type of deal. Available values: `newbusiness`, `existingbusiness`.
    * `description` (string, optional): A description of the deal.
    * `hs_priority` (string, optional): The priority of the deal. Available values: `low`, `medium`, `high`.
  </Accordion>

<Accordion title="hubspot/create_record_engagements">
    **Description:** Create a new engagement (e.g., note, email, call, meeting, task) in HubSpot.

* `engagementType` (string, required): The type of engagement. Available values: `NOTE`, `EMAIL`, `CALL`, `MEETING`, `TASK`.
    * `hubspot_owner_id` (string, optional): The user the activity is assigned to.
    * `hs_timestamp` (string, optional): The date and time of the activity.
    * `hs_note_body` (string, optional): The body of the note. (Used for `NOTE`)
    * `hs_task_subject` (string, optional): The title of the task. (Used for `TASK`)
    * `hs_task_body` (string, optional): The notes for the task. (Used for `TASK`)
    * `hs_task_status` (string, optional): The status of the task. (Used for `TASK`)
    * `hs_meeting_title` (string, optional): The title of the meeting. (Used for `MEETING`)
    * `hs_meeting_body` (string, optional): The description for the meeting. (Used for `MEETING`)
    * `hs_meeting_start_time` (string, optional): The start time of the meeting. (Used for `MEETING`)
    * `hs_meeting_end_time` (string, optional): The end time of the meeting. (Used for `MEETING`)
  </Accordion>

<Accordion title="hubspot/update_company">
    **Description:** Update an existing company record in HubSpot.

* `recordId` (string, required): The ID of the company to update.
    * `name` (string, optional): Name of the company.
    * `domain` (string, optional): Company Domain Name.
    * `industry` (string, optional): Industry.
    * `phone` (string, optional): Phone Number.
    * `city` (string, optional): City.
    * `state` (string, optional): State/Region.
    * `zip` (string, optional): Postal Code.
    * `numberofemployees` (number, optional): Number of Employees.
    * `annualrevenue` (number, optional): Annual Revenue.
    * `description` (string, optional): Description.
  </Accordion>

<Accordion title="hubspot/create_record_any">
    **Description:** Create a record for a specified object type in HubSpot.

* `recordType` (string, required): The object type ID of the custom object.
    * Additional parameters depend on the custom object's schema.
  </Accordion>

<Accordion title="hubspot/update_contact">
    **Description:** Update an existing contact record in HubSpot.

* `recordId` (string, required): The ID of the contact to update.
    * `firstname` (string, optional): First Name.
    * `lastname` (string, optional): Last Name.
    * `email` (string, optional): Email address.
    * `phone` (string, optional): Phone Number.
    * `company` (string, optional): Company Name.
    * `jobtitle` (string, optional): Job Title.
    * `lifecyclestage` (string, optional): Lifecycle Stage.
  </Accordion>

<Accordion title="hubspot/update_deal">
    **Description:** Update an existing deal record in HubSpot.

* `recordId` (string, required): The ID of the deal to update.
    * `dealname` (string, optional): Name of the deal.
    * `amount` (number, optional): The value of the deal.
    * `dealstage` (string, optional): The pipeline stage of the deal.
    * `pipeline` (string, optional): The pipeline the deal belongs to.
    * `closedate` (string, optional): The date the deal is expected to close.
    * `dealtype` (string, optional): The type of deal.
  </Accordion>

<Accordion title="hubspot/update_record_engagements">
    **Description:** Update an existing engagement in HubSpot.

* `recordId` (string, required): The ID of the engagement to update.
    * `hs_note_body` (string, optional): The body of the note.
    * `hs_task_subject` (string, optional): The title of the task.
    * `hs_task_body` (string, optional): The notes for the task.
    * `hs_task_status` (string, optional): The status of the task.
  </Accordion>

<Accordion title="hubspot/update_record_any">
    **Description:** Update a record for a specified object type in HubSpot.

* `recordId` (string, required): The ID of the record to update.
    * `recordType` (string, required): The object type ID of the custom object.
    * Additional parameters depend on the custom object's schema.
  </Accordion>

<Accordion title="hubspot/list_companies">
    **Description:** Get a list of company records from HubSpot.

* `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

<Accordion title="hubspot/list_contacts">
    **Description:** Get a list of contact records from HubSpot.

* `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

<Accordion title="hubspot/list_deals">
    **Description:** Get a list of deal records from HubSpot.

* `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

<Accordion title="hubspot/get_records_engagements">
    **Description:** Get a list of engagement records from HubSpot.

* `objectName` (string, required): The type of engagement to fetch (e.g., "notes").
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

<Accordion title="hubspot/get_records_any">
    **Description:** Get a list of records for any specified object type in HubSpot.

* `recordType` (string, required): The object type ID of the custom object.
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

<Accordion title="hubspot/get_company">
    **Description:** Get a single company record by its ID.

* `recordId` (string, required): The ID of the company to retrieve.
  </Accordion>

<Accordion title="hubspot/get_contact">
    **Description:** Get a single contact record by its ID.

* `recordId` (string, required): The ID of the contact to retrieve.
  </Accordion>

<Accordion title="hubspot/get_deal">
    **Description:** Get a single deal record by its ID.

* `recordId` (string, required): The ID of the deal to retrieve.
  </Accordion>

<Accordion title="hubspot/get_record_by_id_engagements">
    **Description:** Get a single engagement record by its ID.

* `recordId` (string, required): The ID of the engagement to retrieve.
  </Accordion>

<Accordion title="hubspot/get_record_by_id_any">
    **Description:** Get a single record of any specified object type by its ID.

* `recordType` (string, required): The object type ID of the custom object.
    * `recordId` (string, required): The ID of the record to retrieve.
  </Accordion>

<Accordion title="hubspot/search_companies">
    **Description:** Search for company records in HubSpot using a filter formula.

* `filterFormula` (object, optional): A filter in disjunctive normal form (OR of ANDs).
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

<Accordion title="hubspot/search_contacts">
    **Description:** Search for contact records in HubSpot using a filter formula.

* `filterFormula` (object, optional): A filter in disjunctive normal form (OR of ANDs).
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

<Accordion title="hubspot/search_deals">
    **Description:** Search for deal records in HubSpot using a filter formula.

* `filterFormula` (object, optional): A filter in disjunctive normal form (OR of ANDs).
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

<Accordion title="hubspot/search_records_engagements">
    **Description:** Search for engagement records in HubSpot using a filter formula.

* `engagementFilterFormula` (object, optional): A filter for engagements.
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

<Accordion title="hubspot/search_records_any">
    **Description:** Search for records of any specified object type in HubSpot.

* `recordType` (string, required): The object type ID to search.
    * `filterFormula` (string, optional): The filter formula to apply.
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

<Accordion title="hubspot/delete_record_companies">
    **Description:** Delete a company record by its ID.

* `recordId` (string, required): The ID of the company to delete.
  </Accordion>

<Accordion title="hubspot/delete_record_contacts">
    **Description:** Delete a contact record by its ID.

* `recordId` (string, required): The ID of the contact to delete.
  </Accordion>

<Accordion title="hubspot/delete_record_deals">
    **Description:** Delete a deal record by its ID.

* `recordId` (string, required): The ID of the deal to delete.
  </Accordion>

<Accordion title="hubspot/delete_record_engagements">
    **Description:** Delete an engagement record by its ID.

* `recordId` (string, required): The ID of the engagement to delete.
  </Accordion>

<Accordion title="hubspot/delete_record_any">
    **Description:** Delete a record of any specified object type by its ID.

* `recordType` (string, required): The object type ID of the custom object.
    * `recordId` (string, required): The ID of the record to delete.
  </Accordion>

<Accordion title="hubspot/get_contacts_by_list_id">
    **Description:** Get contacts from a specific list by its ID.

* `listId` (string, required): The ID of the list to get contacts from.
    * `paginationParameters` (object, optional): Use `pageCursor` for subsequent pages.
  </Accordion>

<Accordion title="hubspot/describe_action_schema">
    **Description:** Get the expected schema for a given object type and operation.

* `recordType` (string, required): The object type ID (e.g., 'companies').
    * `operation` (string, required): The operation type (e.g., 'CREATE\_RECORD').
  </Accordion>
</AccordionGroup>

### Basic HubSpot Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="hubspot/create_company">
    **Description:** Create a new company record in HubSpot.

    **Parameters:**

    * `name` (string, required): Name of the company.
    * `domain` (string, optional): Company Domain Name.
    * `industry` (string, optional): Industry. Must be one of the predefined values from HubSpot.
    * `phone` (string, optional): Phone Number.
    * `hubspot_owner_id` (string, optional): Company owner ID.
    * `type` (string, optional): Type of the company. Available values: `PROSPECT`, `PARTNER`, `RESELLER`, `VENDOR`, `OTHER`.
    * `city` (string, optional): City.
    * `state` (string, optional): State/Region.
    * `zip` (string, optional): Postal Code.
    * `numberofemployees` (number, optional): Number of Employees.
    * `annualrevenue` (number, optional): Annual Revenue.
    * `timezone` (string, optional): Time Zone.
    * `description` (string, optional): Description.
    * `linkedin_company_page` (string, optional): LinkedIn Company Page URL.
    * `company_email` (string, optional): Company Email.
    * `first_name` (string, optional): First Name of a contact at the company.
    * `last_name` (string, optional): Last Name of a contact at the company.
    * `about_us` (string, optional): About Us.
    * `hs_csm_sentiment` (string, optional): CSM Sentiment. Available values: `at_risk`, `neutral`, `healthy`.
    * `closedate` (string, optional): Close Date.
    * `hs_keywords` (string, optional): Company Keywords. Must be one of the predefined values.
    * `country` (string, optional): Country/Region.
    * `hs_country_code` (string, optional): Country/Region Code.
    * `hs_employee_range` (string, optional): Employee range.
    * `facebook_company_page` (string, optional): Facebook Company Page URL.
    * `facebookfans` (number, optional): Number of Facebook Fans.
    * `hs_gps_coordinates` (string, optional): GPS Coordinates.
    * `hs_gps_error` (string, optional): GPS Error.
    * `googleplus_page` (string, optional): Google Plus Page URL.
    * `owneremail` (string, optional): HubSpot Owner Email.
    * `ownername` (string, optional): HubSpot Owner Name.
    * `hs_ideal_customer_profile` (string, optional): Ideal Customer Profile Tier. Available values: `tier_1`, `tier_2`, `tier_3`.
    * `hs_industry_group` (string, optional): Industry group.
    * `is_public` (boolean, optional): Is Public.
    * `hs_last_metered_enrichment_timestamp` (string, optional): Last Metered Enrichment Timestamp.
    * `hs_lead_status` (string, optional): Lead Status. Available values: `NEW`, `OPEN`, `IN_PROGRESS`, `OPEN_DEAL`, `UNQUALIFIED`, `ATTEMPTED_TO_CONTACT`, `CONNECTED`, `BAD_TIMING`.
    * `lifecyclestage` (string, optional): Lifecycle Stage. Available values: `subscriber`, `lead`, `marketingqualifiedlead`, `salesqualifiedlead`, `opportunity`, `customer`, `evangelist`, `other`.
    * `linkedinbio` (string, optional): LinkedIn Bio.
    * `hs_linkedin_handle` (string, optional): LinkedIn handle.
    * `hs_live_enrichment_deadline` (string, optional): Live enrichment deadline.
    * `hs_logo_url` (string, optional): Logo URL.
    * `hs_analytics_source` (string, optional): Original Traffic Source.
    * `hs_pinned_engagement_id` (number, optional): Pinned Engagement ID.
    * `hs_quick_context` (string, optional): Quick context.
    * `hs_revenue_range` (string, optional): Revenue range.
    * `hs_state_code` (string, optional): State/Region Code.
    * `address` (string, optional): Street Address.
    * `address2` (string, optional): Street Address 2.
    * `hs_is_target_account` (boolean, optional): Target Account.
    * `hs_target_account` (string, optional): Target Account Tier. Available values: `tier_1`, `tier_2`, `tier_3`.
    * `hs_target_account_recommendation_snooze_time` (string, optional): Target Account Recommendation Snooze Time.
    * `hs_target_account_recommendation_state` (string, optional): Target Account Recommendation State. Available values: `DISMISSED`, `NONE`, `SNOOZED`.
    * `total_money_raised` (string, optional): Total Money Raised.
    * `twitterbio` (string, optional): Twitter Bio.
    * `twitterfollowers` (number, optional): Twitter Followers.
    * `twitterhandle` (string, optional): Twitter Handle.
    * `web_technologies` (string, optional): Web Technologies used. Must be one of the predefined values.
    * `website` (string, optional): Website URL.
    * `founded_year` (string, optional): Year Founded.
  </Accordion>

  <Accordion title="hubspot/create_contact">
    **Description:** Create a new contact record in HubSpot.

    **Parameters:**

    * `email` (string, required): Email address of the contact.
    * `firstname` (string, optional): First Name.
    * `lastname` (string, optional): Last Name.
    * `phone` (string, optional): Phone Number.
    * `hubspot_owner_id` (string, optional): Contact owner.
    * `lifecyclestage` (string, optional): Lifecycle Stage. Available values: `subscriber`, `lead`, `marketingqualifiedlead`, `salesqualifiedlead`, `opportunity`, `customer`, `evangelist`, `other`.
    * `hs_lead_status` (string, optional): Lead Status. Available values: `NEW`, `OPEN`, `IN_PROGRESS`, `OPEN_DEAL`, `UNQUALIFIED`, `ATTEMPTED_TO_CONTACT`, `CONNECTED`, `BAD_TIMING`.
    * `annualrevenue` (string, optional): Annual Revenue.
    * `hs_buying_role` (string, optional): Buying Role.
    * `cc_emails` (string, optional): CC Emails.
    * `ch_customer_id` (string, optional): Chargify Customer ID.
    * `ch_customer_reference` (string, optional): Chargify Customer Reference.
    * `chargify_sites` (string, optional): Chargify Site(s).
    * `city` (string, optional): City.
    * `hs_facebook_ad_clicked` (boolean, optional): Clicked Facebook ad.
    * `hs_linkedin_ad_clicked` (string, optional): Clicked LinkedIn Ad.
    * `hs_clicked_linkedin_ad` (string, optional): Clicked on a LinkedIn Ad.
    * `closedate` (string, optional): Close Date.
    * `company` (string, optional): Company Name.
    * `company_size` (string, optional): Company size.
    * `country` (string, optional): Country/Region.
    * `hs_country_region_code` (string, optional): Country/Region Code.
    * `date_of_birth` (string, optional): Date of birth.
    * `degree` (string, optional): Degree.
    * `hs_email_customer_quarantined_reason` (string, optional): Email address quarantine reason.
    * `hs_role` (string, optional): Employment Role. Must be one of the predefined values.
    * `hs_seniority` (string, optional): Employment Seniority. Must be one of the predefined values.
    * `hs_sub_role` (string, optional): Employment Sub Role. Must be one of the predefined values.
    * `hs_employment_change_detected_date` (string, optional): Employment change detected date.
    * `hs_enriched_email_bounce_detected` (boolean, optional): Enriched Email Bounce Detected.
    * `hs_facebookid` (string, optional): Facebook ID.
    * `hs_facebook_click_id` (string, optional): Facebook click id.
    * `fax` (string, optional): Fax Number.
    * `field_of_study` (string, optional): Field of study.
    * `followercount` (number, optional): Follower Count.
    * `gender` (string, optional): Gender.
    * `hs_google_click_id` (string, optional): Google ad click id.
    * `graduation_date` (string, optional): Graduation date.
    * `owneremail` (string, optional): HubSpot Owner Email (legacy).
    * `ownername` (string, optional): HubSpot Owner Name (legacy).
    * `industry` (string, optional): Industry.
    * `hs_inferred_language_codes` (string, optional): Inferred Language Codes. Must be one of the predefined values.
    * `jobtitle` (string, optional): Job Title.
    * `hs_job_change_detected_date` (string, optional): Job change detected date.
    * `job_function` (string, optional): Job function.
    * `hs_journey_stage` (string, optional): Journey Stage. Must be one of the predefined values.
    * `kloutscoregeneral` (number, optional): Klout Score.
    * `hs_last_metered_enrichment_timestamp` (string, optional): Last Metered Enrichment Timestamp.
    * `hs_latest_source` (string, optional): Latest Traffic Source.
    * `hs_latest_source_timestamp` (string, optional): Latest Traffic Source Date.
    * `hs_legal_basis` (string, optional): Legal basis for processing contact's data.
    * `linkedinbio` (string, optional): LinkedIn Bio.
    * `linkedinconnections` (number, optional): LinkedIn Connections.
    * `hs_linkedin_url` (string, optional): LinkedIn URL.
    * `hs_linkedinid` (string, optional): Linkedin ID.
    * `hs_live_enrichment_deadline` (string, optional): Live enrichment deadline.
    * `marital_status` (string, optional): Marital Status.
    * `hs_content_membership_email` (string, optional): Member email.
    * `hs_content_membership_notes` (string, optional): Membership Notes.
    * `message` (string, optional): Message.
    * `military_status` (string, optional): Military status.
    * `mobilephone` (string, optional): Mobile Phone Number.
    * `numemployees` (string, optional): Number of Employees.
    * `hs_analytics_source` (string, optional): Original Traffic Source.
    * `photo` (string, optional): Photo.
    * `hs_pinned_engagement_id` (number, optional): Pinned engagement ID.
    * `zip` (string, optional): Postal Code.
    * `hs_language` (string, optional): Preferred language. Must be one of the predefined values.
    * `associatedcompanyid` (number, optional): Primary Associated Company ID.
    * `hs_email_optout_survey_reason` (string, optional): Reason for opting out of email.
    * `relationship_status` (string, optional): Relationship Status.
    * `hs_returning_to_office_detected_date` (string, optional): Returning to office detected date.
    * `salutation` (string, optional): Salutation.
    * `school` (string, optional): School.
    * `seniority` (string, optional): Seniority.
    * `hs_feedback_show_nps_web_survey` (boolean, optional): Should be shown an NPS web survey.
    * `start_date` (string, optional): Start date.
    * `state` (string, optional): State/Region.
    * `hs_state_code` (string, optional): State/Region Code.
    * `hs_content_membership_status` (string, optional): Status.
    * `address` (string, optional): Street Address.
    * `tax_exempt` (string, optional): Tax Exempt.
    * `hs_timezone` (string, optional): Time Zone. Must be one of the predefined values.
    * `twitterbio` (string, optional): Twitter Bio.
    * `hs_twitterid` (string, optional): Twitter ID.
    * `twitterprofilephoto` (string, optional): Twitter Profile Photo.
    * `twitterhandle` (string, optional): Twitter Username.
    * `vat_number` (string, optional): VAT Number.
    * `ch_verified` (string, optional): Verified for ACH/eCheck Payments.
    * `website` (string, optional): Website URL.
    * `hs_whatsapp_phone_number` (string, optional): WhatsApp Phone Number.
    * `work_email` (string, optional): Work email.
    * `hs_googleplusid` (string, optional): googleplus ID.
  </Accordion>

  <Accordion title="hubspot/create_deal">
    **Description:** Create a new deal record in HubSpot.

    **Parameters:**

    * `dealname` (string, required): Name of the deal.
    * `amount` (number, optional): The value of the deal.
    * `dealstage` (string, optional): The pipeline stage of the deal.
    * `pipeline` (string, optional): The pipeline the deal belongs to.
    * `closedate` (string, optional): The date the deal is expected to close.
    * `hubspot_owner_id` (string, optional): The owner of the deal.
    * `dealtype` (string, optional): The type of deal. Available values: `newbusiness`, `existingbusiness`.
    * `description` (string, optional): A description of the deal.
    * `hs_priority` (string, optional): The priority of the deal. Available values: `low`, `medium`, `high`.
  </Accordion>

  <Accordion title="hubspot/create_record_engagements">
    **Description:** Create a new engagement (e.g., note, email, call, meeting, task) in HubSpot.

    **Parameters:**

    * `engagementType` (string, required): The type of engagement. Available values: `NOTE`, `EMAIL`, `CALL`, `MEETING`, `TASK`.
    * `hubspot_owner_id` (string, optional): The user the activity is assigned to.
    * `hs_timestamp` (string, optional): The date and time of the activity.
    * `hs_note_body` (string, optional): The body of the note. (Used for `NOTE`)
    * `hs_task_subject` (string, optional): The title of the task. (Used for `TASK`)
    * `hs_task_body` (string, optional): The notes for the task. (Used for `TASK`)
    * `hs_task_status` (string, optional): The status of the task. (Used for `TASK`)
    * `hs_meeting_title` (string, optional): The title of the meeting. (Used for `MEETING`)
    * `hs_meeting_body` (string, optional): The description for the meeting. (Used for `MEETING`)
    * `hs_meeting_start_time` (string, optional): The start time of the meeting. (Used for `MEETING`)
    * `hs_meeting_end_time` (string, optional): The end time of the meeting. (Used for `MEETING`)
  </Accordion>

  <Accordion title="hubspot/update_company">
    **Description:** Update an existing company record in HubSpot.

    **Parameters:**

    * `recordId` (string, required): The ID of the company to update.
    * `name` (string, optional): Name of the company.
    * `domain` (string, optional): Company Domain Name.
    * `industry` (string, optional): Industry.
    * `phone` (string, optional): Phone Number.
    * `city` (string, optional): City.
    * `state` (string, optional): State/Region.
    * `zip` (string, optional): Postal Code.
    * `numberofemployees` (number, optional): Number of Employees.
    * `annualrevenue` (number, optional): Annual Revenue.
    * `description` (string, optional): Description.
  </Accordion>

  <Accordion title="hubspot/create_record_any">
    **Description:** Create a record for a specified object type in HubSpot.

    **Parameters:**

    * `recordType` (string, required): The object type ID of the custom object.
    * Additional parameters depend on the custom object's schema.
  </Accordion>

  <Accordion title="hubspot/update_contact">
    **Description:** Update an existing contact record in HubSpot.

    **Parameters:**

    * `recordId` (string, required): The ID of the contact to update.
    * `firstname` (string, optional): First Name.
    * `lastname` (string, optional): Last Name.
    * `email` (string, optional): Email address.
    * `phone` (string, optional): Phone Number.
    * `company` (string, optional): Company Name.
    * `jobtitle` (string, optional): Job Title.
    * `lifecyclestage` (string, optional): Lifecycle Stage.
  </Accordion>

  <Accordion title="hubspot/update_deal">
    **Description:** Update an existing deal record in HubSpot.

    **Parameters:**

    * `recordId` (string, required): The ID of the deal to update.
    * `dealname` (string, optional): Name of the deal.
    * `amount` (number, optional): The value of the deal.
    * `dealstage` (string, optional): The pipeline stage of the deal.
    * `pipeline` (string, optional): The pipeline the deal belongs to.
    * `closedate` (string, optional): The date the deal is expected to close.
    * `dealtype` (string, optional): The type of deal.
  </Accordion>

  <Accordion title="hubspot/update_record_engagements">
    **Description:** Update an existing engagement in HubSpot.

    **Parameters:**

    * `recordId` (string, required): The ID of the engagement to update.
    * `hs_note_body` (string, optional): The body of the note.
    * `hs_task_subject` (string, optional): The title of the task.
    * `hs_task_body` (string, optional): The notes for the task.
    * `hs_task_status` (string, optional): The status of the task.
  </Accordion>

  <Accordion title="hubspot/update_record_any">
    **Description:** Update a record for a specified object type in HubSpot.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update.
    * `recordType` (string, required): The object type ID of the custom object.
    * Additional parameters depend on the custom object's schema.
  </Accordion>

  <Accordion title="hubspot/list_companies">
    **Description:** Get a list of company records from HubSpot.

    **Parameters:**

    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/list_contacts">
    **Description:** Get a list of contact records from HubSpot.

    **Parameters:**

    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/list_deals">
    **Description:** Get a list of deal records from HubSpot.

    **Parameters:**

    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/get_records_engagements">
    **Description:** Get a list of engagement records from HubSpot.

    **Parameters:**

    * `objectName` (string, required): The type of engagement to fetch (e.g., "notes").
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/get_records_any">
    **Description:** Get a list of records for any specified object type in HubSpot.

    **Parameters:**

    * `recordType` (string, required): The object type ID of the custom object.
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/get_company">
    **Description:** Get a single company record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the company to retrieve.
  </Accordion>

  <Accordion title="hubspot/get_contact">
    **Description:** Get a single contact record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the contact to retrieve.
  </Accordion>

  <Accordion title="hubspot/get_deal">
    **Description:** Get a single deal record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the deal to retrieve.
  </Accordion>

  <Accordion title="hubspot/get_record_by_id_engagements">
    **Description:** Get a single engagement record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the engagement to retrieve.
  </Accordion>

  <Accordion title="hubspot/get_record_by_id_any">
    **Description:** Get a single record of any specified object type by its ID.

    **Parameters:**

    * `recordType` (string, required): The object type ID of the custom object.
    * `recordId` (string, required): The ID of the record to retrieve.
  </Accordion>

  <Accordion title="hubspot/search_companies">
    **Description:** Search for company records in HubSpot using a filter formula.

    **Parameters:**

    * `filterFormula` (object, optional): A filter in disjunctive normal form (OR of ANDs).
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/search_contacts">
    **Description:** Search for contact records in HubSpot using a filter formula.

    **Parameters:**

    * `filterFormula` (object, optional): A filter in disjunctive normal form (OR of ANDs).
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/search_deals">
    **Description:** Search for deal records in HubSpot using a filter formula.

    **Parameters:**

    * `filterFormula` (object, optional): A filter in disjunctive normal form (OR of ANDs).
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/search_records_engagements">
    **Description:** Search for engagement records in HubSpot using a filter formula.

    **Parameters:**

    * `engagementFilterFormula` (object, optional): A filter for engagements.
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/search_records_any">
    **Description:** Search for records of any specified object type in HubSpot.

    **Parameters:**

    * `recordType` (string, required): The object type ID to search.
    * `filterFormula` (string, optional): The filter formula to apply.
    * `paginationParameters` (object, optional): Use `pageCursor` to fetch subsequent pages.
  </Accordion>

  <Accordion title="hubspot/delete_record_companies">
    **Description:** Delete a company record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the company to delete.
  </Accordion>

  <Accordion title="hubspot/delete_record_contacts">
    **Description:** Delete a contact record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the contact to delete.
  </Accordion>

  <Accordion title="hubspot/delete_record_deals">
    **Description:** Delete a deal record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the deal to delete.
  </Accordion>

  <Accordion title="hubspot/delete_record_engagements">
    **Description:** Delete an engagement record by its ID.

    **Parameters:**

    * `recordId` (string, required): The ID of the engagement to delete.
  </Accordion>

  <Accordion title="hubspot/delete_record_any">
    **Description:** Delete a record of any specified object type by its ID.

    **Parameters:**

    * `recordType` (string, required): The object type ID of the custom object.
    * `recordId` (string, required): The ID of the record to delete.
  </Accordion>

  <Accordion title="hubspot/get_contacts_by_list_id">
    **Description:** Get contacts from a specific list by its ID.

    **Parameters:**

    * `listId` (string, required): The ID of the list to get contacts from.
    * `paginationParameters` (object, optional): Use `pageCursor` for subsequent pages.
  </Accordion>

  <Accordion title="hubspot/describe_action_schema">
    **Description:** Get the expected schema for a given object type and operation.

    **Parameters:**

    * `recordType` (string, required): The object type ID (e.g., 'companies').
    * `operation` (string, required): The operation type (e.g., 'CREATE\_RECORD').
  </Accordion>
</AccordionGroup>

## Usage Examples

### Basic HubSpot Agent Setup
```

---

## HubSpot Trigger

**URL:** llms-txt#hubspot-trigger

**Contents:**
- Prerequisites
- Setup Steps

Source: https://docs.crewai.com/en/enterprise/guides/hubspot-trigger

Trigger CrewAI crews directly from HubSpot Workflows

This guide provides a step-by-step process to set up HubSpot triggers for CrewAI AOP, enabling you to initiate crews directly from HubSpot Workflows.

* A CrewAI AOP account
* A HubSpot account with the [HubSpot Workflows](https://knowledge.hubspot.com/workflows/create-workflows) feature

<Steps>
  <Step title="Connect your HubSpot account with CrewAI AOP">
    * Log in to your `CrewAI AOP account > Triggers`
    * Select `HubSpot` from the list of available triggers
    * Choose the HubSpot account you want to connect with CrewAI AOP
    * Follow the on-screen prompts to authorize CrewAI AOP access to your HubSpot account
    * A confirmation message will appear once HubSpot is successfully connected with CrewAI AOP
  </Step>

<Step title="Create a HubSpot Workflow">
    * Log in to your `HubSpot account > Automations > Workflows > New workflow`
    * Select the workflow type that fits your needs (e.g., Start from scratch)
    * In the workflow builder, click the Plus (+) icon to add a new action.
    * Choose `Integrated apps > CrewAI > Kickoff a Crew`.
    * Select the Crew you want to initiate.
    * Click `Save` to add the action to your workflow

<Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d53acad518d2e330bd4a69ca76808b11" alt="HubSpot Workflow 1" data-og-width="670" width="670" data-og-height="556" height="556" data-path="images/enterprise/hubspot-workflow-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=54aa0bc6e1080e9dfbd5184e23ebefe3 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9eaec24db82ba8a59ac9c43047ce2d1 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f100f688d3f1961f0328d4141f04ad99 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c2147f9de1f60270ef81c5d271acd272 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=aec4cc0e27775dd21cbfb35fad7c6634 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=24d1d4bb9cc84719f78166c6bfa5de81 2500w" />
    </Frame>
  </Step>

<Step title="Use Crew results with other actions">
    * After the Kickoff a Crew step, click the Plus (+) icon to add a new action.
    * For example, to send an internal email notification, choose `Communications > Send internal email notification`
    * In the Body field, click `Insert data`, select `View properties or action outputs from > Action outputs > Crew Result` to include Crew data in the email
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a096e4d667b63a65b1061bdc5f659199" alt="HubSpot Workflow 2" data-og-width="670" width="670" data-og-height="437" height="437" data-path="images/enterprise/hubspot-workflow-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ffe8190dbfdc46039f7ddfb586566ac2 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=066a379f6f677a48a07d66a61b192722 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=871c51f5376163d894e0945665a17b37 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=eb6be36a9c8432789077b82465038c16 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=448437694af0fd88f3d0667ecd6e9ef9 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0a1ef821542f93d1d51601eb3954273a 2500w" />
      </Frame>
    * Configure any additional actions as needed
    * Review your workflow steps to ensure everything is set up correctly
    * Activate the workflow
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b8e6f426200408867d0a09526a93f32f" alt="HubSpot Workflow 3" data-og-width="670" width="670" data-og-height="647" height="647" data-path="images/enterprise/hubspot-workflow-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0b59d6e2251da148d974ec0605a78acd 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=04629b326d956c53658267c418818165 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=eae451ae67430e9283936cd3d06edb26 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=389235975e0ca14bbb3a6b1b307d7508 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0863f7fdf8ef41628ab5b2093700f25f 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=89186e6b7ebc362512ea3dc05407dcec 2500w" />
      </Frame>
  </Step>
</Steps>

For more detailed information on available actions and customization options, refer to the [HubSpot Workflows Documentation](https://knowledge.hubspot.com/workflows/create-workflows).

---

## Human Input on Execution

**URL:** llms-txt#human-input-on-execution

**Contents:**
- Human input in agent execution
- Using human input with CrewAI
  - Example:

Source: https://docs.crewai.com/en/learn/human-input-on-execution

Integrating CrewAI with human input during execution in complex decision-making processes and leveraging the full capabilities of the agent's attributes and tools.

## Human input in agent execution

Human input is critical in several agent execution scenarios, allowing agents to request additional information or clarification when necessary.
This feature is especially useful in complex decision-making processes or when agents require more details to complete a task effectively.

## Using human input with CrewAI

To integrate human input into agent execution, set the `human_input` flag in the task definition. When enabled, the agent prompts the user for input before delivering its final answer.
This input can provide extra context, clarify ambiguities, or validate the agent's output.

```python Code theme={null}
import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

os.environ["SERPER_API_KEY"] = "Your Key"  # serper.dev API key
os.environ["OPENAI_API_KEY"] = "Your Key"

**Examples:**

Example 1 (unknown):
```unknown

```

---

## Human-in-the-Loop (HITL) Workflows

**URL:** llms-txt#human-in-the-loop-(hitl)-workflows

**Contents:**
- Setting Up HITL Workflows
- Best Practices
- Common Use Cases

Source: https://docs.crewai.com/en/learn/human-in-the-loop

Learn how to implement Human-in-the-Loop workflows in CrewAI for enhanced decision-making

Human-in-the-Loop (HITL) is a powerful approach that combines artificial intelligence with human expertise to enhance decision-making and improve task outcomes. This guide shows you how to implement HITL within CrewAI.

## Setting Up HITL Workflows

<Steps>
  <Step title="Configure Your Task">
    Set up your task with human input enabled:

<Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cb2e2bab131e9eff86b0c51dceb16e11" alt="Crew Human Input" data-og-width="624" width="624" data-og-height="165" height="165" data-path="images/enterprise/crew-human-input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1bc2a85e5aa6e736a118fe2c91452dc6 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=137c8e9c09c9a93ba1b683ad3e247e0d 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=79c8be91790b117c1498568ca48f4287 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4da8411c0c26ee98c0dcdde6117353fe 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1b24b707df7ec697db2652d80ed3ff8f 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=39a7543043c397cf4ff84582216ddb65 2500w" />
    </Frame>
  </Step>

<Step title="Provide Webhook URL">
    When kicking off your crew, include a webhook URL for human input:

<Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f2d298c0b4c7b3a62e1dee4e2e6f1bb3" alt="Crew Webhook URL" data-og-width="624" width="624" data-og-height="259" height="259" data-path="images/enterprise/crew-webhook-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=80f52cbe2cd1c6a2a4cd3e2039c22971 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6496d6f5e1fe13fec8be8a406e635b26 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=27cfbbf1fecdab2540df4aeb7ddd15b6 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=57d3439e96917a0627189bfd188af4a0 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cad1f034d8fd4113f08df6bf1a58f3fa 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=fba10cd375c57bcd9b2a216067b5bd44 2500w" />
    </Frame>

Example with Bearer authentication:

Or with Basic authentication:

<Step title="Receive Webhook Notification">
    Once the crew completes the task requiring human input, you'll receive a webhook notification containing:

* Execution ID
    * Task ID
    * Task output
  </Step>

<Step title="Review Task Output">
    The system will pause in the `Pending Human Input` state. Review the task output carefully.
  </Step>

<Step title="Submit Human Feedback">
    Call the resume endpoint of your crew with the following information:

<Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1e1c2ca22a2d674426f8e663fed33eca" alt="Crew Resume Endpoint" data-og-width="624" width="624" data-og-height="261" height="261" data-path="images/enterprise/crew-resume-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=09014207ae06e6522303b77e4648f0d4 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1ad53990ab04014e622b3acdb37ca604 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=afb11308edffa03de969712505cf95ab 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9bd69f0d75ec47ac2c6280f24a550bff 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f81e1ebcdc8a9348133503eb5eb4e37a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b12843fa2b80cc86580220766a1f4cc4 2500w" />
    </Frame>

<Warning>
      **Critical: Webhook URLs Must Be Provided Again**:
      You **must** provide the same webhook URLs (`taskWebhookUrl`, `stepWebhookUrl`, `crewWebhookUrl`) in the resume call that you used in the kickoff call. Webhook configurations are **NOT** automatically carried over from kickoff - they must be explicitly included in the resume request to continue receiving notifications for task completion, agent steps, and crew completion.
    </Warning>

Example resume call with webhooks:

<Warning>
      **Feedback Impact on Task Execution**:
      It's crucial to exercise care when providing feedback, as the entire feedback content will be incorporated as additional context for further task executions.
    </Warning>

* All information in your feedback becomes part of the task's context.
    * Irrelevant details may negatively influence it.
    * Concise, relevant feedback helps maintain task focus and efficiency.
    * Always review your feedback carefully before submission to ensure it contains only pertinent information that will positively guide the task's execution.
  </Step>

<Step title="Handle Negative Feedback">
    If you provide negative feedback:

* The crew will retry the task with added context from your feedback.
    * You'll receive another webhook notification for further review.
    * Repeat steps 4-6 until satisfied.
  </Step>

<Step title="Execution Continuation">
    When you submit positive feedback, the execution will proceed to the next steps.
  </Step>
</Steps>

* **Be Specific**: Provide clear, actionable feedback that directly addresses the task at hand
* **Stay Relevant**: Only include information that will help improve the task execution
* **Be Timely**: Respond to HITL prompts promptly to avoid workflow delays
* **Review Carefully**: Double-check your feedback before submitting to ensure accuracy

HITL workflows are particularly valuable for:

* Quality assurance and validation
* Complex decision-making scenarios
* Sensitive or high-stakes operations
* Creative tasks requiring human judgment
* Compliance and regulatory reviews

**Examples:**

Example 1 (unknown):
```unknown
Or with Basic authentication:
```

Example 2 (unknown):
```unknown
</Step>

  <Step title="Receive Webhook Notification">
    Once the crew completes the task requiring human input, you'll receive a webhook notification containing:

    * Execution ID
    * Task ID
    * Task output
  </Step>

  <Step title="Review Task Output">
    The system will pause in the `Pending Human Input` state. Review the task output carefully.
  </Step>

  <Step title="Submit Human Feedback">
    Call the resume endpoint of your crew with the following information:

    <Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1e1c2ca22a2d674426f8e663fed33eca" alt="Crew Resume Endpoint" data-og-width="624" width="624" data-og-height="261" height="261" data-path="images/enterprise/crew-resume-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=09014207ae06e6522303b77e4648f0d4 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1ad53990ab04014e622b3acdb37ca604 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=afb11308edffa03de969712505cf95ab 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9bd69f0d75ec47ac2c6280f24a550bff 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f81e1ebcdc8a9348133503eb5eb4e37a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b12843fa2b80cc86580220766a1f4cc4 2500w" />
    </Frame>

    <Warning>
      **Critical: Webhook URLs Must Be Provided Again**:
      You **must** provide the same webhook URLs (`taskWebhookUrl`, `stepWebhookUrl`, `crewWebhookUrl`) in the resume call that you used in the kickoff call. Webhook configurations are **NOT** automatically carried over from kickoff - they must be explicitly included in the resume request to continue receiving notifications for task completion, agent steps, and crew completion.
    </Warning>

    Example resume call with webhooks:
```

---

## Image Generation with DALL-E

**URL:** llms-txt#image-generation-with-dall-e

**Contents:**
- Prerequisites
- Setting Up the DALL-E Tool
- Using the DALL-E Tool
  - Example Agent Configuration
  - Expected Output
- Best Practices
- Troubleshooting

Source: https://docs.crewai.com/en/learn/dalle-image-generation

Learn how to use DALL-E for AI-powered image generation in your CrewAI projects

CrewAI supports integration with OpenAI's DALL-E, allowing your AI agents to generate images as part of their tasks. This guide will walk you through how to set up and use the DALL-E tool in your CrewAI projects.

* crewAI installed (latest version)
* OpenAI API key with access to DALL-E

## Setting Up the DALL-E Tool

<Steps>
  <Step title="Import the DALL-E tool">
    
  </Step>

<Step title="Add the DALL-E tool to your agent configuration">
    
  </Step>
</Steps>

## Using the DALL-E Tool

Once you've added the DALL-E tool to your agent, it can generate images based on text prompts. The tool will return a URL to the generated image, which can be used in the agent's output or passed to other agents for further processing.

### Example Agent Configuration

The agent with the DALL-E tool will be able to generate the image and provide a URL in its response. You can then download the image.

<Frame>
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7b6378a1ee0aad5d3941193c6802312c" alt="DALL-E Image" data-og-width="670" width="670" data-og-height="670" height="670" data-path="images/enterprise/dall-e-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=95b3ae8ec53f789746846831fa981b32 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f880f86fa3b648a257ac74fcc7838dce 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c98e8fd36d462d3806c398c1f074efb2 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=68af7edd51913d04723c0fbae774ea1d 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=07c15be8399f83239d49e28f6667a28d 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/dall-e-image.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=619edc0ffc57a1eddd3cd7f9715b6b0a 2500w" />
</Frame>

1. **Be specific in your image generation prompts** to get the best results.
2. **Consider generation time** - Image generation can take some time, so factor this into your task planning.
3. **Follow usage policies** - Always comply with OpenAI's usage policies when generating images.

1. **Check API access** - Ensure your OpenAI API key has access to DALL-E.
2. **Version compatibility** - Check that you're using the latest version of crewAI and crewai-tools.
3. **Tool configuration** - Verify that the DALL-E tool is correctly added to the agent's tool list.

**Examples:**

Example 1 (unknown):
```unknown
</Step>

  <Step title="Add the DALL-E tool to your agent configuration">
```

Example 2 (unknown):
```unknown
</Step>
</Steps>

## Using the DALL-E Tool

Once you've added the DALL-E tool to your agent, it can generate images based on text prompts. The tool will return a URL to the generated image, which can be used in the agent's output or passed to other agents for further processing.

### Example Agent Configuration
```

---

## Initialize the tool to read any files the agents knows or lean the path for

**URL:** llms-txt#initialize-the-tool-to-read-any-files-the-agents-knows-or-lean-the-path-for

file_read_tool = FileReadTool()

---

## Instantiate the crew with a sequential process

**URL:** llms-txt#instantiate-the-crew-with-a-sequential-process

crew = Crew(
    agents=[blog_agent],
    tasks=[task1],
    verbose=True,
    process=Process.sequential,
)

---

## Instantiate your crew with a custom manager

**URL:** llms-txt#instantiate-your-crew-with-a-custom-manager

crew = Crew(
    agents=[researcher, writer],
    tasks=[task],
    manager_agent=manager,
    process=Process.hierarchical,
)

---

## Instantiate your crew with a sequential process

**URL:** llms-txt#instantiate-your-crew-with-a-sequential-process

crew = Crew(
    agents=[researcher, writer], tasks=[task1, task2], verbose=1, process=Process.sequential
)

---

## `InvokeCrewAIAutomationTool`

**URL:** llms-txt#`invokecrewaiautomationtool`

**Contents:**
- Installation
- Requirements
- Usage

The `InvokeCrewAIAutomationTool` provides CrewAI Platform API integration with external crew services. This tool allows you to invoke and interact with CrewAI Platform automations from within your CrewAI agents, enabling seamless integration between different crew workflows.

* CrewAI Platform API access
* Valid bearer token for authentication
* Network access to CrewAI Platform automation endpoints

Here's how to use the tool with a CrewAI agent:

```python {2, 4-9} theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import InvokeCrewAIAutomationTool

**Examples:**

Example 1 (unknown):
```unknown
## Requirements

* CrewAI Platform API access
* Valid bearer token for authentication
* Network access to CrewAI Platform automation endpoints

## Usage

Here's how to use the tool with a CrewAI agent:
```

---

## Jira Integration

**URL:** llms-txt#jira-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Jira Integration
  - 1. Connect Your Jira Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Jira Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/jira

Issue tracking and project management with Jira integration for CrewAI.

Enable your agents to manage issues, projects, and workflows through Jira. Create and update issues, track project progress, manage assignments, and streamline your project management with AI-powered automation.

Before using the Jira integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Jira account with appropriate project permissions
* Connected your Jira account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Jira Integration

### 1. Connect Your Jira Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Jira** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for issue and project management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="jira/create_issue">
    **Description:** Create an issue in Jira.

* `summary` (string, required): Summary - A brief one-line summary of the issue. (example: "The printer stopped working").
    * `project` (string, optional): Project - The project which the issue belongs to. Defaults to the user's first project if not provided. Use Connect Portal Workflow Settings to allow users to select a Project.
    * `issueType` (string, optional): Issue type - Defaults to Task if not provided.
    * `jiraIssueStatus` (string, optional): Status - Defaults to the project's first status if not provided.
    * `assignee` (string, optional): Assignee - Defaults to the authenticated user if not provided.
    * `descriptionType` (string, optional): Description Type - Select the Description Type.
      * Options: `description`, `descriptionJSON`
    * `description` (string, optional): Description - A detailed description of the issue. This field appears only when 'descriptionType' = 'description'.
    * `additionalFields` (string, optional): Additional Fields - Specify any other fields that should be included in JSON format. Use Connect Portal Workflow Settings to allow users to select which Issue Fields to update.
      
  </Accordion>

<Accordion title="jira/update_issue">
    **Description:** Update an issue in Jira.

* `issueKey` (string, required): Issue Key (example: "TEST-1234").
    * `summary` (string, optional): Summary - A brief one-line summary of the issue. (example: "The printer stopped working").
    * `issueType` (string, optional): Issue type - Use Connect Portal Workflow Settings to allow users to select an Issue Type.
    * `jiraIssueStatus` (string, optional): Status - Use Connect Portal Workflow Settings to allow users to select a Status.
    * `assignee` (string, optional): Assignee - Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `descriptionType` (string, optional): Description Type - Select the Description Type.
      * Options: `description`, `descriptionJSON`
    * `description` (string, optional): Description - A detailed description of the issue. This field appears only when 'descriptionType' = 'description'.
    * `additionalFields` (string, optional): Additional Fields - Specify any other fields that should be included in JSON format.
  </Accordion>

<Accordion title="jira/get_issue_by_key">
    **Description:** Get an issue by key in Jira.

* `issueKey` (string, required): Issue Key (example: "TEST-1234").
  </Accordion>

<Accordion title="jira/filter_issues">
    **Description:** Search issues in Jira using filters.

* `jqlQuery` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
      
      Available operators: `$stringExactlyMatches`, `$stringDoesNotExactlyMatch`, `$stringIsIn`, `$stringIsNotIn`, `$stringContains`, `$stringDoesNotContain`, `$stringGreaterThan`, `$stringLessThan`
    * `limit` (string, optional): Limit results - Limit the maximum number of issues to return. Defaults to 10 if left blank.
  </Accordion>

<Accordion title="jira/search_by_jql">
    **Description:** Search issues by JQL in Jira.

* `jqlQuery` (string, required): JQL Query (example: "project = PROJECT").
    * `paginationParameters` (object, optional): Pagination parameters for paginated results.
      
  </Accordion>

<Accordion title="jira/update_issue_any">
    **Description:** Update any issue in Jira. Use DESCRIBE\_ACTION\_SCHEMA to get properties schema for this function.

**Parameters:** No specific parameters - use JIRA\_DESCRIBE\_ACTION\_SCHEMA first to get the expected schema.
  </Accordion>

<Accordion title="jira/describe_action_schema">
    **Description:** Get the expected schema for an issue type. Use this function first if no other function matches the issue type you want to operate on.

* `issueTypeId` (string, required): Issue Type ID.
    * `projectKey` (string, required): Project key.
    * `operation` (string, required): Operation Type value, for example CREATE\_ISSUE or UPDATE\_ISSUE.
  </Accordion>

<Accordion title="jira/get_projects">
    **Description:** Get Projects in Jira.

* `paginationParameters` (object, optional): Pagination Parameters.
      
  </Accordion>

<Accordion title="jira/get_issue_types_by_project">
    **Description:** Get Issue Types by project in Jira.

* `project` (string, required): Project key.
  </Accordion>

<Accordion title="jira/get_issue_types">
    **Description:** Get all Issue Types in Jira.

**Parameters:** None required.
  </Accordion>

<Accordion title="jira/get_issue_status_by_project">
    **Description:** Get issue statuses for a given project.

* `project` (string, required): Project key.
  </Accordion>

<Accordion title="jira/get_all_assignees_by_project">
    **Description:** Get assignees for a given project.

* `project` (string, required): Project key.
  </Accordion>
</AccordionGroup>

### Basic Jira Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="jira/create_issue">
    **Description:** Create an issue in Jira.

    **Parameters:**

    * `summary` (string, required): Summary - A brief one-line summary of the issue. (example: "The printer stopped working").
    * `project` (string, optional): Project - The project which the issue belongs to. Defaults to the user's first project if not provided. Use Connect Portal Workflow Settings to allow users to select a Project.
    * `issueType` (string, optional): Issue type - Defaults to Task if not provided.
    * `jiraIssueStatus` (string, optional): Status - Defaults to the project's first status if not provided.
    * `assignee` (string, optional): Assignee - Defaults to the authenticated user if not provided.
    * `descriptionType` (string, optional): Description Type - Select the Description Type.
      * Options: `description`, `descriptionJSON`
    * `description` (string, optional): Description - A detailed description of the issue. This field appears only when 'descriptionType' = 'description'.
    * `additionalFields` (string, optional): Additional Fields - Specify any other fields that should be included in JSON format. Use Connect Portal Workflow Settings to allow users to select which Issue Fields to update.
```

Example 4 (unknown):
```unknown
</Accordion>

  <Accordion title="jira/update_issue">
    **Description:** Update an issue in Jira.

    **Parameters:**

    * `issueKey` (string, required): Issue Key (example: "TEST-1234").
    * `summary` (string, optional): Summary - A brief one-line summary of the issue. (example: "The printer stopped working").
    * `issueType` (string, optional): Issue type - Use Connect Portal Workflow Settings to allow users to select an Issue Type.
    * `jiraIssueStatus` (string, optional): Status - Use Connect Portal Workflow Settings to allow users to select a Status.
    * `assignee` (string, optional): Assignee - Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `descriptionType` (string, optional): Description Type - Select the Description Type.
      * Options: `description`, `descriptionJSON`
    * `description` (string, optional): Description - A detailed description of the issue. This field appears only when 'descriptionType' = 'description'.
    * `additionalFields` (string, optional): Additional Fields - Specify any other fields that should be included in JSON format.
  </Accordion>

  <Accordion title="jira/get_issue_by_key">
    **Description:** Get an issue by key in Jira.

    **Parameters:**

    * `issueKey` (string, required): Issue Key (example: "TEST-1234").
  </Accordion>

  <Accordion title="jira/filter_issues">
    **Description:** Search issues in Jira using filters.

    **Parameters:**

    * `jqlQuery` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
```

---

## Kickoff Crew Asynchronously

**URL:** llms-txt#kickoff-crew-asynchronously

**Contents:**
- Introduction
- Asynchronous Crew Execution
  - Method Signature
  - Parameters
  - Returns
- Potential Use Cases
- Example: Single Asynchronous Crew Execution

Source: https://docs.crewai.com/en/learn/kickoff-async

Kickoff a Crew Asynchronously

CrewAI provides the ability to kickoff a crew asynchronously, allowing you to start the crew execution in a non-blocking manner.
This feature is particularly useful when you want to run multiple crews concurrently or when you need to perform other tasks while the crew is executing.

## Asynchronous Crew Execution

To kickoff a crew asynchronously, use the `kickoff_async()` method. This method initiates the crew execution in a separate thread, allowing the main thread to continue executing other tasks.

* `inputs` (dict): A dictionary containing the input data required for the tasks.

* `CrewOutput`: An object representing the result of the crew execution.

## Potential Use Cases

* **Parallel Content Generation**: Kickoff multiple independent crews asynchronously, each responsible for generating content on different topics. For example, one crew might research and draft an article on AI trends, while another crew generates social media posts about a new product launch. Each crew operates independently, allowing content production to scale efficiently.

* **Concurrent Market Research Tasks**: Launch multiple crews asynchronously to conduct market research in parallel. One crew might analyze industry trends, while another examines competitor strategies, and yet another evaluates consumer sentiment. Each crew independently completes its task, enabling faster and more comprehensive insights.

* **Independent Travel Planning Modules**: Execute separate crews to independently plan different aspects of a trip. One crew might handle flight options, another handles accommodation, and a third plans activities. Each crew works asynchronously, allowing various components of the trip to be planned simultaneously and independently for faster results.

## Example: Single Asynchronous Crew Execution

Here's an example of how to kickoff a crew asynchronously using asyncio and awaiting the result:

```python Code theme={null}
import asyncio
from crewai import Crew, Agent, Task

**Examples:**

Example 1 (unknown):
```unknown
### Parameters

* `inputs` (dict): A dictionary containing the input data required for the tasks.

### Returns

* `CrewOutput`: An object representing the result of the crew execution.

## Potential Use Cases

* **Parallel Content Generation**: Kickoff multiple independent crews asynchronously, each responsible for generating content on different topics. For example, one crew might research and draft an article on AI trends, while another crew generates social media posts about a new product launch. Each crew operates independently, allowing content production to scale efficiently.

* **Concurrent Market Research Tasks**: Launch multiple crews asynchronously to conduct market research in parallel. One crew might analyze industry trends, while another examines competitor strategies, and yet another evaluates consumer sentiment. Each crew independently completes its task, enabling faster and more comprehensive insights.

* **Independent Travel Planning Modules**: Execute separate crews to independently plan different aspects of a trip. One crew might handle flight options, another handles accommodation, and a third plans activities. Each crew works asynchronously, allowing various components of the trip to be planned simultaneously and independently for faster results.

## Example: Single Asynchronous Crew Execution

Here's an example of how to kickoff a crew asynchronously using asyncio and awaiting the result:
```

---

## Knowledge

**URL:** llms-txt#knowledge

**Contents:**
- Overview
- Quickstart Examples
  - Vector store (RAG) client configuration

Source: https://docs.crewai.com/en/concepts/knowledge

What is knowledge in CrewAI and how to use it.

Knowledge in CrewAI is a powerful system that allows AI agents to access and utilize external information sources during their tasks.
Think of it as giving your agents a reference library they can consult while working.

<Info>
  Key benefits of using Knowledge:

* Enhance agents with domain-specific information
  * Support decisions with real-world data
  * Maintain context across conversations
  * Ground responses in factual information
</Info>

## Quickstart Examples

<Tip>
  For file-based Knowledge Sources, make sure to place your files in a `knowledge` directory at the root of your project.
  Also, use relative paths from the `knowledge` directory when creating the source.
</Tip>

### Vector store (RAG) client configuration

CrewAI exposes a provider-neutral RAG client abstraction for vector stores. The default provider is ChromaDB, and Qdrant is supported as well. You can switch providers using configuration utilities.

* ChromaDB (default)
* Qdrant

```python Code theme={null}
from crewai.rag.config.utils import set_rag_config, get_rag_client, clear_rag_config

---

## Linear Integration

**URL:** llms-txt#linear-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Linear Integration
  - 1. Connect Your Linear Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Linear Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/linear

Software project and bug tracking with Linear integration for CrewAI.

Enable your agents to manage issues, projects, and development workflows through Linear. Create and update issues, manage project timelines, organize teams, and streamline your software development process with AI-powered automation.

Before using the Linear integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Linear account with appropriate workspace permissions
* Connected your Linear account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Linear Integration

### 1. Connect Your Linear Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Linear** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for issue and project management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="linear/create_issue">
    **Description:** Create a new issue in Linear.

* `teamId` (string, required): Team ID - Specify the Team ID of the parent for this new issue. Use Connect Portal Workflow Settings to allow users to select a Team ID. (example: "a70bdf0f-530a-4887-857d-46151b52b47c").
    * `title` (string, required): Title - Specify a title for this issue.
    * `description` (string, optional): Description - Specify a description for this issue.
    * `statusId` (string, optional): Status - Specify the state or status of this issue.
    * `priority` (string, optional): Priority - Specify the priority of this issue as an integer.
    * `dueDate` (string, optional): Due Date - Specify the due date of this issue in ISO 8601 format.
    * `cycleId` (string, optional): Cycle ID - Specify the cycle associated with this issue.
    * `additionalFields` (object, optional): Additional Fields.
      
  </Accordion>

<Accordion title="linear/update_issue">
    **Description:** Update an issue in Linear.

* `issueId` (string, required): Issue ID - Specify the Issue ID of the issue to update. (example: "90fbc706-18cd-42c9-ae66-6bd344cc8977").
    * `title` (string, optional): Title - Specify a title for this issue.
    * `description` (string, optional): Description - Specify a description for this issue.
    * `statusId` (string, optional): Status - Specify the state or status of this issue.
    * `priority` (string, optional): Priority - Specify the priority of this issue as an integer.
    * `dueDate` (string, optional): Due Date - Specify the due date of this issue in ISO 8601 format.
    * `cycleId` (string, optional): Cycle ID - Specify the cycle associated with this issue.
    * `additionalFields` (object, optional): Additional Fields.
      
  </Accordion>

<Accordion title="linear/get_issue_by_id">
    **Description:** Get an issue by ID in Linear.

* `issueId` (string, required): Issue ID - Specify the record ID of the issue to fetch. (example: "90fbc706-18cd-42c9-ae66-6bd344cc8977").
  </Accordion>

<Accordion title="linear/get_issue_by_issue_identifier">
    **Description:** Get an issue by issue identifier in Linear.

* `externalId` (string, required): External ID - Specify the human-readable Issue identifier of the issue to fetch. (example: "ABC-1").
  </Accordion>

<Accordion title="linear/search_issue">
    **Description:** Search issues in Linear.

* `queryTerm` (string, required): Query Term - The search term to look for.
    * `issueFilterFormula` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
      
      Available fields: `title`, `number`, `project`, `createdAt`
      Available operators: `$stringExactlyMatches`, `$stringDoesNotExactlyMatch`, `$stringIsIn`, `$stringIsNotIn`, `$stringStartsWith`, `$stringDoesNotStartWith`, `$stringEndsWith`, `$stringDoesNotEndWith`, `$stringContains`, `$stringDoesNotContain`, `$stringGreaterThan`, `$stringLessThan`, `$numberGreaterThanOrEqualTo`, `$numberLessThanOrEqualTo`, `$numberGreaterThan`, `$numberLessThan`, `$dateTimeAfter`, `$dateTimeBefore`
  </Accordion>

<Accordion title="linear/delete_issue">
    **Description:** Delete an issue in Linear.

* `issueId` (string, required): Issue ID - Specify the record ID of the issue to delete. (example: "90fbc706-18cd-42c9-ae66-6bd344cc8977").
  </Accordion>

<Accordion title="linear/archive_issue">
    **Description:** Archive an issue in Linear.

* `issueId` (string, required): Issue ID - Specify the record ID of the issue to archive. (example: "90fbc706-18cd-42c9-ae66-6bd344cc8977").
  </Accordion>

<Accordion title="linear/create_sub_issue">
    **Description:** Create a sub-issue in Linear.

* `parentId` (string, required): Parent ID - Specify the Issue ID for the parent of this new issue.
    * `teamId` (string, required): Team ID - Specify the Team ID of the parent for this new sub-issue. Use Connect Portal Workflow Settings to allow users to select a Team ID. (example: "a70bdf0f-530a-4887-857d-46151b52b47c").
    * `title` (string, required): Title - Specify a title for this issue.
    * `description` (string, optional): Description - Specify a description for this issue.
    * `additionalFields` (object, optional): Additional Fields.
      
  </Accordion>

<Accordion title="linear/create_project">
    **Description:** Create a new project in Linear.

* `teamIds` (object, required): Team ID - Specify the team ID(s) this project is associated with as a string or a JSON array. Use Connect Portal User Settings to allow your user to select a Team ID.
      
    * `projectName` (string, required): Project Name - Specify the name of the project. (example: "My Linear Project").
    * `description` (string, optional): Project Description - Specify a description for this project.
    * `additionalFields` (object, optional): Additional Fields.
      
  </Accordion>

<Accordion title="linear/update_project">
    **Description:** Update a project in Linear.

* `projectId` (string, required): Project ID - Specify the ID of the project to update. (example: "a6634484-6061-4ac7-9739-7dc5e52c796b").
    * `projectName` (string, optional): Project Name - Specify the name of the project to update. (example: "My Linear Project").
    * `description` (string, optional): Project Description - Specify a description for this project.
    * `additionalFields` (object, optional): Additional Fields.
      
  </Accordion>

<Accordion title="linear/get_project_by_id">
    **Description:** Get a project by ID in Linear.

* `projectId` (string, required): Project ID - Specify the Project ID of the project to fetch. (example: "a6634484-6061-4ac7-9739-7dc5e52c796b").
  </Accordion>

<Accordion title="linear/delete_project">
    **Description:** Delete a project in Linear.

* `projectId` (string, required): Project ID - Specify the Project ID of the project to delete. (example: "a6634484-6061-4ac7-9739-7dc5e52c796b").
  </Accordion>

<Accordion title="linear/search_teams">
    **Description:** Search teams in Linear.

* `teamFilterFormula` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
      
      Available fields: `id`, `name`
  </Accordion>
</AccordionGroup>

### Basic Linear Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="linear/create_issue">
    **Description:** Create a new issue in Linear.

    **Parameters:**

    * `teamId` (string, required): Team ID - Specify the Team ID of the parent for this new issue. Use Connect Portal Workflow Settings to allow users to select a Team ID. (example: "a70bdf0f-530a-4887-857d-46151b52b47c").
    * `title` (string, required): Title - Specify a title for this issue.
    * `description` (string, optional): Description - Specify a description for this issue.
    * `statusId` (string, optional): Status - Specify the state or status of this issue.
    * `priority` (string, optional): Priority - Specify the priority of this issue as an integer.
    * `dueDate` (string, optional): Due Date - Specify the due date of this issue in ISO 8601 format.
    * `cycleId` (string, optional): Cycle ID - Specify the cycle associated with this issue.
    * `additionalFields` (object, optional): Additional Fields.
```

Example 4 (unknown):
```unknown
</Accordion>

  <Accordion title="linear/update_issue">
    **Description:** Update an issue in Linear.

    **Parameters:**

    * `issueId` (string, required): Issue ID - Specify the Issue ID of the issue to update. (example: "90fbc706-18cd-42c9-ae66-6bd344cc8977").
    * `title` (string, optional): Title - Specify a title for this issue.
    * `description` (string, optional): Description - Specify a description for this issue.
    * `statusId` (string, optional): Status - Specify the state or status of this issue.
    * `priority` (string, optional): Priority - Specify the priority of this issue as an integer.
    * `dueDate` (string, optional): Due Date - Specify the due date of this issue in ISO 8601 format.
    * `cycleId` (string, optional): Cycle ID - Specify the cycle associated with this issue.
    * `additionalFields` (object, optional): Additional Fields.
```

---

## `LinkupSearchTool`

**URL:** llms-txt#`linkupsearchtool`

**Contents:**
- Description
- Installation
- Steps to Get Started
- Example

The `LinkupSearchTool` provides the ability to query the Linkup API for contextual information and retrieve structured results. This tool is ideal for enriching workflows with up-to-date and reliable information from Linkup, allowing agents to access relevant data during their tasks.

To use this tool, you need to install the Linkup SDK:

## Steps to Get Started

To effectively use the `LinkupSearchTool`, follow these steps:

1. **API Key**: Obtain a Linkup API key.
2. **Environment Setup**: Set up your environment with the API key.
3. **Install SDK**: Install the Linkup SDK using the command above.

The following example demonstrates how to initialize the tool and use it in an agent:

```python Code theme={null}
from crewai_tools import LinkupSearchTool
from crewai import Agent
import os

**Examples:**

Example 1 (unknown):
```unknown
## Steps to Get Started

To effectively use the `LinkupSearchTool`, follow these steps:

1. **API Key**: Obtain a Linkup API key.
2. **Environment Setup**: Set up your environment with the API key.
3. **Install SDK**: Install the Linkup SDK using the command above.

## Example

The following example demonstrates how to initialize the tool and use it in an agent:
```

---

## `LlamaIndexTool`

**URL:** llms-txt#`llamaindextool`

**Contents:**
- Description
- Installation
- Steps to Get Started
- Example
  - From a LlamaIndex Tool

The `LlamaIndexTool` is designed to be a general wrapper around LlamaIndex tools and query engines, enabling you to leverage LlamaIndex resources in terms of RAG/agentic pipelines as tools to plug into CrewAI agents. This tool allows you to seamlessly integrate LlamaIndex's powerful data processing and retrieval capabilities into your CrewAI workflows.

To use this tool, you need to install LlamaIndex:

## Steps to Get Started

To effectively use the `LlamaIndexTool`, follow these steps:

1. **Install LlamaIndex**: Install the LlamaIndex package using the command above.
2. **Set Up LlamaIndex**: Follow the [LlamaIndex documentation](https://docs.llamaindex.ai/) to set up a RAG/agent pipeline.
3. **Create a Tool or Query Engine**: Create a LlamaIndex tool or query engine that you want to use with CrewAI.

The following examples demonstrate how to initialize the tool from different LlamaIndex components:

### From a LlamaIndex Tool

```python Code theme={null}
from crewai_tools import LlamaIndexTool
from crewai import Agent
from llama_index.core.tools import FunctionTool

**Examples:**

Example 1 (unknown):
```unknown
## Steps to Get Started

To effectively use the `LlamaIndexTool`, follow these steps:

1. **Install LlamaIndex**: Install the LlamaIndex package using the command above.
2. **Set Up LlamaIndex**: Follow the [LlamaIndex documentation](https://docs.llamaindex.ai/) to set up a RAG/agent pipeline.
3. **Create a Tool or Query Engine**: Create a LlamaIndex tool or query engine that you want to use with CrewAI.

## Example

The following examples demonstrate how to initialize the tool from different LlamaIndex components:

### From a LlamaIndex Tool
```

---

## LLMs

**URL:** llms-txt#llms

**Contents:**
- Overview
- What are LLMs?
- Setting up your LLM
- Provider Configuration Examples
- Streaming Responses
- Async LLM Calls
- Structured LLM Calls

Source: https://docs.crewai.com/en/concepts/llms

A comprehensive guide to configuring and using Large Language Models (LLMs) in your CrewAI projects

CrewAI integrates with multiple LLM providers through providers native sdks, giving you the flexibility to choose the right model for your specific use case. This guide will help you understand how to configure and use different LLM providers in your CrewAI projects.

Large Language Models (LLMs) are the core intelligence behind CrewAI agents. They enable agents to understand context, make decisions, and generate human-like responses. Here's what you need to know:

<CardGroup cols={2}>
  <Card title="LLM Basics" icon="brain">
    Large Language Models are AI systems trained on vast amounts of text data. They power the intelligence of your CrewAI agents, enabling them to understand and generate human-like text.
  </Card>

<Card title="Context Window" icon="window">
    The context window determines how much text an LLM can process at once. Larger windows (e.g., 128K tokens) allow for more context but may be more expensive and slower.
  </Card>

<Card title="Temperature" icon="temperature-three-quarters">
    Temperature (0.0 to 1.0) controls response randomness. Lower values (e.g., 0.2) produce more focused, deterministic outputs, while higher values (e.g., 0.8) increase creativity and variability.
  </Card>

<Card title="Provider Selection" icon="server">
    Each LLM provider (e.g., OpenAI, Anthropic, Google) offers different models with varying capabilities, pricing, and features. Choose based on your needs for accuracy, speed, and cost.
  </Card>
</CardGroup>

## Setting up your LLM

There are different places in CrewAI code where you can specify the model to use. Once you specify the model you are using, you will need to provide the configuration (like an API key) for each of the model providers you use. See the [provider configuration examples](#provider-configuration-examples) section for your provider.

<Tabs>
  <Tab title="1. Environment Variables">
    The simplest way to get started. Set the model in your environment directly, through an `.env` file or in your app code. If you used `crewai create` to bootstrap your project, it will be set already.

<Warning>
      Never commit API keys to version control. Use environment files (.env) or your system's secret management.
    </Warning>
  </Tab>

<Tab title="2. YAML Configuration">
    Create a YAML file to define your agent configurations. This method is great for version control and team collaboration:

<Info>
      The YAML configuration allows you to:

* Version control your agent settings
      * Easily switch between different models
      * Share configurations across team members
      * Document model choices and their purposes
    </Info>
  </Tab>

<Tab title="3. Direct Code">
    For maximum flexibility, configure LLMs directly in your Python code:

<Info>
      Parameter explanations:

* `temperature`: Controls randomness (0.0-1.0)
      * `timeout`: Maximum wait time for response
      * `max_tokens`: Limits response length
      * `top_p`: Alternative to temperature for sampling
      * `frequency_penalty`: Reduces word repetition
      * `presence_penalty`: Encourages new topics
      * `response_format`: Specifies output structure
      * `seed`: Ensures consistent outputs
    </Info>
  </Tab>
</Tabs>

## Provider Configuration Examples

CrewAI supports a multitude of LLM providers, each offering unique features, authentication methods, and model capabilities.
In this section, you'll find detailed examples that help you select, configure, and optimize the LLM that best fits your project's needs.

<AccordionGroup>
  <Accordion title="OpenAI">
    CrewAI provides native integration with OpenAI through the OpenAI Python SDK.

**Advanced Configuration:**

**Structured Outputs:**

**Supported Environment Variables:**

* `OPENAI_API_KEY`: Your OpenAI API key (required)
    * `OPENAI_BASE_URL`: Custom base URL for OpenAI API (optional)

* Native function calling support (except o1 models)
    * Structured outputs with JSON schema
    * Streaming support for real-time responses
    * Token usage tracking
    * Stop sequences support (except o1 models)
    * Log probabilities for token-level insights
    * Reasoning effort control for o1 models

**Supported Models:**

| Model        | Context Window | Best For                                    |
    | ------------ | -------------- | ------------------------------------------- |
    | gpt-4.1      | 1M tokens      | Latest model with enhanced capabilities     |
    | gpt-4.1-mini | 1M tokens      | Efficient version with large context        |
    | gpt-4.1-nano | 1M tokens      | Ultra-efficient variant                     |
    | gpt-4o       | 128,000 tokens | Optimized for speed and intelligence        |
    | gpt-4o-mini  | 200,000 tokens | Cost-effective with large context           |
    | gpt-4-turbo  | 128,000 tokens | Long-form content, document analysis        |
    | gpt-4        | 8,192 tokens   | High-accuracy tasks, complex reasoning      |
    | o1           | 200,000 tokens | Advanced reasoning, complex problem-solving |
    | o1-preview   | 128,000 tokens | Preview of reasoning capabilities           |
    | o1-mini      | 128,000 tokens | Efficient reasoning model                   |
    | o3-mini      | 200,000 tokens | Lightweight reasoning model                 |
    | o4-mini      | 200,000 tokens | Next-gen efficient reasoning                |

**Note:** To use OpenAI, install the required dependencies:

<Accordion title="Meta-Llama">
    Meta's Llama API provides access to Meta's family of large language models.
    The API is available through the [Meta Llama API](https://llama.developer.meta.com?utm_source=partner-crewai\&utm_medium=website).
    Set the following environment variables in your `.env` file:

Example usage in your CrewAI project:

All models listed here [https://llama.developer.meta.com/docs/models/](https://llama.developer.meta.com/docs/models/) are supported.

| Model ID                                            | Input context length | Output context length | Input Modalities | Output Modalities |
    | --------------------------------------------------- | -------------------- | --------------------- | ---------------- | ----------------- |
    | `meta_llama/Llama-4-Scout-17B-16E-Instruct-FP8`     | 128k                 | 4028                  | Text, Image      | Text              |
    | `meta_llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 128k                 | 4028                  | Text, Image      | Text              |
    | `meta_llama/Llama-3.3-70B-Instruct`                 | 128k                 | 4028                  | Text             | Text              |
    | `meta_llama/Llama-3.3-8B-Instruct`                  | 128k                 | 4028                  | Text             | Text              |
  </Accordion>

<Accordion title="Anthropic">
    CrewAI provides native integration with Anthropic through the Anthropic Python SDK.

**Advanced Configuration:**

**Supported Environment Variables:**

* `ANTHROPIC_API_KEY`: Your Anthropic API key (required)

* Native tool use support for Claude 3+ models
    * Streaming support for real-time responses
    * Automatic system message handling
    * Stop sequences for controlled output
    * Token usage tracking
    * Multi-turn tool use conversations

* `max_tokens` is a **required** parameter for all Anthropic models
    * Claude uses `stop_sequences` instead of `stop`
    * System messages are handled separately from conversation messages
    * First message must be from the user (automatically handled)
    * Messages must alternate between user and assistant

**Supported Models:**

| Model                      | Context Window | Best For                                 |
    | -------------------------- | -------------- | ---------------------------------------- |
    | claude-3-7-sonnet          | 200,000 tokens | Advanced reasoning and agentic tasks     |
    | claude-3-5-sonnet-20241022 | 200,000 tokens | Latest Sonnet with best performance      |
    | claude-3-5-haiku           | 200,000 tokens | Fast, compact model for quick responses  |
    | claude-3-opus              | 200,000 tokens | Most capable for complex tasks           |
    | claude-3-sonnet            | 200,000 tokens | Balanced intelligence and speed          |
    | claude-3-haiku             | 200,000 tokens | Fastest for simple tasks                 |
    | claude-2.1                 | 200,000 tokens | Extended context, reduced hallucinations |
    | claude-2                   | 100,000 tokens | Versatile model for various tasks        |
    | claude-instant             | 100,000 tokens | Fast, cost-effective for everyday tasks  |

**Note:** To use Anthropic, install the required dependencies:

<Accordion title="Google (Gemini API)">
    CrewAI provides native integration with Google Gemini through the Google Gen AI Python SDK.

Set your API key in your `.env` file. If you need a key, check [AI Studio](https://aistudio.google.com/apikey).

**Advanced Configuration:**

**Vertex AI Configuration:**

**Supported Environment Variables:**

* `GOOGLE_API_KEY` or `GEMINI_API_KEY`: Your Google API key (required for Gemini API)
    * `GOOGLE_CLOUD_PROJECT`: Google Cloud project ID (for Vertex AI)
    * `GOOGLE_CLOUD_LOCATION`: GCP location (defaults to `us-central1`)
    * `GOOGLE_GENAI_USE_VERTEXAI`: Set to `true` to use Vertex AI

* Native function calling support for Gemini 1.5+ and 2.x models
    * Streaming support for real-time responses
    * Multimodal capabilities (text, images, video)
    * Safety settings configuration
    * Support for both Gemini API and Vertex AI
    * Automatic system instruction handling
    * Token usage tracking

Google offers a range of powerful models optimized for different use cases.

| Model                     | Context Window | Best For                                                  |
    | ------------------------- | -------------- | --------------------------------------------------------- |
    | gemini-2.5-flash          | 1M tokens      | Adaptive thinking, cost efficiency                        |
    | gemini-2.5-pro            | 1M tokens      | Enhanced thinking and reasoning, multimodal understanding |
    | gemini-2.0-flash          | 1M tokens      | Next generation features, speed, thinking                 |
    | gemini-2.0-flash-thinking | 32,768 tokens  | Advanced reasoning with thinking process                  |
    | gemini-2.0-flash-lite     | 1M tokens      | Cost efficiency and low latency                           |
    | gemini-1.5-pro            | 2M tokens      | Best performing, logical reasoning, coding                |
    | gemini-1.5-flash          | 1M tokens      | Balanced multimodal model, good for most tasks            |
    | gemini-1.5-flash-8b       | 1M tokens      | Fastest, most cost-efficient                              |
    | gemini-1.0-pro            | 32,768 tokens  | Earlier generation model                                  |

The Gemini API also supports [Gemma models](https://ai.google.dev/gemma/docs) hosted on Google infrastructure.

| Model       | Context Window | Best For                            |
    | ----------- | -------------- | ----------------------------------- |
    | gemma-3-1b  | 32,000 tokens  | Ultra-lightweight tasks             |
    | gemma-3-4b  | 128,000 tokens | Efficient general-purpose tasks     |
    | gemma-3-12b | 128,000 tokens | Balanced performance and efficiency |
    | gemma-3-27b | 128,000 tokens | High-performance tasks              |

**Note:** To use Google Gemini, install the required dependencies:

The full list of models is available in the [Gemini model docs](https://ai.google.dev/gemini-api/docs/models).
  </Accordion>

<Accordion title="Google (Vertex AI)">
    Get credentials from your Google Cloud Console and save it to a JSON file, then load it with the following code:

Example usage in your CrewAI project:

Google offers a range of powerful models optimized for different use cases:

| Model                          | Context Window | Best For                                                                                                         |
    | ------------------------------ | -------------- | ---------------------------------------------------------------------------------------------------------------- |
    | gemini-2.5-flash-preview-04-17 | 1M tokens      | Adaptive thinking, cost efficiency                                                                               |
    | gemini-2.5-pro-preview-05-06   | 1M tokens      | Enhanced thinking and reasoning, multimodal understanding, advanced coding, and more                             |
    | gemini-2.0-flash               | 1M tokens      | Next generation features, speed, thinking, and realtime streaming                                                |
    | gemini-2.0-flash-lite          | 1M tokens      | Cost efficiency and low latency                                                                                  |
    | gemini-1.5-flash               | 1M tokens      | Balanced multimodal model, good for most tasks                                                                   |
    | gemini-1.5-flash-8B            | 1M tokens      | Fastest, most cost-efficient, good for high-frequency tasks                                                      |
    | gemini-1.5-pro                 | 2M tokens      | Best performing, wide variety of reasoning tasks including logical reasoning, coding, and creative collaboration |
  </Accordion>

<Accordion title="Azure">
    CrewAI provides native integration with Azure AI Inference and Azure OpenAI through the Azure AI Inference Python SDK.

**Endpoint URL Formats:**

For Azure OpenAI deployments:

For Azure AI Inference endpoints:

**Advanced Configuration:**

**Supported Environment Variables:**

* `AZURE_API_KEY`: Your Azure API key (required)
    * `AZURE_ENDPOINT`: Your Azure endpoint URL (required, also checks `AZURE_OPENAI_ENDPOINT` and `AZURE_API_BASE`)
    * `AZURE_API_VERSION`: API version (optional, defaults to `2024-06-01`)

* Native function calling support for Azure OpenAI models (gpt-4, gpt-4o, gpt-3.5-turbo, etc.)
    * Streaming support for real-time responses
    * Automatic endpoint URL validation and correction
    * Comprehensive error handling with retry logic
    * Token usage tracking

**Note:** To use Azure AI Inference, install the required dependencies:

<Accordion title="AWS Bedrock">
    CrewAI provides native integration with AWS Bedrock through the boto3 SDK using the Converse API.

**Advanced Configuration:**

**Supported Environment Variables:**

* `AWS_ACCESS_KEY_ID`: AWS access key (required)
    * `AWS_SECRET_ACCESS_KEY`: AWS secret key (required)
    * `AWS_SESSION_TOKEN`: AWS session token for temporary credentials (optional)
    * `AWS_DEFAULT_REGION`: AWS region (defaults to `us-east-1`)

* Native tool calling support via Converse API
    * Streaming and non-streaming responses
    * Comprehensive error handling with retry logic
    * Guardrail configuration for content filtering
    * Model-specific parameters via `additional_model_request_fields`
    * Token usage tracking and stop reason logging
    * Support for all Bedrock foundation models
    * Automatic conversation format handling

* Uses the modern Converse API for unified model access
    * Automatic handling of model-specific conversation requirements
    * System messages are handled separately from conversation
    * First message must be from user (automatically handled)
    * Some models (like Cohere) require conversation to end with user message

[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) is a managed service that provides access to multiple foundation models from top AI companies through a unified API.

| Model                   | Context Window     | Best For                                                                                                                              |
    | ----------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
    | Amazon Nova Pro         | Up to 300k tokens  | High-performance, model balancing accuracy, speed, and cost-effectiveness across diverse tasks.                                       |
    | Amazon Nova Micro       | Up to 128k tokens  | High-performance, cost-effective text-only model optimized for lowest latency responses.                                              |
    | Amazon Nova Lite        | Up to 300k tokens  | High-performance, affordable multimodal processing for images, video, and text with real-time capabilities.                           |
    | Claude 3.7 Sonnet       | Up to 128k tokens  | High-performance, best for complex reasoning, coding & AI agents                                                                      |
    | Claude 3.5 Sonnet v2    | Up to 200k tokens  | State-of-the-art model specialized in software engineering, agentic capabilities, and computer interaction at optimized cost.         |
    | Claude 3.5 Sonnet       | Up to 200k tokens  | High-performance model delivering superior intelligence and reasoning across diverse tasks with optimal speed-cost balance.           |
    | Claude 3.5 Haiku        | Up to 200k tokens  | Fast, compact multimodal model optimized for quick responses and seamless human-like interactions                                     |
    | Claude 3 Sonnet         | Up to 200k tokens  | Multimodal model balancing intelligence and speed for high-volume deployments.                                                        |
    | Claude 3 Haiku          | Up to 200k tokens  | Compact, high-speed multimodal model optimized for quick responses and natural conversational interactions                            |
    | Claude 3 Opus           | Up to 200k tokens  | Most advanced multimodal model exceling at complex tasks with human-like reasoning and superior contextual understanding.             |
    | Claude 2.1              | Up to 200k tokens  | Enhanced version with expanded context window, improved reliability, and reduced hallucinations for long-form and RAG applications    |
    | Claude                  | Up to 100k tokens  | Versatile model excelling in sophisticated dialogue, creative content, and precise instruction following.                             |
    | Claude Instant          | Up to 100k tokens  | Fast, cost-effective model for everyday tasks like dialogue, analysis, summarization, and document Q\&A                               |
    | Llama 3.1 405B Instruct | Up to 128k tokens  | Advanced LLM for synthetic data generation, distillation, and inference for chatbots, coding, and domain-specific tasks.              |
    | Llama 3.1 70B Instruct  | Up to 128k tokens  | Powers complex conversations with superior contextual understanding, reasoning and text generation.                                   |
    | Llama 3.1 8B Instruct   | Up to 128k tokens  | Advanced state-of-the-art model with language understanding, superior reasoning, and text generation.                                 |
    | Llama 3 70B Instruct    | Up to 8k tokens    | Powers complex conversations with superior contextual understanding, reasoning and text generation.                                   |
    | Llama 3 8B Instruct     | Up to 8k tokens    | Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation.                                   |
    | Titan Text G1 - Lite    | Up to 4k tokens    | Lightweight, cost-effective model optimized for English tasks and fine-tuning with focus on summarization and content generation.     |
    | Titan Text G1 - Express | Up to 8k tokens    | Versatile model for general language tasks, chat, and RAG applications with support for English and 100+ languages.                   |
    | Cohere Command          | Up to 4k tokens    | Model specialized in following user commands and delivering practical enterprise solutions.                                           |
    | Jurassic-2 Mid          | Up to 8,191 tokens | Cost-effective model balancing quality and affordability for diverse language tasks like Q\&A, summarization, and content generation. |
    | Jurassic-2 Ultra        | Up to 8,191 tokens | Model for advanced text generation and comprehension, excelling in complex tasks like analysis and content creation.                  |
    | Jamba-Instruct          | Up to 256k tokens  | Model with extended context window optimized for cost-effective text generation, summarization, and Q\&A.                             |
    | Mistral 7B Instruct     | Up to 32k tokens   | This LLM follows instructions, completes requests, and generates creative text.                                                       |
    | Mistral 8x7B Instruct   | Up to 32k tokens   | An MOE LLM that follows instructions, completes requests, and generates creative text.                                                |
    | DeepSeek R1             | 32,768 tokens      | Advanced reasoning model                                                                                                              |

**Note:** To use AWS Bedrock, install the required dependencies:

<Accordion title="Amazon SageMaker">

Example usage in your CrewAI project:

<Accordion title="Mistral">
    Set the following environment variables in your `.env` file:

Example usage in your CrewAI project:

<Accordion title="Nvidia NIM">
    Set the following environment variables in your `.env` file:

Example usage in your CrewAI project:

Nvidia NIM provides a comprehensive suite of models for various use cases, from general-purpose tasks to specialized applications.

| Model                                       | Context Window | Best For                                                                                                                    |
    | ------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------- |
    | nvidia/mistral-nemo-minitron-8b-8k-instruct | 8,192 tokens   | State-of-the-art small language model delivering superior accuracy for chatbot, virtual assistants, and content generation. |
    | nvidia/nemotron-4-mini-hindi-4b-instruct    | 4,096 tokens   | A bilingual Hindi-English SLM for on-device inference, tailored specifically for Hindi Language.                            |
    | nvidia/llama-3.1-nemotron-70b-instruct      | 128k tokens    | Customized for enhanced helpfulness in responses                                                                            |
    | nvidia/llama3-chatqa-1.5-8b                 | 128k tokens    | Advanced LLM to generate high-quality, context-aware responses for chatbots and search engines.                             |
    | nvidia/llama3-chatqa-1.5-70b                | 128k tokens    | Advanced LLM to generate high-quality, context-aware responses for chatbots and search engines.                             |
    | nvidia/vila                                 | 128k tokens    | Multi-modal vision-language model that understands text/img/video and creates informative responses                         |
    | nvidia/neva-22                              | 4,096 tokens   | Multi-modal vision-language model that understands text/images and generates informative responses                          |
    | nvidia/nemotron-mini-4b-instruct            | 8,192 tokens   | General-purpose tasks                                                                                                       |
    | nvidia/usdcode-llama3-70b-instruct          | 128k tokens    | State-of-the-art LLM that answers OpenUSD knowledge queries and generates USD-Python code.                                  |
    | nvidia/nemotron-4-340b-instruct             | 4,096 tokens   | Creates diverse synthetic data that mimics the characteristics of real-world data.                                          |
    | meta/codellama-70b                          | 100k tokens    | LLM capable of generating code from natural language and vice versa.                                                        |
    | meta/llama2-70b                             | 4,096 tokens   | Cutting-edge large language AI model capable of generating text and code in response to prompts.                            |
    | meta/llama3-8b-instruct                     | 8,192 tokens   | Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation.                         |
    | meta/llama3-70b-instruct                    | 8,192 tokens   | Powers complex conversations with superior contextual understanding, reasoning and text generation.                         |
    | meta/llama-3.1-8b-instruct                  | 128k tokens    | Advanced state-of-the-art model with language understanding, superior reasoning, and text generation.                       |
    | meta/llama-3.1-70b-instruct                 | 128k tokens    | Powers complex conversations with superior contextual understanding, reasoning and text generation.                         |
    | meta/llama-3.1-405b-instruct                | 128k tokens    | Advanced LLM for synthetic data generation, distillation, and inference for chatbots, coding, and domain-specific tasks.    |
    | meta/llama-3.2-1b-instruct                  | 128k tokens    | Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation.        |
    | meta/llama-3.2-3b-instruct                  | 128k tokens    | Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation.        |
    | meta/llama-3.2-11b-vision-instruct          | 128k tokens    | Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation.        |
    | meta/llama-3.2-90b-vision-instruct          | 128k tokens    | Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation.        |
    | google/gemma-7b                             | 8,192 tokens   | Cutting-edge text generation model text understanding, transformation, and code generation.                                 |
    | google/gemma-2b                             | 8,192 tokens   | Cutting-edge text generation model text understanding, transformation, and code generation.                                 |
    | google/codegemma-7b                         | 8,192 tokens   | Cutting-edge model built on Google's Gemma-7B specialized for code generation and code completion.                          |
    | google/codegemma-1.1-7b                     | 8,192 tokens   | Advanced programming model for code generation, completion, reasoning, and instruction following.                           |
    | google/recurrentgemma-2b                    | 8,192 tokens   | Novel recurrent architecture based language model for faster inference when generating long sequences.                      |
    | google/gemma-2-9b-it                        | 8,192 tokens   | Cutting-edge text generation model text understanding, transformation, and code generation.                                 |
    | google/gemma-2-27b-it                       | 8,192 tokens   | Cutting-edge text generation model text understanding, transformation, and code generation.                                 |
    | google/gemma-2-2b-it                        | 8,192 tokens   | Cutting-edge text generation model text understanding, transformation, and code generation.                                 |
    | google/deplot                               | 512 tokens     | One-shot visual language understanding model that translates images of plots into tables.                                   |
    | google/paligemma                            | 8,192 tokens   | Vision language model adept at comprehending text and visual inputs to produce informative responses.                       |
    | mistralai/mistral-7b-instruct-v0.2          | 32k tokens     | This LLM follows instructions, completes requests, and generates creative text.                                             |
    | mistralai/mixtral-8x7b-instruct-v0.1        | 8,192 tokens   | An MOE LLM that follows instructions, completes requests, and generates creative text.                                      |
    | mistralai/mistral-large                     | 4,096 tokens   | Creates diverse synthetic data that mimics the characteristics of real-world data.                                          |
    | mistralai/mixtral-8x22b-instruct-v0.1       | 8,192 tokens   | Creates diverse synthetic data that mimics the characteristics of real-world data.                                          |
    | mistralai/mistral-7b-instruct-v0.3          | 32k tokens     | This LLM follows instructions, completes requests, and generates creative text.                                             |
    | nv-mistralai/mistral-nemo-12b-instruct      | 128k tokens    | Most advanced language model for reasoning, code, multilingual tasks; runs on a single GPU.                                 |
    | mistralai/mamba-codestral-7b-v0.1           | 256k tokens    | Model for writing and interacting with code across a wide range of programming languages and tasks.                         |
    | microsoft/phi-3-mini-128k-instruct          | 128K tokens    | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.                                       |
    | microsoft/phi-3-mini-4k-instruct            | 4,096 tokens   | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.                                       |
    | microsoft/phi-3-small-8k-instruct           | 8,192 tokens   | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.                                       |
    | microsoft/phi-3-small-128k-instruct         | 128K tokens    | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.                                       |
    | microsoft/phi-3-medium-4k-instruct          | 4,096 tokens   | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.                                       |
    | microsoft/phi-3-medium-128k-instruct        | 128K tokens    | Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.                                       |
    | microsoft/phi-3.5-mini-instruct             | 128K tokens    | Lightweight multilingual LLM powering AI applications in latency bound, memory/compute constrained environments             |
    | microsoft/phi-3.5-moe-instruct              | 128K tokens    | Advanced LLM based on Mixture of Experts architecture to deliver compute efficient content generation                       |
    | microsoft/kosmos-2                          | 1,024 tokens   | Groundbreaking multimodal model designed to understand and reason about visual elements in images.                          |
    | microsoft/phi-3-vision-128k-instruct        | 128k tokens    | Cutting-edge open multimodal model exceling in high-quality reasoning from images.                                          |
    | microsoft/phi-3.5-vision-instruct           | 128k tokens    | Cutting-edge open multimodal model exceling in high-quality reasoning from images.                                          |
    | databricks/dbrx-instruct                    | 12k tokens     | A general-purpose LLM with state-of-the-art performance in language understanding, coding, and RAG.                         |
    | snowflake/arctic                            | 1,024 tokens   | Delivers high efficiency inference for enterprise applications focused on SQL generation and coding.                        |
    | aisingapore/sea-lion-7b-instruct            | 4,096 tokens   | LLM to represent and serve the linguistic and cultural diversity of Southeast Asia                                          |
    | ibm/granite-8b-code-instruct                | 4,096 tokens   | Software programming LLM for code generation, completion, explanation, and multi-turn conversion.                           |
    | ibm/granite-34b-code-instruct               | 8,192 tokens   | Software programming LLM for code generation, completion, explanation, and multi-turn conversion.                           |
    | ibm/granite-3.0-8b-instruct                 | 4,096 tokens   | Advanced Small Language Model supporting RAG, summarization, classification, code, and agentic AI                           |
    | ibm/granite-3.0-3b-a800m-instruct           | 4,096 tokens   | Highly efficient Mixture of Experts model for RAG, summarization, entity extraction, and classification                     |
    | mediatek/breeze-7b-instruct                 | 4,096 tokens   | Creates diverse synthetic data that mimics the characteristics of real-world data.                                          |
    | upstage/solar-10.7b-instruct                | 4,096 tokens   | Excels in NLP tasks, particularly in instruction-following, reasoning, and mathematics.                                     |
    | writer/palmyra-med-70b-32k                  | 32k tokens     | Leading LLM for accurate, contextually relevant responses in the medical domain.                                            |
    | writer/palmyra-med-70b                      | 32k tokens     | Leading LLM for accurate, contextually relevant responses in the medical domain.                                            |
    | writer/palmyra-fin-70b-32k                  | 32k tokens     | Specialized LLM for financial analysis, reporting, and data processing                                                      |
    | 01-ai/yi-large                              | 32k tokens     | Powerful model trained on English and Chinese for diverse tasks including chatbot and creative writing.                     |
    | deepseek-ai/deepseek-coder-6.7b-instruct    | 2k tokens      | Powerful coding model offering advanced capabilities in code generation, completion, and infilling                          |
    | rakuten/rakutenai-7b-instruct               | 1,024 tokens   | Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation.                         |
    | rakuten/rakutenai-7b-chat                   | 1,024 tokens   | Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation.                         |
    | baichuan-inc/baichuan2-13b-chat             | 4,096 tokens   | Support Chinese and English chat, coding, math, instruction following, solving quizzes                                      |
  </Accordion>

<Accordion title="Local NVIDIA NIM Deployed using WSL2">
    NVIDIA NIM enables you to run powerful LLMs locally on your Windows machine using WSL2 (Windows Subsystem for Linux).
    This approach allows you to leverage your NVIDIA GPU for private, secure, and cost-effective AI inference without relying on cloud services.
    Perfect for development, testing, or production scenarios where data privacy or offline capabilities are required.

Here is a step-by-step guide to setting up a local NVIDIA NIM model:

1. Follow installation instructions from [NVIDIA Website](https://docs.nvidia.com/nim/wsl2/latest/getting-started.html)

2. Install the local model. For Llama 3.1-8b follow [instructions](https://build.nvidia.com/meta/llama-3_1-8b-instruct/deploy)

3. Configure your crewai local models:

<Accordion title="Groq">
    Set the following environment variables in your `.env` file:

Example usage in your CrewAI project:

| Model            | Context Window | Best For                              |
    | ---------------- | -------------- | ------------------------------------- |
    | Llama 3.1 70B/8B | 131,072 tokens | High-performance, large context tasks |
    | Llama 3.2 Series | 8,192 tokens   | General-purpose tasks                 |
    | Mixtral 8x7B     | 32,768 tokens  | Balanced performance and context      |
  </Accordion>

<Accordion title="IBM watsonx.ai">
    Set the following environment variables in your `.env` file:

Example usage in your CrewAI project:

<Accordion title="Ollama (Local LLMs)">
    1. Install Ollama: [ollama.ai](https://ollama.ai/)
    2. Run a model: `ollama run llama3`
    3. Configure:

<Accordion title="Fireworks AI">
    Set the following environment variables in your `.env` file:

Example usage in your CrewAI project:

<Accordion title="Perplexity AI">
    Set the following environment variables in your `.env` file:

Example usage in your CrewAI project:

<Accordion title="Hugging Face">
    Set the following environment variables in your `.env` file:

Example usage in your CrewAI project:

<Accordion title="SambaNova">
    Set the following environment variables in your `.env` file:

Example usage in your CrewAI project:

| Model            | Context Window       | Best For                              |
    | ---------------- | -------------------- | ------------------------------------- |
    | Llama 3.1 70B/8B | Up to 131,072 tokens | High-performance, large context tasks |
    | Llama 3.1 405B   | 8,192 tokens         | High-performance and output quality   |
    | Llama 3.2 Series | 8,192 tokens         | General-purpose, multimodal tasks     |
    | Llama 3.3 70B    | Up to 131,072 tokens | High-performance and output quality   |
    | Qwen2 familly    | 8,192 tokens         | High-performance and output quality   |
  </Accordion>

<Accordion title="Cerebras">
    Set the following environment variables in your `.env` file:

Example usage in your CrewAI project:

<Info>
      Cerebras features:

* Fast inference speeds
      * Competitive pricing
      * Good balance of speed and quality
      * Support for long context windows
    </Info>
  </Accordion>

<Accordion title="Open Router">
    Set the following environment variables in your `.env` file:

Example usage in your CrewAI project:

<Info>
      Open Router models:

* openrouter/deepseek/deepseek-r1
      * openrouter/deepseek/deepseek-chat
    </Info>
  </Accordion>

<Accordion title="Nebius AI Studio">
    Set the following environment variables in your `.env` file:

Example usage in your CrewAI project:

<Info>
      Nebius AI Studio features:

* Large collection of open source models
      * Higher rate limits
      * Competitive pricing
      * Good balance of speed and quality
    </Info>
  </Accordion>
</AccordionGroup>

## Streaming Responses

CrewAI supports streaming responses from LLMs, allowing your application to receive and process outputs in real-time as they're generated.

<Tabs>
  <Tab title="Basic Setup">
    Enable streaming by setting the `stream` parameter to `True` when initializing your LLM:

When streaming is enabled, responses are delivered in chunks as they're generated, creating a more responsive user experience.
  </Tab>

<Tab title="Event Handling">
    CrewAI emits events for each chunk received during streaming:

<Tip>
      [Click here](/en/concepts/event-listener#event-listeners) for more details
    </Tip>
  </Tab>

<Tab title="Agent & Task Tracking">
    All LLM events in CrewAI include agent and task information, allowing you to track and filter LLM interactions by specific agents or tasks:

<Info>
      This feature is particularly useful for:

* Debugging specific agent behaviors
      * Logging LLM usage by task type
      * Auditing which agents are making what types of LLM calls
      * Performance monitoring of specific tasks
    </Info>
  </Tab>
</Tabs>

CrewAI supports asynchronous LLM calls for improved performance and concurrency in your AI workflows. Async calls allow you to run multiple LLM requests concurrently without blocking, making them ideal for high-throughput applications and parallel agent operations.

<Tabs>
  <Tab title="Basic Usage">
    Use the `acall` method for asynchronous LLM requests:

The `acall` method supports all the same parameters as the synchronous `call` method, including messages, tools, and callbacks.
  </Tab>

<Tab title="With Streaming">
    Combine async calls with streaming for real-time concurrent responses:

## Structured LLM Calls

CrewAI supports structured responses from LLM calls by allowing you to define a `response_format` using a Pydantic model. This enables the framework to automatically parse and validate the output, making it easier to integrate the response into your application without manual post-processing.

For example, you can define a Pydantic model to represent the expected response structure and pass it as the `response_format` when instantiating the LLM. The model will then be used to convert the LLM output into a structured Python object.

```python Code theme={null}
from crewai import LLM

class Dog(BaseModel):
    name: str
    age: int
    breed: str

llm = LLM(model="gpt-4o", response_format=Dog)

response = llm.call(
    "Analyze the following messages and return the name, age, and breed. "
    "Meet Kona! She is 3 years old and is a black german shepherd."
)
print(response)

**Examples:**

Example 1 (unknown):
```unknown
<Warning>
      Never commit API keys to version control. Use environment files (.env) or your system's secret management.
    </Warning>
  </Tab>

  <Tab title="2. YAML Configuration">
    Create a YAML file to define your agent configurations. This method is great for version control and team collaboration:
```

Example 2 (unknown):
```unknown
<Info>
      The YAML configuration allows you to:

      * Version control your agent settings
      * Easily switch between different models
      * Share configurations across team members
      * Document model choices and their purposes
    </Info>
  </Tab>

  <Tab title="3. Direct Code">
    For maximum flexibility, configure LLMs directly in your Python code:
```

Example 3 (unknown):
```unknown
<Info>
      Parameter explanations:

      * `temperature`: Controls randomness (0.0-1.0)
      * `timeout`: Maximum wait time for response
      * `max_tokens`: Limits response length
      * `top_p`: Alternative to temperature for sampling
      * `frequency_penalty`: Reduces word repetition
      * `presence_penalty`: Encourages new topics
      * `response_format`: Specifies output structure
      * `seed`: Ensures consistent outputs
    </Info>
  </Tab>
</Tabs>

## Provider Configuration Examples

CrewAI supports a multitude of LLM providers, each offering unique features, authentication methods, and model capabilities.
In this section, you'll find detailed examples that help you select, configure, and optimize the LLM that best fits your project's needs.

<AccordionGroup>
  <Accordion title="OpenAI">
    CrewAI provides native integration with OpenAI through the OpenAI Python SDK.
```

Example 4 (unknown):
```unknown
**Basic Usage:**
```

---

## Load agents from repositories

**URL:** llms-txt#load-agents-from-repositories

researcher = Agent(
    from_repository="market-research-agent"
)

writer = Agent(
    from_repository="content-writer-agent"
)

---

## Managed agent on Bedrock

**URL:** llms-txt#managed-agent-on-bedrock

**Contents:**
- **Best Practices**

knowledge_router = BedrockInvokeAgentTool(
    agent_id="bedrock-agent-id",
    agent_alias_id="prod",
)

automation_strategist = Agent(
    role="Automation Strategist",
    goal="Orchestrate external automations and summarise their output",
    backstory="You coordinate enterprise workflows and know when to delegate tasks to specialised services.",
    tools=[analysis_automation, knowledge_router],
    verbose=True,
)

execute_playbook = Task(
    description="Run the analysis automation and ask the Bedrock agent for executive talking points.",
    agent=automation_strategist,
)

Crew(agents=[automation_strategist], tasks=[execute_playbook]).kickoff()
```

## **Best Practices**

* **Secure credentials**: Store API keys and bearer tokens in environment variables or a secrets manager
* **Plan for latency**: External automations may take longer—set appropriate polling intervals and timeouts
* **Reuse sessions**: Bedrock Agents support session IDs so you can maintain context across multiple tool calls
* **Validate responses**: Normalise remote output (JSON, text, status codes) before forwarding it to downstream tasks
* **Monitor usage**: Track audit logs in CrewAI Platform or AWS CloudWatch to stay ahead of quota limits and failures

---

## Microsoft Excel Integration

**URL:** llms-txt#microsoft-excel-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Microsoft Excel Integration
  - 1. Connect Your Microsoft Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Excel Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/microsoft_excel

Workbook and data management with Microsoft Excel integration for CrewAI.

Enable your agents to create and manage Excel workbooks, worksheets, tables, and charts in OneDrive or SharePoint. Manipulate data ranges, create visualizations, manage tables, and streamline your spreadsheet workflows with AI-powered automation.

Before using the Microsoft Excel integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Microsoft 365 account with Excel and OneDrive/SharePoint access
* Connected your Microsoft account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Microsoft Excel Integration

### 1. Connect Your Microsoft Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Microsoft Excel** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for files and Excel workbook access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="microsoft_excel/create_workbook">
    **Description:** Create a new Excel workbook in OneDrive or SharePoint.

* `file_path` (string, required): Path where to create the workbook (e.g., 'MyWorkbook.xlsx')
    * `worksheets` (array, optional): Initial worksheets to create
      
  </Accordion>

<Accordion title="microsoft_excel/get_workbooks">
    **Description:** Get all Excel workbooks from OneDrive or SharePoint.

* `select` (string, optional): Select specific properties to return
    * `filter` (string, optional): Filter results using OData syntax
    * `expand` (string, optional): Expand related resources inline
    * `top` (integer, optional): Number of items to return. Minimum: 1, Maximum: 999
    * `orderby` (string, optional): Order results by specified properties
  </Accordion>

<Accordion title="microsoft_excel/get_worksheets">
    **Description:** Get all worksheets in an Excel workbook.

* `file_id` (string, required): The ID of the Excel file
    * `select` (string, optional): Select specific properties to return (e.g., 'id,name,position')
    * `filter` (string, optional): Filter results using OData syntax
    * `expand` (string, optional): Expand related resources inline
    * `top` (integer, optional): Number of items to return. Minimum: 1, Maximum: 999
    * `orderby` (string, optional): Order results by specified properties
  </Accordion>

<Accordion title="microsoft_excel/create_worksheet">
    **Description:** Create a new worksheet in an Excel workbook.

* `file_id` (string, required): The ID of the Excel file
    * `name` (string, required): Name of the new worksheet
  </Accordion>

<Accordion title="microsoft_excel/get_range_data">
    **Description:** Get data from a specific range in an Excel worksheet.

* `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `range` (string, required): Range address (e.g., 'A1:C10')
  </Accordion>

<Accordion title="microsoft_excel/update_range_data">
    **Description:** Update data in a specific range in an Excel worksheet.

* `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `range` (string, required): Range address (e.g., 'A1:C10')
    * `values` (array, required): 2D array of values to set in the range
      
  </Accordion>

<Accordion title="microsoft_excel/add_table">
    **Description:** Create a table in an Excel worksheet.

* `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `range` (string, required): Range for the table (e.g., 'A1:D10')
    * `has_headers` (boolean, optional): Whether the first row contains headers. Default: true
  </Accordion>

<Accordion title="microsoft_excel/get_tables">
    **Description:** Get all tables in an Excel worksheet.

* `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
  </Accordion>

<Accordion title="microsoft_excel/add_table_row">
    **Description:** Add a new row to an Excel table.

* `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `table_name` (string, required): Name of the table
    * `values` (array, required): Array of values for the new row
      
  </Accordion>

<Accordion title="microsoft_excel/create_chart">
    **Description:** Create a chart in an Excel worksheet.

* `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `chart_type` (string, required): Type of chart (e.g., 'ColumnClustered', 'Line', 'Pie')
    * `source_data` (string, required): Range of data for the chart (e.g., 'A1:B10')
    * `series_by` (string, optional): How to interpret the data ('Auto', 'Columns', or 'Rows'). Default: Auto
  </Accordion>

<Accordion title="microsoft_excel/get_cell">
    **Description:** Get the value of a single cell in an Excel worksheet.

* `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `row` (integer, required): Row number (0-based)
    * `column` (integer, required): Column number (0-based)
  </Accordion>

<Accordion title="microsoft_excel/get_used_range">
    **Description:** Get the used range of an Excel worksheet (contains all data).

* `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
  </Accordion>

<Accordion title="microsoft_excel/list_charts">
    **Description:** Get all charts in an Excel worksheet.

* `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
  </Accordion>

<Accordion title="microsoft_excel/delete_worksheet">
    **Description:** Delete a worksheet from an Excel workbook.

* `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet to delete
  </Accordion>

<Accordion title="microsoft_excel/delete_table">
    **Description:** Delete a table from an Excel worksheet.

* `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `table_name` (string, required): Name of the table to delete
  </Accordion>

<Accordion title="microsoft_excel/list_names">
    **Description:** Get all named ranges in an Excel workbook.

* `file_id` (string, required): The ID of the Excel file
  </Accordion>
</AccordionGroup>

### Basic Excel Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="microsoft_excel/create_workbook">
    **Description:** Create a new Excel workbook in OneDrive or SharePoint.

    **Parameters:**

    * `file_path` (string, required): Path where to create the workbook (e.g., 'MyWorkbook.xlsx')
    * `worksheets` (array, optional): Initial worksheets to create
```

Example 4 (unknown):
```unknown
</Accordion>

  <Accordion title="microsoft_excel/get_workbooks">
    **Description:** Get all Excel workbooks from OneDrive or SharePoint.

    **Parameters:**

    * `select` (string, optional): Select specific properties to return
    * `filter` (string, optional): Filter results using OData syntax
    * `expand` (string, optional): Expand related resources inline
    * `top` (integer, optional): Number of items to return. Minimum: 1, Maximum: 999
    * `orderby` (string, optional): Order results by specified properties
  </Accordion>

  <Accordion title="microsoft_excel/get_worksheets">
    **Description:** Get all worksheets in an Excel workbook.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `select` (string, optional): Select specific properties to return (e.g., 'id,name,position')
    * `filter` (string, optional): Filter results using OData syntax
    * `expand` (string, optional): Expand related resources inline
    * `top` (integer, optional): Number of items to return. Minimum: 1, Maximum: 999
    * `orderby` (string, optional): Order results by specified properties
  </Accordion>

  <Accordion title="microsoft_excel/create_worksheet">
    **Description:** Create a new worksheet in an Excel workbook.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `name` (string, required): Name of the new worksheet
  </Accordion>

  <Accordion title="microsoft_excel/get_range_data">
    **Description:** Get data from a specific range in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `range` (string, required): Range address (e.g., 'A1:C10')
  </Accordion>

  <Accordion title="microsoft_excel/update_range_data">
    **Description:** Update data in a specific range in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `range` (string, required): Range address (e.g., 'A1:C10')
    * `values` (array, required): 2D array of values to set in the range
```

---

## Microsoft OneDrive Integration

**URL:** llms-txt#microsoft-onedrive-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Microsoft OneDrive Integration
  - 1. Connect Your Microsoft Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Microsoft OneDrive Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/microsoft_onedrive

File and folder management with Microsoft OneDrive integration for CrewAI.

Enable your agents to upload, download, and manage files and folders in Microsoft OneDrive. Automate file operations, organize content, create sharing links, and streamline your cloud storage workflows with AI-powered automation.

Before using the Microsoft OneDrive integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Microsoft account with OneDrive access
* Connected your Microsoft account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Microsoft OneDrive Integration

### 1. Connect Your Microsoft Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Microsoft OneDrive** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for file access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="microsoft_onedrive/list_files">
    **Description:** List files and folders in OneDrive.

* `top` (integer, optional): Number of items to retrieve (max 1000). Default is `50`.
    * `orderby` (string, optional): Order by field (e.g., "name asc", "lastModifiedDateTime desc"). Default is "name asc".
    * `filter` (string, optional): OData filter expression.
  </Accordion>

<Accordion title="microsoft_onedrive/get_file_info">
    **Description:** Get information about a specific file or folder.

* `item_id` (string, required): The ID of the file or folder.
  </Accordion>

<Accordion title="microsoft_onedrive/download_file">
    **Description:** Download a file from OneDrive.

* `item_id` (string, required): The ID of the file to download.
  </Accordion>

<Accordion title="microsoft_onedrive/upload_file">
    **Description:** Upload a file to OneDrive.

* `file_name` (string, required): Name of the file to upload.
    * `content` (string, required): Base64 encoded file content.
  </Accordion>

<Accordion title="microsoft_onedrive/create_folder">
    **Description:** Create a new folder in OneDrive.

* `folder_name` (string, required): Name of the folder to create.
  </Accordion>

<Accordion title="microsoft_onedrive/delete_item">
    **Description:** Delete a file or folder from OneDrive.

* `item_id` (string, required): The ID of the file or folder to delete.
  </Accordion>

<Accordion title="microsoft_onedrive/copy_item">
    **Description:** Copy a file or folder in OneDrive.

* `item_id` (string, required): The ID of the file or folder to copy.
    * `parent_id` (string, optional): The ID of the destination folder (optional, defaults to root).
    * `new_name` (string, optional): New name for the copied item (optional).
  </Accordion>

<Accordion title="microsoft_onedrive/move_item">
    **Description:** Move a file or folder in OneDrive.

* `item_id` (string, required): The ID of the file or folder to move.
    * `parent_id` (string, required): The ID of the destination folder.
    * `new_name` (string, optional): New name for the item (optional).
  </Accordion>

<Accordion title="microsoft_onedrive/search_files">
    **Description:** Search for files and folders in OneDrive.

* `query` (string, required): Search query string.
    * `top` (integer, optional): Number of results to return (max 1000). Default is `50`.
  </Accordion>

<Accordion title="microsoft_onedrive/share_item">
    **Description:** Create a sharing link for a file or folder.

* `item_id` (string, required): The ID of the file or folder to share.
    * `type` (string, optional): Type of sharing link. Enum: `view`, `edit`, `embed`. Default is `view`.
    * `scope` (string, optional): Scope of the sharing link. Enum: `anonymous`, `organization`. Default is `anonymous`.
  </Accordion>

<Accordion title="microsoft_onedrive/get_thumbnails">
    **Description:** Get thumbnails for a file.

* `item_id` (string, required): The ID of the file.
  </Accordion>
</AccordionGroup>

### Basic Microsoft OneDrive Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="microsoft_onedrive/list_files">
    **Description:** List files and folders in OneDrive.

    **Parameters:**

    * `top` (integer, optional): Number of items to retrieve (max 1000). Default is `50`.
    * `orderby` (string, optional): Order by field (e.g., "name asc", "lastModifiedDateTime desc"). Default is "name asc".
    * `filter` (string, optional): OData filter expression.
  </Accordion>

  <Accordion title="microsoft_onedrive/get_file_info">
    **Description:** Get information about a specific file or folder.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder.
  </Accordion>

  <Accordion title="microsoft_onedrive/download_file">
    **Description:** Download a file from OneDrive.

    **Parameters:**

    * `item_id` (string, required): The ID of the file to download.
  </Accordion>

  <Accordion title="microsoft_onedrive/upload_file">
    **Description:** Upload a file to OneDrive.

    **Parameters:**

    * `file_name` (string, required): Name of the file to upload.
    * `content` (string, required): Base64 encoded file content.
  </Accordion>

  <Accordion title="microsoft_onedrive/create_folder">
    **Description:** Create a new folder in OneDrive.

    **Parameters:**

    * `folder_name` (string, required): Name of the folder to create.
  </Accordion>

  <Accordion title="microsoft_onedrive/delete_item">
    **Description:** Delete a file or folder from OneDrive.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder to delete.
  </Accordion>

  <Accordion title="microsoft_onedrive/copy_item">
    **Description:** Copy a file or folder in OneDrive.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder to copy.
    * `parent_id` (string, optional): The ID of the destination folder (optional, defaults to root).
    * `new_name` (string, optional): New name for the copied item (optional).
  </Accordion>

  <Accordion title="microsoft_onedrive/move_item">
    **Description:** Move a file or folder in OneDrive.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder to move.
    * `parent_id` (string, required): The ID of the destination folder.
    * `new_name` (string, optional): New name for the item (optional).
  </Accordion>

  <Accordion title="microsoft_onedrive/search_files">
    **Description:** Search for files and folders in OneDrive.

    **Parameters:**

    * `query` (string, required): Search query string.
    * `top` (integer, optional): Number of results to return (max 1000). Default is `50`.
  </Accordion>

  <Accordion title="microsoft_onedrive/share_item">
    **Description:** Create a sharing link for a file or folder.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder to share.
    * `type` (string, optional): Type of sharing link. Enum: `view`, `edit`, `embed`. Default is `view`.
    * `scope` (string, optional): Scope of the sharing link. Enum: `anonymous`, `organization`. Default is `anonymous`.
  </Accordion>

  <Accordion title="microsoft_onedrive/get_thumbnails">
    **Description:** Get thumbnails for a file.

    **Parameters:**

    * `item_id` (string, required): The ID of the file.
  </Accordion>
</AccordionGroup>

## Usage Examples

### Basic Microsoft OneDrive Agent Setup
```

---

## Microsoft SharePoint Integration

**URL:** llms-txt#microsoft-sharepoint-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Microsoft SharePoint Integration
  - 1. Connect Your Microsoft Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic SharePoint Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/microsoft_sharepoint

Site, list, and document management with Microsoft SharePoint integration for CrewAI.

Enable your agents to access and manage SharePoint sites, lists, and document libraries. Retrieve site information, manage list items, upload and organize files, and streamline your SharePoint workflows with AI-powered automation.

Before using the Microsoft SharePoint integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Microsoft 365 account with SharePoint access
* Connected your Microsoft account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Microsoft SharePoint Integration

### 1. Connect Your Microsoft Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Microsoft SharePoint** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for SharePoint sites and content access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="microsoft_sharepoint/get_sites">
    **Description:** Get all SharePoint sites the user has access to.

* `search` (string, optional): Search query to filter sites
    * `select` (string, optional): Select specific properties to return (e.g., 'displayName,id,webUrl')
    * `filter` (string, optional): Filter results using OData syntax
    * `expand` (string, optional): Expand related resources inline
    * `top` (integer, optional): Number of items to return. Minimum: 1, Maximum: 999
    * `skip` (integer, optional): Number of items to skip. Minimum: 0
    * `orderby` (string, optional): Order results by specified properties (e.g., 'displayName desc')
  </Accordion>

<Accordion title="microsoft_sharepoint/get_site">
    **Description:** Get information about a specific SharePoint site.

* `site_id` (string, required): The ID of the SharePoint site
    * `select` (string, optional): Select specific properties to return (e.g., 'displayName,id,webUrl,drives')
    * `expand` (string, optional): Expand related resources inline (e.g., 'drives,lists')
  </Accordion>

<Accordion title="microsoft_sharepoint/get_site_lists">
    **Description:** Get all lists in a SharePoint site.

* `site_id` (string, required): The ID of the SharePoint site
  </Accordion>

<Accordion title="microsoft_sharepoint/get_list">
    **Description:** Get information about a specific list.

* `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
  </Accordion>

<Accordion title="microsoft_sharepoint/get_list_items">
    **Description:** Get items from a SharePoint list.

* `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `expand` (string, optional): Expand related data (e.g., 'fields')
  </Accordion>

<Accordion title="microsoft_sharepoint/create_list_item">
    **Description:** Create a new item in a SharePoint list.

* `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `fields` (object, required): The field values for the new item
      
  </Accordion>

<Accordion title="microsoft_sharepoint/update_list_item">
    **Description:** Update an item in a SharePoint list.

* `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `item_id` (string, required): The ID of the item to update
    * `fields` (object, required): The field values to update
      
  </Accordion>

<Accordion title="microsoft_sharepoint/delete_list_item">
    **Description:** Delete an item from a SharePoint list.

* `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `item_id` (string, required): The ID of the item to delete
  </Accordion>

<Accordion title="microsoft_sharepoint/upload_file_to_library">
    **Description:** Upload a file to a SharePoint document library.

* `site_id` (string, required): The ID of the SharePoint site
    * `file_path` (string, required): The path where to upload the file (e.g., 'folder/filename.txt')
    * `content` (string, required): The file content to upload
  </Accordion>

<Accordion title="microsoft_sharepoint/get_drive_items">
    **Description:** Get files and folders from a SharePoint document library.

* `site_id` (string, required): The ID of the SharePoint site
  </Accordion>

<Accordion title="microsoft_sharepoint/delete_drive_item">
    **Description:** Delete a file or folder from SharePoint document library.

* `site_id` (string, required): The ID of the SharePoint site
    * `item_id` (string, required): The ID of the file or folder to delete
  </Accordion>
</AccordionGroup>

### Basic SharePoint Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="microsoft_sharepoint/get_sites">
    **Description:** Get all SharePoint sites the user has access to.

    **Parameters:**

    * `search` (string, optional): Search query to filter sites
    * `select` (string, optional): Select specific properties to return (e.g., 'displayName,id,webUrl')
    * `filter` (string, optional): Filter results using OData syntax
    * `expand` (string, optional): Expand related resources inline
    * `top` (integer, optional): Number of items to return. Minimum: 1, Maximum: 999
    * `skip` (integer, optional): Number of items to skip. Minimum: 0
    * `orderby` (string, optional): Order results by specified properties (e.g., 'displayName desc')
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_site">
    **Description:** Get information about a specific SharePoint site.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `select` (string, optional): Select specific properties to return (e.g., 'displayName,id,webUrl,drives')
    * `expand` (string, optional): Expand related resources inline (e.g., 'drives,lists')
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_site_lists">
    **Description:** Get all lists in a SharePoint site.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_list">
    **Description:** Get information about a specific list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_list_items">
    **Description:** Get items from a SharePoint list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `expand` (string, optional): Expand related data (e.g., 'fields')
  </Accordion>

  <Accordion title="microsoft_sharepoint/create_list_item">
    **Description:** Create a new item in a SharePoint list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `fields` (object, required): The field values for the new item
```

Example 4 (unknown):
```unknown
</Accordion>

  <Accordion title="microsoft_sharepoint/update_list_item">
    **Description:** Update an item in a SharePoint list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `item_id` (string, required): The ID of the item to update
    * `fields` (object, required): The field values to update
```

---

## Microsoft Teams Integration

**URL:** llms-txt#microsoft-teams-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Microsoft Teams Integration
  - 1. Connect Your Microsoft Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Microsoft Teams Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/microsoft_teams

Team collaboration and communication with Microsoft Teams integration for CrewAI.

Enable your agents to access Teams data, send messages, create meetings, and manage channels. Automate team communication, schedule meetings, retrieve messages, and streamline your collaboration workflows with AI-powered automation.

Before using the Microsoft Teams integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Microsoft account with Teams access
* Connected your Microsoft account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Microsoft Teams Integration

### 1. Connect Your Microsoft Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Microsoft Teams** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for Teams access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="microsoft_teams/get_teams">
    **Description:** Get all teams the user is a member of.

* No parameters required.
  </Accordion>

<Accordion title="microsoft_teams/get_channels">
    **Description:** Get channels in a specific team.

* `team_id` (string, required): The ID of the team.
  </Accordion>

<Accordion title="microsoft_teams/send_message">
    **Description:** Send a message to a Teams channel.

* `team_id` (string, required): The ID of the team.
    * `channel_id` (string, required): The ID of the channel.
    * `message` (string, required): The message content.
    * `content_type` (string, optional): Content type (html or text). Enum: `html`, `text`. Default is `text`.
  </Accordion>

<Accordion title="microsoft_teams/get_messages">
    **Description:** Get messages from a Teams channel.

* `team_id` (string, required): The ID of the team.
    * `channel_id` (string, required): The ID of the channel.
    * `top` (integer, optional): Number of messages to retrieve (max 50). Default is `20`.
  </Accordion>

<Accordion title="microsoft_teams/create_meeting">
    **Description:** Create a Teams meeting.

* `subject` (string, required): Meeting subject/title.
    * `startDateTime` (string, required): Meeting start time (ISO 8601 format with timezone).
    * `endDateTime` (string, required): Meeting end time (ISO 8601 format with timezone).
  </Accordion>

<Accordion title="microsoft_teams/search_online_meetings_by_join_url">
    **Description:** Search online meetings by Join Web URL.

* `join_web_url` (string, required): The join web URL of the meeting to search for.
  </Accordion>
</AccordionGroup>

### Basic Microsoft Teams Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="microsoft_teams/get_teams">
    **Description:** Get all teams the user is a member of.

    **Parameters:**

    * No parameters required.
  </Accordion>

  <Accordion title="microsoft_teams/get_channels">
    **Description:** Get channels in a specific team.

    **Parameters:**

    * `team_id` (string, required): The ID of the team.
  </Accordion>

  <Accordion title="microsoft_teams/send_message">
    **Description:** Send a message to a Teams channel.

    **Parameters:**

    * `team_id` (string, required): The ID of the team.
    * `channel_id` (string, required): The ID of the channel.
    * `message` (string, required): The message content.
    * `content_type` (string, optional): Content type (html or text). Enum: `html`, `text`. Default is `text`.
  </Accordion>

  <Accordion title="microsoft_teams/get_messages">
    **Description:** Get messages from a Teams channel.

    **Parameters:**

    * `team_id` (string, required): The ID of the team.
    * `channel_id` (string, required): The ID of the channel.
    * `top` (integer, optional): Number of messages to retrieve (max 50). Default is `20`.
  </Accordion>

  <Accordion title="microsoft_teams/create_meeting">
    **Description:** Create a Teams meeting.

    **Parameters:**

    * `subject` (string, required): Meeting subject/title.
    * `startDateTime` (string, required): Meeting start time (ISO 8601 format with timezone).
    * `endDateTime` (string, required): Meeting end time (ISO 8601 format with timezone).
  </Accordion>

  <Accordion title="microsoft_teams/search_online_meetings_by_join_url">
    **Description:** Search online meetings by Join Web URL.

    **Parameters:**

    * `join_web_url` (string, required): The join web URL of the meeting to search for.
  </Accordion>
</AccordionGroup>

## Usage Examples

### Basic Microsoft Teams Agent Setup
```

---

## Microsoft Teams Trigger

**URL:** llms-txt#microsoft-teams-trigger

**Contents:**
- Overview
- Enabling the Microsoft Teams Trigger
- Example: Summarize a new chat thread
- Testing Locally

Source: https://docs.crewai.com/en/enterprise/guides/microsoft-teams-trigger

Kick off crews from Microsoft Teams chat activity

Use the Microsoft Teams trigger to start automations whenever a new chat is created. Common patterns include summarizing inbound requests, routing urgent messages to support teams, or creating follow-up tasks in other systems.

<Tip>
  Confirm Microsoft Teams is connected under **Tools & Integrations** and enabled in the **Triggers** tab for your deployment.
</Tip>

## Enabling the Microsoft Teams Trigger

1. Open your deployment in CrewAI AOP
2. Go to the **Triggers** tab
3. Locate **Microsoft Teams** and switch the toggle to enable

<Frame caption="Microsoft Teams trigger connection">
  <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=21eced4a8a635d17e32dccbeaf4ac217" alt="Enable or disable triggers with toggle" data-og-width="2192" width="2192" data-og-height="492" height="492" data-path="images/enterprise/msteams-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=3acc624c7b67651b5cd41df314902c41 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=1270b8fb54dc348f6cd242d2f3fd6480 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=76c96b3b169dd164c31e7bf88d4fdd8c 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=04b9e72848e035c107a0857ae708a0f3 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=bee29617f472e6d4709d74c764d201c8 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=c73be9f59015ab22173857ce635a2be9 2500w" />
</Frame>

## Example: Summarize a new chat thread

The crew parses thread metadata (subject, created time, roster) and generates an action plan for the receiving team.

Test your Microsoft Teams trigger integration locally using the CrewAI CLI:

```bash  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
The crew parses thread metadata (subject, created time, roster) and generates an action plan for the receiving team.

## Testing Locally

Test your Microsoft Teams trigger integration locally using the CrewAI CLI:
```

---

## Microsoft Word Integration

**URL:** llms-txt#microsoft-word-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Microsoft Word Integration
  - 1. Connect Your Microsoft Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Microsoft Word Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/microsoft_word

Document creation and management with Microsoft Word integration for CrewAI.

Enable your agents to create, read, and manage Word documents and text files in OneDrive or SharePoint. Automate document creation, retrieve content, manage document properties, and streamline your document workflows with AI-powered automation.

Before using the Microsoft Word integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Microsoft account with Word and OneDrive/SharePoint access
* Connected your Microsoft account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Microsoft Word Integration

### 1. Connect Your Microsoft Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Microsoft Word** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for file access
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="microsoft_word/get_documents">
    **Description:** Get all Word documents from OneDrive or SharePoint.

* `select` (string, optional): Select specific properties to return.
    * `filter` (string, optional): Filter results using OData syntax.
    * `expand` (string, optional): Expand related resources inline.
    * `top` (integer, optional): Number of items to return (min 1, max 999).
    * `orderby` (string, optional): Order results by specified properties.
  </Accordion>

<Accordion title="microsoft_word/create_text_document">
    **Description:** Create a text document (.txt) with content. RECOMMENDED for programmatic content creation that needs to be readable and editable.

* `file_name` (string, required): Name of the text document (should end with .txt).
    * `content` (string, optional): Text content for the document. Default is "This is a new text document created via API."
  </Accordion>

<Accordion title="microsoft_word/get_document_content">
    **Description:** Get the content of a document (works best with text files).

* `file_id` (string, required): The ID of the document.
  </Accordion>

<Accordion title="microsoft_word/get_document_properties">
    **Description:** Get properties and metadata of a document.

* `file_id` (string, required): The ID of the document.
  </Accordion>

<Accordion title="microsoft_word/delete_document">
    **Description:** Delete a document.

* `file_id` (string, required): The ID of the document to delete.
  </Accordion>
</AccordionGroup>

### Basic Microsoft Word Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="microsoft_word/get_documents">
    **Description:** Get all Word documents from OneDrive or SharePoint.

    **Parameters:**

    * `select` (string, optional): Select specific properties to return.
    * `filter` (string, optional): Filter results using OData syntax.
    * `expand` (string, optional): Expand related resources inline.
    * `top` (integer, optional): Number of items to return (min 1, max 999).
    * `orderby` (string, optional): Order results by specified properties.
  </Accordion>

  <Accordion title="microsoft_word/create_text_document">
    **Description:** Create a text document (.txt) with content. RECOMMENDED for programmatic content creation that needs to be readable and editable.

    **Parameters:**

    * `file_name` (string, required): Name of the text document (should end with .txt).
    * `content` (string, optional): Text content for the document. Default is "This is a new text document created via API."
  </Accordion>

  <Accordion title="microsoft_word/get_document_content">
    **Description:** Get the content of a document (works best with text files).

    **Parameters:**

    * `file_id` (string, required): The ID of the document.
  </Accordion>

  <Accordion title="microsoft_word/get_document_properties">
    **Description:** Get properties and metadata of a document.

    **Parameters:**

    * `file_id` (string, required): The ID of the document.
  </Accordion>

  <Accordion title="microsoft_word/delete_document">
    **Description:** Delete a document.

    **Parameters:**

    * `file_id` (string, required): The ID of the document to delete.
  </Accordion>
</AccordionGroup>

## Usage Examples

### Basic Microsoft Word Agent Setup
```

---

## Notion Integration

**URL:** llms-txt#notion-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Notion Integration
  - 1. Connect Your Notion Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Actions
- Usage Examples
  - Basic Notion Agent Setup

Source: https://docs.crewai.com/en/enterprise/integrations/notion

User management and commenting with Notion integration for CrewAI.

Enable your agents to manage users and create comments through Notion. Access workspace user information and create comments on pages and discussions, streamlining your collaboration workflows with AI-powered automation.

Before using the Notion integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Notion account with appropriate workspace permissions
* Connected your Notion account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)

## Setting Up Notion Integration

### 1. Connect Your Notion Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Notion** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for user access and comment creation
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

<AccordionGroup>
  <Accordion title="notion/list_users">
    **Description:** List all users in the workspace.

* `page_size` (integer, optional): Number of items returned in the response. Minimum: 1, Maximum: 100, Default: 100
    * `start_cursor` (string, optional): Cursor for pagination. Return results after this cursor.
  </Accordion>

<Accordion title="notion/get_user">
    **Description:** Retrieve a specific user by ID.

* `user_id` (string, required): The ID of the user to retrieve.
  </Accordion>

<Accordion title="notion/create_comment">
    **Description:** Create a comment on a page or discussion.

* `parent` (object, required): The parent page or discussion to comment on.
      
      or
      
    * `rich_text` (array, required): The rich text content of the comment.
      
  </Accordion>
</AccordionGroup>

### Basic Notion Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Actions

<AccordionGroup>
  <Accordion title="notion/list_users">
    **Description:** List all users in the workspace.

    **Parameters:**

    * `page_size` (integer, optional): Number of items returned in the response. Minimum: 1, Maximum: 100, Default: 100
    * `start_cursor` (string, optional): Cursor for pagination. Return results after this cursor.
  </Accordion>

  <Accordion title="notion/get_user">
    **Description:** Retrieve a specific user by ID.

    **Parameters:**

    * `user_id` (string, required): The ID of the user to retrieve.
  </Accordion>

  <Accordion title="notion/create_comment">
    **Description:** Create a comment on a page or discussion.

    **Parameters:**

    * `parent` (object, required): The parent page or discussion to comment on.
```

Example 4 (unknown):
```unknown
or
```

---

## No crew knowledge needed

**URL:** llms-txt#no-crew-knowledge-needed

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()  # Works perfectly
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
#### Example 2: Both Agent and Crew Knowledge
```

---

## No crew-level knowledge required

**URL:** llms-txt#no-crew-level-knowledge-required

crew = Crew(
    agents=[specialist_agent],
    tasks=[task]
)

result = crew.kickoff()  # Agent knowledge works independently
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
#### What Happens During `crew.kickoff()`

When you call `crew.kickoff()`, here's the exact sequence:
```

---

## Open Telemetry Logs

**URL:** llms-txt#open-telemetry-logs

**Contents:**
- Prerequisites
- How to capture telemetry logs

Source: https://docs.crewai.com/en/enterprise/guides/capture_telemetry_logs

Understand how to capture telemetry logs from your CrewAI AOP deployments

CrewAI AOP provides a powerful way to capture telemetry logs from your deployments. This allows you to monitor the performance of your agents and workflows, and to debug issues that may arise.

<CardGroup cols={2}>
  <Card title="ENTERPRISE OTEL SETUP enabled" icon="users">
    Your organization should have ENTERPRISE OTEL SETUP enabled
  </Card>

<Card title="OTEL collector setup" icon="server">
    Your organization should have an OTEL collector setup or a provider like Datadog log intake setup
  </Card>
</CardGroup>

## How to capture telemetry logs

1. Go to settings/organization tab
2. Configure your OTEL collector setup
3. Save

Example to setup OTEL log collection capture to Datadog.

<Frame>
    <img src="https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=5bb359765661a61f7012824fe35b0978" alt="Capture Telemetry Logs" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/crewai-otel-export.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=280&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=2bee9ddb6077fca900cc42e98c1c1c77 280w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=560&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=ceae34948ba9b7daeff1a277d78f8991 560w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=840&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=3e86994eb05fe4c9005a8a62f272b618 840w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=1100&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=3b498ed5c28cb90d415721f636e16ac3 1100w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=1650&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=35463fcfaa322eacbb1e862ce638a093 1650w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=2500&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=fa9f64fe474823fedc93cfdf66d36b4b 2500w" />
</Frame>

---

## Option 1: Match your LLM provider

**URL:** llms-txt#option-1:-match-your-llm-provider

crew = Crew(
    agents=[agent],
    tasks=[task],
    memory=True,
    embedder={
        "provider": "anthropic", # Match your LLM provider
        "config": {
            "api_key": "your-anthropic-key",
            "model": "text-embedding-3-small"
        }
    }
)

---

## Option 1: Use Voyage AI (recommended by Anthropic for Claude users)

**URL:** llms-txt#option-1:-use-voyage-ai-(recommended-by-anthropic-for-claude-users)

crew = Crew(
    agents=[agent],
    tasks=[...],
    knowledge_sources=[knowledge_source],
    embedder={
        "provider": "voyageai",  # Recommended for Claude users
        "config": {
            "api_key": "your-voyage-api-key",
            "model": "voyage-3"  # or "voyage-3-large" for best quality
        }
    }
)

---

## Option 2: Use local embeddings (no external API calls)

**URL:** llms-txt#option-2:-use-local-embeddings-(no-external-api-calls)

**Contents:**
  - Debugging Storage Issues

crew = Crew(
    agents=[agent],
    tasks=[task],
    memory=True,
    embedder={
        "provider": "ollama",
        "config": {"model": "mxbai-embed-large"}
    }
)
python  theme={null}
import os
from crewai.utilities.paths import db_storage_path

storage_path = db_storage_path()
print(f"Storage path: {storage_path}")
print(f"Path exists: {os.path.exists(storage_path)}")
print(f"Is writable: {os.access(storage_path, os.W_OK) if os.path.exists(storage_path) else 'Path does not exist'}")

**Examples:**

Example 1 (unknown):
```unknown
### Debugging Storage Issues

#### Check Storage Permissions
```

---

## Or use consistent embedding providers

**URL:** llms-txt#or-use-consistent-embedding-providers

crew = Crew(
    agents=[...],
    tasks=[...],
    knowledge_sources=[...],
    embedder={"provider": "openai", "config": {"model": "text-embedding-3-small"}}
)
bash  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
**"ChromaDB permission denied" errors:**
```

---

## Overview

**URL:** llms-txt#overview

**Contents:**
- **Available Tools**
- **Common Use Cases**
- **Quick Start Example**

Source: https://docs.crewai.com/en/tools/integration/overview

Connect CrewAI agents with external automations and managed AI services

Integration tools let your agents hand off work to other automation platforms and managed AI services. Use them when a workflow needs to invoke an existing CrewAI deployment or delegate specialised tasks to providers such as Amazon Bedrock.

## **Available Tools**

<CardGroup cols={2}>
  <Card title="CrewAI Run Automation Tool" icon="robot" href="/en/tools/integration/crewaiautomationtool">
    Invoke live CrewAI Platform automations, pass custom inputs, and poll for results directly from your agent.
  </Card>

<Card title="Bedrock Invoke Agent Tool" icon="aws" href="/en/tools/integration/bedrockinvokeagenttool">
    Call Amazon Bedrock Agents from your crews, reuse AWS guardrails, and stream responses back into the workflow.
  </Card>
</CardGroup>

## **Common Use Cases**

* **Chain automations**: Kick off an existing CrewAI deployment from within another crew or flow
* **Enterprise hand-off**: Route tasks to Bedrock Agents that already encapsulate company logic and guardrails
* **Hybrid workflows**: Combine CrewAI reasoning with downstream systems that expose their own agent APIs
* **Long-running jobs**: Poll external automations and merge the final results back into the current run

## **Quick Start Example**

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import InvokeCrewAIAutomationTool
from crewai_tools.aws.bedrock.agents.invoke_agent_tool import BedrockInvokeAgentTool

---

## Patronus AI Evaluation

**URL:** llms-txt#patronus-ai-evaluation

**Contents:**
- Overview
- Key Features
- Evaluation Tools
- Installation
- Steps to Get Started
- Examples
  - Using PatronusEvalTool

[Patronus AI](https://patronus.ai) provides comprehensive evaluation and monitoring capabilities for CrewAI agents, enabling you to assess model outputs, agent behaviors, and overall system performance. This integration allows you to implement continuous evaluation workflows that help maintain quality and reliability in production environments.

* **Automated Evaluation**: Real-time assessment of agent outputs and behaviors
* **Custom Criteria**: Define specific evaluation criteria tailored to your use cases
* **Performance Monitoring**: Track agent performance metrics over time
* **Quality Assurance**: Ensure consistent output quality across different scenarios
* **Safety & Compliance**: Monitor for potential issues and policy violations

Patronus provides three main evaluation tools for different use cases:

1. **PatronusEvalTool**: Allows agents to select the most appropriate evaluator and criteria for the evaluation task.
2. **PatronusPredefinedCriteriaEvalTool**: Uses predefined evaluator and criteria specified by the user.
3. **PatronusLocalEvaluatorTool**: Uses custom function evaluators defined by the user.

To use these tools, you need to install the Patronus package:

You'll also need to set up your Patronus API key as an environment variable:

## Steps to Get Started

To effectively use the Patronus evaluation tools, follow these steps:

1. **Install Patronus**: Install the Patronus package using the command above.
2. **Set Up API Key**: Set your Patronus API key as an environment variable.
3. **Choose the Right Tool**: Select the appropriate Patronus evaluation tool based on your needs.
4. **Configure the Tool**: Configure the tool with the necessary parameters.

### Using PatronusEvalTool

The following example demonstrates how to use the `PatronusEvalTool`, which allows agents to select the most appropriate evaluator and criteria:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import PatronusEvalTool

**Examples:**

Example 1 (unknown):
```unknown
You'll also need to set up your Patronus API key as an environment variable:
```

Example 2 (unknown):
```unknown
## Steps to Get Started

To effectively use the Patronus evaluation tools, follow these steps:

1. **Install Patronus**: Install the Patronus package using the command above.
2. **Set Up API Key**: Set your Patronus API key as an environment variable.
3. **Choose the Right Tool**: Select the appropriate Patronus evaluation tool based on your needs.
4. **Configure the Tool**: Configure the tool with the necessary parameters.

## Examples

### Using PatronusEvalTool

The following example demonstrates how to use the `PatronusEvalTool`, which allows agents to select the most appropriate evaluator and criteria:
```

---

## Perfect for precision tasks

**URL:** llms-txt#perfect-for-precision-tasks

**Contents:**
  - Alternative Approaches for Large Data

precision_agent = Agent(
    role="Code Security Auditor",
    goal="Identify security vulnerabilities in code",
    backstory="Security expert requiring complete code context",
    respect_context_window=False,  # Prefer failure over incomplete analysis
    max_retry_limit=1,  # Fail fast on context issues
    verbose=True
)
python Code theme={null}
from crewai_tools import RagTool

**Examples:**

Example 1 (unknown):
```unknown
### Alternative Approaches for Large Data

When dealing with very large datasets, consider these strategies:

#### 1. Use RAG Tools
```

---

## Planning

**URL:** llms-txt#planning

**Contents:**
- Overview
  - Using the Planning Feature

Source: https://docs.crewai.com/en/concepts/planning

Learn how to add planning to your CrewAI Crew and improve their performance.

The planning feature in CrewAI allows you to add planning capability to your crew. When enabled, before each Crew iteration,
all Crew information is sent to an AgentPlanner that will plan the tasks step by step, and this plan will be added to each task description.

### Using the Planning Feature

Getting started with the planning feature is very easy, the only step required is to add `planning=True` to your Crew:

<CodeGroup>
  
</CodeGroup>

From this point on, your crew will have planning enabled, and the tasks will be planned before each iteration.

<Warning>
  When planning is enabled, crewAI will use `gpt-4o-mini` as the default LLM for planning, which requires a valid OpenAI API key. Since your agents might be using different LLMs, this could cause confusion if you don't have an OpenAI API key configured or if you're experiencing unexpected behavior related to LLM API calls.
</Warning>

Now you can define the LLM that will be used to plan the tasks.

When running the base case example, you will see something like the output below, which represents the output of the `AgentPlanner`
responsible for creating the step-by-step logic to add to the Agents' tasks.

**Task Tools:** None specified

**Agent Tools:** None specified

**Step-by-Step Plan:**

1. **Review the Bullet Points:**
     - Carefully read through the list of 10 bullet points provided by the AI LLMs Senior Data Researcher.

2. **Outline the Report:**
     - Create an outline with each bullet point as a main section heading.
     - Plan sub-sections under each main heading to cover different aspects of the topic.

3. **Research Further Details:**
     - For each bullet point, conduct additional research if necessary to gather more detailed information.
     - Look for case studies, examples, and statistical data to support each section.

4. **Write Detailed Sections:**
     - Expand each bullet point into a comprehensive section.
     - Ensure each section includes an introduction, detailed explanation, examples, and a conclusion.
     - Use markdown formatting for headings, subheadings, lists, and emphasis.

5. **Review and Edit:**
     - Proofread the report for clarity, coherence, and correctness.
     - Make sure the report flows logically from one section to the next.
     - Format the report according to markdown standards.

6. **Finalize the Report:**
     - Ensure the report is complete with all sections expanded and detailed.
     - Double-check formatting and make any necessary adjustments.

**Expected Output:**
  A fully fledged report with the main topics, each with a full section of information. Formatted as markdown without '`
</CodeGroup>

**Examples:**

Example 1 (unknown):
```unknown
</CodeGroup>

From this point on, your crew will have planning enabled, and the tasks will be planned before each iteration.

<Warning>
  When planning is enabled, crewAI will use `gpt-4o-mini` as the default LLM for planning, which requires a valid OpenAI API key. Since your agents might be using different LLMs, this could cause confusion if you don't have an OpenAI API key configured or if you're experiencing unexpected behavior related to LLM API calls.
</Warning>

#### Planning LLM

Now you can define the LLM that will be used to plan the tasks.

When running the base case example, you will see something like the output below, which represents the output of the `AgentPlanner`
responsible for creating the step-by-step logic to add to the Agents' tasks.

<CodeGroup>
```

Example 2 (unknown):
```unknown

```

---

## Processes

**URL:** llms-txt#processes

**Contents:**
- Overview
- Process Implementations
- The Role of Processes in Teamwork
- Assigning Processes to a Crew

Source: https://docs.crewai.com/en/concepts/processes

Detailed guide on workflow management through processes in CrewAI, with updated implementation details.

<Tip>
  Processes orchestrate the execution of tasks by agents, akin to project management in human teams.
  These processes ensure tasks are distributed and executed efficiently, in alignment with a predefined strategy.
</Tip>

## Process Implementations

* **Sequential**: Executes tasks sequentially, ensuring tasks are completed in an orderly progression.
* **Hierarchical**: Organizes tasks in a managerial hierarchy, where tasks are delegated and executed based on a structured chain of command. A manager language model (`manager_llm`) or a custom manager agent (`manager_agent`) must be specified in the crew to enable the hierarchical process, facilitating the creation and management of tasks by the manager.
* **Consensual Process (Planned)**: Aiming for collaborative decision-making among agents on task execution, this process type introduces a democratic approach to task management within CrewAI. It is planned for future development and is not currently implemented in the codebase.

## The Role of Processes in Teamwork

Processes enable individual agents to operate as a cohesive unit, streamlining their efforts to achieve common objectives with efficiency and coherence.

## Assigning Processes to a Crew

To assign a process to a crew, specify the process type upon crew creation to set the execution strategy. For a hierarchical process, ensure to define `manager_llm` or `manager_agent` for the manager agent.

```python  theme={null}
from crewai import Crew, Process

---

## Reasoning

**URL:** llms-txt#reasoning

**Contents:**
- Overview
- Usage
- How It Works
- Configuration Options
- Example

Source: https://docs.crewai.com/en/concepts/reasoning

Learn how to enable and use agent reasoning to improve task execution.

Agent reasoning is a feature that allows agents to reflect on a task and create a plan before execution. This helps agents approach tasks more methodically and ensures they're ready to perform the assigned work.

To enable reasoning for an agent, simply set `reasoning=True` when creating the agent:

When reasoning is enabled, before executing a task, the agent will:

1. Reflect on the task and create a detailed plan
2. Evaluate whether it's ready to execute the task
3. Refine the plan as necessary until it's ready or max\_reasoning\_attempts is reached
4. Inject the reasoning plan into the task description before execution

This process helps the agent break down complex tasks into manageable steps and identify potential challenges before starting.

## Configuration Options

<ParamField body="reasoning" type="bool" default="False">
  Enable or disable reasoning
</ParamField>

<ParamField body="max_reasoning_attempts" type="int" default="None">
  Maximum number of attempts to refine the plan before proceeding with execution. If None (default), the agent will continue refining until it's ready.
</ParamField>

Here's a complete example:

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
## How It Works

When reasoning is enabled, before executing a task, the agent will:

1. Reflect on the task and create a detailed plan
2. Evaluate whether it's ready to execute the task
3. Refine the plan as necessary until it's ready or max\_reasoning\_attempts is reached
4. Inject the reasoning plan into the task description before execution

This process helps the agent break down complex tasks into manageable steps and identify potential challenges before starting.

## Configuration Options

<ParamField body="reasoning" type="bool" default="False">
  Enable or disable reasoning
</ParamField>

<ParamField body="max_reasoning_attempts" type="int" default="None">
  Maximum number of attempts to refine the plan before proceeding with execution. If None (default), the agent will continue refining until it's ready.
</ParamField>

## Example

Here's a complete example:
```

---

## Replay Tasks from Latest Crew Kickoff

**URL:** llms-txt#replay-tasks-from-latest-crew-kickoff

**Contents:**
- Introduction
  - Replaying from Specific Task Using the CLI
  - Replaying from a Task Programmatically
- Conclusion

Source: https://docs.crewai.com/en/learn/replay-tasks-from-latest-crew-kickoff

Replay tasks from the latest crew.kickoff(...)

CrewAI provides the ability to replay from a task specified from the latest crew kickoff. This feature is particularly useful when you've finished a kickoff and may want to retry certain tasks or don't need to refetch data over and your agents already have the context saved from the kickoff execution so you just need to replay the tasks you want to.

<Note>
  You must run `crew.kickoff()` before you can replay a task.
  Currently, only the latest kickoff is supported, so if you use `kickoff_for_each`, it will only allow you to replay from the most recent crew run.
</Note>

Here's an example of how to replay from a task:

### Replaying from Specific Task Using the CLI

To use the replay feature, follow these steps:

<Steps>
  <Step title="Open your terminal or command prompt." />

<Step title="Navigate to the directory where your CrewAI project is located." />

<Step title="Run the following commands:">
    To view the latest kickoff task\_ids use:

Once you have your `task_id` to replay, use:

<Note>
  Ensure `crewai` is installed and configured correctly in your development environment.
</Note>

### Replaying from a Task Programmatically

To replay from a task programmatically, use the following steps:

<Steps>
  <Step title="Specify the `task_id` and input parameters for the replay process.">
    Specify the `task_id` and input parameters for the replay process.
  </Step>

<Step title="Execute the replay command within a try-except block to handle potential errors.">
    Execute the replay command within a try-except block to handle potential errors.

<CodeGroup>
      
    </CodeGroup>
  </Step>
</Steps>

With the above enhancements and detailed functionality, replaying specific tasks in CrewAI has been made more efficient and robust.
Ensure you follow the commands and steps precisely to make the most of these features.

**Examples:**

Example 1 (unknown):
```unknown
Once you have your `task_id` to replay, use:
```

Example 2 (unknown):
```unknown
</Step>
</Steps>

<Note>
  Ensure `crewai` is installed and configured correctly in your development environment.
</Note>

### Replaying from a Task Programmatically

To replay from a task programmatically, use the following steps:

<Steps>
  <Step title="Specify the `task_id` and input parameters for the replay process.">
    Specify the `task_id` and input parameters for the replay process.
  </Step>

  <Step title="Execute the replay command within a try-except block to handle potential errors.">
    Execute the replay command within a try-except block to handle potential errors.

    <CodeGroup>
```

---

## Reset all memory storage

**URL:** llms-txt#reset-all-memory-storage

crew = Crew(agents=[...], tasks=[...], memory=True)

---

## rest of the code ...

**URL:** llms-txt#rest-of-the-code-...

**Contents:**
- Conclusion

Tools are pivotal in extending the capabilities of CrewAI agents, enabling them to undertake a broad spectrum of tasks and collaborate effectively.
When building solutions with CrewAI, leverage both custom and existing tools to empower your agents and enhance the AI ecosystem. Consider utilizing error handling, caching mechanisms,
and the flexibility of tool arguments to optimize your agents' performance and capabilities.

---

## Run CrewAI workflow

**URL:** llms-txt#run-crewai-workflow

**Contents:**
- Tool Parameters
  - Required Parameters
  - QdrantConfig Parameters
  - Optional Tool Parameters
- Advanced Filtering
  - Dynamic Filtering

crew = Crew(
    agents=[search_agent, answer_agent],
    tasks=[search_task, answer_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(
    inputs={"query": "What is the role of X in the document?"}
)
print(result)
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## Tool Parameters

### Required Parameters

* `qdrant_config` (QdrantConfig): Configuration object containing all Qdrant settings

### QdrantConfig Parameters

* `qdrant_url` (str): The URL of your Qdrant server
* `qdrant_api_key` (str, optional): API key for authentication with Qdrant
* `collection_name` (str): Name of the Qdrant collection to search
* `limit` (int): Maximum number of results to return (default: 3)
* `score_threshold` (float): Minimum similarity score threshold (default: 0.35)
* `filter` (Any, optional): Qdrant Filter instance for advanced filtering (default: None)

### Optional Tool Parameters

* `custom_embedding_fn` (Callable\[\[str], list\[float]]): Custom function for text vectorization
* `qdrant_package` (str): Base package path for Qdrant (default: "qdrant\_client")
* `client` (Any): Pre-initialized Qdrant client (optional)

## Advanced Filtering

The QdrantVectorSearchTool supports powerful filtering capabilities to refine your search results:

### Dynamic Filtering

Use `filter_by` and `filter_value` parameters in your search to filter results on-the-fly:
```

---

## Run the task

**URL:** llms-txt#run-the-task

**Contents:**
- Implementation Details
- Conclusion

crew = Crew(agents=[browser_agent], tasks=[search_task])
result = crew.kickoff()
python Code theme={null}
class MultiOnTool(BaseTool):
    """Tool to wrap MultiOn Browse Capabilities."""

name: str = "Multion Browse Tool"
    description: str = """Multion gives the ability for LLMs to control web browsers using natural language instructions.
            If the status is 'CONTINUE', reissue the same instruction to continue execution
        """
    
    # Implementation details...
    
    def _run(self, cmd: str, *args: Any, **kwargs: Any) -> str:
        """
        Run the Multion client with the given command.
        
        Args:
            cmd (str): The detailed and specific natural language instruction for web browsing
            *args (Any): Additional arguments to pass to the Multion client
            **kwargs (Any): Additional keyword arguments to pass to the Multion client
        """
        # Implementation details...
```

The `MultiOnTool` provides a powerful way to integrate web browsing capabilities into CrewAI agents. By enabling agents to interact with websites through natural language instructions, it opens up a wide range of possibilities for web-based tasks, from data collection and research to automated interactions with web services.

**Examples:**

Example 1 (unknown):
```unknown
If the status returned is `CONTINUE`, the agent should be instructed to reissue the same instruction to continue execution.

## Implementation Details

The `MultiOnTool` is implemented as a subclass of `BaseTool` from CrewAI. It wraps the MultiOn client to provide web browsing capabilities:
```

---

## Run the task through a crew

**URL:** llms-txt#run-the-task-through-a-crew

**Contents:**
- Implementation Details
- Conclusion

crew = Crew(agents=[web_scraper_agent], tasks=[extract_task])
result = crew.kickoff()
python Code theme={null}
class ScrapeElementFromWebsiteTool(BaseTool):
    name: str = "Read a website content"
    description: str = "A tool that can be used to read a website content."
    
    # Implementation details...
    
    def _run(self, **kwargs: Any) -> Any:
        website_url = kwargs.get("website_url", self.website_url)
        css_element = kwargs.get("css_element", self.css_element)
        page = requests.get(
            website_url,
            headers=self.headers,
            cookies=self.cookies if self.cookies else {},
        )
        parsed = BeautifulSoup(page.content, "html.parser")
        elements = parsed.select(css_element)
        return "\n".join([element.get_text() for element in elements])
```

The `ScrapeElementFromWebsiteTool` provides a powerful way to extract specific elements from websites using CSS selectors. By enabling agents to target only the content they need, it makes web scraping tasks more efficient and focused. This tool is particularly useful for data extraction, content monitoring, and research tasks where specific information needs to be extracted from web pages.

**Examples:**

Example 1 (unknown):
```unknown
## Implementation Details

The `ScrapeElementFromWebsiteTool` uses the `requests` library to fetch the web page and `BeautifulSoup` to parse the HTML and extract the specified elements:
```

---

## `S3ReaderTool`

**URL:** llms-txt#`s3readertool`

**Contents:**
- Description
- Installation
- Steps to Get Started
- Example

The `S3ReaderTool` is designed to read files from Amazon S3 buckets. This tool allows CrewAI agents to access and retrieve content stored in S3, making it ideal for workflows that require reading data, configuration files, or any other content stored in AWS S3 storage.

To use this tool, you need to install the required dependencies:

## Steps to Get Started

To effectively use the `S3ReaderTool`, follow these steps:

1. **Install Dependencies**: Install the required packages using the command above.
2. **Configure AWS Credentials**: Set up your AWS credentials as environment variables.
3. **Initialize the Tool**: Create an instance of the tool.
4. **Specify S3 Path**: Provide the S3 path to the file you want to read.

The following example demonstrates how to use the `S3ReaderTool` to read a file from an S3 bucket:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools.aws.s3 import S3ReaderTool

**Examples:**

Example 1 (unknown):
```unknown
## Steps to Get Started

To effectively use the `S3ReaderTool`, follow these steps:

1. **Install Dependencies**: Install the required packages using the command above.
2. **Configure AWS Credentials**: Set up your AWS credentials as environment variables.
3. **Initialize the Tool**: Create an instance of the tool.
4. **Specify S3 Path**: Provide the S3 path to the file you want to read.

## Example

The following example demonstrates how to use the `S3ReaderTool` to read a file from an S3 bucket:
```

---

## `S3WriterTool`

**URL:** llms-txt#`s3writertool`

**Contents:**
- Description
- Installation
- Steps to Get Started
- Example

The `S3WriterTool` is designed to write content to files in Amazon S3 buckets. This tool allows CrewAI agents to create or update files in S3, making it ideal for workflows that require storing data, saving configuration files, or persisting any other content to AWS S3 storage.

To use this tool, you need to install the required dependencies:

## Steps to Get Started

To effectively use the `S3WriterTool`, follow these steps:

1. **Install Dependencies**: Install the required packages using the command above.
2. **Configure AWS Credentials**: Set up your AWS credentials as environment variables.
3. **Initialize the Tool**: Create an instance of the tool.
4. **Specify S3 Path and Content**: Provide the S3 path where you want to write the file and the content to be written.

The following example demonstrates how to use the `S3WriterTool` to write content to a file in an S3 bucket:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools.aws.s3 import S3WriterTool

**Examples:**

Example 1 (unknown):
```unknown
## Steps to Get Started

To effectively use the `S3WriterTool`, follow these steps:

1. **Install Dependencies**: Install the required packages using the command above.
2. **Configure AWS Credentials**: Set up your AWS credentials as environment variables.
3. **Initialize the Tool**: Create an instance of the tool.
4. **Specify S3 Path and Content**: Provide the S3 path where you want to write the file and the content to be written.

## Example

The following example demonstrates how to use the `S3WriterTool` to write content to a file in an S3 bucket:
```

---

## Salesforce Integration

**URL:** llms-txt#salesforce-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Salesforce Integration
  - 1. Connect Your Salesforce Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Tools
  - **Record Management**
  - **Record Updates**
  - **Record Retrieval**

Source: https://docs.crewai.com/en/enterprise/integrations/salesforce

CRM and sales automation with Salesforce integration for CrewAI.

Enable your agents to manage customer relationships, sales processes, and data through Salesforce. Create and update records, manage leads and opportunities, execute SOQL queries, and streamline your CRM workflows with AI-powered automation.

Before using the Salesforce integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Salesforce account with appropriate permissions
* Connected your Salesforce account through the [Integrations page](https://app.crewai.com/integrations)

## Setting Up Salesforce Integration

### 1. Connect Your Salesforce Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Salesforce** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for CRM and sales management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

### **Record Management**

<AccordionGroup>
  <Accordion title="salesforce/create_record_contact">
    **Description:** Create a new Contact record in Salesforce.

* `FirstName` (string, optional): First Name
    * `LastName` (string, required): Last Name - This field is required
    * `accountId` (string, optional): Account ID - The Account that the Contact belongs to
    * `Email` (string, optional): Email address
    * `Title` (string, optional): Title of the contact, such as CEO or Vice President
    * `Description` (string, optional): A description of the Contact
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Contact fields
  </Accordion>

<Accordion title="salesforce/create_record_lead">
    **Description:** Create a new Lead record in Salesforce.

* `FirstName` (string, optional): First Name
    * `LastName` (string, required): Last Name - This field is required
    * `Company` (string, required): Company - This field is required
    * `Email` (string, optional): Email address
    * `Phone` (string, optional): Phone number
    * `Website` (string, optional): Website URL
    * `Title` (string, optional): Title of the contact, such as CEO or Vice President
    * `Status` (string, optional): Lead Status - Use Connect Portal Workflow Settings to select Lead Status
    * `Description` (string, optional): A description of the Lead
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Lead fields
  </Accordion>

<Accordion title="salesforce/create_record_opportunity">
    **Description:** Create a new Opportunity record in Salesforce.

* `Name` (string, required): The Opportunity name - This field is required
    * `StageName` (string, optional): Opportunity Stage - Use Connect Portal Workflow Settings to select stage
    * `CloseDate` (string, optional): Close Date in YYYY-MM-DD format - Defaults to 30 days from current date
    * `AccountId` (string, optional): The Account that the Opportunity belongs to
    * `Amount` (string, optional): Estimated total sale amount
    * `Description` (string, optional): A description of the Opportunity
    * `OwnerId` (string, optional): The Salesforce user assigned to work on this Opportunity
    * `NextStep` (string, optional): Description of next task in closing Opportunity
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Opportunity fields
  </Accordion>

<Accordion title="salesforce/create_record_task">
    **Description:** Create a new Task record in Salesforce.

* `whatId` (string, optional): Related to ID - The ID of the Account or Opportunity this Task is related to
    * `whoId` (string, optional): Name ID - The ID of the Contact or Lead this Task is related to
    * `subject` (string, required): Subject of the task
    * `activityDate` (string, optional): Activity Date in YYYY-MM-DD format
    * `description` (string, optional): A description of the Task
    * `taskSubtype` (string, required): Task Subtype - Options: task, email, listEmail, call
    * `Status` (string, optional): Status - Options: Not Started, In Progress, Completed
    * `ownerId` (string, optional): Assigned To ID - The Salesforce user assigned to this Task
    * `callDurationInSeconds` (string, optional): Call Duration in seconds
    * `isReminderSet` (boolean, optional): Whether reminder is set
    * `reminderDateTime` (string, optional): Reminder Date/Time in ISO format
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Task fields
  </Accordion>

<Accordion title="salesforce/create_record_account">
    **Description:** Create a new Account record in Salesforce.

* `Name` (string, required): The Account name - This field is required
    * `OwnerId` (string, optional): The Salesforce user assigned to this Account
    * `Website` (string, optional): Website URL
    * `Phone` (string, optional): Phone number
    * `Description` (string, optional): Account description
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Account fields
  </Accordion>

<Accordion title="salesforce/create_record_any">
    **Description:** Create a record of any object type in Salesforce.

**Note:** This is a flexible tool for creating records of custom or unknown object types.
  </Accordion>
</AccordionGroup>

### **Record Updates**

<AccordionGroup>
  <Accordion title="salesforce/update_record_contact">
    **Description:** Update an existing Contact record in Salesforce.

* `recordId` (string, required): The ID of the record to update
    * `FirstName` (string, optional): First Name
    * `LastName` (string, optional): Last Name
    * `accountId` (string, optional): Account ID - The Account that the Contact belongs to
    * `Email` (string, optional): Email address
    * `Title` (string, optional): Title of the contact
    * `Description` (string, optional): A description of the Contact
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Contact fields
  </Accordion>

<Accordion title="salesforce/update_record_lead">
    **Description:** Update an existing Lead record in Salesforce.

* `recordId` (string, required): The ID of the record to update
    * `FirstName` (string, optional): First Name
    * `LastName` (string, optional): Last Name
    * `Company` (string, optional): Company name
    * `Email` (string, optional): Email address
    * `Phone` (string, optional): Phone number
    * `Website` (string, optional): Website URL
    * `Title` (string, optional): Title of the contact
    * `Status` (string, optional): Lead Status
    * `Description` (string, optional): A description of the Lead
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Lead fields
  </Accordion>

<Accordion title="salesforce/update_record_opportunity">
    **Description:** Update an existing Opportunity record in Salesforce.

* `recordId` (string, required): The ID of the record to update
    * `Name` (string, optional): The Opportunity name
    * `StageName` (string, optional): Opportunity Stage
    * `CloseDate` (string, optional): Close Date in YYYY-MM-DD format
    * `AccountId` (string, optional): The Account that the Opportunity belongs to
    * `Amount` (string, optional): Estimated total sale amount
    * `Description` (string, optional): A description of the Opportunity
    * `OwnerId` (string, optional): The Salesforce user assigned to work on this Opportunity
    * `NextStep` (string, optional): Description of next task in closing Opportunity
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Opportunity fields
  </Accordion>

<Accordion title="salesforce/update_record_task">
    **Description:** Update an existing Task record in Salesforce.

* `recordId` (string, required): The ID of the record to update
    * `whatId` (string, optional): Related to ID - The ID of the Account or Opportunity this Task is related to
    * `whoId` (string, optional): Name ID - The ID of the Contact or Lead this Task is related to
    * `subject` (string, optional): Subject of the task
    * `activityDate` (string, optional): Activity Date in YYYY-MM-DD format
    * `description` (string, optional): A description of the Task
    * `Status` (string, optional): Status - Options: Not Started, In Progress, Completed
    * `ownerId` (string, optional): Assigned To ID - The Salesforce user assigned to this Task
    * `callDurationInSeconds` (string, optional): Call Duration in seconds
    * `isReminderSet` (boolean, optional): Whether reminder is set
    * `reminderDateTime` (string, optional): Reminder Date/Time in ISO format
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Task fields
  </Accordion>

<Accordion title="salesforce/update_record_account">
    **Description:** Update an existing Account record in Salesforce.

* `recordId` (string, required): The ID of the record to update
    * `Name` (string, optional): The Account name
    * `OwnerId` (string, optional): The Salesforce user assigned to this Account
    * `Website` (string, optional): Website URL
    * `Phone` (string, optional): Phone number
    * `Description` (string, optional): Account description
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Account fields
  </Accordion>

<Accordion title="salesforce/update_record_any">
    **Description:** Update a record of any object type in Salesforce.

**Note:** This is a flexible tool for updating records of custom or unknown object types.
  </Accordion>
</AccordionGroup>

### **Record Retrieval**

<AccordionGroup>
  <Accordion title="salesforce/get_record_by_id_contact">
    **Description:** Get a Contact record by its ID.

* `recordId` (string, required): Record ID of the Contact
  </Accordion>

<Accordion title="salesforce/get_record_by_id_lead">
    **Description:** Get a Lead record by its ID.

* `recordId` (string, required): Record ID of the Lead
  </Accordion>

<Accordion title="salesforce/get_record_by_id_opportunity">
    **Description:** Get an Opportunity record by its ID.

* `recordId` (string, required): Record ID of the Opportunity
  </Accordion>

<Accordion title="salesforce/get_record_by_id_task">
    **Description:** Get a Task record by its ID.

* `recordId` (string, required): Record ID of the Task
  </Accordion>

<Accordion title="salesforce/get_record_by_id_account">
    **Description:** Get an Account record by its ID.

* `recordId` (string, required): Record ID of the Account
  </Accordion>

<Accordion title="salesforce/get_record_by_id_any">
    **Description:** Get a record of any object type by its ID.

* `recordType` (string, required): Record Type (e.g., "CustomObject\_\_c")
    * `recordId` (string, required): Record ID
  </Accordion>
</AccordionGroup>

### **Record Search**

<AccordionGroup>
  <Accordion title="salesforce/search_records_contact">
    **Description:** Search for Contact records with advanced filtering.

* `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

<Accordion title="salesforce/search_records_lead">
    **Description:** Search for Lead records with advanced filtering.

* `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

<Accordion title="salesforce/search_records_opportunity">
    **Description:** Search for Opportunity records with advanced filtering.

* `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

<Accordion title="salesforce/search_records_task">
    **Description:** Search for Task records with advanced filtering.

* `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

<Accordion title="salesforce/search_records_account">
    **Description:** Search for Account records with advanced filtering.

* `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

<Accordion title="salesforce/search_records_any">
    **Description:** Search for records of any object type.

* `recordType` (string, required): Record Type to search
    * `filterFormula` (string, optional): Filter search criteria
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>
</AccordionGroup>

### **List View Retrieval**

<AccordionGroup>
  <Accordion title="salesforce/get_record_by_view_id_contact">
    **Description:** Get Contact records from a specific List View.

* `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

<Accordion title="salesforce/get_record_by_view_id_lead">
    **Description:** Get Lead records from a specific List View.

* `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

<Accordion title="salesforce/get_record_by_view_id_opportunity">
    **Description:** Get Opportunity records from a specific List View.

* `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

<Accordion title="salesforce/get_record_by_view_id_task">
    **Description:** Get Task records from a specific List View.

* `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

<Accordion title="salesforce/get_record_by_view_id_account">
    **Description:** Get Account records from a specific List View.

* `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

<Accordion title="salesforce/get_record_by_view_id_any">
    **Description:** Get records of any object type from a specific List View.

* `recordType` (string, required): Record Type
    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>
</AccordionGroup>

### **Custom Fields**

<AccordionGroup>
  <Accordion title="salesforce/create_custom_field_contact">
    **Description:** Deploy custom fields for Contact objects.

* `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

<Accordion title="salesforce/create_custom_field_lead">
    **Description:** Deploy custom fields for Lead objects.

* `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

<Accordion title="salesforce/create_custom_field_opportunity">
    **Description:** Deploy custom fields for Opportunity objects.

* `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

<Accordion title="salesforce/create_custom_field_task">
    **Description:** Deploy custom fields for Task objects.

* `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

<Accordion title="salesforce/create_custom_field_account">
    **Description:** Deploy custom fields for Account objects.

* `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

<Accordion title="salesforce/create_custom_field_any">
    **Description:** Deploy custom fields for any object type.

**Note:** This is a flexible tool for creating custom fields on custom or unknown object types.
  </Accordion>
</AccordionGroup>

### **Advanced Operations**

<AccordionGroup>
  <Accordion title="salesforce/write_soql_query">
    **Description:** Execute custom SOQL queries against your Salesforce data.

* `query` (string, required): SOQL Query (e.g., "SELECT Id, Name FROM Account WHERE Name = 'Example'")
  </Accordion>

<Accordion title="salesforce/create_custom_object">
    **Description:** Deploy a new custom object in Salesforce.

* `label` (string, required): Object Label for tabs, page layouts, and reports
    * `pluralLabel` (string, required): Plural Label (e.g., "Accounts")
    * `description` (string, optional): A description of the Custom Object
    * `recordName` (string, required): Record Name that appears in layouts and searches (e.g., "Account Name")
  </Accordion>

<Accordion title="salesforce/describe_action_schema">
    **Description:** Get the expected schema for operations on specific object types.

* `recordType` (string, required): Record Type to describe
    * `operation` (string, required): Operation Type (e.g., "CREATE\_RECORD" or "UPDATE\_RECORD")

**Note:** Use this function first when working with custom objects to understand their schema before performing operations.
  </Accordion>
</AccordionGroup>

### Basic Salesforce Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Tools

### **Record Management**

<AccordionGroup>
  <Accordion title="salesforce/create_record_contact">
    **Description:** Create a new Contact record in Salesforce.

    **Parameters:**

    * `FirstName` (string, optional): First Name
    * `LastName` (string, required): Last Name - This field is required
    * `accountId` (string, optional): Account ID - The Account that the Contact belongs to
    * `Email` (string, optional): Email address
    * `Title` (string, optional): Title of the contact, such as CEO or Vice President
    * `Description` (string, optional): A description of the Contact
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Contact fields
  </Accordion>

  <Accordion title="salesforce/create_record_lead">
    **Description:** Create a new Lead record in Salesforce.

    **Parameters:**

    * `FirstName` (string, optional): First Name
    * `LastName` (string, required): Last Name - This field is required
    * `Company` (string, required): Company - This field is required
    * `Email` (string, optional): Email address
    * `Phone` (string, optional): Phone number
    * `Website` (string, optional): Website URL
    * `Title` (string, optional): Title of the contact, such as CEO or Vice President
    * `Status` (string, optional): Lead Status - Use Connect Portal Workflow Settings to select Lead Status
    * `Description` (string, optional): A description of the Lead
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Lead fields
  </Accordion>

  <Accordion title="salesforce/create_record_opportunity">
    **Description:** Create a new Opportunity record in Salesforce.

    **Parameters:**

    * `Name` (string, required): The Opportunity name - This field is required
    * `StageName` (string, optional): Opportunity Stage - Use Connect Portal Workflow Settings to select stage
    * `CloseDate` (string, optional): Close Date in YYYY-MM-DD format - Defaults to 30 days from current date
    * `AccountId` (string, optional): The Account that the Opportunity belongs to
    * `Amount` (string, optional): Estimated total sale amount
    * `Description` (string, optional): A description of the Opportunity
    * `OwnerId` (string, optional): The Salesforce user assigned to work on this Opportunity
    * `NextStep` (string, optional): Description of next task in closing Opportunity
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Opportunity fields
  </Accordion>

  <Accordion title="salesforce/create_record_task">
    **Description:** Create a new Task record in Salesforce.

    **Parameters:**

    * `whatId` (string, optional): Related to ID - The ID of the Account or Opportunity this Task is related to
    * `whoId` (string, optional): Name ID - The ID of the Contact or Lead this Task is related to
    * `subject` (string, required): Subject of the task
    * `activityDate` (string, optional): Activity Date in YYYY-MM-DD format
    * `description` (string, optional): A description of the Task
    * `taskSubtype` (string, required): Task Subtype - Options: task, email, listEmail, call
    * `Status` (string, optional): Status - Options: Not Started, In Progress, Completed
    * `ownerId` (string, optional): Assigned To ID - The Salesforce user assigned to this Task
    * `callDurationInSeconds` (string, optional): Call Duration in seconds
    * `isReminderSet` (boolean, optional): Whether reminder is set
    * `reminderDateTime` (string, optional): Reminder Date/Time in ISO format
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Task fields
  </Accordion>

  <Accordion title="salesforce/create_record_account">
    **Description:** Create a new Account record in Salesforce.

    **Parameters:**

    * `Name` (string, required): The Account name - This field is required
    * `OwnerId` (string, optional): The Salesforce user assigned to this Account
    * `Website` (string, optional): Website URL
    * `Phone` (string, optional): Phone number
    * `Description` (string, optional): Account description
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Account fields
  </Accordion>

  <Accordion title="salesforce/create_record_any">
    **Description:** Create a record of any object type in Salesforce.

    **Note:** This is a flexible tool for creating records of custom or unknown object types.
  </Accordion>
</AccordionGroup>

### **Record Updates**

<AccordionGroup>
  <Accordion title="salesforce/update_record_contact">
    **Description:** Update an existing Contact record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `FirstName` (string, optional): First Name
    * `LastName` (string, optional): Last Name
    * `accountId` (string, optional): Account ID - The Account that the Contact belongs to
    * `Email` (string, optional): Email address
    * `Title` (string, optional): Title of the contact
    * `Description` (string, optional): A description of the Contact
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Contact fields
  </Accordion>

  <Accordion title="salesforce/update_record_lead">
    **Description:** Update an existing Lead record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `FirstName` (string, optional): First Name
    * `LastName` (string, optional): Last Name
    * `Company` (string, optional): Company name
    * `Email` (string, optional): Email address
    * `Phone` (string, optional): Phone number
    * `Website` (string, optional): Website URL
    * `Title` (string, optional): Title of the contact
    * `Status` (string, optional): Lead Status
    * `Description` (string, optional): A description of the Lead
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Lead fields
  </Accordion>

  <Accordion title="salesforce/update_record_opportunity">
    **Description:** Update an existing Opportunity record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `Name` (string, optional): The Opportunity name
    * `StageName` (string, optional): Opportunity Stage
    * `CloseDate` (string, optional): Close Date in YYYY-MM-DD format
    * `AccountId` (string, optional): The Account that the Opportunity belongs to
    * `Amount` (string, optional): Estimated total sale amount
    * `Description` (string, optional): A description of the Opportunity
    * `OwnerId` (string, optional): The Salesforce user assigned to work on this Opportunity
    * `NextStep` (string, optional): Description of next task in closing Opportunity
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Opportunity fields
  </Accordion>

  <Accordion title="salesforce/update_record_task">
    **Description:** Update an existing Task record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `whatId` (string, optional): Related to ID - The ID of the Account or Opportunity this Task is related to
    * `whoId` (string, optional): Name ID - The ID of the Contact or Lead this Task is related to
    * `subject` (string, optional): Subject of the task
    * `activityDate` (string, optional): Activity Date in YYYY-MM-DD format
    * `description` (string, optional): A description of the Task
    * `Status` (string, optional): Status - Options: Not Started, In Progress, Completed
    * `ownerId` (string, optional): Assigned To ID - The Salesforce user assigned to this Task
    * `callDurationInSeconds` (string, optional): Call Duration in seconds
    * `isReminderSet` (boolean, optional): Whether reminder is set
    * `reminderDateTime` (string, optional): Reminder Date/Time in ISO format
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Task fields
  </Accordion>

  <Accordion title="salesforce/update_record_account">
    **Description:** Update an existing Account record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `Name` (string, optional): The Account name
    * `OwnerId` (string, optional): The Salesforce user assigned to this Account
    * `Website` (string, optional): Website URL
    * `Phone` (string, optional): Phone number
    * `Description` (string, optional): Account description
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Account fields
  </Accordion>

  <Accordion title="salesforce/update_record_any">
    **Description:** Update a record of any object type in Salesforce.

    **Note:** This is a flexible tool for updating records of custom or unknown object types.
  </Accordion>
</AccordionGroup>

### **Record Retrieval**

<AccordionGroup>
  <Accordion title="salesforce/get_record_by_id_contact">
    **Description:** Get a Contact record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Contact
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_lead">
    **Description:** Get a Lead record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Lead
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_opportunity">
    **Description:** Get an Opportunity record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Opportunity
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_task">
    **Description:** Get a Task record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Task
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_account">
    **Description:** Get an Account record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Account
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_any">
    **Description:** Get a record of any object type by its ID.

    **Parameters:**

    * `recordType` (string, required): Record Type (e.g., "CustomObject\_\_c")
    * `recordId` (string, required): Record ID
  </Accordion>
</AccordionGroup>

### **Record Search**

<AccordionGroup>
  <Accordion title="salesforce/search_records_contact">
    **Description:** Search for Contact records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_lead">
    **Description:** Search for Lead records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_opportunity">
    **Description:** Search for Opportunity records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_task">
    **Description:** Search for Task records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_account">
    **Description:** Search for Account records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_any">
    **Description:** Search for records of any object type.

    **Parameters:**

    * `recordType` (string, required): Record Type to search
    * `filterFormula` (string, optional): Filter search criteria
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>
</AccordionGroup>

### **List View Retrieval**

<AccordionGroup>
  <Accordion title="salesforce/get_record_by_view_id_contact">
    **Description:** Get Contact records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_lead">
    **Description:** Get Lead records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_opportunity">
    **Description:** Get Opportunity records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_task">
    **Description:** Get Task records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_account">
    **Description:** Get Account records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_any">
    **Description:** Get records of any object type from a specific List View.

    **Parameters:**

    * `recordType` (string, required): Record Type
    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>
</AccordionGroup>

### **Custom Fields**

<AccordionGroup>
  <Accordion title="salesforce/create_custom_field_contact">
    **Description:** Deploy custom fields for Contact objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_lead">
    **Description:** Deploy custom fields for Lead objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_opportunity">
    **Description:** Deploy custom fields for Opportunity objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_task">
    **Description:** Deploy custom fields for Task objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_account">
    **Description:** Deploy custom fields for Account objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_any">
    **Description:** Deploy custom fields for any object type.

    **Note:** This is a flexible tool for creating custom fields on custom or unknown object types.
  </Accordion>
</AccordionGroup>

### **Advanced Operations**

<AccordionGroup>
  <Accordion title="salesforce/write_soql_query">
    **Description:** Execute custom SOQL queries against your Salesforce data.

    **Parameters:**

    * `query` (string, required): SOQL Query (e.g., "SELECT Id, Name FROM Account WHERE Name = 'Example'")
  </Accordion>

  <Accordion title="salesforce/create_custom_object">
    **Description:** Deploy a new custom object in Salesforce.

    **Parameters:**

    * `label` (string, required): Object Label for tabs, page layouts, and reports
    * `pluralLabel` (string, required): Plural Label (e.g., "Accounts")
    * `description` (string, optional): A description of the Custom Object
    * `recordName` (string, required): Record Name that appears in layouts and searches (e.g., "Account Name")
  </Accordion>

  <Accordion title="salesforce/describe_action_schema">
    **Description:** Get the expected schema for operations on specific object types.

    **Parameters:**

    * `recordType` (string, required): Record Type to describe
    * `operation` (string, required): Operation Type (e.g., "CREATE\_RECORD" or "UPDATE\_RECORD")

    **Note:** Use this function first when working with custom objects to understand their schema before performing operations.
  </Accordion>
</AccordionGroup>

## Usage Examples

### Basic Salesforce Agent Setup
```

---

## Salesforce Trigger

**URL:** llms-txt#salesforce-trigger

**Contents:**
- Overview
- Demo
- Getting Started
- Use Cases
- Next Steps

Source: https://docs.crewai.com/en/enterprise/guides/salesforce-trigger

Trigger CrewAI crews from Salesforce workflows for CRM automation

CrewAI AOP can be triggered from Salesforce to automate customer relationship management workflows and enhance your sales operations.

Salesforce is a leading customer relationship management (CRM) platform that helps businesses streamline their sales, service, and marketing operations. By setting up CrewAI triggers from Salesforce, you can:

* Automate lead scoring and qualification
* Generate personalized sales materials
* Enhance customer service with AI-powered responses
* Streamline data analysis and reporting

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/oJunVqjjfu4" title="CrewAI + Salesforce trigger demo" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

To set up Salesforce triggers:

1. **Contact Support**: Reach out to CrewAI AOP support for assistance with Salesforce trigger setup
2. **Review Requirements**: Ensure you have the necessary Salesforce permissions and API access
3. **Configure Connection**: Work with the support team to establish the connection between CrewAI and your Salesforce instance
4. **Test Triggers**: Verify the triggers work correctly with your specific use cases

Common Salesforce + CrewAI trigger scenarios include:

* **Lead Processing**: Automatically analyze and score incoming leads
* **Proposal Generation**: Create customized proposals based on opportunity data
* **Customer Insights**: Generate analysis reports from customer interaction history
* **Follow-up Automation**: Create personalized follow-up messages and recommendations

For detailed setup instructions and advanced configuration options, please contact CrewAI AOP support who can provide tailored guidance for your specific Salesforce environment and business needs.

---

## `ScrapeElementFromWebsiteTool`

**URL:** llms-txt#`scrapeelementfromwebsitetool`

**Contents:**
- Description
- Installation
- Steps to Get Started
- Example

The `ScrapeElementFromWebsiteTool` is designed to extract specific elements from websites using CSS selectors. This tool allows CrewAI agents to scrape targeted content from web pages, making it useful for data extraction tasks where only specific parts of a webpage are needed.

To use this tool, you need to install the required dependencies:

## Steps to Get Started

To effectively use the `ScrapeElementFromWebsiteTool`, follow these steps:

1. **Install Dependencies**: Install the required packages using the command above.
2. **Identify CSS Selectors**: Determine the CSS selectors for the elements you want to extract from the website.
3. **Initialize the Tool**: Create an instance of the tool with the necessary parameters.

The following example demonstrates how to use the `ScrapeElementFromWebsiteTool` to extract specific elements from a website:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeElementFromWebsiteTool

**Examples:**

Example 1 (unknown):
```unknown
## Steps to Get Started

To effectively use the `ScrapeElementFromWebsiteTool`, follow these steps:

1. **Install Dependencies**: Install the required packages using the command above.
2. **Identify CSS Selectors**: Determine the CSS selectors for the elements you want to extract from the website.
3. **Initialize the Tool**: Create an instance of the tool with the necessary parameters.

## Example

The following example demonstrates how to use the `ScrapeElementFromWebsiteTool` to extract specific elements from a website:
```

---

## Sequential Processes

**URL:** llms-txt#sequential-processes

**Contents:**
- Introduction
- Sequential Process Overview
  - Key Features
- Implementing the Sequential Process

Source: https://docs.crewai.com/en/learn/sequential-process

A comprehensive guide to utilizing the sequential processes for task execution in CrewAI projects.

CrewAI offers a flexible framework for executing tasks in a structured manner, supporting both sequential and hierarchical processes.
This guide outlines how to effectively implement these processes to ensure efficient task execution and project completion.

## Sequential Process Overview

The sequential process ensures tasks are executed one after the other, following a linear progression.
This approach is ideal for projects requiring tasks to be completed in a specific order.

* **Linear Task Flow**: Ensures orderly progression by handling tasks in a predetermined sequence.
* **Simplicity**: Best suited for projects with clear, step-by-step tasks.
* **Easy Monitoring**: Facilitates easy tracking of task completion and project progress.

## Implementing the Sequential Process

To use the sequential process, assemble your crew and define tasks in the order they need to be executed.

```python Code theme={null}
from crewai import Crew, Process, Agent, Task, TaskOutput, CrewOutput

---

## Slack Integration

**URL:** llms-txt#slack-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Slack Integration
  - 1. Connect Your Slack Workspace
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Tools
  - **User Management**
  - **Channel Management**
  - **Messaging**

Source: https://docs.crewai.com/en/enterprise/integrations/slack

Team communication and collaboration with Slack integration for CrewAI.

Enable your agents to manage team communication through Slack. Send messages, search conversations, manage channels, and coordinate team activities to streamline your collaboration workflows with AI-powered automation.

Before using the Slack integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Slack workspace with appropriate permissions
* Connected your Slack workspace through the [Integrations page](https://app.crewai.com/integrations)

## Setting Up Slack Integration

### 1. Connect Your Slack Workspace

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Slack** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for team communication
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

### **User Management**

<AccordionGroup>
  <Accordion title="slack/list_members">
    **Description:** List all members in a Slack channel.

* No parameters required - retrieves all channel members
  </Accordion>

<Accordion title="slack/get_user_by_email">
    **Description:** Find a user in your Slack workspace by their email address.

* `email` (string, required): The email address of a user in the workspace
  </Accordion>

<Accordion title="slack/get_users_by_name">
    **Description:** Search for users by their name or display name.

* `name` (string, required): User's real name to search for
    * `displayName` (string, required): User's display name to search for
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>
</AccordionGroup>

### **Channel Management**

<AccordionGroup>
  <Accordion title="slack/list_channels">
    **Description:** List all channels in your Slack workspace.

* No parameters required - retrieves all accessible channels
  </Accordion>
</AccordionGroup>

<AccordionGroup>
  <Accordion title="slack/send_message">
    **Description:** Send a message to a Slack channel.

* `channel` (string, required): Channel name or ID - Use Connect Portal Workflow Settings to allow users to select a channel, or enter a channel name to create a new channel
    * `message` (string, required): The message text to send
    * `botName` (string, required): The name of the bot that sends this message
    * `botIcon` (string, required): Bot icon - Can be either an image URL or an emoji (e.g., ":dog:")
    * `blocks` (object, optional): Slack Block Kit JSON for rich message formatting with attachments and interactive elements
    * `authenticatedUser` (boolean, optional): If true, message appears to come from your authenticated Slack user instead of the application (defaults to false)
  </Accordion>

<Accordion title="slack/send_direct_message">
    **Description:** Send a direct message to a specific user in Slack.

* `memberId` (string, required): Recipient user ID - Use Connect Portal Workflow Settings to allow users to select a workspace member
    * `message` (string, required): The message text to send
    * `botName` (string, required): The name of the bot that sends this message
    * `botIcon` (string, required): Bot icon - Can be either an image URL or an emoji (e.g., ":dog:")
    * `blocks` (object, optional): Slack Block Kit JSON for rich message formatting with attachments and interactive elements
    * `authenticatedUser` (boolean, optional): If true, message appears to come from your authenticated Slack user instead of the application (defaults to false)
  </Accordion>
</AccordionGroup>

### **Search & Discovery**

<AccordionGroup>
  <Accordion title="slack/search_messages">
    **Description:** Search for messages across your Slack workspace.

* `query` (string, required): Search query using Slack search syntax to find messages that match specified criteria

**Search Query Examples:**

* `"project update"` - Search for messages containing "project update"
    * `from:@john in:#general` - Search for messages from John in the #general channel
    * `has:link after:2023-01-01` - Search for messages with links after January 1, 2023
    * `in:@channel before:yesterday` - Search for messages in a specific channel before yesterday
  </Accordion>
</AccordionGroup>

## Block Kit Integration

Slack's Block Kit allows you to create rich, interactive messages. Here are some examples of how to use the `blocks` parameter:

### Simple Text with Attachment

### Rich Formatting with Sections

### Basic Slack Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Tools

### **User Management**

<AccordionGroup>
  <Accordion title="slack/list_members">
    **Description:** List all members in a Slack channel.

    **Parameters:**

    * No parameters required - retrieves all channel members
  </Accordion>

  <Accordion title="slack/get_user_by_email">
    **Description:** Find a user in your Slack workspace by their email address.

    **Parameters:**

    * `email` (string, required): The email address of a user in the workspace
  </Accordion>

  <Accordion title="slack/get_users_by_name">
    **Description:** Search for users by their name or display name.

    **Parameters:**

    * `name` (string, required): User's real name to search for
    * `displayName` (string, required): User's display name to search for
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>
</AccordionGroup>

### **Channel Management**

<AccordionGroup>
  <Accordion title="slack/list_channels">
    **Description:** List all channels in your Slack workspace.

    **Parameters:**

    * No parameters required - retrieves all accessible channels
  </Accordion>
</AccordionGroup>

### **Messaging**

<AccordionGroup>
  <Accordion title="slack/send_message">
    **Description:** Send a message to a Slack channel.

    **Parameters:**

    * `channel` (string, required): Channel name or ID - Use Connect Portal Workflow Settings to allow users to select a channel, or enter a channel name to create a new channel
    * `message` (string, required): The message text to send
    * `botName` (string, required): The name of the bot that sends this message
    * `botIcon` (string, required): Bot icon - Can be either an image URL or an emoji (e.g., ":dog:")
    * `blocks` (object, optional): Slack Block Kit JSON for rich message formatting with attachments and interactive elements
    * `authenticatedUser` (boolean, optional): If true, message appears to come from your authenticated Slack user instead of the application (defaults to false)
  </Accordion>

  <Accordion title="slack/send_direct_message">
    **Description:** Send a direct message to a specific user in Slack.

    **Parameters:**

    * `memberId` (string, required): Recipient user ID - Use Connect Portal Workflow Settings to allow users to select a workspace member
    * `message` (string, required): The message text to send
    * `botName` (string, required): The name of the bot that sends this message
    * `botIcon` (string, required): Bot icon - Can be either an image URL or an emoji (e.g., ":dog:")
    * `blocks` (object, optional): Slack Block Kit JSON for rich message formatting with attachments and interactive elements
    * `authenticatedUser` (boolean, optional): If true, message appears to come from your authenticated Slack user instead of the application (defaults to false)
  </Accordion>
</AccordionGroup>

### **Search & Discovery**

<AccordionGroup>
  <Accordion title="slack/search_messages">
    **Description:** Search for messages across your Slack workspace.

    **Parameters:**

    * `query` (string, required): Search query using Slack search syntax to find messages that match specified criteria

    **Search Query Examples:**

    * `"project update"` - Search for messages containing "project update"
    * `from:@john in:#general` - Search for messages from John in the #general channel
    * `has:link after:2023-01-01` - Search for messages with links after January 1, 2023
    * `in:@channel before:yesterday` - Search for messages in a specific channel before yesterday
  </Accordion>
</AccordionGroup>

## Block Kit Integration

Slack's Block Kit allows you to create rich, interactive messages. Here are some examples of how to use the `blocks` parameter:

### Simple Text with Attachment
```

Example 4 (unknown):
```unknown
### Rich Formatting with Sections
```

---

## `SnowflakeSearchTool`

**URL:** llms-txt#`snowflakesearchtool`

**Contents:**
- Description
- Installation
- Steps to Get Started
- Example

The `SnowflakeSearchTool` is designed to connect to Snowflake data warehouses and execute SQL queries with advanced features like connection pooling, retry logic, and asynchronous execution. This tool allows CrewAI agents to interact with Snowflake databases, making it ideal for data analysis, reporting, and business intelligence tasks that require access to enterprise data stored in Snowflake.

To use this tool, you need to install the required dependencies:

## Steps to Get Started

To effectively use the `SnowflakeSearchTool`, follow these steps:

1. **Install Dependencies**: Install the required packages using one of the commands above.
2. **Configure Snowflake Connection**: Create a `SnowflakeConfig` object with your Snowflake credentials.
3. **Initialize the Tool**: Create an instance of the tool with the necessary configuration.
4. **Execute Queries**: Use the tool to run SQL queries against your Snowflake database.

The following example demonstrates how to use the `SnowflakeSearchTool` to query data from a Snowflake database:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import SnowflakeSearchTool, SnowflakeConfig

**Examples:**

Example 1 (unknown):
```unknown
Or alternatively:
```

Example 2 (unknown):
```unknown
## Steps to Get Started

To effectively use the `SnowflakeSearchTool`, follow these steps:

1. **Install Dependencies**: Install the required packages using one of the commands above.
2. **Configure Snowflake Connection**: Create a `SnowflakeConfig` object with your Snowflake credentials.
3. **Initialize the Tool**: Create an instance of the tool with the necessary configuration.
4. **Execute Queries**: Use the tool to run SQL queries against your Snowflake database.

## Example

The following example demonstrates how to use the `SnowflakeSearchTool` to query data from a Snowflake database:
```

---

## so now agents can only search within that website

**URL:** llms-txt#so-now-agents-can-only-search-within-that-website

**Contents:**
- Arguments
- Customization Options

tool = WebsiteSearchTool(website='https://example.com')
python Code theme={null}
tool = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google-generativeai", # or openai, ollama, ...
            config=dict(
                model_name="gemini-embedding-001",
                task_type="RETRIEVAL_DOCUMENT",
                # title="Embeddings",
            ),
        ),
    )
)
```

**Examples:**

Example 1 (unknown):
```unknown
## Arguments

* `website`: An optional argument intended to specify the website URL for focused searches. This argument is designed to enhance the tool's flexibility by allowing targeted searches when necessary.

## Customization Options

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:
```

---

## Specialist agents

**URL:** llms-txt#specialist-agents

researcher = Agent(
    role="Researcher",
    goal="Provide accurate research and analysis",
    backstory="Expert researcher with deep analytical skills",
    allow_delegation=False,  # Specialists focus on their expertise
    verbose=True
)

writer = Agent(
    role="Writer", 
    goal="Create compelling content",
    backstory="Skilled writer who creates engaging content",
    allow_delegation=False,
    verbose=True
)

---

## src/guide_creator_flow/crews/content_crew/config/agents.yaml

**URL:** llms-txt#src/guide_creator_flow/crews/content_crew/config/agents.yaml

content_writer:
  role: >
    Educational Content Writer
  goal: >
    Create engaging, informative content that thoroughly explains the assigned topic
    and provides valuable insights to the reader
  backstory: >
    You are a talented educational writer with expertise in creating clear, engaging
    content. You have a gift for explaining complex concepts in accessible language
    and organizing information in a way that helps readers build their understanding.
  llm: provider/model-id  # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...

content_reviewer:
  role: >
    Educational Content Reviewer and Editor
  goal: >
    Ensure content is accurate, comprehensive, well-structured, and maintains
    consistency with previously written sections
  backstory: >
    You are a meticulous editor with years of experience reviewing educational
    content. You have an eye for detail, clarity, and coherence. You excel at
    improving content while maintaining the original author's voice and ensuring
    consistent quality across multiple sections.
  llm: provider/model-id  # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...
yaml  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
These agent definitions establish the specialized roles and perspectives that will shape how our AI agents approach content creation. Notice how each agent has a distinct purpose and expertise.

2. Next, update the tasks configuration file to define the specific writing and reviewing tasks:
```

---

## src/guide_creator_flow/crews/content_crew/config/tasks.yaml

**URL:** llms-txt#src/guide_creator_flow/crews/content_crew/config/tasks.yaml

write_section_task:
  description: >
    Write a comprehensive section on the topic: "{section_title}"

Section description: {section_description}
    Target audience: {audience_level} level learners

Your content should:
    1. Begin with a brief introduction to the section topic
    2. Explain all key concepts clearly with examples
    3. Include practical applications or exercises where appropriate
    4. End with a summary of key points
    5. Be approximately 500-800 words in length

Format your content in Markdown with appropriate headings, lists, and emphasis.

Previously written sections:
    {previous_sections}

Make sure your content maintains consistency with previously written sections
    and builds upon concepts that have already been explained.
  expected_output: >
    A well-structured, comprehensive section in Markdown format that thoroughly
    explains the topic and is appropriate for the target audience.
  agent: content_writer

review_section_task:
  description: >
    Review and improve the following section on "{section_title}":

Target audience: {audience_level} level learners

Previously written sections:
    {previous_sections}

Your review should:
    1. Fix any grammatical or spelling errors
    2. Improve clarity and readability
    3. Ensure content is comprehensive and accurate
    4. Verify consistency with previously written sections
    5. Enhance the structure and flow
    6. Add any missing key information

Provide the improved version of the section in Markdown format.
  expected_output: >
    An improved, polished version of the section that maintains the original
    structure but enhances clarity, accuracy, and consistency.
  agent: content_reviewer
  context:
    - write_section_task
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
These task definitions provide detailed instructions to our agents, ensuring they produce content that meets our quality standards. Note how the `context` parameter in the review task creates a workflow where the reviewer has access to the writer's output.

3. Now, update the crew implementation file to define how our agents and tasks work together:
```

---

## src/guide_creator_flow/crews/content_crew/content_crew.py

**URL:** llms-txt#src/guide_creator_flow/crews/content_crew/content_crew.py

**Contents:**
- Step 5: Create the Flow

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class ContentCrew():
    """Content writing crew"""

agents: List[BaseAgent]
    tasks: List[Task]

@agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_writer'], # type: ignore[index]
            verbose=True
        )

@agent
    def content_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_reviewer'], # type: ignore[index]
            verbose=True
        )

@task
    def write_section_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_section_task'] # type: ignore[index]
        )

@task
    def review_section_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_section_task'], # type: ignore[index]
            context=[self.write_section_task()]
        )

@crew
    def crew(self) -> Crew:
        """Creates the content writing crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
python  theme={null}
#!/usr/bin/env python
import json
import os
from typing import List, Dict
from pydantic import BaseModel, Field
from crewai import LLM
from crewai.flow.flow import Flow, listen, start
from guide_creator_flow.crews.content_crew.content_crew import ContentCrew

**Examples:**

Example 1 (unknown):
```unknown
This crew definition establishes the relationship between our agents and tasks, setting up a sequential process where the content writer creates a draft and then the reviewer improves it. While this crew can function independently, in our flow it will be orchestrated as part of a larger system.

## Step 5: Create the Flow

Now comes the exciting part - creating the flow that will orchestrate the entire guide creation process. This is where we'll combine regular Python code, direct LLM calls, and our content creation crew into a cohesive system.

Our flow will:

1. Get user input for a topic and audience level
2. Make a direct LLM call to create a structured guide outline
3. Process each section sequentially using the content writer crew
4. Combine everything into a final comprehensive document

Let's create our flow in the `main.py` file:
```

---

## src/latest_ai_development/config/agents.yaml

**URL:** llms-txt#src/latest_ai_development/config/agents.yaml

researcher:
  role: >
    {topic} Senior Data Researcher
  goal: >
    Uncover cutting-edge developments in {topic}
  backstory: >
    You're a seasoned researcher with a knack for uncovering the latest
    developments in {topic}. Known for your ability to find the most relevant
    information and present it in a clear and concise manner.

reporting_analyst:
  role: >
    {topic} Reporting Analyst
  goal: >
    Create detailed reports based on {topic} data analysis and research findings
  backstory: >
    You're a meticulous analyst with a keen eye for detail. You're known for
    your ability to turn complex data into clear and concise reports, making
    it easy for others to understand and act on the information you provide.
python Code theme={null}

**Examples:**

Example 1 (unknown):
```unknown
To use this YAML configuration in your code, create a crew class that inherits from `CrewBase`:
```

---

## src/research_crew/config/agents.yaml

**URL:** llms-txt#src/research_crew/config/agents.yaml

**Contents:**
- Step 4: Define Your Tasks

researcher:
  role: >
    Senior Research Specialist for {topic}
  goal: >
    Find comprehensive and accurate information about {topic}
    with a focus on recent developments and key insights
  backstory: >
    You are an experienced research specialist with a talent for
    finding relevant information from various sources. You excel at
    organizing information in a clear and structured manner, making
    complex topics accessible to others.
  llm: provider/model-id  # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...

analyst:
  role: >
    Data Analyst and Report Writer for {topic}
  goal: >
    Analyze research findings and create a comprehensive, well-structured
    report that presents insights in a clear and engaging way
  backstory: >
    You are a skilled analyst with a background in data interpretation
    and technical writing. You have a talent for identifying patterns
    and extracting meaningful insights from research data, then
    communicating those insights effectively through well-crafted reports.
  llm: provider/model-id  # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...
yaml  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
Notice how each agent has a distinct role, goal, and backstory. These elements aren't just descriptive - they actively shape how the agent approaches its tasks. By crafting these carefully, you can create agents with specialized skills and perspectives that complement each other.

## Step 4: Define Your Tasks

With our agents defined, we now need to give them specific tasks to perform. Tasks in CrewAI represent the concrete work that agents will perform, with detailed instructions and expected outputs.

For our research crew, we'll define two main tasks:

1. A **research task** for gathering comprehensive information
2. An **analysis task** for creating an insightful report

Let's modify the `tasks.yaml` file:
```

---

## src/research_crew/config/tasks.yaml

**URL:** llms-txt#src/research_crew/config/tasks.yaml

**Contents:**
- Step 5: Configure Your Crew

research_task:
  description: >
    Conduct thorough research on {topic}. Focus on:
    1. Key concepts and definitions
    2. Historical development and recent trends
    3. Major challenges and opportunities
    4. Notable applications or case studies
    5. Future outlook and potential developments

Make sure to organize your findings in a structured format with clear sections.
  expected_output: >
    A comprehensive research document with well-organized sections covering
    all the requested aspects of {topic}. Include specific facts, figures,
    and examples where relevant.
  agent: researcher

analysis_task:
  description: >
    Analyze the research findings and create a comprehensive report on {topic}.
    Your report should:
    1. Begin with an executive summary
    2. Include all key information from the research
    3. Provide insightful analysis of trends and patterns
    4. Offer recommendations or future considerations
    5. Be formatted in a professional, easy-to-read style with clear headings
  expected_output: >
    A polished, professional report on {topic} that presents the research
    findings with added analysis and insights. The report should be well-structured
    with an executive summary, main sections, and conclusion.
  agent: analyst
  context:
    - research_task
  output_file: output/report.md
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
Note the `context` field in the analysis task - this is a powerful feature that allows the analyst to access the output of the research task. This creates a workflow where information flows naturally between agents, just as it would in a human team.

## Step 5: Configure Your Crew

Now it's time to bring everything together by configuring our crew. The crew is the container that orchestrates how agents work together to complete tasks.

Let's modify the `crew.py` file:
```

---

## src/research_crew/crew.py

**URL:** llms-txt#src/research_crew/crew.py

**Contents:**
- Step 6: Set Up Your Main Script

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class ResearchCrew():
    """Research crew for comprehensive topic analysis and reporting"""

agents: List[BaseAgent]
    tasks: List[Task]

@agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()]
        )

@agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'], # type: ignore[index]
            verbose=True
        )

@task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'] # type: ignore[index]
        )

@task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'], # type: ignore[index]
            output_file='output/report.md'
        )

@crew
    def crew(self) -> Crew:
        """Creates the research crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
python  theme={null}
#!/usr/bin/env python

**Examples:**

Example 1 (unknown):
```unknown
In this code, we're:

1. Creating the researcher agent and equipping it with the SerperDevTool to search the web
2. Creating the analyst agent
3. Setting up the research and analysis tasks
4. Configuring the crew to run tasks sequentially (the analyst will wait for the researcher to finish)

This is where the magic happens - with just a few lines of code, we've defined a collaborative AI system where specialized agents work together in a coordinated process.

## Step 6: Set Up Your Main Script

Now, let's set up the main script that will run our crew. This is where we provide the specific topic we want our crew to research.
```

---

## Start the crew's work

**URL:** llms-txt#start-the-crew's-work

**Contents:**
- Benefits of a Custom Manager Agent
- Setting a Manager LLM

result = crew.kickoff()
python Code theme={null}
from crewai import LLM

manager_llm = LLM(model="gpt-4o")

crew = Crew(
    agents=[researcher, writer],
    tasks=[task],
    process=Process.hierarchical,
    manager_llm=manager_llm
)
```

<Note>
  Either `manager_agent` or `manager_llm` must be set when using the hierarchical process.
</Note>

**Examples:**

Example 1 (unknown):
```unknown
## Benefits of a Custom Manager Agent

* **Enhanced Control**: Tailor the management approach to fit the specific needs of your project.
* **Improved Coordination**: Ensure efficient task coordination and management by an experienced agent.
* **Customizable Management**: Define managerial roles and responsibilities that align with your project's goals.

## Setting a Manager LLM

If you're using the hierarchical process and don't want to set a custom manager agent, you can specify the language model for the manager:
```

---

## Stripe Integration

**URL:** llms-txt#stripe-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Stripe Integration
  - 1. Connect Your Stripe Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Tools
  - **Customer Management**
  - **Subscription Management**
  - **Product Management**

Source: https://docs.crewai.com/en/enterprise/integrations/stripe

Payment processing and subscription management with Stripe integration for CrewAI.

Enable your agents to manage payments, subscriptions, and customer billing through Stripe. Handle customer data, process subscriptions, manage products, and track financial transactions to streamline your payment workflows with AI-powered automation.

Before using the Stripe integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Stripe account with appropriate API permissions
* Connected your Stripe account through the [Integrations page](https://app.crewai.com/integrations)

## Setting Up Stripe Integration

### 1. Connect Your Stripe Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Stripe** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for payment processing
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

### **Customer Management**

<AccordionGroup>
  <Accordion title="stripe/create_customer">
    **Description:** Create a new customer in your Stripe account.

* `emailCreateCustomer` (string, required): Customer's email address
    * `name` (string, optional): Customer's full name
    * `description` (string, optional): Customer description for internal reference
    * `metadataCreateCustomer` (object, optional): Additional metadata as key-value pairs (e.g., `{"field1": 1, "field2": 2}`)
  </Accordion>

<Accordion title="stripe/get_customer_by_id">
    **Description:** Retrieve a specific customer by their Stripe customer ID.

* `idGetCustomer` (string, required): The Stripe customer ID to retrieve
  </Accordion>

<Accordion title="stripe/get_customers">
    **Description:** Retrieve a list of customers with optional filtering.

* `emailGetCustomers` (string, optional): Filter customers by email address
    * `createdAfter` (string, optional): Filter customers created after this date (Unix timestamp)
    * `createdBefore` (string, optional): Filter customers created before this date (Unix timestamp)
    * `limitGetCustomers` (string, optional): Maximum number of customers to return (defaults to 10)
  </Accordion>

<Accordion title="stripe/update_customer">
    **Description:** Update an existing customer's information.

* `customerId` (string, required): The ID of the customer to update
    * `emailUpdateCustomer` (string, optional): Updated email address
    * `name` (string, optional): Updated customer name
    * `description` (string, optional): Updated customer description
    * `metadataUpdateCustomer` (object, optional): Updated metadata as key-value pairs
  </Accordion>
</AccordionGroup>

### **Subscription Management**

<AccordionGroup>
  <Accordion title="stripe/create_subscription">
    **Description:** Create a new subscription for a customer.

* `customerIdCreateSubscription` (string, required): The customer ID for whom the subscription will be created
    * `plan` (string, required): The plan ID for the subscription - Use Connect Portal Workflow Settings to allow users to select a plan
    * `metadataCreateSubscription` (object, optional): Additional metadata for the subscription
  </Accordion>

<Accordion title="stripe/get_subscriptions">
    **Description:** Retrieve subscriptions with optional filtering.

* `customerIdGetSubscriptions` (string, optional): Filter subscriptions by customer ID
    * `subscriptionStatus` (string, optional): Filter by subscription status - Options: incomplete, incomplete\_expired, trialing, active, past\_due, canceled, unpaid
    * `limitGetSubscriptions` (string, optional): Maximum number of subscriptions to return (defaults to 10)
  </Accordion>
</AccordionGroup>

### **Product Management**

<AccordionGroup>
  <Accordion title="stripe/create_product">
    **Description:** Create a new product in your Stripe catalog.

* `productName` (string, required): The product name
    * `description` (string, optional): Product description
    * `metadataProduct` (object, optional): Additional product metadata as key-value pairs
  </Accordion>

<Accordion title="stripe/get_product_by_id">
    **Description:** Retrieve a specific product by its Stripe product ID.

* `productId` (string, required): The Stripe product ID to retrieve
  </Accordion>

<Accordion title="stripe/get_products">
    **Description:** Retrieve a list of products with optional filtering.

* `createdAfter` (string, optional): Filter products created after this date (Unix timestamp)
    * `createdBefore` (string, optional): Filter products created before this date (Unix timestamp)
    * `limitGetProducts` (string, optional): Maximum number of products to return (defaults to 10)
  </Accordion>
</AccordionGroup>

### **Financial Operations**

<AccordionGroup>
  <Accordion title="stripe/get_balance_transactions">
    **Description:** Retrieve balance transactions from your Stripe account.

* `balanceTransactionType` (string, optional): Filter by transaction type - Options: charge, refund, payment, payment\_refund
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>

<Accordion title="stripe/get_plans">
    **Description:** Retrieve subscription plans from your Stripe account.

* `isPlanActive` (boolean, optional): Filter by plan status - true for active plans, false for inactive plans
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>
</AccordionGroup>

### Basic Stripe Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Tools

### **Customer Management**

<AccordionGroup>
  <Accordion title="stripe/create_customer">
    **Description:** Create a new customer in your Stripe account.

    **Parameters:**

    * `emailCreateCustomer` (string, required): Customer's email address
    * `name` (string, optional): Customer's full name
    * `description` (string, optional): Customer description for internal reference
    * `metadataCreateCustomer` (object, optional): Additional metadata as key-value pairs (e.g., `{"field1": 1, "field2": 2}`)
  </Accordion>

  <Accordion title="stripe/get_customer_by_id">
    **Description:** Retrieve a specific customer by their Stripe customer ID.

    **Parameters:**

    * `idGetCustomer` (string, required): The Stripe customer ID to retrieve
  </Accordion>

  <Accordion title="stripe/get_customers">
    **Description:** Retrieve a list of customers with optional filtering.

    **Parameters:**

    * `emailGetCustomers` (string, optional): Filter customers by email address
    * `createdAfter` (string, optional): Filter customers created after this date (Unix timestamp)
    * `createdBefore` (string, optional): Filter customers created before this date (Unix timestamp)
    * `limitGetCustomers` (string, optional): Maximum number of customers to return (defaults to 10)
  </Accordion>

  <Accordion title="stripe/update_customer">
    **Description:** Update an existing customer's information.

    **Parameters:**

    * `customerId` (string, required): The ID of the customer to update
    * `emailUpdateCustomer` (string, optional): Updated email address
    * `name` (string, optional): Updated customer name
    * `description` (string, optional): Updated customer description
    * `metadataUpdateCustomer` (object, optional): Updated metadata as key-value pairs
  </Accordion>
</AccordionGroup>

### **Subscription Management**

<AccordionGroup>
  <Accordion title="stripe/create_subscription">
    **Description:** Create a new subscription for a customer.

    **Parameters:**

    * `customerIdCreateSubscription` (string, required): The customer ID for whom the subscription will be created
    * `plan` (string, required): The plan ID for the subscription - Use Connect Portal Workflow Settings to allow users to select a plan
    * `metadataCreateSubscription` (object, optional): Additional metadata for the subscription
  </Accordion>

  <Accordion title="stripe/get_subscriptions">
    **Description:** Retrieve subscriptions with optional filtering.

    **Parameters:**

    * `customerIdGetSubscriptions` (string, optional): Filter subscriptions by customer ID
    * `subscriptionStatus` (string, optional): Filter by subscription status - Options: incomplete, incomplete\_expired, trialing, active, past\_due, canceled, unpaid
    * `limitGetSubscriptions` (string, optional): Maximum number of subscriptions to return (defaults to 10)
  </Accordion>
</AccordionGroup>

### **Product Management**

<AccordionGroup>
  <Accordion title="stripe/create_product">
    **Description:** Create a new product in your Stripe catalog.

    **Parameters:**

    * `productName` (string, required): The product name
    * `description` (string, optional): Product description
    * `metadataProduct` (object, optional): Additional product metadata as key-value pairs
  </Accordion>

  <Accordion title="stripe/get_product_by_id">
    **Description:** Retrieve a specific product by its Stripe product ID.

    **Parameters:**

    * `productId` (string, required): The Stripe product ID to retrieve
  </Accordion>

  <Accordion title="stripe/get_products">
    **Description:** Retrieve a list of products with optional filtering.

    **Parameters:**

    * `createdAfter` (string, optional): Filter products created after this date (Unix timestamp)
    * `createdBefore` (string, optional): Filter products created before this date (Unix timestamp)
    * `limitGetProducts` (string, optional): Maximum number of products to return (defaults to 10)
  </Accordion>
</AccordionGroup>

### **Financial Operations**

<AccordionGroup>
  <Accordion title="stripe/get_balance_transactions">
    **Description:** Retrieve balance transactions from your Stripe account.

    **Parameters:**

    * `balanceTransactionType` (string, optional): Filter by transaction type - Options: charge, refund, payment, payment\_refund
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>

  <Accordion title="stripe/get_plans">
    **Description:** Retrieve subscription plans from your Stripe account.

    **Parameters:**

    * `isPlanActive` (boolean, optional): Filter by plan status - true for active plans, false for inactive plans
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>
</AccordionGroup>

## Usage Examples

### Basic Stripe Agent Setup
```

---

## Tasks

**URL:** llms-txt#tasks

**Contents:**
- Overview
  - Task Execution Flow
- Task Attributes
- Creating Tasks
  - YAML Configuration (Recommended)

Source: https://docs.crewai.com/en/concepts/tasks

Detailed guide on managing and creating tasks within the CrewAI framework.

In the CrewAI framework, a `Task` is a specific assignment completed by an `Agent`.

Tasks provide all necessary details for execution, such as a description, the agent responsible, required tools, and more, facilitating a wide range of action complexities.

Tasks within CrewAI can be collaborative, requiring multiple agents to work together. This is managed through the task properties and orchestrated by the Crew's process, enhancing teamwork and efficiency.

<Note type="info" title="Enterprise Enhancement: Visual Task Builder">
  CrewAI AOP includes a Visual Task Builder in Crew Studio that simplifies complex task creation and chaining. Design your task flows visually and test them in real-time without writing code.

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c4f5428b111816273b3b53d9cef14fad" alt="Task Builder Screenshot" data-og-width="2654" width="2654" data-og-height="1710" height="1710" data-path="images/enterprise/crew-studio-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=35ea9140f0b9e57da5f45adbc7e2f166 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ae6f0c18ef3679b5466177710fbc4a94 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6c3e2fe013ab4826da90c937a9855635 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7f1474dd7f983532dc910363b96f783a 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f1a6d7e744e6862af5e72dce4deb0fd1 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=74aeb1ccd8e2c8f84d4247b8d0259737 2500w" />

The Visual Task Builder enables:

* Drag-and-drop task creation
  * Visual task dependencies and flow
  * Real-time testing and validation
  * Easy sharing and collaboration
</Note>

### Task Execution Flow

Tasks can be executed in two ways:

* **Sequential**: Tasks are executed in the order they are defined
* **Hierarchical**: Tasks are assigned to agents based on their roles and expertise

The execution flow is defined when creating the crew:

| Attribute                              | Parameters              | Type                        | Description                                                                                                     |                                                                            |
| :------------------------------------- | :---------------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Description**                        | `description`           | `str`                       | A clear, concise statement of what the task entails.                                                            |                                                                            |
| **Expected Output**                    | `expected_output`       | `str`                       | A detailed description of what the task's completion looks like.                                                |                                                                            |
| **Name** *(optional)*                  | `name`                  | `Optional[str]`             | A name identifier for the task.                                                                                 |                                                                            |
| **Agent** *(optional)*                 | `agent`                 | `Optional[BaseAgent]`       | The agent responsible for executing the task.                                                                   |                                                                            |
| **Tools** *(optional)*                 | `tools`                 | `List[BaseTool]`            | The tools/resources the agent is limited to use for this task.                                                  |                                                                            |
| **Context** *(optional)*               | `context`               | `Optional[List["Task"]]`    | Other tasks whose outputs will be used as context for this task.                                                |                                                                            |
| **Async Execution** *(optional)*       | `async_execution`       | `Optional[bool]`            | Whether the task should be executed asynchronously. Defaults to False.                                          |                                                                            |
| **Human Input** *(optional)*           | `human_input`           | `Optional[bool]`            | Whether the task should have a human review the final answer of the agent. Defaults to False.                   |                                                                            |
| **Markdown** *(optional)*              | `markdown`              | `Optional[bool]`            | Whether the task should instruct the agent to return the final answer formatted in Markdown. Defaults to False. |                                                                            |
| **Config** *(optional)*                | `config`                | `Optional[Dict[str, Any]]`  | Task-specific configuration parameters.                                                                         |                                                                            |
| **Output File** *(optional)*           | `output_file`           | `Optional[str]`             | File path for storing the task output.                                                                          |                                                                            |
| **Create Directory** *(optional)*      | `create_directory`      | `Optional[bool]`            | Whether to create the directory for output\_file if it doesn't exist. Defaults to True.                         |                                                                            |
| **Output JSON** *(optional)*           | `output_json`           | `Optional[Type[BaseModel]]` | A Pydantic model to structure the JSON output.                                                                  |                                                                            |
| **Output Pydantic** *(optional)*       | `output_pydantic`       | `Optional[Type[BaseModel]]` | A Pydantic model for task output.                                                                               |                                                                            |
| **Callback** *(optional)*              | `callback`              | `Optional[Any]`             | Function/object to be executed after task completion.                                                           |                                                                            |
| **Guardrail** *(optional)*             | `guardrail`             | `Optional[Callable]`        | Function to validate task output before proceeding to next task.                                                |                                                                            |
| **Guardrails** *(optional)*            | `guardrails`            | \`Optional\[List\[Callable] | List\[str]]\`                                                                                                   | List of guardrails to validate task output before proceeding to next task. |
| **Guardrail Max Retries** *(optional)* | `guardrail_max_retries` | `Optional[int]`             | Maximum number of retries when guardrail validation fails. Defaults to 3.                                       |                                                                            |

<Note type="warning" title="Deprecated: max_retries">
  The task attribute `max_retries` is deprecated and will be removed in v1.0.0.
  Use `guardrail_max_retries` instead to control retry attempts when a guardrail fails.
</Note>

There are two ways to create tasks in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define tasks. We strongly recommend using this approach to define tasks in your CrewAI projects.

After creating your CrewAI project as outlined in the [Installation](/en/installation) section, navigate to the `src/latest_ai_development/config/tasks.yaml` file and modify the template to match your specific task requirements.

<Note>
  Variables in your YAML files (like `{topic}`) will be replaced with values from your inputs when running the crew:

Here's an example of how to configure tasks using YAML:

'
  agent: reporting_analyst
  markdown: true
  output_file: report.md
python crew.py theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## Task Attributes

| Attribute                              | Parameters              | Type                        | Description                                                                                                     |                                                                            |
| :------------------------------------- | :---------------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Description**                        | `description`           | `str`                       | A clear, concise statement of what the task entails.                                                            |                                                                            |
| **Expected Output**                    | `expected_output`       | `str`                       | A detailed description of what the task's completion looks like.                                                |                                                                            |
| **Name** *(optional)*                  | `name`                  | `Optional[str]`             | A name identifier for the task.                                                                                 |                                                                            |
| **Agent** *(optional)*                 | `agent`                 | `Optional[BaseAgent]`       | The agent responsible for executing the task.                                                                   |                                                                            |
| **Tools** *(optional)*                 | `tools`                 | `List[BaseTool]`            | The tools/resources the agent is limited to use for this task.                                                  |                                                                            |
| **Context** *(optional)*               | `context`               | `Optional[List["Task"]]`    | Other tasks whose outputs will be used as context for this task.                                                |                                                                            |
| **Async Execution** *(optional)*       | `async_execution`       | `Optional[bool]`            | Whether the task should be executed asynchronously. Defaults to False.                                          |                                                                            |
| **Human Input** *(optional)*           | `human_input`           | `Optional[bool]`            | Whether the task should have a human review the final answer of the agent. Defaults to False.                   |                                                                            |
| **Markdown** *(optional)*              | `markdown`              | `Optional[bool]`            | Whether the task should instruct the agent to return the final answer formatted in Markdown. Defaults to False. |                                                                            |
| **Config** *(optional)*                | `config`                | `Optional[Dict[str, Any]]`  | Task-specific configuration parameters.                                                                         |                                                                            |
| **Output File** *(optional)*           | `output_file`           | `Optional[str]`             | File path for storing the task output.                                                                          |                                                                            |
| **Create Directory** *(optional)*      | `create_directory`      | `Optional[bool]`            | Whether to create the directory for output\_file if it doesn't exist. Defaults to True.                         |                                                                            |
| **Output JSON** *(optional)*           | `output_json`           | `Optional[Type[BaseModel]]` | A Pydantic model to structure the JSON output.                                                                  |                                                                            |
| **Output Pydantic** *(optional)*       | `output_pydantic`       | `Optional[Type[BaseModel]]` | A Pydantic model for task output.                                                                               |                                                                            |
| **Callback** *(optional)*              | `callback`              | `Optional[Any]`             | Function/object to be executed after task completion.                                                           |                                                                            |
| **Guardrail** *(optional)*             | `guardrail`             | `Optional[Callable]`        | Function to validate task output before proceeding to next task.                                                |                                                                            |
| **Guardrails** *(optional)*            | `guardrails`            | \`Optional\[List\[Callable] | List\[str]]\`                                                                                                   | List of guardrails to validate task output before proceeding to next task. |
| **Guardrail Max Retries** *(optional)* | `guardrail_max_retries` | `Optional[int]`             | Maximum number of retries when guardrail validation fails. Defaults to 3.                                       |                                                                            |

<Note type="warning" title="Deprecated: max_retries">
  The task attribute `max_retries` is deprecated and will be removed in v1.0.0.
  Use `guardrail_max_retries` instead to control retry attempts when a guardrail fails.
</Note>

## Creating Tasks

There are two ways to create tasks in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define tasks. We strongly recommend using this approach to define tasks in your CrewAI projects.

After creating your CrewAI project as outlined in the [Installation](/en/installation) section, navigate to the `src/latest_ai_development/config/tasks.yaml` file and modify the template to match your specific task requirements.

<Note>
  Variables in your YAML files (like `{topic}`) will be replaced with values from your inputs when running the crew:
```

Example 2 (unknown):
```unknown
</Note>

Here's an example of how to configure tasks using YAML:
```

Example 3 (unknown):
```unknown
To use this YAML configuration in your code, create a crew class that inherits from `CrewBase`:
```

---

## Task for site administration

**URL:** llms-txt#task-for-site-administration

**Contents:**
  - Automated Content Workflows

admin_task = Task(
    description="""
    1. Get information about all accessible SharePoint sites
    2. Analyze site structure and content organization
    3. Identify sites with low activity or outdated content
    4. Generate recommendations for site optimization
    """,
    agent=site_administrator,
    expected_output="Site analysis completed with optimization recommendations"
)

crew = Crew(
    agents=[site_administrator],
    tasks=[admin_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

workflow_automator = Agent(
    role="Workflow Automator",
    goal="Automate SharePoint content workflows and processes",
    backstory="An AI assistant that automates complex SharePoint workflows and content management processes.",
    apps=['microsoft_sharepoint']
)

**Examples:**

Example 1 (unknown):
```unknown
### Automated Content Workflows
```

---

## Task to analyze and optimize task distribution

**URL:** llms-txt#task-to-analyze-and-optimize-task-distribution

**Contents:**
  - Getting Help

task_analysis = Task(
    description="""
    Search for all tasks assigned to team members in the last 30 days,
    analyze completion patterns, and create optimization recommendations
    """,
    agent=task_analyst,
    expected_output="Task analysis report with optimization recommendations"
)

crew = Crew(
    agents=[task_analyst],
    tasks=[task_analysis]
)

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with ClickUp integration setup or troubleshooting.
</Card>

---

## Task to analyze data and create reports

**URL:** llms-txt#task-to-analyze-data-and-create-reports

**Contents:**
  - Spreadsheet Creation and Management

analysis_task = Task(
    description="""
    1. Retrieve all sales data from the current month's spreadsheet
    2. Analyze the data for trends and patterns
    3. Create a summary report in a new row with key metrics
    """,
    agent=data_analyst,
    expected_output="Sales data analyzed and summary report created with key insights"
)

crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

spreadsheet_manager = Agent(
    role="Spreadsheet Manager",
    goal="Create and manage spreadsheets efficiently",
    backstory="An AI assistant that specializes in creating and organizing spreadsheets.",
    apps=['google_sheets']
)

**Examples:**

Example 1 (unknown):
```unknown
### Spreadsheet Creation and Management
```

---

## Task to analyze email patterns

**URL:** llms-txt#task-to-analyze-email-patterns

**Contents:**
  - Thread Management

analysis_task = Task(
    description="""
    Search for all unread emails from the last 7 days,
    categorize them by sender domain,
    and create a summary report of communication patterns
    """,
    agent=email_analyst,
    expected_output="Email analysis report with communication patterns and recommendations"
)

crew = Crew(
    agents=[email_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### Thread Management
```

---

## Task to analyze existing data

**URL:** llms-txt#task-to-analyze-existing-data

**Contents:**
  - Workbook Creation and Structure

analysis_task = Task(
    description="Analyze sales data in existing workbooks and create summary charts and tables",
    agent=data_analyst,
    expected_output="Data analyzed with summary charts and tables created"
)

crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

workbook_creator = Agent(
    role="Workbook Creator",
    goal="Create structured Excel workbooks with multiple worksheets and data organization",
    backstory="An AI assistant that creates well-organized Excel workbooks for various business needs.",
    apps=['microsoft_excel']
)

**Examples:**

Example 1 (unknown):
```unknown
### Workbook Creation and Structure
```

---

## Task to analyze project status

**URL:** llms-txt#task-to-analyze-project-status

**Contents:**
  - Automated Issue Management

analysis_task = Task(
    description="""
    1. Get all projects and their issue types
    2. Search for all open issues across projects
    3. Analyze issue distribution by status and assignee
    4. Create a summary report issue with findings
    """,
    agent=project_analyst,
    expected_output="Project analysis completed with summary report created"
)

crew = Crew(
    agents=[project_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

automation_manager = Agent(
    role="Automation Manager",
    goal="Automate issue management and workflow processes",
    backstory="An AI assistant that automates repetitive issue management tasks.",
    apps=['jira']
)

**Examples:**

Example 1 (unknown):
```unknown
### Automated Issue Management
```

---

## Task to automate issue management

**URL:** llms-txt#task-to-automate-issue-management

**Contents:**
  - Advanced Schema-Based Operations

automation_task = Task(
    description="""
    1. Search for all unassigned issues using JQL
    2. Get available assignees for each project
    3. Automatically assign issues based on workload and expertise
    4. Update issue priorities based on age and type
    5. Create weekly sprint planning issues
    """,
    agent=automation_manager,
    expected_output="Issues automatically assigned and sprint planning issues created"
)

crew = Crew(
    agents=[automation_manager],
    tasks=[automation_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

schema_specialist = Agent(
    role="Schema Specialist",
    goal="Handle complex Jira operations using dynamic schemas",
    backstory="An AI assistant that can work with dynamic Jira schemas and custom issue types.",
    apps=['jira']
)

**Examples:**

Example 1 (unknown):
```unknown
### Advanced Schema-Based Operations
```

---

## Task to collect and organize data

**URL:** llms-txt#task-to-collect-and-organize-data

**Contents:**
  - Data Analysis and Reporting

data_collection = Task(
    description="Retrieve current inventory data and add new product entries to the inventory spreadsheet",
    agent=data_collector,
    expected_output="Inventory data retrieved and new products added successfully"
)

crew = Crew(
    agents=[data_collector],
    tasks=[data_collection]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze spreadsheet data and generate insights",
    backstory="An experienced data analyst who extracts insights from spreadsheet data.",
    apps=['google_sheets']
)

**Examples:**

Example 1 (unknown):
```unknown
### Data Analysis and Reporting
```

---

## Task to coordinate availability

**URL:** llms-txt#task-to-coordinate-availability

**Contents:**
  - Automated Scheduling Workflows

availability_task = Task(
    description="""
    1. Get the list of available calendars
    2. Check availability for all calendars next Friday afternoon
    3. Create a team meeting for the first available 2-hour slot
    4. Include Google Meet link and send invitations
    """,
    agent=availability_coordinator,
    expected_output="Team meeting scheduled based on availability with all team members invited"
)

crew = Crew(
    agents=[availability_coordinator],
    tasks=[availability_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

scheduling_automator = Agent(
    role="Scheduling Automator",
    goal="Automate scheduling workflows and calendar management",
    backstory="An AI assistant that automates complex scheduling scenarios and calendar workflows.",
    apps=['google_calendar']
)

**Examples:**

Example 1 (unknown):
```unknown
### Automated Scheduling Workflows
```

---

## Task to coordinate project setup

**URL:** llms-txt#task-to-coordinate-project-setup

**Contents:**
  - Issue Hierarchy and Sub-task Management

project_coordination = Task(
    description="""
    1. Search for engineering teams in Linear
    2. Create a new project for Q2 feature development
    3. Associate the project with relevant teams
    4. Create initial project milestones as issues
    """,
    agent=project_coordinator,
    expected_output="Q2 project created with teams assigned and initial milestones established"
)

crew = Crew(
    agents=[project_coordinator],
    tasks=[project_coordination]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

task_organizer = Agent(
    role="Task Organizer",
    goal="Organize complex issues into manageable sub-tasks",
    backstory="An AI assistant that breaks down complex development work into organized sub-tasks.",
    apps=['linear']
)

**Examples:**

Example 1 (unknown):
```unknown
### Issue Hierarchy and Sub-task Management
```

---

## Task to coordinate team activities

**URL:** llms-txt#task-to-coordinate-team-activities

**Contents:**
  - Collaboration and Communication

coordination_task = Task(
    description="""
    1. List all users in the workspace
    2. Get detailed information for specific team members
    3. Create comments on relevant pages to notify team members about updates
    """,
    agent=team_coordinator,
    expected_output="Team coordination completed with user information gathered and notifications sent"
)

crew = Crew(
    agents=[team_coordinator],
    tasks=[coordination_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

collaboration_facilitator = Agent(
    role="Collaboration Facilitator",
    goal="Facilitate team collaboration through comments and user management",
    backstory="An AI assistant that specializes in team collaboration and communication.",
    apps=['notion']
)

**Examples:**

Example 1 (unknown):
```unknown
### Collaboration and Communication
```

---

## Task to coordinate team communication

**URL:** llms-txt#task-to-coordinate-team-communication

**Contents:**
  - Advanced Messaging with Block Kit

coordination_task = Task(
    description="Send task completion notifications to team members and update project channels",
    agent=communication_manager,
    expected_output="Team notifications sent and project channels updated successfully"
)

crew = Crew(
    agents=[communication_manager],
    tasks=[coordination_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### Advanced Messaging with Block Kit
```

---

## Task to create and assign a task

**URL:** llms-txt#task-to-create-and-assign-a-task

**Contents:**
  - Advanced Project Management

task_management = Task(
    description="Create a task called 'Review quarterly reports' and assign it to the appropriate team member",
    agent=task_manager_agent,
    expected_output="Task created and assigned successfully"
)

crew = Crew(
    agents=[task_manager_agent],
    tasks=[task_management]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

project_coordinator = Agent(
    role="Project Coordinator",
    goal="Coordinate project activities and track progress",
    backstory="An experienced project coordinator who ensures projects run smoothly.",
    apps=['asana']
)

**Examples:**

Example 1 (unknown):
```unknown
### Advanced Project Management
```

---

## Task to create and set up new spreadsheets

**URL:** llms-txt#task-to-create-and-set-up-new-spreadsheets

**Contents:**
  - Automated Data Updates

setup_task = Task(
    description="""
    1. Create a new spreadsheet for quarterly reports
    2. Set up proper headers and structure
    3. Add initial data and formatting
    """,
    agent=spreadsheet_manager,
    expected_output="New quarterly report spreadsheet created and properly structured"
)

crew = Crew(
    agents=[spreadsheet_manager],
    tasks=[setup_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

data_updater = Agent(
    role="Data Updater",
    goal="Automatically update and maintain spreadsheet data",
    backstory="An AI assistant that maintains data accuracy and updates records automatically.",
    apps=['google_sheets']
)

**Examples:**

Example 1 (unknown):
```unknown
### Automated Data Updates
```

---

## Task to create and update contacts

**URL:** llms-txt#task-to-create-and-update-contacts

**Contents:**
  - Contact Group Management

curation_task = Task(
    description="""
    1. Search for existing contacts related to new business partners
    2. Create new contacts for partners not in the system
    3. Update existing contact information with latest details
    4. Organize contacts into appropriate groups
    """,
    agent=contact_curator,
    expected_output="Contact database updated with new partners and organized groups"
)

crew = Crew(
    agents=[contact_curator],
    tasks=[curation_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

group_organizer = Agent(
    role="Contact Group Organizer",
    goal="Organize contacts into meaningful groups and categories",
    backstory="An AI assistant that specializes in contact organization and group management.",
    apps=['google_contacts']
)

**Examples:**

Example 1 (unknown):
```unknown
### Contact Group Management
```

---

## Task to create and update presentations

**URL:** llms-txt#task-to-create-and-update-presentations

**Contents:**
  - Data Integration and Visualization

content_task = Task(
    description="Create a new presentation and add content slides with charts and text",
    agent=content_manager,
    expected_output="Presentation created with updated content and visual elements"
)

crew = Crew(
    agents=[content_manager],
    tasks=[content_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

data_visualizer = Agent(
    role="Data Visualizer",
    goal="Create presentations with data imported from spreadsheets",
    backstory="An AI assistant that specializes in data visualization and presentation integration.",
    apps=['google_slides']
)

**Examples:**

Example 1 (unknown):
```unknown
### Data Integration and Visualization
```

---

## Task to create a contact

**URL:** llms-txt#task-to-create-a-contact

**Contents:**
  - Contact Management

create_contact = Task(
    description="Create a new contact for 'John Doe' with email 'john.doe@example.com'.",
    agent=contact_creator,
    expected_output="Contact created successfully in HubSpot."
)

crew = Crew(
    agents=[contact_creator],
    tasks=[create_contact]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### Contact Management
```

---

## Task to create a meeting

**URL:** llms-txt#task-to-create-a-meeting

**Contents:**
- Troubleshooting
  - Common Issues
  - Getting Help

schedule_meeting_task = Task(
    description="Create a Teams meeting titled 'Weekly Team Sync' scheduled for tomorrow at 10:00 AM lasting for 1 hour (use proper ISO 8601 format with timezone).",
    agent=meeting_scheduler,
    expected_output="Teams meeting created successfully with meeting details."
)

crew = Crew(
    agents=[meeting_scheduler],
    tasks=[schedule_meeting_task]
)

**Authentication Errors**

* Ensure your Microsoft account has the necessary permissions for Teams access.
* Required scopes include: `Team.ReadBasic.All`, `Channel.ReadBasic.All`, `ChannelMessage.Send`, `ChannelMessage.Read.All`, `OnlineMeetings.ReadWrite`, `OnlineMeetings.Read`.
* Verify that the OAuth connection includes all required scopes.

**Team and Channel Access**

* Ensure you are a member of the teams you're trying to access.
* Double-check team IDs and channel IDs for correctness.
* Team and channel IDs can be obtained using the `get_teams` and `get_channels` actions.

**Message Sending Issues**

* Ensure `team_id`, `channel_id`, and `message` are provided for `send_message`.
* Verify that you have permissions to send messages to the specified channel.
* Choose appropriate `content_type` (text or html) based on your message format.

* Ensure `subject`, `startDateTime`, and `endDateTime` are provided.
* Use proper ISO 8601 format with timezone for datetime fields (e.g., '2024-01-20T10:00:00-08:00').
* Verify that the meeting times are in the future.

**Message Retrieval Limitations**

* The `get_messages` action can retrieve a maximum of 50 messages per request.
* Messages are returned in reverse chronological order (newest first).

* For `search_online_meetings_by_join_url`, ensure the join URL is exact and properly formatted.
* The URL should be the complete Teams meeting join URL.

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft Teams integration setup or troubleshooting.
</Card>

---

## Task to create a meeting and add a contact

**URL:** llms-txt#task-to-create-a-meeting-and-add-a-contact

**Contents:**
- Troubleshooting
  - Common Issues
  - Getting Help

schedule_task = Task(
    description="Create a calendar event for tomorrow at 2 PM titled 'Team Meeting' with location 'Conference Room A', and create a new contact for 'John Smith' with email 'john.smith@example.com' and job title 'Project Manager'.",
    agent=scheduler,
    expected_output="Calendar event created and new contact added successfully."
)

crew = Crew(
    agents=[scheduler],
    tasks=[schedule_task]
)

**Authentication Errors**

* Ensure your Microsoft account has the necessary permissions for mail, calendar, and contact access.
* Required scopes include: `Mail.Read`, `Mail.Send`, `Calendars.Read`, `Calendars.ReadWrite`, `Contacts.Read`, `Contacts.ReadWrite`.
* Verify that the OAuth connection includes all required scopes.

**Email Sending Issues**

* Ensure `to_recipients`, `subject`, and `body` are provided for `send_email`.
* Check that email addresses are properly formatted.
* Verify that the account has `Mail.Send` permissions.

**Calendar Event Creation**

* Ensure `subject`, `start_datetime`, and `end_datetime` are provided.
* Use proper ISO 8601 format for datetime fields (e.g., '2024-01-20T10:00:00').
* Verify timezone settings if events appear at incorrect times.

**Contact Management**

* For `create_contact`, ensure `displayName` is provided as it's required.
* When providing `emailAddresses`, use the proper object format with `address` and `name` properties.

**Search and Filter Issues**

* Use proper OData syntax for `filter` parameters.
* For date filters, use ISO 8601 format (e.g., "receivedDateTime ge '2024-01-01T00:00:00Z'").

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft Outlook integration setup or troubleshooting.
</Card>

---

## Task to create a new release

**URL:** llms-txt#task-to-create-a-new-release

**Contents:**
  - Issue Tracking and Management

release_task = Task(
    description="""
    Create a new release v2.1.0 for the project with:
    - Auto-generated release notes
    - Target the main branch
    - Include a description of new features and bug fixes
    """,
    agent=release_manager,
    expected_output="Release v2.1.0 created successfully with release notes"
)

crew = Crew(
    agents=[release_manager],
    tasks=[release_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

project_coordinator = Agent(
    role="Project Coordinator",
    goal="Track and coordinate project issues and development progress",
    backstory="An AI assistant that helps coordinate development work and track project progress.",
    apps=['github']
)

**Examples:**

Example 1 (unknown):
```unknown
### Issue Tracking and Management
```

---

## Task to create comments on pages

**URL:** llms-txt#task-to-create-comments-on-pages

**Contents:**
  - User Information and Team Management

comment_task = Task(
    description="Create a summary comment on the project status page with key updates",
    agent=comment_manager,
    expected_output="Comment created successfully with project status updates"
)

crew = Crew(
    agents=[comment_manager],
    tasks=[comment_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

team_coordinator = Agent(
    role="Team Coordinator",
    goal="Coordinate team activities and manage user information",
    backstory="An AI assistant that helps coordinate team activities and manages user information.",
    apps=['notion']
)

**Examples:**

Example 1 (unknown):
```unknown
### User Information and Team Management
```

---

## Task to create data-driven presentations

**URL:** llms-txt#task-to-create-data-driven-presentations

**Contents:**
  - Presentation Library Management

visualization_task = Task(
    description="""
    1. Create a new presentation for monthly sales report
    2. Import data from the sales spreadsheet
    3. Create charts and visualizations from the imported data
    4. Generate thumbnails for slide previews
    """,
    agent=data_visualizer,
    expected_output="Data-driven presentation created with imported spreadsheet data and visualizations"
)

crew = Crew(
    agents=[data_visualizer],
    tasks=[visualization_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

library_manager = Agent(
    role="Presentation Library Manager",
    goal="Manage and organize presentation libraries",
    backstory="An AI assistant that manages presentation collections and file organization.",
    apps=['google_slides']
)

**Examples:**

Example 1 (unknown):
```unknown
### Presentation Library Management
```

---

## Task to create issue hierarchy

**URL:** llms-txt#task-to-create-issue-hierarchy

**Contents:**
  - Automated Development Workflow

hierarchy_task = Task(
    description="""
    1. Search for large feature issues that need to be broken down
    2. For each complex issue, create sub-issues for different components
    3. Update the parent issues with proper descriptions and links to sub-issues
    4. Assign sub-issues to appropriate team members based on expertise
    """,
    agent=task_organizer,
    expected_output="Complex issues broken down into manageable sub-tasks with proper assignments"
)

crew = Crew(
    agents=[task_organizer],
    tasks=[hierarchy_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

workflow_automator = Agent(
    role="Workflow Automator",
    goal="Automate development workflow processes in Linear",
    backstory="An AI assistant that automates repetitive development workflow tasks.",
    apps=['linear']
)

**Examples:**

Example 1 (unknown):
```unknown
### Automated Development Workflow
```

---

## Task to create structured workbooks

**URL:** llms-txt#task-to-create-structured-workbooks

**Contents:**
  - Data Manipulation and Updates

creation_task = Task(
    description="""
    1. Create a new quarterly report workbook
    2. Add multiple worksheets for different departments
    3. Create tables with headers for data organization
    4. Set up charts for key metrics visualization
    """,
    agent=workbook_creator,
    expected_output="Structured workbook created with multiple worksheets, tables, and charts"
)

crew = Crew(
    agents=[workbook_creator],
    tasks=[creation_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

data_manipulator = Agent(
    role="Data Manipulator",
    goal="Update and manipulate data in Excel worksheets efficiently",
    backstory="An AI assistant that handles data updates, table management, and range operations.",
    apps=['microsoft_excel']
)

**Examples:**

Example 1 (unknown):
```unknown
### Data Manipulation and Updates
```

---

## Task to edit document content

**URL:** llms-txt#task-to-edit-document-content

**Contents:**
  - Advanced Document Operations

edit_content_task = Task(
    description="In document 'your_document_id', insert the text 'Executive Summary: ' at the beginning, then replace all instances of 'TODO' with 'COMPLETED'.",
    agent=text_editor,
    expected_output="Document updated with new text inserted and TODO items replaced."
)

crew = Crew(
    agents=[text_editor],
    tasks=[edit_content_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### Advanced Document Operations
```

---

## Task to facilitate collaboration

**URL:** llms-txt#task-to-facilitate-collaboration

**Contents:**
  - Automated Team Communication

collaboration_task = Task(
    description="""
    1. Identify active users in the workspace
    2. Create contextual comments on project pages to facilitate discussions
    3. Provide status updates and feedback through comments
    """,
    agent=collaboration_facilitator,
    expected_output="Collaboration facilitated with comments created and team members notified"
)

crew = Crew(
    agents=[collaboration_facilitator],
    tasks=[collaboration_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

communication_automator = Agent(
    role="Communication Automator",
    goal="Automate team communication and user management workflows",
    backstory="An AI assistant that automates communication workflows and manages user interactions.",
    apps=['notion']
)

**Examples:**

Example 1 (unknown):
```unknown
### Automated Team Communication
```

---

## Task to format document

**URL:** llms-txt#task-to-format-document

**Contents:**
- Troubleshooting
  - Common Issues
  - Getting Help

format_doc_task = Task(
    description="In document 'your_document_id', insert a page break at position 100, create a named range called 'Introduction' for characters 1-50, and apply batch formatting updates.",
    agent=document_formatter,
    expected_output="Document formatted with page break, named range, and styling applied."
)

crew = Crew(
    agents=[document_formatter],
    tasks=[format_doc_task]
)

**Authentication Errors**

* Ensure your Google account has the necessary permissions for Google Docs access.
* Verify that the OAuth connection includes all required scopes (`https://www.googleapis.com/auth/documents`).

**Document ID Issues**

* Double-check document IDs for correctness.
* Ensure the document exists and is accessible to your account.
* Document IDs can be found in the Google Docs URL.

**Text Insertion and Range Operations**

* When using `insert_text` or `delete_content_range`, ensure index positions are valid.
* Remember that Google Docs uses zero-based indexing.
* The document must have content at the specified index positions.

**Batch Update Request Formatting**

* When using `batch_update`, ensure the `requests` array is correctly formatted according to the Google Docs API documentation.
* Complex updates require specific JSON structures for each request type.

**Replace Text Operations**

* For `replace_text`, ensure the `containsText` parameter exactly matches the text you want to replace.
* Use `matchCase` parameter to control case sensitivity.

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Google Docs integration setup or troubleshooting.
</Card>

---

## Task to list and read documents

**URL:** llms-txt#task-to-list-and-read-documents

**Contents:**
  - Document Cleanup and Organization

read_docs_task = Task(
    description="List all Word documents in my OneDrive, then get the content and properties of the first document found.",
    agent=document_reader,
    expected_output="List of documents with content and properties of the first document."
)

crew = Crew(
    agents=[document_reader],
    tasks=[read_docs_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### Document Cleanup and Organization
```

---

## Task to manage billing operations

**URL:** llms-txt#task-to-manage-billing-operations

**Contents:**
  - Subscription Management

billing_task = Task(
    description="Create a new customer and set up their premium subscription plan",
    agent=billing_manager,
    expected_output="Customer created and subscription activated successfully"
)

crew = Crew(
    agents=[billing_manager],
    tasks=[billing_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

subscription_manager = Agent(
    role="Subscription Manager",
    goal="Manage customer subscriptions and optimize recurring revenue",
    backstory="An AI assistant that specializes in subscription lifecycle management and customer retention.",
    apps=['stripe']
)

**Examples:**

Example 1 (unknown):
```unknown
### Subscription Management
```

---

## Task to manage contacts

**URL:** llms-txt#task-to-manage-contacts

**Contents:**
  - Getting Help

contact_task = Task(
    description="Create a new contact for 'Jane Smith' at 'Global Tech Inc.' with email 'jane.smith@globaltech.com'.",
    agent=crm_manager,
    expected_output="Contact database updated with the new contact."
)

crew = Crew(
    agents=[crm_manager],
    tasks=[contact_task]
)

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with HubSpot integration setup or troubleshooting.
</Card>

---

## Task to manage customer accounts

**URL:** llms-txt#task-to-manage-customer-accounts

**Contents:**
  - Advanced SOQL Queries and Reporting

account_task = Task(
    description="""
    1. Create a new account for TechCorp Inc.
    2. Add John Doe as the primary contact for this account
    3. Create a follow-up task for next week to check on their project status
    """,
    agent=account_manager,
    expected_output="Account, contact, and follow-up task created successfully"
)

crew = Crew(
    agents=[account_manager],
    tasks=[account_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

data_analyst = Agent(
    role="Sales Data Analyst",
    goal="Generate insights from Salesforce data using SOQL queries",
    backstory="An analytical AI that excels at extracting meaningful insights from CRM data.",
    apps=['salesforce']
)

**Examples:**

Example 1 (unknown):
```unknown
### Advanced SOQL Queries and Reporting
```

---

## Task to manage documents

**URL:** llms-txt#task-to-manage-documents

**Contents:**
  - Site Administration and Analysis

document_task = Task(
    description="""
    1. Get all files from the main document library
    2. Upload new policy documents to the appropriate folders
    3. Organize files by department and date
    4. Remove outdated documents
    """,
    agent=document_manager,
    expected_output="Document library organized with new files uploaded and outdated files removed"
)

crew = Crew(
    agents=[document_manager],
    tasks=[document_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

site_administrator = Agent(
    role="Site Administrator",
    goal="Administer and analyze SharePoint sites",
    backstory="An AI assistant that handles site administration and provides insights on site usage.",
    apps=['microsoft_sharepoint']
)

**Examples:**

Example 1 (unknown):
```unknown
### Site Administration and Analysis
```

---

## Task to manage event updates

**URL:** llms-txt#task-to-manage-event-updates

**Contents:**
  - Availability and Calendar Management

event_management = Task(
    description="""
    1. List all events for this week
    2. Update any events that need location changes to include video conference links
    3. Check availability for upcoming meetings
    """,
    agent=event_manager,
    expected_output="Weekly events updated with proper locations and availability checked"
)

crew = Crew(
    agents=[event_manager],
    tasks=[event_management]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

availability_coordinator = Agent(
    role="Availability Coordinator",
    goal="Coordinate availability and manage calendars for scheduling",
    backstory="An AI assistant that specializes in availability management and calendar coordination.",
    apps=['google_calendar']
)

**Examples:**

Example 1 (unknown):
```unknown
### Availability and Calendar Management
```

---

## Task to manage issue workflow

**URL:** llms-txt#task-to-manage-issue-workflow

**Contents:**
  - Project and Team Management

issue_workflow = Task(
    description="Create a feature request issue and update the status of related issues to reflect current progress",
    agent=issue_manager,
    expected_output="Feature request created and related issues updated"
)

crew = Crew(
    agents=[issue_manager],
    tasks=[issue_workflow]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

project_coordinator = Agent(
    role="Project Coordinator",
    goal="Coordinate projects and teams in Linear efficiently",
    backstory="An experienced project coordinator who manages development cycles and team workflows.",
    apps=['linear']
)

**Examples:**

Example 1 (unknown):
```unknown
### Project and Team Management
```

---

## Task to manage list data

**URL:** llms-txt#task-to-manage-list-data

**Contents:**
  - Document Library Management

list_management_task = Task(
    description="Get all lists from the project site, review items, and update status for completed tasks",
    agent=list_manager,
    expected_output="SharePoint lists reviewed and task statuses updated"
)

crew = Crew(
    agents=[list_manager],
    tasks=[list_management_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

document_manager = Agent(
    role="Document Manager",
    goal="Manage SharePoint document libraries and files",
    backstory="An AI assistant that specializes in document organization and file management.",
    apps=['microsoft_sharepoint']
)

**Examples:**

Example 1 (unknown):
```unknown
### Document Library Management
```

---

## Task to manage presentation library

**URL:** llms-txt#task-to-manage-presentation-library

**Contents:**
  - Automated Presentation Workflows

library_task = Task(
    description="""
    1. List all existing presentations
    2. Generate thumbnails for presentation previews
    3. Upload supporting files to Drive and link to presentations
    4. Organize presentations by topic and date
    """,
    agent=library_manager,
    expected_output="Presentation library organized with thumbnails and linked supporting files"
)

crew = Crew(
    agents=[library_manager],
    tasks=[library_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

presentation_automator = Agent(
    role="Presentation Automator",
    goal="Automate presentation creation and management workflows",
    backstory="An AI assistant that automates complex presentation workflows and content generation.",
    apps=['google_slides']
)

**Examples:**

Example 1 (unknown):
```unknown
### Automated Presentation Workflows
```

---

## Task to manage product catalog

**URL:** llms-txt#task-to-manage-product-catalog

**Contents:**
  - Order and Customer Analytics

catalog_task = Task(
    description="""
    1. Create a new product "Premium Coffee Mug" from Coffee Co vendor
    2. Add high-quality product images and descriptions
    3. Search for similar products from the same vendor
    4. Update product tags and pricing strategy
    """,
    agent=product_manager,
    expected_output="Product created and catalog optimized successfully"
)

crew = Crew(
    agents=[product_manager],
    tasks=[catalog_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

analytics_agent = Agent(
    role="E-commerce Analyst",
    goal="Analyze customer behavior and order patterns to optimize store performance",
    backstory="An analytical AI that excels at extracting insights from e-commerce data.",
    apps=['shopify']
)

**Examples:**

Example 1 (unknown):
```unknown
### Order and Customer Analytics
```

---

## Task to manage sales pipeline

**URL:** llms-txt#task-to-manage-sales-pipeline

**Contents:**
  - Contact and Account Management

pipeline_task = Task(
    description="Create a qualified lead and convert it to an opportunity with $50,000 value",
    agent=sales_manager,
    expected_output="Lead created and opportunity established successfully"
)

crew = Crew(
    agents=[sales_manager],
    tasks=[pipeline_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

account_manager = Agent(
    role="Account Manager",
    goal="Manage customer accounts and maintain strong relationships",
    backstory="An AI assistant that specializes in account management and customer relationship building.",
    apps=['salesforce']
)

**Examples:**

Example 1 (unknown):
```unknown
### Contact and Account Management
```

---

## Task to manage store operations

**URL:** llms-txt#task-to-manage-store-operations

**Contents:**
  - Product Management with GraphQL

store_task = Task(
    description="Create a new customer and process their order for 2 Premium Coffee Mugs",
    agent=store_manager,
    expected_output="Customer created and order processed successfully"
)

crew = Crew(
    agents=[store_manager],
    tasks=[store_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

product_manager = Agent(
    role="Product Manager",
    goal="Manage product catalog and inventory with advanced GraphQL capabilities",
    backstory="An AI assistant that specializes in product management and catalog optimization.",
    apps=['shopify']
)

**Examples:**

Example 1 (unknown):
```unknown
### Product Management with GraphQL
```

---

## Task to manage subscription operations

**URL:** llms-txt#task-to-manage-subscription-operations

**Contents:**
  - Financial Analytics and Reporting

subscription_task = Task(
    description="""
    1. Create a new product "Premium Service Plan" with advanced features
    2. Set up subscription plans with different tiers
    3. Create customers and assign them to appropriate plans
    4. Monitor subscription status and handle billing issues
    """,
    agent=subscription_manager,
    expected_output="Subscription management system configured with customers and active plans"
)

crew = Crew(
    agents=[subscription_manager],
    tasks=[subscription_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

financial_analyst = Agent(
    role="Financial Analyst",
    goal="Analyze payment data and generate financial insights",
    backstory="An analytical AI that excels at extracting insights from payment and subscription data.",
    apps=['stripe']
)

**Examples:**

Example 1 (unknown):
```unknown
### Financial Analytics and Reporting
```

---

## Task to manage support workflow

**URL:** llms-txt#task-to-manage-support-workflow

**Contents:**
  - Advanced Ticket Management

support_task = Task(
    description="Create a ticket for login issues, add troubleshooting comments, and update status to resolved",
    agent=support_agent,
    expected_output="Support ticket managed through complete resolution workflow"
)

crew = Crew(
    agents=[support_agent],
    tasks=[support_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

ticket_manager = Agent(
    role="Ticket Manager",
    goal="Manage support ticket workflows and ensure timely resolution",
    backstory="An AI assistant that specializes in support ticket triage and workflow optimization.",
    apps=['zendesk']
)

**Examples:**

Example 1 (unknown):
```unknown
### Advanced Ticket Management
```

---

## Task to manage task workflow

**URL:** llms-txt#task-to-manage-task-workflow

**Contents:**
  - Advanced Project Management

task_workflow = Task(
    description="Create a task for project planning and assign it to the development team",
    agent=task_coordinator,
    expected_output="Task created and assigned successfully"
)

crew = Crew(
    agents=[task_coordinator],
    tasks=[task_workflow]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

project_manager = Agent(
    role="Project Manager",
    goal="Coordinate project activities and track team productivity",
    backstory="An experienced project manager who ensures projects are delivered on time.",
    apps=['clickup']
)

**Examples:**

Example 1 (unknown):
```unknown
### Advanced Project Management
```

---

## Task to manage ticket lifecycle

**URL:** llms-txt#task-to-manage-ticket-lifecycle

**Contents:**
  - Support Analytics and Reporting

ticket_workflow = Task(
    description="""
    1. Create a new support ticket for account access issues
    2. Add internal notes with troubleshooting steps
    3. Update ticket priority based on customer tier
    4. Add resolution comments and close the ticket
    """,
    agent=ticket_manager,
    expected_output="Complete ticket lifecycle managed from creation to resolution"
)

crew = Crew(
    agents=[ticket_manager],
    tasks=[ticket_workflow]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

support_analyst = Agent(
    role="Support Analyst",
    goal="Analyze support metrics and generate insights for team performance",
    backstory="An analytical AI that excels at extracting insights from support data and ticket patterns.",
    apps=['zendesk']
)

**Examples:**

Example 1 (unknown):
```unknown
### Support Analytics and Reporting
```

---

## Task to manipulate data

**URL:** llms-txt#task-to-manipulate-data

**Contents:**
  - Advanced Excel Automation

manipulation_task = Task(
    description="""
    1. Get data from existing worksheets
    2. Update specific ranges with new information
    3. Add new rows to existing tables
    4. Create additional charts based on updated data
    5. Organize data across multiple worksheets
    """,
    agent=data_manipulator,
    expected_output="Data updated across worksheets with new charts and organized structure"
)

crew = Crew(
    agents=[data_manipulator],
    tasks=[manipulation_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

excel_automator = Agent(
    role="Excel Automator",
    goal="Automate complex Excel workflows and data processing",
    backstory="An AI assistant that automates sophisticated Excel operations and data workflows.",
    apps=['microsoft_excel']
)

**Examples:**

Example 1 (unknown):
```unknown
### Advanced Excel Automation
```

---

## Task to organize and share files

**URL:** llms-txt#task-to-organize-and-share-files

**Contents:**
- Troubleshooting
  - Common Issues
  - Getting Help

organize_share_task = Task(
    description="Search for files containing 'presentation' in the name, create a folder called 'Presentations', move the found files to this folder, and create a view-only sharing link for the folder.",
    agent=file_organizer,
    expected_output="Files organized into 'Presentations' folder and sharing link created."
)

crew = Crew(
    agents=[file_organizer],
    tasks=[organize_share_task]
)

**Authentication Errors**

* Ensure your Microsoft account has the necessary permissions for file access (e.g., `Files.Read`, `Files.ReadWrite`).
* Verify that the OAuth connection includes all required scopes.

**File Upload Issues**

* Ensure `file_name` and `content` are provided for file uploads.
* Content must be Base64 encoded for binary files.
* Check that you have write permissions to OneDrive.

**File/Folder ID Issues**

* Double-check item IDs for correctness when accessing specific files or folders.
* Item IDs are returned by other operations like `list_files` or `search_files`.
* Ensure the referenced items exist and are accessible.

**Search and Filter Operations**

* Use appropriate search terms for `search_files` operations.
* For `filter` parameters, use proper OData syntax.

**File Operations (Copy/Move)**

* For `move_item`, ensure both `item_id` and `parent_id` are provided.
* For `copy_item`, only `item_id` is required; `parent_id` defaults to root if not specified.
* Verify that destination folders exist and are accessible.

**Sharing Link Creation**

* Ensure the item exists before creating sharing links.
* Choose appropriate `type` and `scope` based on your sharing requirements.
* `anonymous` scope allows access without sign-in; `organization` requires organizational account.

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft OneDrive integration setup or troubleshooting.
</Card>

---

## Task to organize contact groups

**URL:** llms-txt#task-to-organize-contact-groups

**Contents:**
  - Comprehensive Contact Management

organization_task = Task(
    description="""
    1. List all existing contact groups
    2. Analyze contact distribution across groups
    3. Create new groups for better organization
    4. Move contacts to appropriate groups based on their information
    """,
    agent=group_organizer,
    expected_output="Contacts organized into logical groups with improved structure"
)

crew = Crew(
    agents=[group_organizer],
    tasks=[organization_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

contact_specialist = Agent(
    role="Contact Management Specialist",
    goal="Provide comprehensive contact management across all sources",
    backstory="An AI assistant that handles all aspects of contact management including personal, directory, and other contacts.",
    apps=['google_contacts']
)

**Examples:**

Example 1 (unknown):
```unknown
### Comprehensive Contact Management
```

---

## Task to organize documents

**URL:** llms-txt#task-to-organize-documents

**Contents:**
- Troubleshooting
  - Common Issues
  - Getting Help

organize_task = Task(
    description="List all documents, check their properties, and identify any documents that might be duplicates or outdated for potential cleanup.",
    agent=document_organizer,
    expected_output="Analysis of document library with recommendations for organization."
)

crew = Crew(
    agents=[document_organizer],
    tasks=[organize_task]
)

**Authentication Errors**

* Ensure your Microsoft account has the necessary permissions for file access (e.g., `Files.Read.All`, `Files.ReadWrite.All`).
* Verify that the OAuth connection includes all required scopes.

**File Creation Issues**

* When creating text documents, ensure the `file_name` ends with `.txt` extension.
* Verify that you have write permissions to the target location (OneDrive/SharePoint).

**Document Access Issues**

* Double-check document IDs for correctness when accessing specific documents.
* Ensure the referenced documents exist and are accessible.
* Note that this integration works best with text files (.txt) for content operations.

**Content Retrieval Limitations**

* The `get_document_content` action works best with text files (.txt).
* For complex Word documents (.docx), consider using the document properties action to get metadata.

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft Word integration setup or troubleshooting.
</Card>

---

## Task to organize email threads

**URL:** llms-txt#task-to-organize-email-threads

**Contents:**
  - Getting Help

thread_task = Task(
    description="""
    1. Fetch all threads from the last month
    2. Apply appropriate labels to organize threads by project
    3. Archive or trash threads that are no longer relevant
    """,
    agent=thread_manager,
    expected_output="Email threads organized with appropriate labels and cleanup completed"
)

crew = Crew(
    agents=[thread_manager],
    tasks=[thread_task]
)

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Gmail integration setup or troubleshooting.
</Card>

---

## Task to prepare and send emails

**URL:** llms-txt#task-to-prepare-and-send-emails

**Contents:**
  - Email Search and Analysis

email_coordination = Task(
    description="Search for emails from the marketing team, create a summary draft, and send it to stakeholders",
    agent=email_coordinator,
    expected_output="Summary email sent to stakeholders"
)

crew = Crew(
    agents=[email_coordinator],
    tasks=[email_coordination]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### Email Search and Analysis
```

---

## Task to schedule a meeting with availability check

**URL:** llms-txt#task-to-schedule-a-meeting-with-availability-check

**Contents:**
  - Event Management and Updates

schedule_meeting = Task(
    description="Check availability for next week and schedule a project review meeting with stakeholders",
    agent=meeting_coordinator,
    expected_output="Meeting scheduled after checking availability of all participants"
)

crew = Crew(
    agents=[meeting_coordinator],
    tasks=[schedule_meeting]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

event_manager = Agent(
    role="Event Manager",
    goal="Manage and update calendar events efficiently",
    backstory="An experienced event manager who handles event logistics and updates.",
    apps=['google_calendar']
)

**Examples:**

Example 1 (unknown):
```unknown
### Event Management and Updates
```

---

## Task to search and manage directory

**URL:** llms-txt#task-to-search-and-manage-directory

**Contents:**
  - Contact Creation and Updates

directory_task = Task(
    description="Search for team members in the company directory and create a team contact list",
    agent=directory_manager,
    expected_output="Team directory compiled with contact information"
)

crew = Crew(
    agents=[directory_manager],
    tasks=[directory_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

contact_curator = Agent(
    role="Contact Curator",
    goal="Create and update contact information systematically",
    backstory="An AI assistant that maintains accurate and up-to-date contact information.",
    apps=['google_contacts']
)

**Examples:**

Example 1 (unknown):
```unknown
### Contact Creation and Updates
```

---

## Task to search and retrieve emails

**URL:** llms-txt#task-to-search-and-retrieve-emails

**Contents:**
  - Calendar and Contact Management

search_emails_task = Task(
    description="Get the latest 20 unread emails and provide a summary of the most important ones.",
    agent=email_manager,
    expected_output="Summary of the most important unread emails with key details."
)

crew = Crew(
    agents=[email_manager],
    tasks=[search_emails_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### Calendar and Contact Management
```

---

## Task to send a message and retrieve recent messages

**URL:** llms-txt#task-to-send-a-message-and-retrieve-recent-messages

**Contents:**
  - Meeting Management

messaging_task = Task(
    description="Send a message 'Hello team! This is an automated update from our AI assistant.' to the General channel of team 'your_team_id', then retrieve the last 10 messages from that channel.",
    agent=messenger,
    expected_output="Message sent successfully and recent messages retrieved."
)

crew = Crew(
    agents=[messenger],
    tasks=[messaging_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### Meeting Management
```

---

## Task to send rich notifications

**URL:** llms-txt#task-to-send-rich-notifications

**Contents:**
  - Message Search and Analytics

notification_task = Task(
    description="""
    1. Send a formatted project completion message to #general with progress charts
    2. Send direct messages to team leads with task summaries
    3. Create interactive notification with action buttons for team feedback
    """,
    agent=notification_agent,
    expected_output="Rich notifications sent with interactive elements and formatted content"
)

crew = Crew(
    agents=[notification_agent],
    tasks=[notification_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### Message Search and Analytics
```

---

## Task to update data based on conditions

**URL:** llms-txt#task-to-update-data-based-on-conditions

**Contents:**
  - Complex Data Management Workflow

update_task = Task(
    description="""
    1. Get spreadsheet properties and structure
    2. Read current data from specific ranges
    3. Update values in target ranges with new data
    4. Append new records to the bottom of the sheet
    """,
    agent=data_updater,
    expected_output="Spreadsheet data updated successfully with new values and records"
)

crew = Crew(
    agents=[data_updater],
    tasks=[update_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

workflow_manager = Agent(
    role="Data Workflow Manager",
    goal="Manage complex data workflows across multiple spreadsheets",
    backstory="An AI assistant that orchestrates complex data operations across multiple spreadsheets.",
    apps=['google_sheets']
)

**Examples:**

Example 1 (unknown):
```unknown
### Complex Data Management Workflow
```

---

## Task to upload and manage a file

**URL:** llms-txt#task-to-upload-and-manage-a-file

**Contents:**
  - File Organization and Sharing

file_management_task = Task(
    description="Upload a text file named 'report.txt' with content 'This is a sample report for the project.' Then get information about the uploaded file.",
    agent=file_operator,
    expected_output="File uploaded successfully and file information retrieved."
)

crew = Crew(
    agents=[file_operator],
    tasks=[file_management_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### File Organization and Sharing
```

---

## Task to upload and share documents

**URL:** llms-txt#task-to-upload-and-share-documents

**Contents:**
  - Advanced File Management

document_task = Task(
    description="Upload the quarterly report and share it with the finance team",
    agent=file_manager_agent,
    expected_output="Document uploaded and sharing permissions configured"
)

crew = Crew(
    agents=[file_manager_agent],
    tasks=[document_task]
)

crew.kickoff()
python  theme={null}
from crewai import Agent, Task, Crew

file_organizer = Agent(
    role="File Organizer",
    goal="Maintain organized file structure and manage permissions",
    backstory="An experienced file manager who ensures proper organization and access control.",
    apps=['google_drive']
)

**Examples:**

Example 1 (unknown):
```unknown
### Advanced File Management
```

---

## Task using schema-based operations

**URL:** llms-txt#task-using-schema-based-operations

**Contents:**
- Troubleshooting
  - Common Issues
  - Getting Help

schema_task = Task(
    description="""
    1. Get all projects and their custom issue types
    2. For each custom issue type, describe the action schema
    3. Create issues using the dynamic schema for complex custom fields
    4. Update issues with custom field values based on business rules
    """,
    agent=schema_specialist,
    expected_output="Custom issues created and updated using dynamic schemas"
)

crew = Crew(
    agents=[schema_specialist],
    tasks=[schema_task]
)

**Permission Errors**

* Ensure your Jira account has necessary permissions for the target projects
* Verify that the OAuth connection includes required scopes for Jira API
* Check if you have create/edit permissions for issues in the specified projects

**Invalid Project or Issue Keys**

* Double-check project keys and issue keys for correct format (e.g., "PROJ-123")
* Ensure projects exist and are accessible to your account
* Verify that issue keys reference existing issues

**Issue Type and Status Issues**

* Use JIRA\_GET\_ISSUE\_TYPES\_BY\_PROJECT to get valid issue types for a project
* Use JIRA\_GET\_ISSUE\_STATUS\_BY\_PROJECT to get valid statuses
* Ensure issue types and statuses are available in the target project

**JQL Query Problems**

* Test JQL queries in Jira's issue search before using in API calls
* Ensure field names in JQL are spelled correctly and exist in your Jira instance
* Use proper JQL syntax for complex queries

**Custom Fields and Schema Issues**

* Use JIRA\_DESCRIBE\_ACTION\_SCHEMA to get the correct schema for complex issue types
* Ensure custom field IDs are correct (e.g., "customfield\_10001")
* Verify that custom fields are available in the target project and issue type

**Filter Formula Issues**

* Ensure filter formulas follow the correct JSON structure for disjunctive normal form
* Use valid field names that exist in your Jira configuration
* Test simple filters before building complex multi-condition queries

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Jira integration setup or troubleshooting.
</Card>

---

## This ensures consistency but may not match your LLM provider preference

**URL:** llms-txt#this-ensures-consistency-but-may-not-match-your-llm-provider-preference

knowledge_source = StringKnowledgeSource(content="Research data...")

crew = Crew(
    agents=[agent],
    tasks=[...],
    knowledge_sources=[knowledge_source]
    # Default: Uses OpenAI embeddings even with Claude LLM
)
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
#### Customizing Knowledge Embedding Providers
```

---

## Tools

**URL:** llms-txt#tools

**Contents:**
- Overview
- What is a Tool?
- Key Characteristics of Tools
- Using CrewAI Tools

Source: https://docs.crewai.com/en/concepts/tools

Understanding and leveraging tools within the CrewAI framework for agent collaboration and task execution.

CrewAI tools empower agents with capabilities ranging from web searching and data analysis to collaboration and delegating tasks among coworkers.
This documentation outlines how to create, integrate, and leverage these tools within the CrewAI framework, including a new focus on collaboration tools.

A tool in CrewAI is a skill or function that agents can utilize to perform various actions.
This includes tools from the [CrewAI Toolkit](https://github.com/joaomdmoura/crewai-tools) and [LangChain Tools](https://python.langchain.com/docs/integrations/tools),
enabling everything from simple searches to complex interactions and effective teamwork among agents.

<Note type="info" title="Enterprise Enhancement: Tools Repository">
  CrewAI AOP provides a comprehensive Tools Repository with pre-built integrations for common business systems and APIs. Deploy agents with enterprise tools in minutes instead of days.

The Enterprise Tools Repository includes:

* Pre-built connectors for popular enterprise systems
  * Custom tool creation interface
  * Version control and sharing capabilities
  * Security and compliance features
</Note>

## Key Characteristics of Tools

* **Utility**: Crafted for tasks such as web searching, data analysis, content generation, and agent collaboration.
* **Integration**: Boosts agent capabilities by seamlessly integrating tools into their workflow.
* **Customizability**: Provides the flexibility to develop custom tools or utilize existing ones, catering to the specific needs of agents.
* **Error Handling**: Incorporates robust error handling mechanisms to ensure smooth operation.
* **Caching Mechanism**: Features intelligent caching to optimize performance and reduce redundant operations.
* **Asynchronous Support**: Handles both synchronous and asynchronous tools, enabling non-blocking operations.

## Using CrewAI Tools

To enhance your agents' capabilities with crewAI tools, begin by installing our extra tools package:

Here's an example demonstrating their use:

```python Code theme={null}
import os
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
Here's an example demonstrating their use:
```

---

## Tool Repository

**URL:** llms-txt#tool-repository

**Contents:**
- Overview
- Prerequisites
- Installing Tools
- Adding other packages after installing a tool
- Creating and Publishing Tools
- Updating Tools
- Deleting Tools
- Security Checks

Source: https://docs.crewai.com/en/enterprise/guides/tool-repository

Using the Tool Repository to manage your tools

The Tool Repository is a package manager for CrewAI tools. It allows users to publish, install, and manage tools that integrate with CrewAI crews and flows.

* **Private**: accessible only within your organization (default)
* **Public**: accessible to all CrewAI users if published with the `--public` flag

The repository is not a version control system. Use Git to track code changes and enable collaboration.

Before using the Tool Repository, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account
* [CrewAI CLI](/en/concepts/cli#cli) installed
* uv>=0.5.0 installed. Check out [how to upgrade](https://docs.astral.sh/uv/getting-started/installation/#upgrading-uv)
* [Git](https://git-scm.com) installed and configured
* Access permissions to publish or install tools in your CrewAI AOP organization

This installs the tool and adds it to `pyproject.toml`.

You can use the tool by importing it and adding it to your agents:

## Adding other packages after installing a tool

After installing a tool from the CrewAI AOP Tool Repository, you need to use the `crewai uv` command to add other packages to your project.
Using pure `uv` commands will fail due to authentication to tool repository being handled by the CLI. By using the `crewai uv` command, you can add other packages to your project without having to worry about authentication.
Any `uv` command can be used with the `crewai uv` command, making it a powerful tool for managing your project's dependencies without the hassle of managing authentication through environment variables or other methods.

Say that you have installed a custom tool from the CrewAI AOP Tool Repository called "my-tool":

And now you want to add another package to your project, you can use the following command:

Other commands like `uv sync` or `uv remove` can also be used with the `crewai uv` command:

This will add the package to your project and update `pyproject.toml` accordingly.

## Creating and Publishing Tools

To create a new tool project:

This generates a scaffolded tool project locally.

After making changes, initialize a Git repository and commit the code:

By default, tools are published as private. To make a tool public:

For more details on how to build tools, see [Creating your own tools](/en/concepts/tools#creating-your-own-tools).

To update a published tool:

1. Modify the tool locally
2. Update the version in `pyproject.toml` (e.g., from `0.1.0` to `0.1.1`)
3. Commit the changes and publish

1. Go to [CrewAI AOP](https://app.crewai.com)
2. Navigate to **Tools**
3. Select the tool
4. Click **Delete**

<Warning>
  Deletion is permanent. Deleted tools cannot be restored or re-installed.
</Warning>

Every published version undergoes automated security checks, and are only available to install after they pass.

You can check the security check status of a tool at:

`CrewAI AOP > Tools > Your Tool > Versions`

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with API integration or troubleshooting.
</Card>

**Examples:**

Example 1 (unknown):
```unknown
This installs the tool and adds it to `pyproject.toml`.

You can use the tool by importing it and adding it to your agents:
```

Example 2 (unknown):
```unknown
## Adding other packages after installing a tool

After installing a tool from the CrewAI AOP Tool Repository, you need to use the `crewai uv` command to add other packages to your project.
Using pure `uv` commands will fail due to authentication to tool repository being handled by the CLI. By using the `crewai uv` command, you can add other packages to your project without having to worry about authentication.
Any `uv` command can be used with the `crewai uv` command, making it a powerful tool for managing your project's dependencies without the hassle of managing authentication through environment variables or other methods.

Say that you have installed a custom tool from the CrewAI AOP Tool Repository called "my-tool":
```

Example 3 (unknown):
```unknown
And now you want to add another package to your project, you can use the following command:
```

Example 4 (unknown):
```unknown
Other commands like `uv sync` or `uv remove` can also be used with the `crewai uv` command:
```

---

## to perform a semantic search for a specified query from a text's content across the internet

**URL:** llms-txt#to-perform-a-semantic-search-for-a-specified-query-from-a-text's-content-across-the-internet

**Contents:**
- Referring to Other Tasks

search_tool = SerperDevTool()

task = Task(
  description='Find and summarize the latest AI news',
  expected_output='A bullet list summary of the top 5 most important AI news',
  agent=research_agent,
  tools=[search_tool]
)

crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
print(result)
python Code theme={null}

**Examples:**

Example 1 (unknown):
```unknown
This demonstrates how tasks with specific tools can override an agent's default set for tailored task execution.

## Referring to Other Tasks

In CrewAI, the output of one task is automatically relayed into the next one, but you can specifically define what tasks' output, including multiple, should be used as context for another task.

This is useful when you have a task that depends on the output of another task that is not performed immediately after it. This is done through the `context` attribute of the task:
```

---

## Traces

**URL:** llms-txt#traces

**Contents:**
- Overview
- What are Traces?
- Accessing Traces
- Understanding the Trace Interface
  - 1. Execution Summary
  - 2. Tasks & Agents
  - 3. Final Output
  - 4. Execution Timeline
  - 5. Detailed Task View
- Using Traces for Debugging

Source: https://docs.crewai.com/en/enterprise/features/traces

Using Traces to monitor your Crews

Traces provide comprehensive visibility into your crew executions, helping you monitor performance, debug issues, and optimize your AI agent workflows.

Traces in CrewAI AOP are detailed execution records that capture every aspect of your crew's operation, from initial inputs to final outputs. They record:

* Agent thoughts and reasoning
* Task execution details
* Tool usage and outputs
* Token consumption metrics
* Execution times
* Cost estimates

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9c02d5b7306bf7adaeadd77a018f8fea" alt="Traces Overview" data-og-width="2244" width="2244" data-og-height="1422" height="1422" data-path="images/enterprise/traces-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e66e7c56a8848b69266563ea8cddfc4e 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f590b3901aaa5994042c79426d78bd6c 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0ecb9dcb307e8f130f53393bd3abc12d 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5fc6fcfc51c4e8f4ce16d237228043d6 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=253eaed4ec34a35798dad42e9a388859 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ec818e09bc20b3f72b1bcf1970804d13 2500w" />
</Frame>

<Steps>
  <Step title="Navigate to the Traces Tab">
    Once in your CrewAI AOP dashboard, click on the **Traces** to view all execution records.
  </Step>

<Step title="Select an Execution">
    You'll see a list of all crew executions, sorted by date. Click on any execution to view its detailed trace.
  </Step>
</Steps>

## Understanding the Trace Interface

The trace interface is divided into several sections, each providing different insights into your crew's execution:

### 1. Execution Summary

The top section displays high-level metrics about the execution:

* **Total Tokens**: Number of tokens consumed across all tasks
* **Prompt Tokens**: Tokens used in prompts to the LLM
* **Completion Tokens**: Tokens generated in LLM responses
* **Requests**: Number of API calls made
* **Execution Time**: Total duration of the crew run
* **Estimated Cost**: Approximate cost based on token usage

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a6a26eda2add26a6f649b1727bf90d8d" alt="Execution Summary" data-og-width="2576" width="2576" data-og-height="916" height="916" data-path="images/enterprise/trace-summary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=52f47a0c5d9f2dc1d0c93d1c2446cb10 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=584cdc9fded1e3875799da73e60cdebd 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2e4f500438545badfa9b3bb3704786ce 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c3e0987a95638f9512ba6c64a5927eda 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d80e2d9de9db7449368151ccaac8106b 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=39ccb1a6b12aecd0f6863f2783b1bfc6 2500w" />
</Frame>

### 2. Tasks & Agents

This section shows all tasks and agents that were part of the crew execution:

* Task name and agent assignment
* Agents and LLMs used for each task
* Status (completed/failed)
* Individual execution time of the task

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f0358b4a17e78532500b4a14964bc30c" alt="Task List" data-og-width="1778" width="1778" data-og-height="594" height="594" data-path="images/enterprise/trace-tasks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a775268b18c71e0ffa497c9a4e1ad179 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3dadaad60870c3841f859857d5d6f53d 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a0a1d24573dd32cb9d5a3f089536c547 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2ccc370f5e0b6b38521a5ed39e02b062 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=4d717a70fd61ce713f7d5d91ccf867fe 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2c577a5f8e1acea3942de29c5ca49343 2500w" />
</Frame>

Displays the final result produced by the crew after all tasks are completed.

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5ca9ef8e4071ee570c3e0c8f93ff4253" alt="Final Output" data-og-width="2212" width="2212" data-og-height="1572" height="1572" data-path="images/enterprise/final-output.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ab97b6b386304f03fe21c6ba2393c683 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3839e312b2a9caa45f3f4b72345ea87b 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b032c2c57ffcd5fb558c43915d385f9a 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=63390d70d70f1a2265a224e8c20d0204 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=abc4a7b81c51049ca606130a0dd543f7 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9fc40fc5f8ad52996aba482d62348f0f 2500w" />
</Frame>

### 4. Execution Timeline

A visual representation of when each task started and ended, helping you identify bottlenecks or parallel execution patterns.

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c860975d3e15e3a6988bedc7d1bf6ba4" alt="Execution Timeline" data-og-width="2210" width="2210" data-og-height="1406" height="1406" data-path="images/enterprise/trace-timeline.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b74d67bda34ce88ea23c30c580dfb2fc 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=99c6688c1d290548cc480232bb13b0e0 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=4876c794ddde894e1e2cf15f1926efcb 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c44f7eec8f0998e488bc951eee8961ea 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c25e4827f5a83172483c38f40e6685de 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b3b2f72954e565f7177b5175d89dfe79 2500w" />
</Frame>

### 5. Detailed Task View

When you click on a specific task in the timeline or task list, you'll see:

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=74f5e92354196325edca8d62c29363c7" alt="Detailed Task View" data-og-width="2036" width="2036" data-og-height="1572" height="1572" data-path="images/enterprise/trace-detailed-task.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d260407501639bcd1a45da51762f488e 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e577e06eb7658f045e56f2e40e03cf94 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=fcafbac3507eb800e08153352016bf14 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9b2b0decb758802aaa2d8b0b2bd39e6f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=66a9362f6d8f2edd5a2dad353700e440 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=faadd7f3c9e9176060e21c2987c3d8c9 2500w" />
</Frame>

* **Task Key**: Unique identifier for the task
* **Task ID**: Technical identifier in the system
* **Status**: Current state (completed/running/failed)
* **Agent**: Which agent performed the task
* **LLM**: Language model used for this task
* **Start/End Time**: When the task began and completed
* **Execution Time**: Duration of this specific task
* **Task Description**: What the agent was instructed to do
* **Expected Output**: What output format was requested
* **Input**: Any input provided to this task from previous tasks
* **Output**: The actual result produced by the agent

## Using Traces for Debugging

Traces are invaluable for troubleshooting issues with your crews:

<Steps>
  <Step title="Identify Failure Points">
    When a crew execution doesn't produce the expected results, examine the trace to find where things went wrong. Look for:

* Failed tasks
    * Unexpected agent decisions
    * Tool usage errors
    * Misinterpreted instructions

<Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c892a75b7a22a57949a2641a0fe45bfa" alt="Failure Points" data-og-width="820" width="820" data-og-height="924" height="924" data-path="images/enterprise/failure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ecbcbd312dd467cb5cc1dae4a443c56d 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c0452a9db1f339e63686941a533d8946 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ded3f2fff055c8d16bcad99ad537da46 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f871feb85f88ba397a259ee8392aef3e 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2acf042b2e6b185f1fbc41100751e03f 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1e9fc9104e6b55b586a9b13e120de908 2500w" />
    </Frame>
  </Step>

<Step title="Optimize Performance">
    Use execution metrics to identify performance bottlenecks:

* Tasks that took longer than expected
    * Excessive token usage
    * Redundant tool operations
    * Unnecessary API calls
  </Step>

<Step title="Improve Cost Efficiency">
    Analyze token usage and cost estimates to optimize your crew's efficiency:

* Consider using smaller models for simpler tasks
    * Refine prompts to be more concise
    * Cache frequently accessed information
    * Structure tasks to minimize redundant operations
  </Step>
</Steps>

## Performance and batching

CrewAI batches trace uploads to reduce overhead on high-volume runs:

* A TraceBatchManager buffers events and sends them in batches via the Plus API client
* Reduces network chatter and improves reliability on flaky connections
* Automatically enabled in the default trace listener; no configuration needed

This yields more stable tracing under load while preserving detailed task/agent telemetry.

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with trace analysis or any other CrewAI AOP features.
</Card>

---

## Training

**URL:** llms-txt#training

**Contents:**
- Overview
  - Training Your Crew Using the CLI
  - Training your Crew programmatically
- How trained data is used by agents
  - Training data flow
  - During training runs
  - After training completes
  - File summary
- Small Language Model Considerations
  - Limitations of Small Models in Training Evaluation

Source: https://docs.crewai.com/en/concepts/training

Learn how to train your CrewAI agents by giving them feedback early on and get consistent results.

The training feature in CrewAI allows you to train your AI agents using the command-line interface (CLI).
By running the command `crewai train -n <n_iterations>`, you can specify the number of iterations for the training process.

During training, CrewAI utilizes techniques to optimize the performance of your agents along with human feedback.
This helps the agents improve their understanding, decision-making, and problem-solving abilities.

### Training Your Crew Using the CLI

To use the training feature, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where your CrewAI project is located.
3. Run the following command:

<Tip>
  Replace `<n_iterations>` with the desired number of training iterations and `<filename>` with the appropriate filename ending with `.pkl`.
</Tip>

<Note>
  If you omit `-f`, the output defaults to `trained_agents_data.pkl` in the current working directory. You can pass an absolute path to control where the file is written.
</Note>

### Training your Crew programmatically

To train your crew programmatically, use the following steps:

1. Define the number of iterations for training.
2. Specify the input parameters for the training process.
3. Execute the training command within a try-except block to handle potential errors.

## How trained data is used by agents

CrewAI uses the training artifacts in two ways: during training to incorporate your human feedback, and after training to guide agents with consolidated suggestions.

### Training data flow

### During training runs

* On each iteration, the system records for every agent:
  * `initial_output`: the agent’s first answer
  * `human_feedback`: your inline feedback when prompted
  * `improved_output`: the agent’s follow-up answer after feedback
* This data is stored in a working file named `training_data.pkl` keyed by the agent’s internal ID and iteration.
* While training is active, the agent automatically appends your prior human feedback to its prompt to enforce those instructions on subsequent attempts within the training session.
  Training is interactive: tasks set `human_input = true`, so running in a non-interactive environment will block on user input.

### After training completes

* When `train(...)` finishes, CrewAI evaluates the collected training data per agent and produces a consolidated result containing:
  * `suggestions`: clear, actionable instructions distilled from your feedback and the difference between initial/improved outputs
  * `quality`: a 0–10 score capturing improvement
  * `final_summary`: a step-by-step set of action items for future tasks
* These consolidated results are saved to the filename you pass to `train(...)` (default via CLI is `trained_agents_data.pkl`). Entries are keyed by the agent’s `role` so they can be applied across sessions.
* During normal (non-training) execution, each agent automatically loads its consolidated `suggestions` and appends them to the task prompt as mandatory instructions. This gives you consistent improvements without changing your agent definitions.

* `training_data.pkl` (ephemeral, per-session):
  * Structure: `agent_id -> { iteration_number: { initial_output, human_feedback, improved_output } }`
  * Purpose: capture raw data and human feedback during training
  * Location: saved in the current working directory (CWD)
* `trained_agents_data.pkl` (or your custom filename):
  * Structure: `agent_role -> { suggestions: string[], quality: number, final_summary: string }`
  * Purpose: persist consolidated guidance for future runs
  * Location: written to the CWD by default; use `-f` to set a custom (including absolute) path

## Small Language Model Considerations

<Warning>
  When using smaller language models (≤7B parameters) for training data evaluation, be aware that they may face challenges with generating structured outputs and following complex instructions.
</Warning>

### Limitations of Small Models in Training Evaluation

<CardGroup cols={2}>
  <Card title="JSON Output Accuracy" icon="triangle-exclamation">
    Smaller models often struggle with producing valid JSON responses needed for structured training evaluations, leading to parsing errors and incomplete data.
  </Card>

<Card title="Evaluation Quality" icon="chart-line">
    Models under 7B parameters may provide less nuanced evaluations with limited reasoning depth compared to larger models.
  </Card>

<Card title="Instruction Following" icon="list-check">
    Complex training evaluation criteria may not be fully followed or considered by smaller models.
  </Card>

<Card title="Consistency" icon="rotate">
    Evaluations across multiple training iterations may lack consistency with smaller models.
  </Card>
</CardGroup>

### Recommendations for Training

<Tabs>
  <Tab title="Best Practice">
    For optimal training quality and reliable evaluations, we strongly recommend using models with at least 7B parameters or larger:

<Tip>
      More powerful models provide higher quality feedback with better reasoning, leading to more effective training iterations.
    </Tip>
  </Tab>

<Tab title="Small Model Usage">
    If you must use smaller models for training evaluation, be aware of these constraints:

<Warning>
      While CrewAI includes optimizations for small models, expect less reliable and less nuanced evaluation results that may require more human intervention during training.
    </Warning>
  </Tab>
</Tabs>

### Key Points to Note

* **Positive Integer Requirement:** Ensure that the number of iterations (`n_iterations`) is a positive integer. The code will raise a `ValueError` if this condition is not met.
* **Filename Requirement:** Ensure that the filename ends with `.pkl`. The code will raise a `ValueError` if this condition is not met.
* **Error Handling:** The code handles subprocess errors and unexpected exceptions, providing error messages to the user.
* Trained guidance is applied at prompt time; it does not modify your Python/YAML agent configuration.
* Agents automatically load trained suggestions from a file named `trained_agents_data.pkl` located in the current working directory. If you trained to a different filename, either rename it to `trained_agents_data.pkl` before running, or adjust the loader in code.
* You can change the output filename when calling `crewai train` with `-f/--filename`. Absolute paths are supported if you want to save outside the CWD.

It is important to note that the training process may take some time, depending on the complexity of your agents and will also require your feedback on each iteration.

Once the training is complete, your agents will be equipped with enhanced capabilities and knowledge, ready to tackle complex tasks and provide more consistent and valuable insights.

Remember to regularly update and retrain your agents to ensure they stay up-to-date with the latest information and advancements in the field.

**Examples:**

Example 1 (unknown):
```unknown
<Tip>
  Replace `<n_iterations>` with the desired number of training iterations and `<filename>` with the appropriate filename ending with `.pkl`.
</Tip>

<Note>
  If you omit `-f`, the output defaults to `trained_agents_data.pkl` in the current working directory. You can pass an absolute path to control where the file is written.
</Note>

### Training your Crew programmatically

To train your crew programmatically, use the following steps:

1. Define the number of iterations for training.
2. Specify the input parameters for the training process.
3. Execute the training command within a try-except block to handle potential errors.
```

Example 2 (unknown):
```unknown
## How trained data is used by agents

CrewAI uses the training artifacts in two ways: during training to incorporate your human feedback, and after training to guide agents with consolidated suggestions.

### Training data flow
```

Example 3 (unknown):
```unknown
### During training runs

* On each iteration, the system records for every agent:
  * `initial_output`: the agent’s first answer
  * `human_feedback`: your inline feedback when prompted
  * `improved_output`: the agent’s follow-up answer after feedback
* This data is stored in a working file named `training_data.pkl` keyed by the agent’s internal ID and iteration.
* While training is active, the agent automatically appends your prior human feedback to its prompt to enforce those instructions on subsequent attempts within the training session.
  Training is interactive: tasks set `human_input = true`, so running in a non-interactive environment will block on user input.

### After training completes

* When `train(...)` finishes, CrewAI evaluates the collected training data per agent and produces a consolidated result containing:
  * `suggestions`: clear, actionable instructions distilled from your feedback and the difference between initial/improved outputs
  * `quality`: a 0–10 score capturing improvement
  * `final_summary`: a step-by-step set of action items for future tasks
* These consolidated results are saved to the filename you pass to `train(...)` (default via CLI is `trained_agents_data.pkl`). Entries are keyed by the agent’s `role` so they can be applied across sessions.
* During normal (non-training) execution, each agent automatically loads its consolidated `suggestions` and appends them to the task prompt as mandatory instructions. This gives you consistent improvements without changing your agent definitions.

### File summary

* `training_data.pkl` (ephemeral, per-session):
  * Structure: `agent_id -> { iteration_number: { initial_output, human_feedback, improved_output } }`
  * Purpose: capture raw data and human feedback during training
  * Location: saved in the current working directory (CWD)
* `trained_agents_data.pkl` (or your custom filename):
  * Structure: `agent_role -> { suggestions: string[], quality: number, final_summary: string }`
  * Purpose: persist consolidated guidance for future runs
  * Location: written to the CWD by default; use `-f` to set a custom (including absolute) path

## Small Language Model Considerations

<Warning>
  When using smaller language models (≤7B parameters) for training data evaluation, be aware that they may face challenges with generating structured outputs and following complex instructions.
</Warning>

### Limitations of Small Models in Training Evaluation

<CardGroup cols={2}>
  <Card title="JSON Output Accuracy" icon="triangle-exclamation">
    Smaller models often struggle with producing valid JSON responses needed for structured training evaluations, leading to parsing errors and incomplete data.
  </Card>

  <Card title="Evaluation Quality" icon="chart-line">
    Models under 7B parameters may provide less nuanced evaluations with limited reasoning depth compared to larger models.
  </Card>

  <Card title="Instruction Following" icon="list-check">
    Complex training evaluation criteria may not be fully followed or considered by smaller models.
  </Card>

  <Card title="Consistency" icon="rotate">
    Evaluations across multiple training iterations may lack consistency with smaller models.
  </Card>
</CardGroup>

### Recommendations for Training

<Tabs>
  <Tab title="Best Practice">
    For optimal training quality and reliable evaluations, we strongly recommend using models with at least 7B parameters or larger:
```

Example 4 (unknown):
```unknown
<Tip>
      More powerful models provide higher quality feedback with better reasoning, leading to more effective training iterations.
    </Tip>
  </Tab>

  <Tab title="Small Model Usage">
    If you must use smaller models for training evaluation, be aware of these constraints:
```

---

## Use custom storage

**URL:** llms-txt#use-custom-storage

**Contents:**
- 🧠 Memory System Comparison
- Supported Embedding Providers
  - OpenAI (Default)
  - Ollama
  - Google AI
  - Azure OpenAI
  - Vertex AI
- Security Best Practices
  - Environment Variables

external_memory = ExternalMemory(storage=CustomStorage())

crew = Crew(
    agents=[...],
    tasks=[...],
    external_memory=external_memory
)
python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",
        "config": {"model": "text-embedding-3-small"}
    }
)
python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "ollama",
        "config": {"model": "mxbai-embed-large"}
    }
)
python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "google-generativeai",
        "config": {
            "api_key": "your-api-key",
            "model_name": "gemini-embedding-001"
        }
    }
)
python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "api_key": "your-api-key",
            "api_base": "https://your-resource.openai.azure.com/",
            "api_version": "2023-05-15",
            "model_name": "text-embedding-3-small"
        }
    }
)
python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "vertexai",
        "config": {
            "project_id": "your-project-id",
            "region": "your-region",
            "api_key": "your-api-key",
            "model_name": "textembedding-gecko"
        }
    }
)
python  theme={null}
import os
from crewai import Crew

**Examples:**

Example 1 (unknown):
```unknown
## 🧠 Memory System Comparison

| **Category**        | **Feature**           | **Basic Memory**       | **External Memory**        |
| ------------------- | --------------------- | ---------------------- | -------------------------- |
| **Ease of Use**     | Setup Complexity      | Simple                 | Moderate                   |
|                     | Integration           | Built-in (contextual)  | Standalone                 |
| **Persistence**     | Storage               | Local files            | Custom / Mem0              |
|                     | Cross-session Support | ✅                      | ✅                          |
| **Personalization** | User-specific Memory  | ❌                      | ✅                          |
|                     | Custom Providers      | Limited                | Any provider               |
| **Use Case Fit**    | Recommended For       | Most general use cases | Specialized / custom needs |

## Supported Embedding Providers

### OpenAI (Default)
```

Example 2 (unknown):
```unknown
### Ollama
```

Example 3 (unknown):
```unknown
### Google AI
```

Example 4 (unknown):
```unknown
### Azure OpenAI
```

---

## Use the custom manager in your crew

**URL:** llms-txt#use-the-custom-manager-in-your-crew

**Contents:**
  - Workflow in Action
- Conclusion

project_crew = Crew(
    tasks=[...],
    agents=[researcher, writer],
    manager_agent=manager,  # Use your custom manager agent
    process=Process.hierarchical,
    planning=True,
)
```

<Tip>
  For more details on creating and customizing a manager agent, check out the [Custom Manager Agent documentation](/en/learn/custom-manager-agent).
</Tip>

### Workflow in Action

1. **Task Assignment**: The manager assigns tasks strategically, considering each agent's capabilities and available tools.
2. **Execution and Review**: Agents complete their tasks with the option for asynchronous execution and callback functions for streamlined workflows.
3. **Sequential Task Progression**: Despite being a hierarchical process, tasks follow a logical order for smooth progression, facilitated by the manager's oversight.

Adopting the hierarchical process in CrewAI, with the correct configurations and understanding of the system's capabilities, facilitates an organized and efficient approach to project management.
Utilize the advanced features and customizations to tailor the workflow to your specific needs, ensuring optimal task execution and project success.

---

## Use this LLM configuration with your agents

**URL:** llms-txt#use-this-llm-configuration-with-your-agents

**Contents:**
  - 3. Prompting in CrewAI
  - 4. Guardrails for Safe Crews

python  theme={null}
    from crewai import Agent, LLM
    from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL, Portkey

# Initialize Portkey admin client
    portkey_admin = Portkey(api_key="YOUR_PORTKEY_API_KEY")

# Retrieve prompt using the render API
    prompt_data = portkey_client.prompts.render(
        prompt_id="YOUR_PROMPT_ID",
        variables={
            "agent_role": "Senior Research Scientist",
        }
    )

backstory_agent_prompt=prompt_data.data.messages[0]["content"]

# Set up LLM with Portkey integration
    portkey_llm = LLM(
        model="gpt-4o",
        base_url=PORTKEY_GATEWAY_URL,
        api_key="dummy",
        extra_headers=createHeaders(
            api_key="YOUR_PORTKEY_API_KEY",
            virtual_key="YOUR_OPENAI_VIRTUAL_KEY"
        )
    )

# Create agent using the rendered prompt
    researcher = Agent(
        role="Senior Research Scientist",
        goal="Discover groundbreaking insights about the assigned topic",
        backstory=backstory_agent,  # Use the rendered prompt
        verbose=True,
        llm=portkey_llm
    )
    python  theme={null}
    # Use a specific prompt version
    prompt_data = portkey_admin.prompts.render(
        prompt_id="YOUR_PROMPT_ID@version_number",
        variables={
            "agent_role": "Senior Research Scientist",
            "agent_goal": "Discover groundbreaking insights"
        }
    )
    
    You are a {{agent_role}} with expertise in {{domain}}.

Your mission is to {{agent_goal}} by leveraging your knowledge
    and experience in the field.

Always maintain a {{tone}} tone and focus on providing {{focus_area}}.
    python  theme={null}
    prompt_data = portkey_admin.prompts.render(
        prompt_id="YOUR_PROMPT_ID",
        variables={
            "agent_role": "Senior Research Scientist",
            "domain": "artificial intelligence",
            "agent_goal": "discover groundbreaking insights",
            "tone": "professional",
            "focus_area": "practical applications"
        }
    )
    python  theme={null}
from crewai import Agent, LLM
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

**Examples:**

Example 1 (unknown):
```unknown
This configuration will automatically try Claude if the GPT-4o request fails, ensuring your crew can continue operating.

<CardGroup cols="2">
  <Card title="Automatic Retries" icon="rotate" href="https://portkey.ai/docs/product/ai-gateway/automatic-retries">
    Handles temporary failures automatically. If an LLM call fails, Portkey will retry the same request for the specified number of times - perfect for rate limits or network blips.
  </Card>

  <Card title="Request Timeouts" icon="clock" href="https://portkey.ai/docs/product/ai-gateway/request-timeouts">
    Prevent your agents from hanging. Set timeouts to ensure you get responses (or can fail gracefully) within your required timeframes.
  </Card>

  <Card title="Conditional Routing" icon="route" href="https://portkey.ai/docs/product/ai-gateway/conditional-routing">
    Send different requests to different providers. Route complex reasoning to GPT-4, creative tasks to Claude, and quick responses to Gemini based on your needs.
  </Card>

  <Card title="Fallbacks" icon="shield" href="https://portkey.ai/docs/product/ai-gateway/fallbacks">
    Keep running even if your primary provider fails. Automatically switch to backup providers to maintain availability.
  </Card>

  <Card title="Load Balancing" icon="scale-balanced" href="https://portkey.ai/docs/product/ai-gateway/load-balancing">
    Spread requests across multiple API keys or providers. Great for high-volume crew operations and staying within rate limits.
  </Card>
</CardGroup>

### 3. Prompting in CrewAI

Portkey's Prompt Engineering Studio helps you create, manage, and optimize the prompts used in your CrewAI agents. Instead of hardcoding prompts or instructions, use Portkey's prompt rendering API to dynamically fetch and apply your versioned prompts.

<Frame caption="Manage prompts in Portkey's Prompt Library">
  ![Prompt Playground Interface](https://raw.githubusercontent.com/siddharthsambharia-portkey/Portkey-Product-Images/refs/heads/main/CrewAI%20Portkey%20Docs.webp)
</Frame>

<Tabs>
  <Tab title="Prompt Playground">
    Prompt Playground is a place to compare, test and deploy perfect prompts for your AI application. It's where you experiment with different models, test variables, compare outputs, and refine your prompt engineering strategy before deploying to production. It allows you to:

    1. Iteratively develop prompts before using them in your agents
    2. Test prompts with different variables and models
    3. Compare outputs between different prompt versions
    4. Collaborate with team members on prompt development

    This visual environment makes it easier to craft effective prompts for each step in your CrewAI agents' workflow.
  </Tab>

  <Tab title="Using Prompt Templates">
    The Prompt Render API retrieves your prompt templates with all parameters configured:
```

Example 2 (unknown):
```unknown
</Tab>

  <Tab title="Prompt Versioning">
    You can:

    * Create multiple versions of the same prompt
    * Compare performance between versions
    * Roll back to previous versions if needed
    * Specify which version to use in your code:
```

Example 3 (unknown):
```unknown
</Tab>

  <Tab title="Mustache Templating for variables">
    Portkey prompts use Mustache-style templating for easy variable substitution:
```

Example 4 (unknown):
```unknown
When rendering, simply pass the variables:
```

---

## Using Annotations in crew.py

**URL:** llms-txt#using-annotations-in-crew.py

**Contents:**
- Introduction
- Available Annotations
- Usage Examples
  - 1. Crew Base Class
  - 2. Tool Definition
  - 3. LLM Definition
  - 4. Agent Definition
  - 5. Task Definition
  - 6. Crew Creation
- YAML Configuration

Source: https://docs.crewai.com/en/learn/using-annotations

Learn how to use annotations to properly structure agents, tasks, and components in CrewAI

This guide explains how to use annotations to properly reference **agents**, **tasks**, and other components in the `crew.py` file.

Annotations in the CrewAI framework are used to decorate classes and methods, providing metadata and functionality to various components of your crew. These annotations help in organizing and structuring your code, making it more readable and maintainable.

## Available Annotations

The CrewAI framework provides the following annotations:

* `@CrewBase`: Used to decorate the main crew class.
* `@agent`: Decorates methods that define and return Agent objects.
* `@task`: Decorates methods that define and return Task objects.
* `@crew`: Decorates the method that creates and returns the Crew object.
* `@llm`: Decorates methods that initialize and return Language Model objects.
* `@tool`: Decorates methods that initialize and return Tool objects.
* `@callback`: Used for defining callback methods.
* `@output_json`: Used for methods that output JSON data.
* `@output_pydantic`: Used for methods that output Pydantic models.
* `@cache_handler`: Used for defining cache handling methods.

Let's go through examples of how to use these annotations:

### 1. Crew Base Class

The `@CrewBase` annotation is used to decorate the main crew class. This class typically contains configurations and methods for creating agents, tasks, and the crew itself.

<Tip>
  `@CrewBase` does more than register the class:

* **Configuration bootstrapping:** looks for `agents_config` and `tasks_config` (defaulting to `config/agents.yaml` and `config/tasks.yaml`) beside the class file, loads them at instantiation, and safely falls back to empty dicts if files are missing.
  * **Decorator orchestration:** keeps memoized references to every method marked with `@agent`, `@task`, `@before_kickoff`, or `@after_kickoff` so they are instantiated once per crew and executed in declaration order.
  * **Hook wiring:** automatically attaches the preserved kickoff hooks to the `Crew` object returned by the `@crew` method, making them run before and after `.kickoff()`.
  * **MCP integration:** when the class defines `mcp_server_params`, `get_mcp_tools()` lazily starts an MCP server adapter, hydrates the declared tools, and an internal after-kickoff hook stops the adapter. See [MCP overview](/en/mcp/overview) for adapter configuration details.
</Tip>

### 2. Tool Definition

The `@tool` annotation is used to decorate methods that return tool objects. These tools can be used by agents to perform specific tasks.

### 3. LLM Definition

The `@llm` annotation is used to decorate methods that initialize and return Language Model objects. These LLMs are used by agents for natural language processing tasks.

### 4. Agent Definition

The `@agent` annotation is used to decorate methods that define and return Agent objects.

### 5. Task Definition

The `@task` annotation is used to decorate methods that define and return Task objects. These methods specify the task configuration and the agent responsible for the task.

The `@crew` annotation is used to decorate the method that creates and returns the `Crew` object. This method assembles all the components (agents and tasks) into a functional crew.

## YAML Configuration

The agent configurations are typically stored in a YAML file. Here's an example of how the `agents.yaml` file might look for the researcher agent:

This YAML configuration corresponds to the researcher agent defined in the `LinkedinProfileCrew` class. The configuration specifies the agent's role, goal, backstory, and other properties such as the LLM and tools it uses.

Note how the `llm` and `tools` in the YAML file correspond to the methods decorated with `@llm` and `@tool` in the Python class.

* **Consistent Naming**: Use clear and consistent naming conventions for your methods. For example, agent methods could be named after their roles (e.g., researcher, reporting\_analyst).
* **Environment Variables**: Use environment variables for sensitive information like API keys.
* **Flexibility**: Design your crew to be flexible by allowing easy addition or removal of agents and tasks.
* **YAML-Code Correspondence**: Ensure that the names and structures in your YAML files correspond correctly to the decorated methods in your Python code.

By following these guidelines and properly using annotations, you can create well-structured and maintainable crews using the CrewAI framework.

**Examples:**

Example 1 (unknown):
```unknown
The `@CrewBase` annotation is used to decorate the main crew class. This class typically contains configurations and methods for creating agents, tasks, and the crew itself.

<Tip>
  `@CrewBase` does more than register the class:

  * **Configuration bootstrapping:** looks for `agents_config` and `tasks_config` (defaulting to `config/agents.yaml` and `config/tasks.yaml`) beside the class file, loads them at instantiation, and safely falls back to empty dicts if files are missing.
  * **Decorator orchestration:** keeps memoized references to every method marked with `@agent`, `@task`, `@before_kickoff`, or `@after_kickoff` so they are instantiated once per crew and executed in declaration order.
  * **Hook wiring:** automatically attaches the preserved kickoff hooks to the `Crew` object returned by the `@crew` method, making them run before and after `.kickoff()`.
  * **MCP integration:** when the class defines `mcp_server_params`, `get_mcp_tools()` lazily starts an MCP server adapter, hydrates the declared tools, and an internal after-kickoff hook stops the adapter. See [MCP overview](/en/mcp/overview) for adapter configuration details.
</Tip>

### 2. Tool Definition
```

Example 2 (unknown):
```unknown
The `@tool` annotation is used to decorate methods that return tool objects. These tools can be used by agents to perform specific tasks.

### 3. LLM Definition
```

Example 3 (unknown):
```unknown
The `@llm` annotation is used to decorate methods that initialize and return Language Model objects. These LLMs are used by agents for natural language processing tasks.

### 4. Agent Definition
```

Example 4 (unknown):
```unknown
The `@agent` annotation is used to decorate methods that define and return Agent objects.

### 5. Task Definition
```

---

## Using Multimodal Agents

**URL:** llms-txt#using-multimodal-agents

**Contents:**
- Using Multimodal Agents
  - Enabling Multimodal Capabilities
  - Working with Images

Source: https://docs.crewai.com/en/learn/multimodal-agents

Learn how to enable and use multimodal capabilities in your agents for processing images and other non-text content within the CrewAI framework.

## Using Multimodal Agents

CrewAI supports multimodal agents that can process both text and non-text content like images. This guide will show you how to enable and use multimodal capabilities in your agents.

### Enabling Multimodal Capabilities

To create a multimodal agent, simply set the `multimodal` parameter to `True` when initializing your agent:

When you set `multimodal=True`, the agent is automatically configured with the necessary tools for handling non-text content, including the `AddImageTool`.

### Working with Images

The multimodal agent comes pre-configured with the `AddImageTool`, which allows it to process images. You don't need to manually add this tool - it's automatically included when you enable multimodal capabilities.

Here's a complete example showing how to use a multimodal agent to analyze an image:

```python  theme={null}
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
When you set `multimodal=True`, the agent is automatically configured with the necessary tools for handling non-text content, including the `AddImageTool`.

### Working with Images

The multimodal agent comes pre-configured with the `AddImageTool`, which allows it to process images. You don't need to manually add this tool - it's automatically included when you enable multimodal capabilities.

Here's a complete example showing how to use a multimodal agent to analyze an image:
```

---

## Webhook Streaming

**URL:** llms-txt#webhook-streaming

**Contents:**
- Overview
- Usage
- Webhook Format
- Supported Events
  - Flow Events:
  - Agent Events:
  - Crew Events:
  - Task Events:
  - Tool Usage Events:
  - LLM Events:

Source: https://docs.crewai.com/en/enterprise/features/webhook-streaming

Using Webhook Streaming to stream events to your webhook

Enterprise Event Streaming lets you receive real-time webhook updates about your crews and flows deployed to
CrewAI AOP, such as model calls, tool usage, and flow steps.

When using the Kickoff API, include a `webhooks` object to your request, for example:

If `realtime` is set to `true`, each event is delivered individually and immediately, at the cost of crew/flow performance.

Each webhook sends a list of events:

The `data` object structure varies by event type. Refer to the [event list](https://github.com/crewAIInc/crewAI/tree/main/src/crewai/utilities/events) on GitHub.

As requests are sent over HTTP, the order of events can't be guaranteed. If you need ordering, use the `timestamp` field.

CrewAI supports both system events and custom events in Enterprise Event Streaming. These events are sent to your configured webhook endpoint during crew and flow execution.

* `flow_created`
* `flow_started`
* `flow_finished`
* `flow_plot`
* `method_execution_started`
* `method_execution_finished`
* `method_execution_failed`

* `agent_execution_started`
* `agent_execution_completed`
* `agent_execution_error`
* `lite_agent_execution_started`
* `lite_agent_execution_completed`
* `lite_agent_execution_error`
* `agent_logs_started`
* `agent_logs_execution`
* `agent_evaluation_started`
* `agent_evaluation_completed`
* `agent_evaluation_failed`

* `crew_kickoff_started`
* `crew_kickoff_completed`
* `crew_kickoff_failed`
* `crew_train_started`
* `crew_train_completed`
* `crew_train_failed`
* `crew_test_started`
* `crew_test_completed`
* `crew_test_failed`
* `crew_test_result`

* `task_started`
* `task_completed`
* `task_failed`
* `task_evaluation`

### Tool Usage Events:

* `tool_usage_started`
* `tool_usage_finished`
* `tool_usage_error`
* `tool_validate_input_error`
* `tool_selection_error`
* `tool_execution_error`

* `llm_call_started`
* `llm_call_completed`
* `llm_call_failed`
* `llm_stream_chunk`

### LLM Guardrail Events:

* `llm_guardrail_started`
* `llm_guardrail_completed`

* `memory_query_started`
* `memory_query_completed`
* `memory_query_failed`
* `memory_save_started`
* `memory_save_completed`
* `memory_save_failed`
* `memory_retrieval_started`
* `memory_retrieval_completed`

### Knowledge Events:

* `knowledge_search_query_started`
* `knowledge_search_query_completed`
* `knowledge_search_query_failed`
* `knowledge_query_started`
* `knowledge_query_completed`
* `knowledge_query_failed`

### Reasoning Events:

* `agent_reasoning_started`
* `agent_reasoning_completed`
* `agent_reasoning_failed`

Event names match the internal event bus. See GitHub for the full list of events.

You can emit your own custom events, and they will be delivered through the webhook stream alongside system events.

<CardGroup>
  <Card title="GitHub" icon="github" href="https://github.com/crewAIInc/crewAI/tree/main/src/crewai/utilities/events">
    Full list of events
  </Card>

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
    Contact our support team for assistance with webhook integration or troubleshooting.
  </Card>
</CardGroup>

**Examples:**

Example 1 (unknown):
```unknown
If `realtime` is set to `true`, each event is delivered individually and immediately, at the cost of crew/flow performance.

## Webhook Format

Each webhook sends a list of events:
```

---

## What is CrewAI?

**URL:** llms-txt#what-is-crewai?

**Contents:**
- How Crews Work
  - How It All Works Together
- Key Features
- How Flows Work
  - Key Capabilities
- When to Use Crews vs. Flows
  - Decision Framework
- Why Choose CrewAI?
- Ready to Start Building?

**CrewAI is a lean, lightning-fast Python framework built entirely from scratch—completely independent of LangChain or other agent frameworks.**

CrewAI empowers developers with both high-level simplicity and precise low-level control, ideal for creating autonomous AI agents tailored to any scenario:

* **[CrewAI Crews](/en/guides/crews/first-crew)**: Optimize for autonomy and collaborative intelligence, enabling you to create AI teams where each agent has specific roles, tools, and goals.
* **[CrewAI Flows](/en/guides/flows/first-flow)**: Enable granular, event-driven control, single LLM calls for precise task orchestration and supports Crews natively.

With over 100,000 developers certified through our community courses, CrewAI is rapidly becoming the standard for enterprise-ready AI automation.

<Note>
  Just like a company has departments (Sales, Engineering, Marketing) working together under leadership to achieve business goals, CrewAI helps you create an organization of AI agents with specialized roles collaborating to accomplish complex tasks.
</Note>

<Frame caption="CrewAI Framework Overview">
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=514fd0b06e4128e62f10728d44601975" alt="CrewAI Framework Overview" data-og-width="634" width="634" data-og-height="473" height="473" data-path="images/crews.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=279c5c26c77fc9acc8411677716fa5ee 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=92b76be34b84b36771e0a8eed8976966 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3ef573e6215967af1bb2975a58d0d859 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1af6e6a337b70ca2ce238d8e40f49218 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c5da01705f1373446f8582ac582ff244 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=96464aab7bb5efe4213a7b80f58038aa 2500w" />
</Frame>

| Component     |         Description        | Key Features                                                                                                                      |
| :------------ | :------------------------: | :-------------------------------------------------------------------------------------------------------------------------------- |
| **Crew**      | The top-level organization | • Manages AI agent teams<br />• Oversees workflows<br />• Ensures collaboration<br />• Delivers outcomes                          |
| **AI Agents** |  Specialized team members  | • Have specific roles (researcher, writer)<br />• Use designated tools<br />• Can delegate tasks<br />• Make autonomous decisions |
| **Process**   | Workflow management system | • Defines collaboration patterns<br />• Controls task assignments<br />• Manages interactions<br />• Ensures efficient execution  |
| **Tasks**     |   Individual assignments   | • Have clear objectives<br />• Use specific tools<br />• Feed into larger process<br />• Produce actionable results               |

### How It All Works Together

1. The **Crew** organizes the overall operation
2. **AI Agents** work on their specialized tasks
3. The **Process** ensures smooth collaboration
4. **Tasks** get completed to achieve the goal

<CardGroup cols={2}>
  <Card title="Role-Based Agents" icon="users">
    Create specialized agents with defined roles, expertise, and goals - from researchers to analysts to writers
  </Card>

<Card title="Flexible Tools" icon="screwdriver-wrench">
    Equip agents with custom tools and APIs to interact with external services and data sources
  </Card>

<Card title="Intelligent Collaboration" icon="people-arrows">
    Agents work together, sharing insights and coordinating tasks to achieve complex objectives
  </Card>

<Card title="Task Management" icon="list-check">
    Define sequential or parallel workflows, with agents automatically handling task dependencies
  </Card>
</CardGroup>

<Note>
  While Crews excel at autonomous collaboration, Flows provide structured automations, offering granular control over workflow execution. Flows ensure tasks are executed reliably, securely, and efficiently, handling conditional logic, loops, and dynamic state management with precision. Flows integrate seamlessly with Crews, enabling you to balance high autonomy with exacting control.
</Note>

<Frame caption="CrewAI Framework Overview">
  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=82ea168de2f004553dcea21410cd7d8a" alt="CrewAI Framework Overview" data-og-width="669" width="669" data-og-height="464" height="464" data-path="images/flows.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=4a6177acae3789dd8e4467b791c8966e 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=7900e4cdad93fd37bbcd2f1f2f38b40b 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a83fa78165e93bc1d988a30ebc33889a 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=540eb3d8d8f256d6d703aa5e6111a4cd 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=04fbb8e23728b87efa78a0a776e2d194 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=ff06d73f5d4aa911154c66becf14d732 2500w" />
</Frame>

| Component        |            Description            | Key Features                                                                                                                                                         |
| :--------------- | :-------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Flow**         | Structured workflow orchestration | • Manages execution paths<br />• Handles state transitions<br />• Controls task sequencing<br />• Ensures reliable execution                                         |
| **Events**       |   Triggers for workflow actions   | • Initiate specific processes<br />• Enable dynamic responses<br />• Support conditional branching<br />• Allow for real-time adaptation                             |
| **States**       |    Workflow execution contexts    | • Maintain execution data<br />• Enable persistence<br />• Support resumability<br />• Ensure execution integrity                                                    |
| **Crew Support** |    Enhances workflow automation   | • Injects pockets of agency when needed<br />• Complements structured workflows<br />• Balances automation with intelligence<br />• Enables adaptive decision-making |

<CardGroup cols={2}>
  <Card title="Event-Driven Orchestration" icon="bolt">
    Define precise execution paths responding dynamically to events
  </Card>

<Card title="Fine-Grained Control" icon="sliders">
    Manage workflow states and conditional execution securely and efficiently
  </Card>

<Card title="Native Crew Integration" icon="puzzle-piece">
    Effortlessly combine with Crews for enhanced autonomy and intelligence
  </Card>

<Card title="Deterministic Execution" icon="route">
    Ensure predictable outcomes with explicit control flow and error handling
  </Card>
</CardGroup>

## When to Use Crews vs. Flows

<Note>
  Understanding when to use [Crews](/en/guides/crews/first-crew) versus [Flows](/en/guides/flows/first-flow) is key to maximizing the potential of CrewAI in your applications.
</Note>

| Use Case                | Recommended Approach                 | Why?                                                                                                                                        |
| :---------------------- | :----------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| **Open-ended research** | [Crews](/en/guides/crews/first-crew) | When tasks require creative thinking, exploration, and adaptation                                                                           |
| **Content generation**  | [Crews](/en/guides/crews/first-crew) | For collaborative creation of articles, reports, or marketing materials                                                                     |
| **Decision workflows**  | [Flows](/en/guides/flows/first-flow) | When you need predictable, auditable decision paths with precise control                                                                    |
| **API orchestration**   | [Flows](/en/guides/flows/first-flow) | For reliable integration with multiple external services in a specific sequence                                                             |
| **Hybrid applications** | Combined approach                    | Use [Flows](/en/guides/flows/first-flow) to orchestrate overall process with [Crews](/en/guides/crews/first-crew) handling complex subtasks |

### Decision Framework

* **Choose [Crews](/en/guides/crews/first-crew) when:** You need autonomous problem-solving, creative collaboration, or exploratory tasks
* **Choose [Flows](/en/guides/flows/first-flow) when:** You require deterministic outcomes, auditability, or precise control over execution
* **Combine both when:** Your application needs both structured processes and pockets of autonomous intelligence

## Why Choose CrewAI?

* 🧠 **Autonomous Operation**: Agents make intelligent decisions based on their roles and available tools
* 📝 **Natural Interaction**: Agents communicate and collaborate like human team members
* 🛠️ **Extensible Design**: Easy to add new tools, roles, and capabilities
* 🚀 **Production Ready**: Built for reliability and scalability in real-world applications
* 🔒 **Security-Focused**: Designed with enterprise security requirements in mind
* 💰 **Cost-Efficient**: Optimized to minimize token usage and API calls

## Ready to Start Building?

<CardGroup cols={2}>
  <Card title="Build Your First Crew" icon="users-gear" href="/en/guides/crews/first-crew">
    Step-by-step tutorial to create a collaborative AI team that works together to solve complex problems.
  </Card>

<Card title="Build Your First Flow" icon="diagram-project" href="/en/guides/flows/first-flow">
    Learn how to create structured, event-driven workflows with precise control over execution.
  </Card>
</CardGroup>

<CardGroup cols={3}>
  <Card title="Install CrewAI" icon="wrench" href="/en/installation">
    Get started with CrewAI in your development environment.
  </Card>

<Card title="Quick Start" icon="bolt" href="en/quickstart">
    Follow our quickstart guide to create your first CrewAI agent and get hands-on experience.
  </Card>

<Card title="Join the Community" icon="comments" href="https://community.crewai.com">
    Connect with other developers, get help, and share your CrewAI experiences.
  </Card>
</CardGroup>

---

## Write content to a file in a specified directory

**URL:** llms-txt#write-content-to-a-file-in-a-specified-directory

**Contents:**
- Arguments
- Conclusion

result = file_writer_tool._run('example.txt', 'This is a test content.', 'test_directory')
print(result)
```

* `filename`: The name of the file you want to create or overwrite.
* `content`: The content to write into the file.
* `directory` (optional): The path to the directory where the file will be created. Defaults to the current directory (`.`). If the directory does not exist, it will be created.

By integrating the `FileWriterTool` into your crews, the agents can reliably write content to files across different operating systems.
This tool is essential for tasks that require saving output data, creating structured file systems, and handling cross-platform file operations.
It's particularly recommended for Windows users who may encounter file writing issues with standard Python file operations.

By adhering to the setup and usage guidelines provided, incorporating this tool into projects is straightforward and ensures consistent file writing behavior across all platforms.

---

## Zapier Trigger

**URL:** llms-txt#zapier-trigger

**Contents:**
- Prerequisites
- Step-by-Step Setup
- Tips for Success

Source: https://docs.crewai.com/en/enterprise/guides/zapier-trigger

Trigger CrewAI crews from Zapier workflows to automate cross-app workflows

This guide will walk you through the process of setting up Zapier triggers for CrewAI AOP, allowing you to automate workflows between CrewAI AOP and other applications.

* A CrewAI AOP account
* A Zapier account
* A Slack account (for this specific example)

## Step-by-Step Setup

<Steps>
  <Step title="Set Up the Slack Trigger">
    * In Zapier, create a new Zap.

<Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d7602ce90ddcd4f0365fd821f4ff1ff2" alt="Zapier 1" data-og-width="621" width="621" data-og-height="463" height="463" data-path="images/enterprise/zapier-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3682030aedc56484321e678fe075bd97 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=cf755fd940ed2e79378b91369e620cd9 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e2fc3de247c9054220b0255a1544b160 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6f10592fc96a7ea63bbd8548328c8cea 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ab8d3cce86244b055400ad4ecf60d51d 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=37b9df91c5efb53fd1d6c9a7fc34c624 2500w" />
    </Frame>
  </Step>

<Step title="Choose Slack as your trigger app">
    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e5cdc5705b87b4e06178fa12fb5ef64b" alt="Zapier 2" data-og-width="670" width="670" data-og-height="684" height="684" data-path="images/enterprise/zapier-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f5d12f107504be7a7521ddf91d9ec413 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bebe1ccb4e8d4b4d077d4039b5a8c419 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=edb0a91b6ed81fc58470f998b3329978 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=262296a5be2e6762da49b77fcd9bd5e2 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=40b91cfb93939c2dd0b3f6222b376f90 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=18bd414e6d18ec375cf94d94d2510775 2500w" />
    </Frame>

* Select `New Pushed Message` as the Trigger Event.
    * Connect your Slack account if you haven't already.
  </Step>

<Step title="Configure the CrewAI AOP Action">
    * Add a new action step to your Zap.
    * Choose CrewAI+ as your action app and Kickoff as the Action Event

<Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e52e2404a73623df30d125873bd8ff42" alt="Zapier 5" data-og-width="670" width="670" data-og-height="670" height="670" data-path="images/enterprise/zapier-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=786eec1ccf1fa275c710cd3f35d7c955 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bffb3ef5cd02ccd103a070893842ce2a 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=20c3a2004d6186a7217d6492f093dde5 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3563e2fede93f6c678e6e25269a4781f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1641552fd6d8e6b477875ab53bd6f401 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6c227ade8128df087cd958a98a398605 2500w" />
    </Frame>
  </Step>

<Step title="Connect your CrewAI AOP account">
    * Connect your CrewAI AOP account.
    * Select the appropriate Crew for your workflow.

<Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=13aac37fdb67ee1c9f841a602ac3abf5" alt="Zapier 6" data-og-width="670" width="670" data-og-height="657" height="657" data-path="images/enterprise/zapier-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ad12e0febda29f3e6b68a245b83f17bd 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=08ff0773ed36f8fbb1c33acd90a50f79 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=cf788ee6daea3ef786b456c7a80d79a5 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b5a14e7f332b6ebef8131f6a26835417 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f0b27340ce1a510f990a305674d53107 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=061132e0ca03b82737f62cd4a113b12c 2500w" />
    </Frame>

* Configure the inputs for the Crew using the data from the Slack message.
  </Step>

<Step title="Format the CrewAI AOP Output">
    * Add another action step to format the text output from CrewAI AOP.
    * Use Zapier's formatting tools to convert the Markdown output to HTML.

<Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e772b4803dfffe4de12d9a7ea21484ce" alt="Zapier 8" data-og-width="670" width="670" data-og-height="674" height="674" data-path="images/enterprise/zapier-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d3de75f0a0d65af30620c7d9b89a1802 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=42ec43489c3e07aea4f64790efad63ef 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=68f473bd4c78acb0422d724a8dc9ac27 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d3149ba4fc03d00e00f81e6774dd4253 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ea05c3790b67091e18e32291c2ecceae 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a7519c4547a79061828c08d71091ac18 2500w" />
    </Frame>

<Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9fa4a34d5c511b6bb76f276348928699" alt="Zapier 9" data-og-width="670" width="670" data-og-height="675" height="675" data-path="images/enterprise/zapier-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=722c246b4c43b099734105a8c57e094c 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=91bfde61dfceb3998b85a0fd947b8f1b 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d56af89fb61384149deef33e22b57bfe 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d9097a2e0d8ddf13f0d17c7f65d4a263 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=59e5ad6b6f94117c4bdb264cde97a5ff 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=edf53161c63e0daf6e3e61abf1b1a265 2500w" />
    </Frame>
  </Step>

<Step title="Send the Output via Email">
    * Add a final action step to send the formatted output via email.
    * Choose your preferred email service (e.g., Gmail, Outlook).
    * Configure the email details, including recipient, subject, and body.
    * Insert the formatted CrewAI AOP output into the email body.

<Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f3d2a0c67b29888cfdc5b0d81ba5c29b" alt="Zapier 7" data-og-width="670" width="670" data-og-height="673" height="673" data-path="images/enterprise/zapier-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=399cf0c5f81cbf170a3c8d4d8557b37f 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8b6c488f27b8797c575a711f9b257b81 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f905970cb40554fe1c3674afa7f2209e 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=92ee968916226d374826eb358c264f66 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1853357f43dd7032c890fd3a57fbd99e 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9c5e507725c754d90937f0b7b1ee7699 2500w" />
    </Frame>
  </Step>

<Step title="Kick Off the crew from Slack">
    * Enter the text in your Slack channel

<Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=916dbdffd171dc52c40ebc74cc39a38f" alt="Zapier 10" data-og-width="509" width="509" data-og-height="85" height="85" data-path="images/enterprise/zapier-7b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=fce126149004d422a866d0e9ae00b9b0 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c051b11bd9e2fd2db9a0fbd0997043cd 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2f14112b9c9551239a1b82bd220b85fa 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f302f0da373ef859e49ca1b4a7540b94 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=386dfa4b1f1f4005e705771b39c1ec33 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=57c6a7727031de0aebbdbeb65a03e27c 2500w" />
    </Frame>

* Select the 3 ellipsis button and then chose Push to Zapier

<Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a6a6e2fd0b0b239af4c17ae1f34ad720" alt="Zapier 11" data-og-width="405" width="405" data-og-height="260" height="260" data-path="images/enterprise/zapier-8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e9bb5078ea66e8e7774b262caea53295 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ec7f588235922fd96b8aea884cba1221 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d82c4c5d979814febba30bbfdeb2831d 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7a8f97770f17f96b4585c1b38b000fb8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e8bae8057f2a294c977f7d568660f915 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=301cbedee7d42601db44f3710755653c 2500w" />
    </Frame>
  </Step>

<Step title="Select the crew and then Push to Kick Off">
    <Frame>
      <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=eda865381d7121d38025c2b13abeccdf" alt="Zapier 12" data-og-width="659" width="659" data-og-height="531" height="531" data-path="images/enterprise/zapier-9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=283165c2ef289340b66aa9ed1719f97d 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=d28641bc16596826f13a9d14ac0a2f2b 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=e68731bab42671ec59dfd179c210bd80 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=234f5bffd3865f2a15d744455fef0c90 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=d59b16a7bfbdf3b07d696ef70be0a31a 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=1669d1af7e28868e5f260df18b36dd49 2500w" />
    </Frame>
  </Step>
</Steps>

* Ensure that your CrewAI AOP inputs are correctly mapped from the Slack message.
* Test your Zap thoroughly before turning it on to catch any potential issues.
* Consider adding error handling steps to manage potential failures in the workflow.

By following these steps, you'll have successfully set up Zapier triggers for CrewAI AOP, allowing for automated workflows triggered by Slack messages and resulting in email notifications with CrewAI AOP output.

---

## Zendesk Integration

**URL:** llms-txt#zendesk-integration

**Contents:**
- Overview
- Prerequisites
- Setting Up Zendesk Integration
  - 1. Connect Your Zendesk Account
  - 2. Install Required Package
  - 3. Environment Variable Setup
- Available Tools
  - **Ticket Management**
  - **User Management**
  - **Administrative Tools**

Source: https://docs.crewai.com/en/enterprise/integrations/zendesk

Customer support and helpdesk management with Zendesk integration for CrewAI.

Enable your agents to manage customer support operations through Zendesk. Create and update tickets, manage users, track support metrics, and streamline your customer service workflows with AI-powered automation.

Before using the Zendesk integration, ensure you have:

* A [CrewAI AOP](https://app.crewai.com) account with an active subscription
* A Zendesk account with appropriate API permissions
* Connected your Zendesk account through the [Integrations page](https://app.crewai.com/integrations)

## Setting Up Zendesk Integration

### 1. Connect Your Zendesk Account

1. Navigate to [CrewAI AOP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Zendesk** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for ticket and user management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

Or add it to your `.env` file:

### **Ticket Management**

<AccordionGroup>
  <Accordion title="zendesk/create_ticket">
    **Description:** Create a new support ticket in Zendesk.

* `ticketSubject` (string, required): Ticket subject line (e.g., "Help, my printer is on fire!")
    * `ticketDescription` (string, required): First comment that appears on the ticket (e.g., "The smoke is very colorful.")
    * `requesterName` (string, required): Name of the user requesting support (e.g., "Jane Customer")
    * `requesterEmail` (string, required): Email of the user requesting support (e.g., "[jane@example.com](mailto:jane@example.com)")
    * `assigneeId` (string, optional): Zendesk Agent ID assigned to this ticket - Use Connect Portal Workflow Settings to allow users to select an assignee
    * `ticketType` (string, optional): Ticket type - Options: problem, incident, question, task
    * `ticketPriority` (string, optional): Priority level - Options: urgent, high, normal, low
    * `ticketStatus` (string, optional): Ticket status - Options: new, open, pending, hold, solved, closed
    * `ticketDueAt` (string, optional): Due date for task-type tickets (ISO 8601 timestamp)
    * `ticketTags` (string, optional): Array of tags to apply (e.g., `["enterprise", "other_tag"]`)
    * `ticketExternalId` (string, optional): External ID to link tickets to local records
    * `ticketCustomFields` (object, optional): Custom field values in JSON format
  </Accordion>

<Accordion title="zendesk/update_ticket">
    **Description:** Update an existing support ticket in Zendesk.

* `ticketId` (string, required): ID of the ticket to update (e.g., "35436")
    * `ticketSubject` (string, optional): Updated ticket subject
    * `requesterName` (string, required): Name of the user who requested this ticket
    * `requesterEmail` (string, required): Email of the user who requested this ticket
    * `assigneeId` (string, optional): Updated assignee ID - Use Connect Portal Workflow Settings
    * `ticketType` (string, optional): Updated ticket type - Options: problem, incident, question, task
    * `ticketPriority` (string, optional): Updated priority - Options: urgent, high, normal, low
    * `ticketStatus` (string, optional): Updated status - Options: new, open, pending, hold, solved, closed
    * `ticketDueAt` (string, optional): Updated due date (ISO 8601 timestamp)
    * `ticketTags` (string, optional): Updated tags array
    * `ticketExternalId` (string, optional): Updated external ID
    * `ticketCustomFields` (object, optional): Updated custom field values
  </Accordion>

<Accordion title="zendesk/get_ticket_by_id">
    **Description:** Retrieve a specific ticket by its ID.

* `ticketId` (string, required): The ticket ID to retrieve (e.g., "35436")
  </Accordion>

<Accordion title="zendesk/add_comment_to_ticket">
    **Description:** Add a comment or internal note to an existing ticket.

* `ticketId` (string, required): ID of the ticket to add comment to (e.g., "35436")
    * `commentBody` (string, required): Comment message (accepts plain text or HTML, e.g., "Thanks for your help!")
    * `isInternalNote` (boolean, optional): Set to true for internal notes instead of public replies (defaults to false)
    * `isPublic` (boolean, optional): True for public comments, false for internal notes
  </Accordion>

<Accordion title="zendesk/search_tickets">
    **Description:** Search for tickets using various filters and criteria.

* `ticketSubject` (string, optional): Filter by text in ticket subject
    * `ticketDescription` (string, optional): Filter by text in ticket description and comments
    * `ticketStatus` (string, optional): Filter by status - Options: new, open, pending, hold, solved, closed
    * `ticketType` (string, optional): Filter by type - Options: problem, incident, question, task, no\_type
    * `ticketPriority` (string, optional): Filter by priority - Options: urgent, high, normal, low, no\_priority
    * `requesterId` (string, optional): Filter by requester user ID
    * `assigneeId` (string, optional): Filter by assigned agent ID
    * `recipientEmail` (string, optional): Filter by original recipient email address
    * `ticketTags` (string, optional): Filter by ticket tags
    * `ticketExternalId` (string, optional): Filter by external ID
    * `createdDate` (object, optional): Filter by creation date with operator (EQUALS, LESS\_THAN\_EQUALS, GREATER\_THAN\_EQUALS) and value
    * `updatedDate` (object, optional): Filter by update date with operator and value
    * `dueDate` (object, optional): Filter by due date with operator and value
    * `sort_by` (string, optional): Sort field - Options: created\_at, updated\_at, priority, status, ticket\_type
    * `sort_order` (string, optional): Sort direction - Options: asc, desc
  </Accordion>
</AccordionGroup>

### **User Management**

<AccordionGroup>
  <Accordion title="zendesk/create_user">
    **Description:** Create a new user in Zendesk.

* `name` (string, required): User's full name
    * `email` (string, optional): User's email address (e.g., "[jane@example.com](mailto:jane@example.com)")
    * `phone` (string, optional): User's phone number
    * `role` (string, optional): User role - Options: admin, agent, end-user
    * `externalId` (string, optional): Unique identifier from another system
    * `details` (string, optional): Additional user details
    * `notes` (string, optional): Internal notes about the user
  </Accordion>

<Accordion title="zendesk/update_user">
    **Description:** Update an existing user's information.

* `userId` (string, required): ID of the user to update
    * `name` (string, optional): Updated user name
    * `email` (string, optional): Updated email (adds as secondary email on update)
    * `phone` (string, optional): Updated phone number
    * `role` (string, optional): Updated role - Options: admin, agent, end-user
    * `externalId` (string, optional): Updated external ID
    * `details` (string, optional): Updated user details
    * `notes` (string, optional): Updated internal notes
  </Accordion>

<Accordion title="zendesk/get_user_by_id">
    **Description:** Retrieve a specific user by their ID.

* `userId` (string, required): The user ID to retrieve
  </Accordion>

<Accordion title="zendesk/search_users">
    **Description:** Search for users using various criteria.

* `name` (string, optional): Filter by user name
    * `email` (string, optional): Filter by user email (e.g., "[jane@example.com](mailto:jane@example.com)")
    * `role` (string, optional): Filter by role - Options: admin, agent, end-user
    * `externalId` (string, optional): Filter by external ID
    * `sort_by` (string, optional): Sort field - Options: created\_at, updated\_at
    * `sort_order` (string, optional): Sort direction - Options: asc, desc
  </Accordion>
</AccordionGroup>

### **Administrative Tools**

<AccordionGroup>
  <Accordion title="zendesk/get_ticket_fields">
    **Description:** Retrieve all standard and custom fields available for tickets.

* `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>

<Accordion title="zendesk/get_ticket_audits">
    **Description:** Get audit records (read-only history) for tickets.

* `ticketId` (string, optional): Get audits for specific ticket (if empty, retrieves audits for all non-archived tickets, e.g., "1234")
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>
</AccordionGroup>

Custom fields allow you to store additional information specific to your organization:

## Ticket Priority Levels

Understanding priority levels:

* **urgent** - Critical issues requiring immediate attention
* **high** - Important issues that should be addressed quickly
* **normal** - Standard priority for most tickets
* **low** - Minor issues that can be addressed when convenient

## Ticket Status Workflow

Standard ticket status progression:

* **new** - Recently created, not yet assigned
* **open** - Actively being worked on
* **pending** - Waiting for customer response or external action
* **hold** - Temporarily paused
* **solved** - Issue resolved, awaiting customer confirmation
* **closed** - Ticket completed and closed

### Basic Zendesk Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai import Agent, Task, Crew

**Examples:**

Example 1 (unknown):
```unknown
### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>
```

Example 2 (unknown):
```unknown
Or add it to your `.env` file:
```

Example 3 (unknown):
```unknown
## Available Tools

### **Ticket Management**

<AccordionGroup>
  <Accordion title="zendesk/create_ticket">
    **Description:** Create a new support ticket in Zendesk.

    **Parameters:**

    * `ticketSubject` (string, required): Ticket subject line (e.g., "Help, my printer is on fire!")
    * `ticketDescription` (string, required): First comment that appears on the ticket (e.g., "The smoke is very colorful.")
    * `requesterName` (string, required): Name of the user requesting support (e.g., "Jane Customer")
    * `requesterEmail` (string, required): Email of the user requesting support (e.g., "[jane@example.com](mailto:jane@example.com)")
    * `assigneeId` (string, optional): Zendesk Agent ID assigned to this ticket - Use Connect Portal Workflow Settings to allow users to select an assignee
    * `ticketType` (string, optional): Ticket type - Options: problem, incident, question, task
    * `ticketPriority` (string, optional): Priority level - Options: urgent, high, normal, low
    * `ticketStatus` (string, optional): Ticket status - Options: new, open, pending, hold, solved, closed
    * `ticketDueAt` (string, optional): Due date for task-type tickets (ISO 8601 timestamp)
    * `ticketTags` (string, optional): Array of tags to apply (e.g., `["enterprise", "other_tag"]`)
    * `ticketExternalId` (string, optional): External ID to link tickets to local records
    * `ticketCustomFields` (object, optional): Custom field values in JSON format
  </Accordion>

  <Accordion title="zendesk/update_ticket">
    **Description:** Update an existing support ticket in Zendesk.

    **Parameters:**

    * `ticketId` (string, required): ID of the ticket to update (e.g., "35436")
    * `ticketSubject` (string, optional): Updated ticket subject
    * `requesterName` (string, required): Name of the user who requested this ticket
    * `requesterEmail` (string, required): Email of the user who requested this ticket
    * `assigneeId` (string, optional): Updated assignee ID - Use Connect Portal Workflow Settings
    * `ticketType` (string, optional): Updated ticket type - Options: problem, incident, question, task
    * `ticketPriority` (string, optional): Updated priority - Options: urgent, high, normal, low
    * `ticketStatus` (string, optional): Updated status - Options: new, open, pending, hold, solved, closed
    * `ticketDueAt` (string, optional): Updated due date (ISO 8601 timestamp)
    * `ticketTags` (string, optional): Updated tags array
    * `ticketExternalId` (string, optional): Updated external ID
    * `ticketCustomFields` (object, optional): Updated custom field values
  </Accordion>

  <Accordion title="zendesk/get_ticket_by_id">
    **Description:** Retrieve a specific ticket by its ID.

    **Parameters:**

    * `ticketId` (string, required): The ticket ID to retrieve (e.g., "35436")
  </Accordion>

  <Accordion title="zendesk/add_comment_to_ticket">
    **Description:** Add a comment or internal note to an existing ticket.

    **Parameters:**

    * `ticketId` (string, required): ID of the ticket to add comment to (e.g., "35436")
    * `commentBody` (string, required): Comment message (accepts plain text or HTML, e.g., "Thanks for your help!")
    * `isInternalNote` (boolean, optional): Set to true for internal notes instead of public replies (defaults to false)
    * `isPublic` (boolean, optional): True for public comments, false for internal notes
  </Accordion>

  <Accordion title="zendesk/search_tickets">
    **Description:** Search for tickets using various filters and criteria.

    **Parameters:**

    * `ticketSubject` (string, optional): Filter by text in ticket subject
    * `ticketDescription` (string, optional): Filter by text in ticket description and comments
    * `ticketStatus` (string, optional): Filter by status - Options: new, open, pending, hold, solved, closed
    * `ticketType` (string, optional): Filter by type - Options: problem, incident, question, task, no\_type
    * `ticketPriority` (string, optional): Filter by priority - Options: urgent, high, normal, low, no\_priority
    * `requesterId` (string, optional): Filter by requester user ID
    * `assigneeId` (string, optional): Filter by assigned agent ID
    * `recipientEmail` (string, optional): Filter by original recipient email address
    * `ticketTags` (string, optional): Filter by ticket tags
    * `ticketExternalId` (string, optional): Filter by external ID
    * `createdDate` (object, optional): Filter by creation date with operator (EQUALS, LESS\_THAN\_EQUALS, GREATER\_THAN\_EQUALS) and value
    * `updatedDate` (object, optional): Filter by update date with operator and value
    * `dueDate` (object, optional): Filter by due date with operator and value
    * `sort_by` (string, optional): Sort field - Options: created\_at, updated\_at, priority, status, ticket\_type
    * `sort_order` (string, optional): Sort direction - Options: asc, desc
  </Accordion>
</AccordionGroup>

### **User Management**

<AccordionGroup>
  <Accordion title="zendesk/create_user">
    **Description:** Create a new user in Zendesk.

    **Parameters:**

    * `name` (string, required): User's full name
    * `email` (string, optional): User's email address (e.g., "[jane@example.com](mailto:jane@example.com)")
    * `phone` (string, optional): User's phone number
    * `role` (string, optional): User role - Options: admin, agent, end-user
    * `externalId` (string, optional): Unique identifier from another system
    * `details` (string, optional): Additional user details
    * `notes` (string, optional): Internal notes about the user
  </Accordion>

  <Accordion title="zendesk/update_user">
    **Description:** Update an existing user's information.

    **Parameters:**

    * `userId` (string, required): ID of the user to update
    * `name` (string, optional): Updated user name
    * `email` (string, optional): Updated email (adds as secondary email on update)
    * `phone` (string, optional): Updated phone number
    * `role` (string, optional): Updated role - Options: admin, agent, end-user
    * `externalId` (string, optional): Updated external ID
    * `details` (string, optional): Updated user details
    * `notes` (string, optional): Updated internal notes
  </Accordion>

  <Accordion title="zendesk/get_user_by_id">
    **Description:** Retrieve a specific user by their ID.

    **Parameters:**

    * `userId` (string, required): The user ID to retrieve
  </Accordion>

  <Accordion title="zendesk/search_users">
    **Description:** Search for users using various criteria.

    **Parameters:**

    * `name` (string, optional): Filter by user name
    * `email` (string, optional): Filter by user email (e.g., "[jane@example.com](mailto:jane@example.com)")
    * `role` (string, optional): Filter by role - Options: admin, agent, end-user
    * `externalId` (string, optional): Filter by external ID
    * `sort_by` (string, optional): Sort field - Options: created\_at, updated\_at
    * `sort_order` (string, optional): Sort direction - Options: asc, desc
  </Accordion>
</AccordionGroup>

### **Administrative Tools**

<AccordionGroup>
  <Accordion title="zendesk/get_ticket_fields">
    **Description:** Retrieve all standard and custom fields available for tickets.

    **Parameters:**

    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>

  <Accordion title="zendesk/get_ticket_audits">
    **Description:** Get audit records (read-only history) for tickets.

    **Parameters:**

    * `ticketId` (string, optional): Get audits for specific ticket (if empty, retrieves audits for all non-archived tickets, e.g., "1234")
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>
</AccordionGroup>

## Custom Fields

Custom fields allow you to store additional information specific to your organization:
```

Example 4 (unknown):
```unknown
## Ticket Priority Levels

Understanding priority levels:

* **urgent** - Critical issues requiring immediate attention
* **high** - Important issues that should be addressed quickly
* **normal** - Standard priority for most tickets
* **low** - Minor issues that can be addressed when convenient

## Ticket Status Workflow

Standard ticket status progression:

* **new** - Recently created, not yet assigned
* **open** - Actively being worked on
* **pending** - Waiting for customer response or external action
* **hold** - Temporarily paused
* **solved** - Issue resolved, awaiting customer confirmation
* **closed** - Ticket completed and closed

## Usage Examples

### Basic Zendesk Agent Setup
```

---

## ...

**URL:** llms-txt#...

task1 = Task(
    description='Find and summarize the latest AI news',
    expected_output='A bullet list summary of the top 5 most important AI news',
    agent=research_agent,
    tools=[search_tool]
)

crew = Crew(
    agents=[research_agent],
    tasks=[task1, task2, task3],
    verbose=True
)

result = crew.kickoff()

---
