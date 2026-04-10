# Crewai - Tools

**Pages:** 40

---

## 3. Continue with available tools

**URL:** llms-txt#3.-continue-with-available-tools

---

## Add tools to agent

**URL:** llms-txt#add-tools-to-agent

**Contents:**
- Agent Memory and Context
- Context Window Management
  - How Context Window Management Works
  - Automatic Context Handling (`respect_context_window=True`)

researcher = Agent(
    role="AI Technology Researcher",
    goal="Research the latest AI developments",
    tools=[search_tool, wiki_tool],
    verbose=True
)
python Code theme={null}
from crewai import Agent

analyst = Agent(
    role="Data Analyst",
    goal="Analyze and remember complex data patterns",
    memory=True,  # Enable memory
    verbose=True
)
python Code theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## Agent Memory and Context

Agents can maintain memory of their interactions and use context from previous tasks. This is particularly useful for complex workflows where information needs to be retained across multiple tasks.
```

Example 2 (unknown):
```unknown
<Note>
  When `memory` is enabled, the agent will maintain context across multiple interactions, improving its ability to handle complex, multi-step tasks.
</Note>

## Context Window Management

CrewAI includes sophisticated automatic context window management to handle situations where conversations exceed the language model's token limits. This powerful feature is controlled by the `respect_context_window` parameter.

### How Context Window Management Works

When an agent's conversation history grows too large for the LLM's context window, CrewAI automatically detects this situation and can either:

1. **Automatically summarize content** (when `respect_context_window=True`)
2. **Stop execution with an error** (when `respect_context_window=False`)

### Automatic Context Handling (`respect_context_window=True`)

This is the **default and recommended setting** for most use cases. When enabled, CrewAI will:
```

---

## Add tools to your agent

**URL:** llms-txt#add-tools-to-your-agent

**Contents:**
- **Max Usage Count**

agent = Agent(
    role="Research Analyst",
    tools=[FileReadTool(), SerperDevTool()],
    # ... other configuration
)
python  theme={null}
from crewai_tools import FileReadTool

tool = FileReadTool(max_usage_count=5, ...)
```

Ready to explore? Pick a category above to discover tools that fit your use case!

**Examples:**

Example 1 (unknown):
```unknown
## **Max Usage Count**

You can set a maximum usage count for a tool to prevent it from being used more than a certain number of times.
By default, the max usage count is unlimited.
```

---

## Agent will use tools from working servers and log warnings for failing ones

**URL:** llms-txt#agent-will-use-tools-from-working-servers-and-log-warnings-for-failing-ones

**Contents:**
- Advanced: MCPServerAdapter
- Connection Configuration

**Examples:**

Example 1 (unknown):
```unknown
All connection errors are handled gracefully:

* **Connection failures**: Logged as warnings, agent continues with available tools
* **Timeout errors**: Connections timeout after 30 seconds (configurable)
* **Authentication errors**: Logged clearly for debugging
* **Invalid configurations**: Validation errors are raised at agent creation time

## Advanced: MCPServerAdapter

For complex scenarios requiring manual connection management, use the `MCPServerAdapter` class from `crewai-tools`. Using a Python context manager (`with` statement) is the recommended approach as it automatically handles starting and stopping the connection to the MCP server.

## Connection Configuration

The `MCPServerAdapter` supports several configuration options to customize the connection behavior:

* **`connect_timeout`** (optional): Maximum time in seconds to wait for establishing a connection to the MCP server. Defaults to 30 seconds if not specified. This is particularly useful for remote servers that may have variable response times.
```

---

## Better solution: Use RAG tools for large data

**URL:** llms-txt#better-solution:-use-rag-tools-for-large-data

from crewai_tools import RagTool
agent.tools = [RagTool()]

---

## Bright Data Tools

**URL:** llms-txt#bright-data-tools

**Contents:**
- Installation
- Environment Variables
- Included Tools
- Examples
  - SERP Search
  - Web Unlocker
  - Dataset API
- Troubleshooting
- Example

This set of tools integrates Bright Data services for web extraction.

## Environment Variables

* `BRIGHT_DATA_API_KEY` (required)
* `BRIGHT_DATA_ZONE` (for SERP/Web Unlocker)

