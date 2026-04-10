# N8N Production Deployment Guide

Comprehensive guide for deploying n8n workflows to production environments with operational best practices.

## Pre-Deployment Checklist

### Workflow Validation
- [ ] All nodes properly configured
- [ ] Credentials assigned and tested
- [ ] Error handling implemented
- [ ] Data validation in place
- [ ] Output formats verified
- [ ] No hardcoded values
- [ ] Expressions syntax validated

### Testing Completed
- [ ] Unit tests (individual nodes)
- [ ] Integration tests (full workflow)
- [ ] Error path testing
- [ ] Load testing (if applicable)
- [ ] Security testing
- [ ] Credential validation
- [ ] End-to-end testing in staging

### Documentation
- [ ] Workflow README created
- [ ] Runbook documented
- [ ] Dependencies listed
- [ ] Team contacts defined
- [ ] SLA documented
- [ ] Rollback plan prepared

---

## Environment Setup

### Production n8n Configuration

**Environment Variables**:
```bash
# Core Settings
N8N_HOST=production.n8n.company.com
N8N_PORT=5678
N8N_PROTOCOL=https
NODE_ENV=production

# Security
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=<secure-password>

# Database
DB_TYPE=postgresdb
DB_POSTGRESDB_HOST=postgres.company.com
DB_POSTGRESDB_PORT=5432
DB_POSTGRESDB_DATABASE=n8n_production
DB_POSTGRESDB_USER=n8n_user
DB_POSTGRESDB_PASSWORD=<secure-password>

# Execution
EXECUTIONS_DATA_SAVE_ON_ERROR=all
EXECUTIONS_DATA_SAVE_ON_SUCCESS=all
EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=true
EXECUTIONS_DATA_MAX_AGE=336  # 14 days

# Timezone
GENERIC_TIMEZONE=America/New_York

# Webhook
WEBHOOK_URL=https://production.n8n.company.com/
```

### Infrastructure Requirements

**Minimum Production Specs**:
- CPU: 4 cores
- RAM: 8GB
- Storage: 50GB SSD
- Network: Stable internet connection

**Recommended Production Specs**:
- CPU: 8+ cores
- RAM: 16GB+
- Storage: 100GB+ SSD
- Load Balancer: For high availability
- Database: Dedicated PostgreSQL server

---

## Deployment Strategies

### 1. Blue-Green Deployment

**Setup**:
```
Production (Blue):  active workflows
Staging (Green):    new version
```

**Process**:
1. Deploy new version to Green
2. Run smoke tests
3. Redirect 10% traffic to Green
4. Monitor for errors
5. Gradually increase to 100%
6. Keep Blue as rollback option

### 2. Canary Deployment

**Process**:
1. Deploy to small subset of instances
2. Monitor metrics closely
3. Gradually roll out to more instances
4. Full rollout if successful

### 3. Rolling Update

**Process**:
1. Update one instance at a time
2. Verify health before next
3. Continue until all updated
4. Maintain service availability

---

## Security Best Practices

### 1. Network Security

**HTTPS Only**:
```nginx
# Nginx config
server {
    listen 443 ssl http2;
    server_name n8n.company.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;

    location / {
        proxy_pass http://localhost:5678;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

**Firewall Rules**:
```bash
# Allow HTTPS only
ufw allow 443/tcp
ufw deny 5678/tcp  # Block direct n8n access
```

### 2. Authentication

**Basic Auth** (minimum):
```bash
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=<strong-password>
```

**SSO Integration** (recommended):
- OAuth2 with company identity provider
- SAML integration
- Multi-factor authentication

### 3. Webhook Security

**Authentication**:
```json
{
  "parameters": {
    "authentication": "headerAuth",
    "options": {}
  },
  "credentials": {
    "httpHeaderAuth": {
      "id": "webhook-auth-id",
      "name": "Webhook API Key"
    }
  }
}
```

**IP Whitelisting**:
```nginx
# Nginx config
location /webhook/customer-signup {
    allow 203.0.113.0/24;  # Trusted IPs
    deny all;
    proxy_pass http://localhost:5678;
}
```

### 4. Data Protection

**Encrypt Sensitive Data**:
```bash
# n8n encryption key
N8N_ENCRYPTION_KEY=<generate-secure-key>
```

**Database Encryption**:
```sql
-- PostgreSQL with encryption
ALTER DATABASE n8n_production SET encrypt = on;
```

**Audit Logging**:
```bash
# Enable audit logs
N8N_LOG_LEVEL=info
N8N_LOG_OUTPUT=file
N8N_LOG_FILE_LOCATION=/var/log/n8n/
```

---

## Monitoring and Alerting

### 1. Health Checks

**Endpoint**:
```
GET /healthz
```

**Monitoring Service**:
```yaml
# Prometheus config
scrape_configs:
  - job_name: 'n8n'
    static_configs:
      - targets: ['n8n.company.com:5678']
    metrics_path: '/metrics'
    scrape_interval: 30s
