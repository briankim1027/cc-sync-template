# N8N Credential Setup Guide

Complete guide for configuring credentials in n8n workflows.

## Credential Management Basics

### Storage Location
Credentials are stored in n8n's credential management system, not in workflow JSON.

**Workflow JSON Reference**:
```json
{
  "credentials": {
    "slackApi": {
      "id": "credential-uuid",
      "name": "Slack Production Account"
    }
  }
}
```

**Important**: Credential IDs must be replaced when importing workflows to different n8n instances.

---

## Common Credential Types

### 1. Slack API

**Credential Type**: `slackApi`

**Setup Steps**:
1. Go to https://api.slack.com/apps
2. Create new app or select existing
3. Navigate to OAuth & Permissions
4. Add OAuth Scopes:
   - `chat:write` - Post messages
   - `channels:read` - List channels
   - `users:read` - Read user info
5. Install app to workspace
6. Copy "Bot User OAuth Token"

**In n8n**:
1. Credentials → Add Credential → Slack
2. Paste OAuth Token
3. Test connection
4. Save as "Slack Production"

**JSON Reference**:
```json
{
  "credentials": {
    "slackApi": {
      "id": "uuid",
      "name": "Slack Production"
    }
  }
}
```

---

### 2. Gmail OAuth2

**Credential Type**: `gmailOAuth2`

**Setup Steps**:
1. Go to Google Cloud Console
2. Create project or select existing
3. Enable Gmail API
4. Create OAuth 2.0 Client ID
5. Add authorized redirect URI: `https://your-n8n-instance/rest/oauth2-credential/callback`
6. Copy Client ID and Client Secret

**In n8n**:
1. Credentials → Add Credential → Gmail OAuth2
2. Enter Client ID and Client Secret
3. Click "Connect my account"
4. Authorize Google account
5. Save as "Gmail Account"

**JSON Reference**:
```json
{
  "credentials": {
    "gmailOAuth2": {
      "id": "uuid",
      "name": "Gmail Account"
    }
  }
}
```

---

### 3. HTTP Header Authentication

**Credential Type**: `httpHeaderAuth`

**Use Case**: API keys in headers (e.g., `X-API-Key`, `Authorization`)

**Setup in n8n**:
1. Credentials → Add Credential → Header Auth
2. Name: `X-API-Key` (or custom header name)
3. Value: Your API key
4. Save as "API Service Auth"

**JSON Reference**:
```json
{
  "credentials": {
    "httpHeaderAuth": {
      "id": "uuid",
      "name": "API Service Auth"
    }
  }
}
```

**Node Configuration**:
```json
{
  "parameters": {
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "httpHeaderAuth"
  },
  "credentials": {
    "httpHeaderAuth": {
      "id": "credential-id",
      "name": "API Service Auth"
    }
  }
}
```

---

### 4. PostgreSQL / MySQL

**Credential Type**: `postgres` or `mySql`

**Setup in n8n**:
1. Credentials → Add Credential → Postgres/MySQL
2. Host: database hostname or IP
3. Port: 5432 (Postgres) / 3306 (MySQL)
4. Database: database name
5. User: database username
6. Password: database password
7. Optional: SSL certificate
8. Test connection
9. Save as "Production Database"

**JSON Reference**:
```json
{
  "credentials": {
    "postgres": {
      "id": "uuid",
      "name": "Production Database"
    }
  }
}
```

---

### 5. Google Sheets OAuth2

**Credential Type**: `googleSheetsOAuth2Api`

**Setup Steps**:
1. Google Cloud Console → Enable Google Sheets API
2. Create OAuth 2.0 credentials
3. Add redirect URI: n8n callback URL
4. Download credentials JSON

**In n8n**:
1. Credentials → Add Credential → Google Sheets OAuth2
2. Enter Client ID and Secret
3. Authenticate with Google account
4. Grant sheets permissions
5. Save as "Google Sheets Access"

**JSON Reference**:
```json
{
  "credentials": {
    "googleSheetsOAuth2Api": {
      "id": "uuid",
      "name": "Google Sheets Access"
    }
  }
}
```

---

### 6. Basic Authentication

**Credential Type**: `httpBasicAuth`

**Use Case**: Username/password authentication

**Setup in n8n**:
1. Credentials → Add Credential → Basic Auth
2. Username: your username
3. Password: your password
4. Save as "Service Basic Auth"

**JSON Reference**:
```json
{
  "credentials": {
    "httpBasicAuth": {
      "id": "uuid",
      "name": "Service Basic Auth"
    }
  }
}
```

---

## Credential Best Practices

### 1. Naming Conventions

Use descriptive names indicating:
- Service name
- Environment (dev/staging/prod)
- Account type

**Examples**:
- ✅ "Slack Production - Sales Channel"
- ✅ "Gmail - Support Team"
- ✅ "PostgreSQL - Production DB"
- ❌ "My Credential"
- ❌ "Test"

### 2. Environment Separation

Create separate credentials for each environment:

```
Development:
- "Slack Dev"
- "Gmail Dev"
- "PostgreSQL Dev"

Production:
- "Slack Production"
- "Gmail Production"
- "PostgreSQL Production"
```

### 3. Least Privilege

Grant minimum required permissions:

**Slack Example**:
- ✅ Only `chat:write` if posting messages
- ❌ Don't grant `admin` scope unnecessarily

**Database Example**:
- ✅ Read-only user for reporting workflows
- ❌ Don't use admin account for queries

### 4. Rotation Schedule

Regularly rotate credentials:
- API keys: Every 90 days
- Database passwords: Every 180 days
- OAuth tokens: Refresh as needed

### 5. Secret Management

**Never**:
- ❌ Hardcode credentials in workflow nodes
- ❌ Share credential IDs across teams
- ❌ Expose credentials in logs

**Always**:
- ✅ Use n8n credential manager
- ✅ Limit access to credential management
- ✅ Audit credential usage

---

## Credential Migration

When moving workflows between n8n instances:

### Step 1: Export Workflow
Workflow JSON contains credential references but not actual secrets.

### Step 2: Identify Required Credentials
```json
{
  "credentials": {
    "slackApi": {
      "id": "old-uuid",
      "name": "Slack Production"
    },
    "gmailOAuth2": {
      "id": "old-uuid",
      "name": "Gmail Account"
    }
  }
}
```

### Step 3: Create Credentials in Target Instance
Manually create each credential in new n8n instance.

### Step 4: Update Workflow
After import, n8n will prompt to select credentials for each node.

---

## Troubleshooting

### Issue: "Credential not found"

**Cause**: Referenced credential doesn't exist

**Solution**:
1. Check credential name in workflow JSON
2. Create missing credential in n8n
3. Re-select credential in node configuration

### Issue: Authentication Failed

**Cause**: Invalid or expired credentials

**Solution**:
1. Test credential connection
2. Verify API key/token is valid
3. Check permission scopes
4. Refresh OAuth tokens if needed

### Issue: OAuth Connection Fails

**Cause**: Redirect URI mismatch

**Solution**:
1. Verify redirect URI in OAuth app settings
2. Format: `https://your-n8n.com/rest/oauth2-credential/callback`
3. Ensure HTTPS is used
4. Check n8n base URL setting

---

## Security Checklist

- [ ] All credentials use n8n credential manager (no hardcoded secrets)
- [ ] Credentials follow naming conventions
- [ ] Separate dev/production credentials created
- [ ] Minimum required permissions granted
- [ ] Credential rotation schedule established
- [ ] Access to credential management restricted
- [ ] Credentials tested and validated
- [ ] Documentation maintained for credential purposes