Create credentials at [https://brightdata.com/](https://brightdata.com/) (sign up, then create an API token and zone).
See their docs: [https://developers.brightdata.com/](https://developers.brightdata.com/)

* `BrightDataSearchTool`: SERP search (Google/Bing/Yandex) with geo/language/device options.
* `BrightDataWebUnlockerTool`: Scrape pages with anti-bot bypass and rendering.
* `BrightDataDatasetTool`: Run Dataset API jobs and fetch results.

* 401/403: verify `BRIGHT_DATA_API_KEY` and `BRIGHT_DATA_ZONE`.
* Empty/blocked content: enable rendering or try a different zone.

**Examples:**

Example 1 (unknown):
```unknown
## Environment Variables

* `BRIGHT_DATA_API_KEY` (required)
* `BRIGHT_DATA_ZONE` (for SERP/Web Unlocker)

Create credentials at [https://brightdata.com/](https://brightdata.com/) (sign up, then create an API token and zone).
See their docs: [https://developers.brightdata.com/](https://developers.brightdata.com/)

## Included Tools

* `BrightDataSearchTool`: SERP search (Google/Bing/Yandex) with geo/language/device options.
* `BrightDataWebUnlockerTool`: Scrape pages with anti-bot bypass and rendering.
* `BrightDataDatasetTool`: Run Dataset API jobs and fetch results.

## Examples

### SERP Search
```

Example 2 (unknown):
```unknown
### Web Unlocker
```

Example 3 (unknown):
```unknown
### Dataset API
```

Example 4 (unknown):
```unknown
## Troubleshooting

* 401/403: verify `BRIGHT_DATA_API_KEY` and `BRIGHT_DATA_ZONE`.
* Empty/blocked content: enable rendering or try a different zone.

## Example
```

---

## `ComposioToolSet`

**URL:** llms-txt#`composiotoolset`

**Contents:**
- Description
- Installation
- Example

Composio is an integration platform that allows you to connect your AI agents to 250+ tools. Key features include:

* **Enterprise-Grade Authentication**: Built-in support for OAuth, API Keys, JWT with automatic token refresh
* **Full Observability**: Detailed tool usage logs, execution timestamps, and more

To incorporate Composio tools into your project, follow the instructions below:

After the installation is complete, either run `composio login` or export your composio API key as `COMPOSIO_API_KEY`. Get your Composio API key from [here](https://app.composio.dev)

The following example demonstrates how to initialize the tool and execute a github action:

1. Initialize Composio toolset

2. Connect your GitHub account

* Retrieving all the tools from an app (not recommended for production):

* Filtering tools based on tags:

* Filtering tools based on use case:

<Tip>Set `advanced` to True to get actions for complex use cases</Tip>

* Using specific tools:

In this demo, we will use the `GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER` action from the GitHub app.

Learn more about filtering actions [here](https://docs.composio.dev/patterns/tools/use-tools/use-specific-actions)

* More detailed list of tools can be found [here](https://app.composio.dev)

**Examples:**

Example 1 (unknown):
```unknown
After the installation is complete, either run `composio login` or export your composio API key as `COMPOSIO_API_KEY`. Get your Composio API key from [here](https://app.composio.dev)

## Example

The following example demonstrates how to initialize the tool and execute a github action:

1. Initialize Composio toolset
```

Example 2 (unknown):
```unknown
2. Connect your GitHub account

<CodeGroup>
```

Example 3 (unknown):
```unknown

```

Example 4 (unknown):
```unknown
</CodeGroup>

3. Get Tools

* Retrieving all the tools from an app (not recommended for production):
```

---

## Create agent with MCP tools using string references

**URL:** llms-txt#create-agent-with-mcp-tools-using-string-references

research_agent = Agent(
    role="Research Analyst",
    goal="Find and analyze information using advanced search tools",
    backstory="Expert researcher with access to multiple data sources",
    mcps=[
        "https://mcp.exa.ai/mcp?api_key=your_key&profile=your_profile",
        "crewai-amp:weather-service#current_conditions"
    ]
)

---

## Create AI tools

**URL:** llms-txt#create-ai-tools

image_generator = DallETool()
vision_processor = VisionTool()
code_executor = CodeInterpreterTool()

---

## Create automation tools

**URL:** llms-txt#create-automation-tools

apify_automation = ApifyActorTool()
platform_integration = ComposioTool()
browser_automation = MultiOnTool()

---

## Create cloud tools

**URL:** llms-txt#create-cloud-tools

s3_reader = S3ReaderTool()
s3_writer = S3WriterTool()
bedrock_agent = BedrockInvokeAgentTool()

---

## Create Custom Tools

**URL:** llms-txt#create-custom-tools

**Contents:**
- Creating and Utilizing Tools in CrewAI
  - Subclassing `BaseTool`
  - Using the `tool` Decorator
  - Defining a Cache Function for the Tool
  - Creating Async Tools

Source: https://docs.crewai.com/en/learn/create-custom-tools

Comprehensive guide on crafting, using, and managing custom tools within the CrewAI framework, including new functionalities and error handling.

## Creating and Utilizing Tools in CrewAI

This guide provides detailed instructions on creating custom tools for the CrewAI framework and how to efficiently manage and utilize these tools,
incorporating the latest functionalities such as tool delegation, error handling, and dynamic tool calling. It also highlights the importance of collaboration tools,
enabling agents to perform a wide range of actions.

### Subclassing `BaseTool`

To create a personalized tool, inherit from `BaseTool` and define the necessary attributes, including the `args_schema` for input validation, and the `_run` method.

### Using the `tool` Decorator

Alternatively, you can use the tool decorator `@tool`. This approach allows you to define the tool's attributes and functionality directly within a function,
offering a concise and efficient way to create specialized tools tailored to your needs.

### Defining a Cache Function for the Tool

To optimize tool performance with caching, define custom caching strategies using the `cache_function` attribute.

### Creating Async Tools

CrewAI supports async tools for non-blocking I/O operations. This is useful when your tool needs to make HTTP requests, database queries, or other I/O-bound operations.

#### Using the `@tool` Decorator with Async Functions

The simplest way to create an async tool is using the `@tool` decorator with an async function:

#### Subclassing `BaseTool` with Async Support

For more control, subclass `BaseTool` and implement both `_run` (sync) and `_arun` (async) methods:

By adhering to these guidelines and incorporating new functionalities and collaboration tools into your tool creation and management processes,
you can leverage the full capabilities of the CrewAI framework, enhancing both the development experience and the efficiency of your AI agents.

**Examples:**

Example 1 (unknown):
```unknown
### Using the `tool` Decorator

Alternatively, you can use the tool decorator `@tool`. This approach allows you to define the tool's attributes and functionality directly within a function,
offering a concise and efficient way to create specialized tools tailored to your needs.
```

Example 2 (unknown):
```unknown
### Defining a Cache Function for the Tool

To optimize tool performance with caching, define custom caching strategies using the `cache_function` attribute.
```

Example 3 (unknown):
```unknown
### Creating Async Tools

CrewAI supports async tools for non-blocking I/O operations. This is useful when your tool needs to make HTTP requests, database queries, or other I/O-bound operations.

#### Using the `@tool` Decorator with Async Functions

The simplest way to create an async tool is using the `@tool` decorator with an async function:
```

Example 4 (unknown):
```unknown
#### Subclassing `BaseTool` with Async Support

For more control, subclass `BaseTool` and implement both `_run` (sync) and `_arun` (async) methods:
```

---

## Create database tools

**URL:** llms-txt#create-database-tools

mysql_db = MySQLTool()
vector_search = QdrantVectorSearchTool()
nl_to_sql = NL2SQLTool()

---

## Create research tools

**URL:** llms-txt#create-research-tools

web_search = SerperDevTool()
code_search = GitHubSearchTool()
video_research = YoutubeVideoSearchTool()
tavily_search = TavilySearchTool()
content_extractor = TavilyExtractorTool()

---

## Create scraping tools

**URL:** llms-txt#create-scraping-tools

simple_scraper = ScrapeWebsiteTool()
advanced_scraper = FirecrawlScrapeWebsiteTool()
browser_automation = SeleniumScrapingTool()

---

## Create tools

**URL:** llms-txt#create-tools

file_reader = FileReadTool()
pdf_searcher = PDFSearchTool()
json_processor = JSONSearchTool()

---

## CrewAI creates tools: "mcp_exa_ai_search", "mcp_exa_ai_analyze"

**URL:** llms-txt#crewai-creates-tools:-"mcp_exa_ai_search",-"mcp_exa_ai_analyze"

agent = Agent(
    role="Tool Organization Demo",
    goal="Show how tool naming works",
    backstory="Demonstrates automatic tool organization",
    mcps=[
        "https://mcp.exa.ai/mcp?api_key=key",      # Tools: mcp_exa_ai_*
        "https://weather.service.com/mcp",         # Tools: weather_service_com_*
        "crewai-amp:financial-data"                # Tools: financial_data_*
    ]
)

---

## Each server's tools get unique prefixes based on the server name

**URL:** llms-txt#each-server's-tools-get-unique-prefixes-based-on-the-server-name

---

## First agent creation - discovers tools from server

**URL:** llms-txt#first-agent-creation---discovers-tools-from-server

agent1 = Agent(role="First", goal="Test", backstory="Test",
               mcps=["https://api.example.com/mcp"])

---

## Full service with all tools

**URL:** llms-txt#full-service-with-all-tools

"crewai-amp:financial-data"

---

## Gmail Trigger

**URL:** llms-txt#gmail-trigger

**Contents:**
- Overview
- Enabling the Gmail Trigger
- Example: Process new emails
  - Testing Locally

Source: https://docs.crewai.com/en/enterprise/guides/gmail-trigger

Trigger automations when Gmail events occur (e.g., new emails, labels).

Use the Gmail Trigger to kick off your deployed crews when Gmail events happen in connected accounts, such as receiving a new email or messages matching a label/filter.

<Tip>
  Make sure Gmail is connected in Tools & Integrations and the trigger is enabled for your deployment.
</Tip>

## Enabling the Gmail Trigger

1. Open your deployment in CrewAI AOP
2. Go to the **Triggers** tab
3. Locate **Gmail** and switch the toggle to enable

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=10b3ee6296f323168473593b64a1e4c8" alt="Enable or disable triggers with toggle" data-og-width="1984" width="1984" data-og-height="866" height="866" data-path="images/enterprise/trigger-selected.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=27137c8d8c072ece3319e9f4c8ee0185 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=842109fa147a6a91b9f9480e450a8ee0 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5f2cbab1be7662c99854f88496f42b4b 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5fa4240b233d980059d3db96c493fda4 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=37f3001a39aab6400b8df45fad9b5cfa 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b2959938cb0f239a6113c9a8b7aa0356 2500w" />
</Frame>

## Example: Process new emails

When a new email arrives, the Gmail Trigger will send the payload to your Crew or Flow. Below is a Crew example that parses and processes the trigger payload.

The Gmail payload will be available via the standard context mechanisms.

Test your Gmail trigger integration locally using the CrewAI CLI:

```bash  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
The Gmail payload will be available via the standard context mechanisms.

### Testing Locally

Test your Gmail trigger integration locally using the CrewAI CLI:
```

---

## Good - only get the tools you need

**URL:** llms-txt#good---only-get-the-tools-you-need

mcps=["https://weather.api.com/mcp#get_forecast"]

---

## Google Calendar Trigger

**URL:** llms-txt#google-calendar-trigger

**Contents:**
- Overview
- Enabling the Google Calendar Trigger
- Example: Summarize meeting details
- Testing Locally

Source: https://docs.crewai.com/en/enterprise/guides/google-calendar-trigger

Kick off crews when Google Calendar events are created, updated, or cancelled

Use the Google Calendar trigger to launch automations whenever calendar events change. Common use cases include briefing a team before a meeting, notifying stakeholders when a critical event is cancelled, or summarizing daily schedules.

<Tip>
  Make sure Google Calendar is connected in **Tools & Integrations** and enabled for the deployment you want to automate.
</Tip>

## Enabling the Google Calendar Trigger

1. Open your deployment in CrewAI AOP
2. Go to the **Triggers** tab
3. Locate **Google Calendar** and switch the toggle to enable

<Frame>
  <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e6594f439112ba76a399585e3e69e166" alt="Enable or disable triggers with toggle" data-og-width="2228" width="2228" data-og-height="1000" height="1000" data-path="images/enterprise/calendar-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=fa2e4f7da20c86c5ad7a6b7e2ab96116 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c3f8a6638774eadefa5a5924328d5787 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=a2b8c83efc9a11a156877a8f061ca39c 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c772c71eda91c64d2db474c2ecb74159 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=35c5f5fe2de12a82aa0f1f798380def1 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=1fefaff8a0a2cf8e9d7d4c11203ed0eb 2500w" />
</Frame>

## Example: Summarize meeting details

The snippet below mirrors the `calendar-event-crew.py` example in the trigger repository. It parses the payload, analyses the attendees and timing, and produces a meeting brief for downstream tools.

Use `crewai_trigger_payload` exactly as it is delivered by the trigger so the crew can extract the proper fields.

Test your Google Calendar trigger integration locally using the CrewAI CLI:

```bash  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
Use `crewai_trigger_payload` exactly as it is delivered by the trigger so the crew can extract the proper fields.

## Testing Locally

Test your Google Calendar trigger integration locally using the CrewAI CLI:
```

---

## Importing crewAI tools

**URL:** llms-txt#importing-crewai-tools

from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

---

## Initialize different automation tools

**URL:** llms-txt#initialize-different-automation-tools

data_collection_tool = InvokeCrewAIAutomationTool(
    crew_api_url="https://data-collection-crew-[...].crewai.com",
    crew_bearer_token="your_bearer_token_here",
    crew_name="Data Collection Automation",
    crew_description="Collects and preprocesses raw data"
)

analysis_tool = InvokeCrewAIAutomationTool(
    crew_api_url="https://analysis-crew-[...].crewai.com",
    crew_bearer_token="your_bearer_token_here",
    crew_name="Analysis Automation",
    crew_description="Performs advanced data analysis and modeling"
)

reporting_tool = InvokeCrewAIAutomationTool(
    crew_api_url="https://reporting-crew-[...].crewai.com",
    crew_bearer_token="your_bearer_token_here",
    crew_name="Reporting Automation",
    crew_description="Generates comprehensive reports and visualizations"
)

---

## Initialize from LlamaHub Tools

**URL:** llms-txt#initialize-from-llamahub-tools

**Contents:**
  - From a LlamaIndex Query Engine

wolfram_spec = WolframAlphaToolSpec(app_id="your_app_id")
wolfram_tools = wolfram_spec.to_tool_list()
tools = [LlamaIndexTool.from_tool(t) for t in wolfram_tools]
python Code theme={null}
from crewai_tools import LlamaIndexTool
from llama_index.core import VectorStoreIndex
from llama_index.core.readers import SimpleDirectoryReader

**Examples:**

Example 1 (unknown):
```unknown
### From a LlamaIndex Query Engine
```

---

## Initialize tools with session management

**URL:** llms-txt#initialize-tools-with-session-management

initial_tool = BedrockInvokeAgentTool(
    agent_id="your-agent-id",
    agent_alias_id="your-agent-alias-id",
    session_id="custom-session-id"
)

followup_tool = BedrockInvokeAgentTool(
    agent_id="your-agent-id",
    agent_alias_id="your-agent-alias-id",
    session_id="custom-session-id"
)

final_tool = BedrockInvokeAgentTool(
    agent_id="your-agent-id",
    agent_alias_id="your-agent-alias-id",
    session_id="custom-session-id",
    end_session=True
)

---

## Instantiate tools

**URL:** llms-txt#instantiate-tools

docs_tool = DirectoryReadTool(directory='./blog-posts')
file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

---

## LangChain Tool

**URL:** llms-txt#langchain-tool

**Contents:**
- `LangChainTool`

Source: https://docs.crewai.com/en/tools/ai-ml/langchaintool

The `LangChainTool` is a wrapper for LangChain tools and query engines.

<Info>
  CrewAI seamlessly integrates with LangChain's comprehensive [list of tools](https://python.langchain.com/docs/integrations/tools/), all of which can be used with CrewAI.
</Info>

```python Code theme={null}
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai.tools import BaseTool
from pydantic import Field
from langchain_community.utilities import GoogleSerperAPIWrapper

---

## Less efficient - gets all tools from server

**URL:** llms-txt#less-efficient---gets-all-tools-from-server

**Contents:**
  - 2. Handle Authentication Securely

mcps=["https://weather.api.com/mcp"]
python  theme={null}
import os

**Examples:**

Example 1 (unknown):
```unknown
### 2. Handle Authentication Securely
```

---

## Loading Tools

**URL:** llms-txt#loading-tools

search_tool = SerperDevTool()

---

## Marketplace

**URL:** llms-txt#marketplace

**Contents:**
- Overview
- Discoverability
- Install & Enable
- Related

Source: https://docs.crewai.com/en/enterprise/features/marketplace

Discover, install, and govern reusable assets for your enterprise crews.

The Marketplace provides a curated surface for discovering integrations, internal tools, and reusable assets that accelerate crew development.

<Frame>
    <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=77786aca40c58c31775cb4de35b26d54" alt="Marketplace Overview" data-og-width="3040" width="3040" data-og-height="2266" height="2266" data-path="images/enterprise/marketplace-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=ae939d5b2f6f4d087498ec8a3a342ea7 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=6113d807f99c7de5a4ac3012518dbfcc 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=9e21e42a266f06cb864455b8935f54fc 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=41b47b8f0c3694766edfffe121f81402 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=b8d75afbe1aeb98abc3cfd55d90ebce0 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=a798183edcdfddb19e6ae6b7ab0ab76b 2500w" />
</Frame>

* Browse by category and capability
* Search for assets by name or keyword

* One‑click install for approved assets
* Enable or disable per crew as needed
* Configure required environment variables and scopes

<Frame>
    <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=cc15b069d1d4da8555e9630e1e874346" alt="Install & Configure" data-og-width="2672" width="2672" data-og-height="2266" height="2266" data-path="images/enterprise/marketplace-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=cfdaa8690cb6651c51c5ba579364fb7a 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=2ddf18661fb7c7ad08e3f1029311813f 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=b0c3ee1f87a674b1ae31956a201e4b10 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=cedd73cab5194bd1381d594d0b102e2a 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=acfc5d304485f464f7bb5780c97ab237 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=1ea74be846d2c2eaf37cd372273f6347 2500w" />
</Frame>

You can also download the templates directly from the marketplace by clicking on the `Download` button so
you can use them locally or refine them to your needs.

<CardGroup cols={3}>
  <Card title="Tools & Integrations" href="/en/enterprise/features/tools-and-integrations" icon="wrench">
    Connect external apps and manage internal tools your agents can use.
  </Card>

<Card title="Tool Repository" href="/en/enterprise/guides/tool-repository#tool-repository" icon="toolbox">
    Publish and install tools to enhance your crews' capabilities.
  </Card>

<Card title="Agents Repository" href="/en/enterprise/features/agent-repositories" icon="people-group">
    Store, share, and reuse agent definitions across teams and projects.
  </Card>
</CardGroup>

---

## MCP Servers as Tools in CrewAI

**URL:** llms-txt#mcp-servers-as-tools-in-crewai

**Contents:**
- Overview
  - 🚀 **Simple DSL Integration** (Recommended)

Source: https://docs.crewai.com/en/mcp/overview

Learn how to integrate MCP servers as tools in your CrewAI agents using the `crewai-tools` library.

The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) provides a standardized way for AI agents to provide context to LLMs by communicating with external services, known as MCP Servers.

CrewAI offers **two approaches** for MCP integration:

### 🚀 **Simple DSL Integration** (Recommended)

Use the `mcps` field directly on agents for seamless MCP tool integration. The DSL supports both **string references** (for quick setup) and **structured configurations** (for full control).

#### String-Based References (Quick Setup)

Perfect for remote HTTPS servers and CrewAI AOP marketplace:

```python  theme={null}
from crewai import Agent

agent = Agent(
    role="Research Analyst",
    goal="Research and analyze information",
    backstory="Expert researcher with access to external tools",
    mcps=[
        "https://mcp.exa.ai/mcp?api_key=your_key",           # External MCP server
        "https://api.weather.com/mcp#get_forecast",          # Specific tool from server
        "crewai-amp:financial-data",                         # CrewAI AOP marketplace
        "crewai-amp:research-tools#pubmed_search"            # Specific AMP tool
    ]
)

---

## MCP tools are now automatically available!

**URL:** llms-txt#mcp-tools-are-now-automatically-available!

---

## MCP tools are now automatically available to your agent!

**URL:** llms-txt#mcp-tools-are-now-automatically-available-to-your-agent!

**Contents:**
  - 🔧 **Advanced: MCPServerAdapter** (For Complex Scenarios)
- Video Tutorial
- Installation

python  theme={null}
from crewai import Agent
from crewai.mcp import MCPServerStdio, MCPServerHTTP, MCPServerSSE
from crewai.mcp.filters import create_static_tool_filter

agent = Agent(
    role="Advanced Research Analyst",
    goal="Research with full control over MCP connections",
    backstory="Expert researcher with advanced tool access",
    mcps=[
        # Stdio transport for local servers
        MCPServerStdio(
            command="npx",
            args=["-y", "@modelcontextprotocol/server-filesystem"],
            env={"API_KEY": "your_key"},
            tool_filter=create_static_tool_filter(
                allowed_tool_names=["read_file", "list_directory"]
            ),
            cache_tools_list=True,
        ),
        # HTTP/Streamable HTTP transport for remote servers
        MCPServerHTTP(
            url="https://api.example.com/mcp",
            headers={"Authorization": "Bearer your_token"},
            streamable=True,
            cache_tools_list=True,
        ),
        # SSE transport for real-time streaming
        MCPServerSSE(
            url="https://stream.example.com/mcp/sse",
            headers={"Authorization": "Bearer your_token"},
        ),
    ]
)
shell  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
#### Structured Configurations (Full Control)

For complete control over connection settings, tool filtering, and all transport types:
```

Example 2 (unknown):
```unknown
### 🔧 **Advanced: MCPServerAdapter** (For Complex Scenarios)

For advanced use cases requiring manual connection management, the `crewai-tools` library provides the `MCPServerAdapter` class.

We currently support the following transport mechanisms:

* **Stdio**: for local servers (communication via standard input/output between processes on the same machine)
* **Server-Sent Events (SSE)**: for remote servers (unidirectional, real-time data streaming from server to client over HTTP)
* **Streamable HTTPS**: for remote servers (flexible, potentially bi-directional communication over HTTPS, often utilizing SSE for server-to-client streams)

## Video Tutorial

Watch this video tutorial for a comprehensive guide on MCP integration with CrewAI:

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/TpQ45lAZh48" title="CrewAI MCP Integration Guide" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Installation

CrewAI MCP integration requires the `mcp` library:
```

---

## OneDrive Trigger

**URL:** llms-txt#onedrive-trigger

**Contents:**
- Overview
- Enabling the OneDrive Trigger
- Example: Audit file permissions
- Testing Locally

Source: https://docs.crewai.com/en/enterprise/guides/onedrive-trigger

Automate responses to OneDrive file activity

Start automations when files change inside OneDrive. You can generate audit summaries, notify security teams about external sharing, or update downstream line-of-business systems with new document metadata.

<Tip>
  Connect OneDrive in **Tools & Integrations** and toggle the trigger on for your deployment.
</Tip>

## Enabling the OneDrive Trigger

1. Open your deployment in CrewAI AOP
2. Go to the **Triggers** tab
3. Locate **OneDrive** and switch the toggle to enable

<Frame caption="Microsoft OneDrive trigger connection">
  <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=55774f3aee2c024ee81e8d543d9391be" alt="Enable or disable triggers with toggle" data-og-width="2166" width="2166" data-og-height="478" height="478" data-path="images/enterprise/onedrive-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=82cf038f92dfd9771c87ff44d364c42b 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=d79a78258619bcc517c9bcbf0e1b42f4 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=6e5fc33aaebcffe573195b7b7a85986e 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=bbd2f96f33f12988c8c52f36e178e553 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=ef16d274ea3fe359655c8ac163b3c97a 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=0efecea63f338e2cdf7372a627993bac 2500w" />
</Frame>

## Example: Audit file permissions

The crew inspects file metadata, user activity, and permission changes to produce a compliance-friendly summary.

Test your OneDrive trigger integration locally using the CrewAI CLI:

```bash  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
The crew inspects file metadata, user activity, and permission changes to produce a compliance-friendly summary.

## Testing Locally

Test your OneDrive trigger integration locally using the CrewAI CLI:
```

---

## Original MCP server has tools: "search", "analyze"

**URL:** llms-txt#original-mcp-server-has-tools:-"search",-"analyze"

---

## Outlook Trigger

**URL:** llms-txt#outlook-trigger

**Contents:**
- Overview
- Enabling the Outlook Trigger
- Example: Summarize a new email
- Testing Locally

Source: https://docs.crewai.com/en/enterprise/guides/outlook-trigger

Launch automations from Outlook emails and calendar updates

Automate responses when Outlook delivers a new message or when an event is removed from the calendar. Teams commonly route escalations, file tickets, or alert attendees of cancellations.

<Tip>
  Connect Outlook in **Tools & Integrations** and ensure the trigger is enabled for your deployment.
</Tip>

## Enabling the Outlook Trigger

1. Open your deployment in CrewAI AOP
2. Go to the **Triggers** tab
3. Locate **Outlook** and switch the toggle to enable

<Frame caption="Microsoft Outlook trigger connection">
  <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=f8a739ad0963ccddafeed60f21366628" alt="Enable or disable triggers with toggle" data-og-width="2186" width="2186" data-og-height="508" height="508" data-path="images/enterprise/outlook-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=03b5121587c619936c87f05e15992f08 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=651d2efd933f7109b216d343e6d6a6ce 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=a7a27424bf507c739280376fd57ea80d 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=481164952ea35f62566b09d392a0910b 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=f4d3db361e699578e9ce44bde1e683fd 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=aaabf7a26259291cf3b8545a4c3a996d 2500w" />
</Frame>

## Example: Summarize a new email

The crew extracts sender details, subject, body preview, and attachments before generating a structured response.

Test your Outlook trigger integration locally using the CrewAI CLI:

```bash  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
The crew extracts sender details, subject, body preview, and attachments before generating a structured response.

## Testing Locally

Test your Outlook trigger integration locally using the CrewAI CLI:
```

---

## Tools & Integrations

**URL:** llms-txt#tools-&-integrations

**Contents:**
- Overview
- Explore
- Related

Source: https://docs.crewai.com/en/enterprise/features/tools-and-integrations

Connect external apps and manage internal tools your agents can use.

Tools & Integrations is the central hub for connecting third‑party apps and managing internal tools that your agents can use at runtime.

<Frame>
    <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c31a4b9031f0f517fdce3baa48471f58" alt="Tools & Integrations Overview" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/enterprise/crew_connectors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9e592d155e388bb67d003b26884dc081 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=0c8aa20b2dc82de9ea3d2da6920e4195 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=782fe13ea53120f6d2f8e643a7a7b838 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=780cd735280c569e6e93caa8262b12d1 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=08bfe86a58ca08ec36ae67dca4aa5cf9 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e2bbe3b0fe0234001e030b501fa4d76c 2500w" />
</Frame>

<Tabs>
  <Tab title="Integrations" icon="plug">
    ## Agent Apps (Integrations)

Connect enterprise‑grade applications (e.g., Gmail, Google Drive, HubSpot, Slack) via OAuth to enable agent actions.

<Steps>
      <Step title="Connect">
        Click <b>Connect</b> on an app and complete OAuth.
      </Step>

<Step title="Configure">
        Optionally adjust scopes, triggers, and action availability.
      </Step>

<Step title="Use in Agents">
        Connected services become available as tools for your agents.
      </Step>
    </Steps>

<Frame>
            <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=43abfc4eae390e308bed0b8e15238a54" alt="Integrations Grid" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/agent-apps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e5e30bd3d904891d5c2c4d9d6182002a 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=a146a0d69ff2309e7eac8d2f07da1cba 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c85a4a7ebe043fc6819957ff51f3ef0d 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=4ea77f15a4fe2671267f7e3668615970 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=7835e5d197251834d83a6dd7c7813d0a 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=06cea3ae58b49b925566a7962585b148 2500w" />
    </Frame>

### Connect your Account

1. Go to <Link href="https://app.crewai.com/crewai_plus/connectors">Integrations</Link>
    2. Click <b>Connect</b> on the desired service
    3. Complete the OAuth flow and grant scopes
    4. Copy your Enterprise Token from <Link href="https://app.crewai.com/crewai_plus/settings/integrations">Integration Settings</Link>

<Frame>
            <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4e7388bcb76f3f8aa6c6802dd0a98956" alt="Enterprise Token" data-og-width="2264" width="2264" data-og-height="540" height="540" data-path="images/enterprise/enterprise_action_auth_token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f3d1bd9cd9783d3e83f42ab6ee42d26c 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=df1514f746270a9ae5fc252c07806761 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a16c5c7986003435afad4106ccbaa7c5 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=81dabefb14a7f604a68c74eff26dff90 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=2833c9f202a291f2cf022026db261793 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=eeece6b187aebd0ec9e8af29d8bfc889 2500w" />
    </Frame>

### Install Integration Tools

To use the integrations locally, you need to install the latest `crewai-tools` package.

### Environment Variable Setup

<Note>
      To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
    </Note>

Or add it to your `.env` file:

<Tip>
      Use the new streamlined approach to integrate enterprise apps. Simply specify the app and its actions directly in the Agent configuration.
    </Tip>

On a deployed crew, you can specify which actions are available for each integration from the service settings page.

<Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2e689397eabeacd23d0c226ff40566fd" alt="Filter Actions" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/enterprise/filtering_enterprise_action_tools.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a6045a09da61d593e04098a4627777c9 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=257b1eea0bca2def5d43df960a4171ef 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6b9b8686a4fec0c0cdd8c7aa9acd4695 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e16c10384300b96d4962e2847f6633bf 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6de59b5409513b100c5cd36a69701e5f 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=32ed2ecc611c989e0fe9d8cb351740fa 2500w" />
    </Frame>

### Scoped Deployments (multi‑user orgs)

You can scope each integration to a specific user. For example, a crew that connects to Google can use a specific user’s Gmail account.

<Tip>
      Useful when different teams/users must keep data access separated.
    </Tip>

Use the `user_bearer_token` to scope authentication to the requesting user. If the user isn’t logged in, the crew won’t use connected integrations. Otherwise it falls back to the default bearer token configured for the deployment.

<Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d62aed15392f304cfc16bfa38ab91a54" alt="User Bearer Token" data-og-width="532" width="532" data-og-height="732" height="732" data-path="images/enterprise/user_bearer_token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=efe731a753ab7efb10a65f648fba75a7 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=232d8d25cd253f071856f53425cc40c2 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=df7b4956ab7668c23380394d8ce0f6c1 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=523850a6b69b5dd47ceaca3681f0ac35 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=561dcfa07461ecc8c39cd80865802d5e 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=06fbc44278b7d23fd2befd6b745622e7 2500w" />
    </Frame>

#### Communication & Collaboration

* Gmail — Manage emails and drafts
    * Slack — Workspace notifications and alerts
    * Microsoft — Office 365 and Teams integration

#### Project Management

* Jira — Issue tracking and project management
    * ClickUp — Task and productivity management
    * Asana — Team task and project coordination
    * Notion — Page and database management
    * Linear — Software project and bug tracking
    * GitHub — Repository and issue management

#### Customer Relationship Management

* Salesforce — CRM account and opportunity management
    * HubSpot — Sales pipeline and contact management
    * Zendesk — Customer support ticket management

#### Business & Finance

* Stripe — Payment processing and customer management
    * Shopify — E‑commerce store and product management

#### Productivity & Storage

* Google Sheets — Spreadsheet data synchronization
    * Google Calendar — Event and schedule management
    * Box — File storage and document management

…and more to come!
  </Tab>

<Tab title="Internal Tools" icon="toolbox">
    ## Internal Tools

Create custom tools locally, publish them on CrewAI AOP Tool Repository and use them in your agents.

<Tip>
      Before running the commands below, make sure you log in to your CrewAI AOP account by running this command:

<Frame>
            <img src="https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=b31a82341fb4dcd784c2ecfc1c3d576c" alt="Internal Tool Detail" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/tools-integrations-internal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?w=280&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=4b7ea6075327365b2486b405db715126 280w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?w=560&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=857f73fdff530aa6c7d801267e3cbc8a 560w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?w=840&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=2e844aa05d5c5367f9f8c14deeb78ad7 840w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?w=1100&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=fd26df60df1b528fc1644e08289738da 1100w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?w=1650&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=11d2cd7d7e38cb9cfeed2e23c4e3fe87 1650w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?w=2500&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=cba0837b7f2039f9c59cdafb81cc53b9 2500w" />
    </Frame>

<Steps>
      <Step title="Create">
        Create a new tool locally.

<Step title="Publish">
        Publish the tool to the CrewAI AOP Tool Repository.

<Step title="Install">
        Install the tool from the CrewAI AOP Tool Repository.

* Name and description
    * Visibility (Private / Public)
    * Required environment variables
    * Version history and downloads
    * Team and role access

<Frame>
            <img src="https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=1896ebecec784bc15411a0309a0cf973" alt="Internal Tool Detail" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/tool-configs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?w=280&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=fa0c14f9439ebad25474aa422f8b1bd7 280w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?w=560&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=d135d69d85a0ccb8d99403def21c8529 560w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?w=840&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=f65ac1de79956f4178a610be29c6e212 840w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?w=1100&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=3b13a8181819dbf6b07ed52f239f588a 1100w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?w=1650&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=0dc0e377941d126e06fa76cb176b70e2 1650w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?w=2500&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=53bf0fa4215eb47d5959d1c46a232db1 2500w" />
    </Frame>
  </Tab>
</Tabs>

<CardGroup cols={2}>
  <Card title="Tool Repository" href="/en/enterprise/guides/tool-repository#tool-repository" icon="toolbox">
    Create, publish, and version custom tools for your organization.
  </Card>

<Card title="Webhook Automation" href="/en/enterprise/guides/webhook-automation" icon="bolt">
    Automate workflows and integrate with external platforms and services.
  </Card>
</CardGroup>

**Examples:**

Example 1 (unknown):
```unknown
### Environment Variable Setup

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
### Usage Example

    <Tip>
      Use the new streamlined approach to integrate enterprise apps. Simply specify the app and its actions directly in the Agent configuration.
    </Tip>
```

Example 4 (unknown):
```unknown
### Filtering Tools
```

---

## Tools Overview

**URL:** llms-txt#tools-overview

**Contents:**
- **Tool Categories**
- **Quick Access**
- **Getting Started**

Source: https://docs.crewai.com/en/tools/overview

Discover CrewAI's extensive library of 40+ tools to supercharge your AI agents

CrewAI provides an extensive library of pre-built tools to enhance your agents' capabilities. From file processing to web scraping, database queries to AI services - we've got you covered.

## **Tool Categories**

<CardGroup cols={2}>
  <Card title="File & Document" icon="folder-open" href="/en/tools/file-document/overview" color="#3B82F6">
    Read, write, and search through various file formats including PDF, DOCX, JSON, CSV, and more. Perfect for document processing workflows.
  </Card>

<Card title="Web Scraping & Browsing" icon="globe" href="/en/tools/web-scraping/overview" color="#10B981">
    Extract data from websites, automate browser interactions, and scrape content at scale with tools like Firecrawl, Selenium, and more.
  </Card>

<Card title="Search & Research" icon="magnifying-glass" href="/en/tools/search-research/overview" color="#F59E0B">
    Perform web searches, find code repositories, research YouTube content, and discover information across the internet.
  </Card>

<Card title="Database & Data" icon="database" href="/en/tools/database-data/overview" color="#8B5CF6">
    Connect to SQL databases, vector stores, and data warehouses. Query MySQL, PostgreSQL, Snowflake, Qdrant, and Weaviate.
  </Card>

<Card title="AI & Machine Learning" icon="brain" href="/en/tools/ai-ml/overview" color="#EF4444">
    Generate images with DALL-E, process vision tasks, integrate with LangChain, build RAG systems, and leverage code interpreters.
  </Card>

<Card title="Cloud & Storage" icon="cloud" href="/en/tools/cloud-storage/overview" color="#06B6D4">
    Interact with cloud services including AWS S3, Amazon Bedrock, and other cloud storage and AI services.
  </Card>

<Card title="Automation" icon="bolt" href="/en/tools/automation/overview" color="#84CC16">
    Automate workflows with Apify, Composio, and other platforms to connect your agents with external services.
  </Card>

<Card title="Integrations" icon="plug" href="/en/tools/tool-integrations/overview" color="#0891B2">
    Integrate CrewAI with external systems like Amazon Bedrock and the CrewAI Automation toolkit.
  </Card>
</CardGroup>

Need a specific tool? Here are some popular choices:

<CardGroup cols={3}>
  <Card title="RAG Tool" icon="image" href="/en/tools/ai-ml/ragtool">
    Implement Retrieval-Augmented Generation
  </Card>

<Card title="Serper Dev" icon="book-atlas" href="/en/tools/search-research/serperdevtool">
    Google search API
  </Card>

<Card title="File Read" icon="file" href="/en/tools/file-document/filereadtool">
    Read any file type
  </Card>

<Card title="Scrape Website" icon="globe" href="/en/tools/web-scraping/scrapewebsitetool">
    Extract web content
  </Card>

<Card title="Code Interpreter" icon="code" href="/en/tools/ai-ml/codeinterpretertool">
    Execute Python code
  </Card>

<Card title="S3 Reader" icon="cloud" href="/en/tools/cloud-storage/s3readertool">
    Access AWS S3 files
  </Card>
</CardGroup>

## **Getting Started**

To use any tool in your CrewAI project:

1. **Import** the tool in your crew configuration
2. **Add** it to your agent's tools list
3. **Configure** any required API keys or settings

```python  theme={null}
from crewai_tools import FileReadTool, SerperDevTool

---
