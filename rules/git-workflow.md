# Git Workflow Rules

**Purpose**: Maintain clean Git history and streamlined collaboration.

---

## 📝 Commit Message Format

### Conventional Commits

**Format**: `type(scope): description`

```
type(scope): short description

Optional longer description explaining the change in detail.

Optional footer with issue references.
```

### Commit Types

| Type       | Description             | Example                                     |
| ---------- | ----------------------- | ------------------------------------------- |
| `feat`     | New feature             | `feat(auth): add OAuth login`               |
| `fix`      | Bug fix                 | `fix(api): handle null user response`       |
| `docs`     | Documentation only      | `docs(readme): update installation steps`   |
| `style`    | Code style/formatting   | `style(ui): fix button alignment`           |
| `refactor` | Code restructuring      | `refactor(utils): simplify date formatting` |
| `test`     | Adding/updating tests   | `test(auth): add login validation tests`    |
| `chore`    | Maintenance tasks       | `chore(deps): update dependencies`          |
| `perf`     | Performance improvement | `perf(api): optimize database queries`      |
| `ci`       | CI/CD changes           | `ci(github): add test workflow`             |
| `build`    | Build system changes    | `build(webpack): update config`             |
| `revert`   | Revert previous commit  | `revert: feat(auth): add OAuth login`       |

### Scope (Optional)

Indicates the affected area:

- `auth` - Authentication
- `api` - API routes
- `ui` - User interface
- `db` - Database
- `config` - Configuration

### Description

- ✅ Use imperative mood ("add" not "added" or "adds")
- ✅ Start with lowercase
- ✅ No period at the end
- ✅ Max 50 characters
- ✅ Be specific and concise

**Examples:**

```bash
# ✅ GOOD
feat(auth): add password reset functionality
fix(api): prevent race condition in user creation
docs(contributing): add code review guidelines
test(checkout): add payment flow tests
refactor(utils): extract validation logic

# ❌ BAD
Updated stuff
fix bug
Added new feature
fixed the login page
```

### Body (Optional)

- Wrap at 72 characters
- Explain **what** and **why**, not **how**
- Separate from subject with blank line

**Example:**

```
feat(auth): add two-factor authentication

Implements TOTP-based 2FA to improve account security.
Users can enable 2FA in account settings and use
authenticator apps like Google Authenticator.

Closes #123
```

### Footer (Optional)

Reference issues, breaking changes:

```
feat(api): update user endpoint response format

BREAKING CHANGE: User endpoint now returns `userId` instead of `id`

Closes #456
```

---

## 🌿 Branch Strategy

### Branch Naming Convention

**Format**: `type/short-description`

**Types:**

- `feature/` - New features
- `fix/` - Bug fixes
- `hotfix/` - Emergency fixes
- `refactor/` - Code refactoring
- `docs/` - Documentation
- `test/` - Test-related changes
- `chore/` - Maintenance

**Examples:**

```bash
# ✅ GOOD
feature/oauth-login
fix/user-avatar-upload
hotfix/payment-processing-error
refactor/api-error-handling
docs/update-readme
test/add-e2e-tests

# ❌ BAD
new-feature
john-working-branch
test
fix
```

### Main Branches

#### `main` (or `master`)

- Production-ready code
- Always stable
- Protected (requires PR + review)
- Direct commits forbidden

#### `develop` (if using Git Flow)

- Integration branch
- Next release candidate
- Features merge here first

### Feature Development Flow

```bash
# 1. Create feature branch from develop/main
git checkout develop
git pull origin develop
git checkout -b feature/user-profile

# 2. Work on feature, commit regularly
git add .
git commit -m "feat(profile): add user bio field"

# 3. Keep branch updated
git fetch origin
git rebase origin/develop

# 4. Push to remote
git push origin feature/user-profile

# 5. Create Pull Request
# (via GitHub/GitLab/Bitbucket UI)

# 6. After PR approval and merge, delete branch
git checkout develop
git pull origin develop
git branch -d feature/user-profile
```

---

## 🔀 Pull Request (PR) Process

### Creating a PR

**1. Title**: Use commit message format

```
feat(auth): add OAuth login
```

**2. Description**: Fill PR template

```markdown
## Description

Implements OAuth login using Google and GitHub providers.

## Type of Change

- [x] New feature
- [ ] Bug fix
- [ ] Breaking change
- [ ] Documentation update

## Testing

- [x] Unit tests added
- [x] Integration tests added
- [x] Manual testing completed

## Checklist

- [x] Code follows style guidelines
- [x] Self-review completed
- [x] Comments added for complex code
- [x] Documentation updated
- [x] No new warnings generated
- [x] Tests pass locally

## Screenshots (if applicable)

[Add screenshots of UI changes]

## Related Issues

Closes #123
```

**3. Reviewers**: Request at least one reviewer

**4. Labels**: Add appropriate labels

- `feature`, `bug`, `documentation`
- `high-priority`, `needs-review`

### Reviewing a PR

**Reviewer Responsibilities:**

