# Agent Delegation Rules

**Purpose**: Define when and how to delegate tasks to specialized subagents.

---

## 🤖 When to Delegate to Agents

### General Principles

**Delegate when:**

- ✅ Task requires specialized expertise
- ✅ Task is clearly scoped and isolated
- ✅ Agent has specific tools/knowledge for the task
- ✅ Task would benefit from focused attention

**Don't delegate when:**

- ❌ Task is too vague or undefined
- ❌ Requires context from multiple domains
- ❌ Simple task that takes more time to delegate
- ❌ Continuous back-and-forth needed

---

## 👥 Available Agents & When to Use

### Architecture & Design

#### `system-architect`

**Use for:**

- System architecture design decisions
- Technology stack selection
- Scalability planning
- Infrastructure design
- Microservices architecture

**Example:**

```
@system-architect Design a scalable architecture for a social media platform
with 1M+ users, focusing on real-time messaging and feed generation.
```

#### `frontend-architect` / `backend-architect`

**Use for:**

- Layer-specific architecture decisions
- Design patterns for frontend/backend
- State management architecture
- API design

**Example:**

```
@backend-architect Design API architecture for multi-tenant SaaS application
with row-level security and efficient query patterns.
```

---

### Development

#### `tdd-guide`

**Use for:**

- Implementing features using TDD
- Creating test suites
- Improving test coverage
- Test strategy planning

**Example:**

```
@tdd-guide Implement user registration feature using TDD methodology
```

#### `python-expert` / `frontend-engineer`

**Use for:**

- Language-specific best practices
- Framework-specific implementation
- Optimization for specific tech stack

**Example:**

```
@python-expert Optimize this data processing pipeline using Python best practices
```

---

### Quality & Security

#### `code-reviewer`

**Use for:**

- Code quality review
- Best practices verification
- Code smell detection
- Maintainability assessment

**Example:**

```
@code-reviewer Review the authentication module for code quality and best practices
```

#### `security-engineer`

**Use for:**

- Security vulnerability assessment
- Authentication/authorization review
- Input validation review
- Secure coding practices

**Example:**

```
@security-engineer Review this payment processing code for security vulnerabilities
```

#### `quality-engineer`

**Use for:**

- Test strategy
- Quality metrics
- QA processes
- Bug prevention strategies

---

### Performance & Optimization

#### `performance-engineer`

**Use for:**

- Performance optimization
- Profiling and bottleneck detection
- Scalability improvements
- Resource optimization

**Example:**

```
@performance-engineer Analyze and optimize this database query that's causing slow page loads
```

#### `refactoring-expert`

**Use for:**

- Code refactoring
- Removing technical debt
- Improving code structure
- Dead code removal

**Example:**

```
@refactoring-expert Refactor this 800-line component into smaller, reusable pieces
```

---

### Documentation & Analysis

#### `technical-writer` / `document-writer`

**Use for:**

- API documentation
- User guides
- Architecture documentation
- README files

**Example:**

```
@technical-writer Create comprehensive API documentation for the user service
```

#### `requirements-analyst`

**Use for:**

- Analyzing requirements
- Clarifying specifications
- Breaking down features
- User story creation

**Example:**

```
@requirements-analyst Analyze these requirements and create detailed user stories
with acceptance criteria
```

#### `root-cause-analyst`

**Use for:**

- Debugging complex issues
- Root cause analysis
- Post-mortem analysis
- Systematic problem solving

**Example:**

```
@root-cause-analyst Investigate why users are experiencing intermittent login failures
```

---

## 📋 Agent Delegation Best Practices

### 1. Provide Clear Context

**❌ BAD:**

```
@code-reviewer Review my code
```

**✅ GOOD:**

```
@code-reviewer Review the user authentication module (src/auth/) focusing on:
1. Security best practices
2. Error handling
3. Code organization
4. Test coverage
```

### 2. Define Scope and Constraints

**Include:**

- Specific files/modules
- Constraints (time, resources, dependencies)
- Success criteria
- What NOT to change

**Example:**

```
@refactoring-expert Refactor the payment processing module:
- Keep existing API interface unchanged
- Focus on improving testability
- Don't change the database schema
- Maintain backward compatibility
```

### 3. Specify Expected Output

**Example:**

```
@system-architect Design authentication system. Provide:
1. Architecture diagram
2. Technology recommendations
3. Security considerations
4. Scalability plan
```

### 4. Review Agent Output

**Always:**