```

### 2. Metrics to Monitor

**System Metrics**:
- CPU usage (< 80%)
- Memory usage (< 85%)
- Disk usage (< 90%)
- Network latency (< 100ms)

**Application Metrics**:
- Workflow execution count
- Success rate (> 99%)
- Average execution time
- Failed execution count
- Active webhook count

**Business Metrics**:
- Processed transactions
- API call volumes
- SLA compliance
- Cost per execution

### 3. Alerting Rules

**Critical Alerts** (immediate response):
```yaml
alerts:
  - name: WorkflowFailureRate
    condition: failure_rate > 5%
    action: page_oncall

  - name: SystemDown
    condition: health_check_fails
    action: page_oncall + create_incident

  - name: DatabaseConnection
    condition: db_connection_lost
    action: page_oncall + failover
```

**Warning Alerts** (attention needed):
```yaml
alerts:
  - name: SlowExecution
    condition: avg_execution_time > 30s
    action: slack_alert

  - name: HighCPU
    condition: cpu > 80%
    action: slack_alert + email
```

### 4. Logging Strategy

**Log Levels**:
- ERROR: Failed executions, system errors
- WARN: Retries, slow performance
- INFO: Execution starts/completions
- DEBUG: Detailed execution data (dev only)

**Log Aggregation**:
```yaml
# Filebeat config
filebeat.inputs:
  - type: log
    paths:
      - /var/log/n8n/*.log
    fields:
      service: n8n
      environment: production

output.elasticsearch:
  hosts: ["elasticsearch:9200"]
```

**Log Retention**:
- ERROR logs: 90 days
- WARN logs: 60 days
- INFO logs: 30 days
- DEBUG logs: 7 days (if enabled)

---

## Backup and Recovery

### 1. Database Backups

**Automated Backups**:
```bash
#!/bin/bash
# Daily PostgreSQL backup
BACKUP_DIR=/backups/n8n
DATE=$(date +%Y%m%d_%H%M%S)

pg_dump -h postgres.company.com \
        -U n8n_user \
        -d n8n_production \
        -F c \
        -f $BACKUP_DIR/n8n_prod_$DATE.dump

# Retain 30 days of backups
find $BACKUP_DIR -name "*.dump" -mtime +30 -delete
```

**Backup Schedule**:
- Full backup: Daily at 2 AM
- Incremental: Every 6 hours
- Retention: 30 days
- Offsite copy: Weekly to S3

### 2. Workflow Backup

**Export Workflows**:
```bash
#!/bin/bash
# Export all workflows
n8n export:workflow --all --output=/backups/workflows/

# Version control
cd /backups/workflows
git add .
git commit -m "Backup $(date +%Y-%m-%d)"
git push
```

### 3. Disaster Recovery

**RTO (Recovery Time Objective)**: 1 hour
**RPO (Recovery Point Objective)**: 6 hours

**Recovery Steps**:
1. Provision new n8n instance
2. Restore database from latest backup
3. Import workflows from git
4. Reconfigure credentials
5. Update DNS/load balancer
6. Verify critical workflows
7. Resume normal operations

---

## Performance Optimization

### 1. Database Optimization

**PostgreSQL Tuning**:
```sql
-- Increase connection pool
max_connections = 200

-- Optimize memory
shared_buffers = 4GB
effective_cache_size = 12GB
work_mem = 64MB

-- Improve query performance
random_page_cost = 1.1
effective_io_concurrency = 200

-- Index executions table
CREATE INDEX idx_executions_finished ON executions(finished);
CREATE INDEX idx_executions_workflow ON executions(workflowId);
```

### 2. Workflow Optimization

**Best Practices**:
- Minimize node count (combine operations)
- Use parallel execution where possible
- Implement pagination for large datasets
- Cache frequently accessed data
- Set appropriate timeouts
- Limit retry attempts

**Example Optimization**:
```
Before (Sequential - 30s):
[API Call 1] → [API Call 2] → [API Call 3]

After (Parallel - 10s):
     → [API Call 1] →
[...]→ [API Call 2] → [Merge]
     → [API Call 3] →
```

### 3. Resource Scaling

**Horizontal Scaling**:
```yaml
# Docker Compose with multiple workers
services:
  n8n-1:
    image: n8nio/n8n
    environment:
      - EXECUTIONS_PROCESS=own

  n8n-2:
    image: n8nio/n8n
    environment:
      - EXECUTIONS_PROCESS=own

  load-balancer:
    image: nginx
    depends_on:
      - n8n-1
      - n8n-2
```

**Vertical Scaling**:
- Increase CPU cores for compute-heavy workflows
- Add RAM for large dataset processing
- Upgrade to SSD for faster database access

---

## Operational Runbooks

### Runbook: Handle Failed Workflow

**Symptoms**: Workflow execution failed

**Steps**:
1. Check execution logs in n8n UI
2. Identify failing node
3. Review error message
4. Check if transient error (network, API limit)
5. If transient: Retry execution
6. If persistent: Investigate node configuration
7. Fix issue and re-run
8. Document incident

### Runbook: High CPU Usage

**Symptoms**: CPU > 80% sustained

**Steps**:
1. Check running workflows: `/executions/current`
2. Identify resource-intensive workflows
3. Check for infinite loops
4. Review recent workflow changes
5. Temporarily disable problematic workflows
6. Optimize or scale as needed
7. Re-enable with monitoring

### Runbook: Database Connection Lost

**Symptoms**: Cannot connect to PostgreSQL

**Steps**:
1. Check database server status
2. Verify network connectivity
3. Check connection pool exhaustion
4. Restart n8n if needed
5. Investigate root cause
6. Implement fix
7. Update monitoring alerts

---

## Compliance and Audit

### GDPR Compliance

**Data Retention**:
```bash
# Auto-delete old executions
N8N_EXECUTIONS_DATA_PRUNE=true
N8N_EXECUTIONS_DATA_MAX_AGE=90  # days
```

**Data Access**:
- Log all workflow access
- Implement role-based access control
- Provide data export capability
- Enable data deletion on request

### SOC 2 Requirements

**Access Control**:
- Multi-factor authentication
- Role-based permissions
- Audit logging enabled
- Regular access reviews

**Change Management**:
- Version control for workflows
- Code review process
- Testing in staging first
- Documented deployment process

### Audit Logging

**Log All**:
- Workflow modifications
- Credential changes
- User access
- Execution history
- Configuration changes

---

## Cost Optimization

### Resource Monitoring

**Track Costs By**:
- Workflow execution count
- API call volumes
- Storage usage
- Compute resources

### Optimization Strategies

1. **Reduce Execution Frequency**:
   - Batch operations instead of real-time
   - Increase schedule intervals where acceptable

2. **Optimize API Calls**:
   - Cache API responses
   - Batch requests
   - Use webhooks instead of polling

3. **Clean Up**:
   - Archive old workflows
   - Delete test workflows in production
   - Prune execution history

4. **Right-Size Infrastructure**:
   - Monitor actual resource usage
   - Scale down if over-provisioned
   - Use auto-scaling for variable loads

---

## Deployment Checklist

### Pre-Deployment
- [ ] All tests passing in staging
- [ ] Code review completed
- [ ] Documentation updated
- [ ] Credentials configured
- [ ] Backup taken
- [ ] Rollback plan ready
- [ ] Team notified
- [ ] Maintenance window scheduled (if needed)

### Deployment
- [ ] Deploy to production
- [ ] Run smoke tests
- [ ] Verify critical workflows
- [ ] Check monitoring dashboards
- [ ] Verify webhook endpoints
- [ ] Test error handling

### Post-Deployment
- [ ] Monitor for 1 hour minimum
- [ ] Check error rates
- [ ] Verify SLA metrics
- [ ] Update documentation
- [ ] Notify stakeholders of completion
- [ ] Close deployment ticket
- [ ] Conduct retrospective (if issues occurred)
