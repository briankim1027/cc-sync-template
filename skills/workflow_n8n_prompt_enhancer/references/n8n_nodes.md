# N8N Common Nodes Reference

This reference documents the most commonly used n8n nodes and their typical configurations for workflow automation.

## Trigger Nodes

### Webhook
**Purpose**: Receive HTTP requests to start workflows

**Common Configuration**:
```
- Method: POST/GET/PUT/DELETE
- Authentication: None/Header Auth/Query Auth/Basic Auth
- Response Mode: When last node finishes/Immediately
- Response Data: Last node/First entry/All entries
```

**Use Cases**:
- API integrations
- External system notifications
- Form submissions
- Third-party service webhooks

**Data Format**:
```json
{
  "headers": {},
  "params": {},
  "query": {},
  "body": {}
}
```

### Schedule Trigger
**Purpose**: Start workflows on time-based schedules

**Common Configuration**:
```
- Trigger Times: Cron Expression
- Common Patterns:
  - "0 9 * * 1-5" → Weekdays at 9am
  - "0 */6 * * *" → Every 6 hours
  - "0 0 * * 0" → Every Sunday at midnight
```

**Use Cases**:
- Daily reports
- Weekly backups
- Periodic data synchronization
- Scheduled notifications

### Manual Trigger
**Purpose**: Manually start workflows for testing or one-off operations

**Use Cases**:
- Testing workflows
- Admin operations
- On-demand tasks

### Form Trigger
**Purpose**: Display a form and trigger workflow on submission

**Common Configuration**:
```
- Form Fields: Text/Number/Email/Date/Dropdown
- Submit Button Text: Custom text
- Redirect URL: Optional post-submission redirect
```

## Communication Nodes

### Gmail
**Purpose**: Send emails via Gmail

**Common Configuration**:
```
- From Email: sender@domain.com
- To Email: {{$json["email"]}} (dynamic)
- Subject: Can include expressions
- Email Type: HTML or Text
- Attachments: Optional binary data
```

**Common Expressions**:
- `{{$json["email"]}}` - Dynamic recipient
- `{{$json["name"]}}` - Personalization
- `{{new Date().toLocaleDateString()}}` - Current date

### SMTP
**Purpose**: Send emails via custom SMTP server

**Common Configuration**:
```
- Host: smtp.server.com
- Port: 587/465/25
- Secure: SSL/TLS
- From Email: noreply@domain.com
```

### Slack
**Purpose**: Send messages to Slack channels or users

**Common Configuration**:
```
- Channel: #channel-name or @username
- Text: Message content with markdown
- Blocks: Rich message formatting
- Attachments: Links, images
```

**Message Format**:
```
🎉 New Customer Signup!
Name: {{$json["name"]}}
Email: {{$json["email"]}}
Plan: {{$json["plan"]}}
```

### Discord
**Purpose**: Send messages to Discord channels

**Common Configuration**:
```
- Webhook URL: Discord webhook endpoint
- Content: Message text
- Embeds: Rich embeds with fields
```

### Telegram
**Purpose**: Send messages via Telegram bot

**Common Configuration**:
```
- Chat ID: Target chat/user
- Message: Text with markdown/HTML
- Reply Markup: Inline keyboards
```

## Data Processing Nodes

### Set
**Purpose**: Set/modify JSON data in the workflow

**Common Operations**:
```
- Add field: name = "value"
- Copy field: newField = {{$json["oldField"]}}
- Transform: upperName = {{$json["name"].toUpperCase()}}
- Remove field: Delete specific fields
```

**Use Cases**:
- Data transformation
- Field renaming
- Adding computed fields
- Removing sensitive data

### Code (JavaScript)
**Purpose**: Execute custom JavaScript for complex logic

**Common Configuration**:
```javascript
// Access input data
const items = $input.all();

// Process each item
for (const item of items) {
  item.json.fullName = `${item.json.firstName} ${item.json.lastName}`;
  item.json.timestamp = new Date().toISOString();
}

// Return modified items
return items;
```

**Use Cases**:
- Complex data transformations
- Custom business logic
- Date/time calculations
- String manipulation

### Function
**Purpose**: Execute JavaScript functions on items

**Common Patterns**:
```javascript
// Filter items
return items.filter(item => item.json.active === true);

// Map transformations
return items.map(item => ({
  json: {
    id: item.json.userId,
    email: item.json.email.toLowerCase()
  }
}));

// Aggregate data
const total = items.reduce((sum, item) => sum + item.json.amount, 0);
```

### Item Lists
**Purpose**: Split/aggregate items for processing

**Operations**:
- Split Out: Convert single item with array into multiple items
- Aggregate: Combine multiple items into single item with array

**Use Cases**:
- Processing batch data
- Combining results
- Iterating over arrays

## Logic & Flow Control Nodes

### IF
**Purpose**: Conditional routing based on logic

**Common Conditions**:
```
- String: equals/contains/starts with/ends with
- Number: =/</>/<=/>=/!=
- Boolean: is true/false
- Exists: field exists/doesn't exist
```