- ✅ Review agent suggestions before applying
- ✅ Verify recommendations fit your context
- ✅ Test proposed changes
- ✅ Adapt to your specific needs

**Never:**

- ❌ Blindly apply all agent suggestions
- ❌ Skip testing agent-generated code
- ❌ Ignore project-specific constraints

---

## 🎯 Agent Scope Guidelines

### Limit Agent Scope

**Each agent should:**

- ✅ Focus on single domain/task
- ✅ Have clear success criteria
- ✅ Complete work independently
- ✅ Have limited tool access

### Agent Tool Access

**Typical tool access by agent type:**

- **Read-only Agents** (analysts, reviewers)
  - Read, Grep, Search
- **Code Generation Agents** (developers, architects)
  - Read, Edit, Create, Bash
- **Full-Access Agents** (orchestrators)
  - All tools

---

## 🔄 Agent Orchestration

### Sequential Delegation

**When one agent's output feeds another:**

```
1. @requirements-analyst Analyze user story and create specs
2. @system-architect Design system based on specs
3. @tdd-guide Implement features using TDD
4. @code-reviewer Review implementation
5. @security-engineer Security audit
```

### Parallel Delegation

**When tasks are independent:**

```
Parallel tasks:
- @frontend-engineer Build UI components
- @backend-engineer Build API endpoints
- @technical-writer Create documentation
```

---

## 🛠️ Model Selection for Agents

### Agent Performance Tiers

**opus** - Complex reasoning, critical decisions

- `system-architect`
- `security-engineer`
- `tdd-guide`
- `code-reviewer`

**sonnet** - Balanced performance, general tasks

- `frontend-engineer`
- `backend-engineer`
- `refactoring-expert`
- `technical-writer`

**haiku** - Fast, simple tasks

- Simple code generation
- Documentation formatting
- Basic analysis

### Example Agent Definition

```markdown
---
name: security-engineer
description: Security vulnerability assessment and secure coding practices
tools: Read, Grep, Bash
model: opus  ← Use opus for critical security work
---

You are a senior security engineer specializing in...
```

---

## ⚠️ Common Delegation Mistakes

### 1. Over-Delegation

**❌ DON'T:**

```
@code-reviewer Review this 2-line function
```

**Instead:** Review simple code yourself

### 2. Under-Specification

**❌ DON'T:**

```
@system-architect Design a system
```

**Instead:** Provide requirements, constraints, scale

### 3. Wrong Agent

**❌ DON'T:**

```
@frontend-engineer Review database schema
```

**Instead:** Choose agent matching expertise

### 4. No Review

**❌ DON'T:** Apply agent output without review
**Instead:** Always review and test suggestions

---

## ✅ Agent Delegation Checklist

Before delegating:

- [ ] Task is clearly defined
- [ ] Appropriate agent selected
- [ ] Context provided
- [ ] Scope and constraints specified
- [ ] Success criteria defined
- [ ] Expected output format described

After agent completes:

- [ ] Review output thoroughly
- [ ] Verify suggestions fit project
- [ ] Test any code changes
- [ ] Adapt as needed
- [ ] Document decisions

---

## 🎓 Learning from Agents

### Extract Patterns

**When agents solve problems:**

- ✅ Document the approach
- ✅ Save to LEARNINGS.md
- ✅ Create reusable templates
- ✅ Update project guidelines

**Example:**

```
Agent @security-engineer suggested using bcrypt with cost factor 12.
→ Add to security guidelines
→ Create utility function
→ Document in LEARNINGS.md
```

---

## 📊 Agent Effectiveness

### Measure Agent Value

**Track:**

- Time saved
- Quality improvements
- Issues prevented
- Knowledge transferred

**Optimize:**

- Refine agent prompts
- Adjust tool access
- Update delegation criteria
- Improve context provision

---

## 🔗 Integration with Other Rules

**Agents should follow:**

- [security.md](file:///C:/Users/c/.claude/rules/security.md) - Security rules
- [coding-style.md](file:///C:/Users/c/.claude/rules/coding-style.md) - Code style
- [testing.md](file:///C:/Users/c/.claude/rules/testing.md) - Testing requirements
- [git-workflow.md](file:///C:/Users/c/.claude/rules/git-workflow.md) - Git conventions

---

## 📚 Resources

- Agent definitions: `~/.claude/agents/`
- Agent templates: Check existing agents for examples
- Delegation patterns: Document successful patterns in LEARNINGS.md

---

**Remember**: Agents are tools. Use them strategically, provide clear context, and always review their output.