- ✅ Check code quality
- ✅ Verify tests exist and pass
- ✅ Test functionality locally
- ✅ Review for security issues
- ✅ Suggest improvements
- ✅ Approve or request changes

**Review Comments:**

```markdown
# ✅ GOOD (Constructive)

Consider using a Map instead of an object here for better performance with large datasets.

# 🤔 ASK QUESTIONS

Why did we choose this approach over using the built-in validation?

# 📝 NITPICK (Minor)

Nit: This variable could be more descriptive. Maybe `authenticatedUser` instead of `user`?

# ❌ BLOCKING (Must Fix)

This exposes the user's email address in the error message. Please sanitize before returning.
```

### Merging Strategy

**Option 1: Squash and Merge** (Recommended)

- Combines all commits into one
- Clean, linear history
- Good for feature branches

**Option 2: Rebase and Merge**

- Maintains individual commits
- Linear history
- Good for reviewed, clean commits

**Option 3: Merge Commit**

- Creates merge commit
- Preserves full history
- Can be messy

**After Merging:**

```bash
# Delete feature branch
git branch -d feature/user-profile
git push origin --delete feature/user-profile
```

---

## 🔥 Hotfix Process

For critical production bugs:

```bash
# 1. Create hotfix branch from main
git checkout main
git pull origin main
git checkout -b hotfix/payment-error

# 2. Fix the issue
# ... make changes ...
git commit -m "fix(payment): resolve null pointer exception"

# 3. Create PR to main (expedited review)
# 4. After merge to main, also merge to develop
git checkout develop
git merge hotfix/payment-error
git push origin develop

# 5. Tag the release
git checkout main
git tag -a v1.2.1 -m "Hotfix: payment error"
git push origin v1.2.1
```

---

## 🏷️ Tagging & Releases

### Semantic Versioning

**Format**: `vMAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

**Examples:**

- `v1.0.0` - Initial release
- `v1.1.0` - Added new feature
- `v1.1.1` - Bug fix
- `v2.0.0` - Breaking changes

### Creating Tags

```bash
# Annotated tag (recommended)
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin v1.2.0

# Lightweight tag
git tag v1.2.0
git push origin v1.2.0

# Tag specific commit
git tag -a v1.2.0 abc1234 -m "Release version 1.2.0"
```

---

## 🚫 What NOT to Commit

### Never Commit:

- ❌ Secrets (API keys, passwords, tokens)
- ❌ Environment files (`.env`)
- ❌ Compiled binaries
- ❌ Dependencies (`node_modules/`, `venv/`)
- ❌ IDE-specific files (`.idea/`, `.vscode/` unless shared)
- ❌ OS files (`.DS_Store`, `Thumbs.db`)
- ❌ Log files
- ❌ Temporary files

### .gitignore Example

```gitignore
# Dependencies
node_modules/
venv/
.pnp
.pnp.js

# Environment variables
.env
.env.local
.env.production

# Build outputs
dist/
build/
*.log

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Testing
coverage/
.nyc_output/

# Misc
*.cache
.temp/
```

---

## 🔄 Keeping Branch Updated

### Rebase vs Merge

**Use Rebase** (Preferred):

```bash
# Update your feature branch with latest develop
git fetch origin
git rebase origin/develop

# If conflicts
# 1. Resolve conflicts
# 2. git add .
# 3. git rebase --continue
```

**Use Merge** (If needed):

```bash
git fetch origin
git merge origin/develop
```

---

## ✅ Git Workflow Checklist

Before committing:

- [ ] Code is tested and working
- [ ] All tests pass
- [ ] No debugging code (console.log, debugger)
- [ ] No secrets in code
- [ ] Commit message follows convention
- [ ] Changes are focused (one feature/fix per commit)

Before creating PR:

- [ ] Branch is up to date with base branch
- [ ] All commits follow commit convention
- [ ] PR title is clear and descriptive
- [ ] PR description filled out
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No merge conflicts
- [ ] Self-review completed

Before merging PR:

- [ ] At least one approval
- [ ] All tests passing in CI
- [ ] No merge conflicts
- [ ] Code review comments addressed

---

## 🚀 Advanced: Git Hooks

### Pre-commit Hook

```bash
#!/bin/sh
# .git/hooks/pre-commit

echo "Running pre-commit checks..."

# Run linter
npm run lint || {
  echo "❌ Linting failed. Please fix errors before committing."
  exit 1
}

# Run tests
npm test || {
  echo "❌ Tests failed. Please fix before committing."
  exit 1
}

# Check for secrets
if git diff --cached | grep -i "api_key\|password\|secret"; then
  echo "❌ Possible secret detected! Please review."
  exit 1
fi

echo "✅ Pre-commit checks passed!"
```

### Using Husky + lint-staged

```json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged",
      "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    }
  },
  "lint-staged": {
    "*.{js,ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{json,md}": ["prettier --write"]
  }
}
```

---

## 📚 Resources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Semantic Versioning](https://semver.org/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

---

**Remember**: Good Git hygiene makes collaboration easier and history more useful.