**Example**:
```
Condition: {{$json["status"]}} equals "active"
→ True: Send welcome email
→ False: Send re-activation email
```

### Switch
**Purpose**: Route to multiple paths based on value

**Common Configuration**:
```
Mode: Rules/Expression
Rules:
  - Output 1: status = "new"
  - Output 2: status = "active"
  - Output 3: status = "churned"
Fallback: Default output
```

### Merge
**Purpose**: Combine data from multiple branches

**Modes**:
- Append: Combine all items sequentially
- Keep Key Matches: Match items by key field
- Merge By Index: Match items by position
- Merge By Position: Combine items at same index
- Multiplex: Create combinations

**Use Cases**:
- Combining parallel operations
- Data enrichment from multiple sources
- Joining datasets

### Wait
**Purpose**: Pause workflow execution

**Modes**:
- After Time Interval: Wait fixed duration (5 minutes, 1 hour)
- At Specific Time: Wait until date/time
- On Webhook Call: Wait for external trigger

**Use Cases**:
- Rate limiting
- Delayed notifications
- Waiting for external processes

## Data Storage Nodes

### Google Sheets
**Purpose**: Read/write Google Sheets data

**Common Operations**:
- Append Row: Add new row with data
- Update Row: Modify existing row by ID/range
- Lookup: Find rows matching criteria
- Read: Get all rows or specific range

**Common Configuration**:
```
- Spreadsheet ID: From URL
- Sheet Name: "Sheet1"
- Columns: Map JSON fields to sheet columns
```

**Use Cases**:
- Logging workflow results
- Reading configuration data
- Collecting form submissions
- Data export

### Airtable
**Purpose**: Interact with Airtable bases

**Common Operations**:
- Create: Add new records
- Update: Modify existing records
- List: Query records with filters
- Get: Retrieve specific record

### HTTP Request
**Purpose**: Make API calls to external services

**Common Configuration**:
```
- Method: GET/POST/PUT/DELETE/PATCH
- URL: API endpoint (can include expressions)
- Authentication: None/Basic/OAuth2/API Key
- Headers: Content-Type, Authorization
- Body: JSON/Form/Raw
```

**Common Headers**:
```
Content-Type: application/json
Authorization: Bearer {{$credentials.token}}
Accept: application/json
```

**Use Cases**:
- REST API integration
- External service calls
- Webhooks to other systems
- Data fetching

### Database Nodes
**Purpose**: Interact with databases (PostgreSQL, MySQL, MongoDB)

**Common Operations**:
- Insert: Add new records
- Update: Modify existing records
- Find: Query with filters
- Execute Query: Run custom SQL/queries

## Utility Nodes

### Error Trigger
**Purpose**: Handle errors from other workflows

**Configuration**:
```
- Trigger On: Error in any workflow/specific workflow
```

**Use Cases**:
- Centralized error handling
- Error notifications
- Retry mechanisms
- Error logging

### Respond to Webhook
**Purpose**: Send custom response to webhook trigger

**Common Configuration**:
```
- Response Code: 200/201/400/500
- Response Body: JSON/Text/HTML
- Headers: Custom response headers
```

**Use Cases**:
- API endpoints
- Webhook acknowledgments
- Custom error responses

### Stop and Error
**Purpose**: Halt workflow execution with error

**Configuration**:
```
- Error Message: Custom error description
```

**Use Cases**:
- Validation failures
- Critical errors
- Preventing invalid operations

### Read/Write Files from Disk
**Purpose**: File system operations

**Operations**:
- Read: Load file contents
- Write: Save binary/text data
- Delete: Remove files

### HTML Extract
**Purpose**: Parse HTML and extract data

**Common Configuration**:
```
- Extraction Mode: CSS Selector/XPath
- Selector: .class-name, #id, tag[attr]
```

### XML
**Purpose**: Parse XML data to JSON

**Use Cases**:
- SOAP API responses
- RSS feeds
- XML file processing

## Node Combination Patterns

### Data Enrichment Pattern
```
Trigger → Fetch User Data (HTTP) → Fetch Account Data (Database)
→ Merge → Transform → Send Notification
```

### Error Handling Pattern
```
Main Flow → [Try] Operation → Success Path
          → [Error Trigger] → Log Error → Notify Admin → Retry/Fallback
```

### Batch Processing Pattern
```
Schedule → Fetch Items (API) → Split Out → Process Each
→ Aggregate Results → Store (Database) → Summary Email
```

### Conditional Routing Pattern
```
Trigger → Validate → IF Node
                    → True: Process A → Email Success
                    → False: Process B → Email Failure
```

## Best Practices

1. **Use meaningful node names**: Rename nodes to describe their purpose
2. **Add notes**: Document complex logic with sticky notes
3. **Handle errors**: Always include error handling for external operations
4. **Validate input**: Check data before processing
5. **Use expressions wisely**: Keep expressions simple and readable
6. **Test incrementally**: Test each node before building the full workflow
7. **Use credentials**: Store API keys and passwords in n8n credentials
8. **Enable workflow**: Remember to activate workflows after building
