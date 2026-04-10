# Security Rules

**Critical**: These security rules MUST be followed for ALL code changes.

## 🔒 No Hardcoded Secrets

### Never Commit Sensitive Data

- ❌ **Never** hardcode API keys, passwords, tokens, or secrets
- ✅ **Always** use environment variables or secret management services
- ✅ Ensure `.env` files are in `.gitignore`
- ✅ Use `.env.example` with placeholder values for documentation

### Examples

**❌ BAD:**

```typescript
const API_KEY = "sk-1234567890abcdef";
const DATABASE_URL = "postgresql://user:password@localhost/db";
```

**✅ GOOD:**

```typescript
const API_KEY = process.env.API_KEY;
const DATABASE_URL = process.env.DATABASE_URL;

if (!API_KEY || !DATABASE_URL) {
  throw new Error("Required environment variables are missing");
}
```

### Secret Scanning

- Run automated secret detection before commits
- Review code for accidental secret exposure
- Rotate compromised credentials immediately

---

## 🛡️ Input Validation

### Validate All User Inputs

- ✅ **Always** validate user input on both client and server
- ✅ Sanitize data before processing
- ✅ Use type checking and schema validation
- ❌ **Never** trust client-side validation alone

### Examples

**TypeScript with Zod:**

```typescript
import { z } from "zod";

const UserSchema = z.object({
  email: z.string().email(),
  age: z.number().min(18).max(120),
  username: z
    .string()
    .min(3)
    .max(30)
    .regex(/^[a-zA-Z0-9_]+$/),
});

// Validate input
try {
  const validatedData = UserSchema.parse(userInput);
} catch (error) {
  // Handle validation error
  return { error: "Invalid input" };
}
```

**Python with Pydantic:**

```python
from pydantic import BaseModel, EmailStr, validator

class User(BaseModel):
    email: EmailStr
    age: int
    username: str

    @validator('age')
    def validate_age(cls, v):
        if v < 18 or v > 120:
            raise ValueError('Age must be between 18 and 120')
        return v
```

---

## 💉 SQL Injection Prevention

### Use Parameterized Queries

- ✅ **Always** use parameterized queries or ORMs
- ❌ **Never** concatenate user input into SQL strings
- ✅ Use prepared statements

### Examples

**❌ BAD (Vulnerable to SQL Injection):**

```typescript
const query = `SELECT * FROM users WHERE username = '${username}'`;
```

**✅ GOOD (Parameterized):**

```typescript
// Using Prisma ORM
const user = await prisma.user.findUnique({
  where: { username: username },
});

// Using raw SQL with parameters
const user = await db.query("SELECT * FROM users WHERE username = $1", [
  username,
]);
```

**Python with SQLAlchemy:**

```python
# ✅ GOOD
from sqlalchemy import text

stmt = text("SELECT * FROM users WHERE username = :username")
result = conn.execute(stmt, {"username": username})
```

---

## 🔓 Authentication & Authorization

### Authentication Best Practices

- ✅ Use established libraries (Passport.js, NextAuth, Auth0)
- ✅ Implement secure password hashing (bcrypt, argon2)
- ✅ Use JWT with proper expiration
- ✅ Implement refresh token rotation
- ❌ **Never** store passwords in plain text
- ❌ **Never** use weak hashing (MD5, SHA1)

### Authorization Checks

- ✅ Always verify user permissions before operations
- ✅ Implement role-based access control (RBAC)
- ✅ Check authorization on server-side (not just UI)

**Example:**

```typescript
// Middleware to check authentication
export function requireAuth(handler: NextApiHandler) {
  return async (req: NextApiRequest, res: NextApiResponse) => {
    const session = await getSession(req);

    if (!session) {
      return res.status(401).json({ error: "Unauthorized" });
    }

    return handler(req, res);
  };
}

// Middleware to check authorization
export function requireRole(role: string) {
  return async (req: NextApiRequest, res: NextApiResponse, next: Function) => {
    const user = await getCurrentUser(req);

    if (!user || user.role !== role) {
      return res.status(403).json({ error: "Forbidden" });
    }

    next();
  };
}
```

---

## 🌐 XSS (Cross-Site Scripting) Prevention

### Sanitize Output

- ✅ Escape user-generated content before rendering
- ✅ Use framework built-in escaping (React automatically escapes)
- ✅ Set proper Content-Security-Policy headers
- ❌ **Never** use `dangerouslySetInnerHTML` without sanitization

### Examples

**React (Automatic Escaping):**

```typescript
// ✅ Safe - React escapes by default
<div>{userInput}</div>

// ❌ Dangerous
<div dangerouslySetInnerHTML={{ __html: userInput }} />

// ✅ Safe with sanitization
import DOMPurify from 'dompurify';
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userInput) }} />
```

**Content Security Policy:**

```typescript
// Next.js headers
export const headers = {
  "Content-Security-Policy":
    "default-src 'self'; script-src 'self' 'unsafe-inline';",
};
```

---

## 🚨 Error Handling & Logging

### Secure Error Messages

- ✅ Log detailed errors server-side
- ✅ Return generic error messages to clients
- ❌ **Never** expose stack traces to users
- ❌ **Never** include sensitive data in error messages

### Examples

**❌ BAD:**

```typescript
catch (error) {
  res.status(500).json({
    error: error.message,  // Might expose internal details
    stack: error.stack     // ❌ Never expose stack trace
  });
}
```

**✅ GOOD:**

```typescript
catch (error) {
  // Log detailed error server-side
  console.error('Database error:', {
    error: error.message,
    stack: error.stack,
    user: req.userId,
    timestamp: new Date()
  });

  // Return generic error to client
  res.status(500).json({
    error: 'An internal error occurred. Please try again later.'
  });
}
```

---

## 📦 Dependency Security

### Keep Dependencies Updated

- ✅ Regularly update dependencies
- ✅ Run security audits (`npm audit`, `pip-audit`)
- ✅ Review dependencies before adding
- ✅ Use `package-lock.json` or `yarn.lock`
- ⚠️ Monitor for known vulnerabilities

### Commands

```bash
# Node.js
npm audit
npm audit fix

# Python
pip-audit
safety check

# Check for outdated packages
npm outdated
pip list --outdated
```

---

## 🔐 HTTPS & Secure Communication

### Always Use HTTPS

- ✅ Force HTTPS in production
- ✅ Use secure cookies (`secure`, `httpOnly`, `sameSite`)
- ✅ Implement HSTS (HTTP Strict Transport Security)

**Example:**

```typescript
// Set secure cookie
res.setHeader("Set-Cookie", [
  `token=${token}; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=3600`,
]);

// HSTS header
res.setHeader(
  "Strict-Transport-Security",
  "max-age=31536000; includeSubDomains",
);
```

---

## 🔑 CORS (Cross-Origin Resource Sharing)

### Configure CORS Properly

- ✅ Explicitly whitelist allowed origins
- ❌ **Never** use `Access-Control-Allow-Origin: *` in production
- ✅ Use credentials only with specific origins

**Example:**

```typescript
const allowedOrigins = ["https://yourdomain.com", "https://app.yourdomain.com"];

app.use(
  cors({
    origin: (origin, callback) => {
      if (!origin || allowedOrigins.includes(origin)) {
        callback(null, true);
      } else {
        callback(new Error("Not allowed by CORS"));
      }
    },
    credentials: true,
  }),
);
```

---

## 📝 Security Checklist

Before every deployment, verify:

- [ ] No hardcoded secrets in code
- [ ] All environment variables properly configured
- [ ] Input validation on all user inputs
- [ ] SQL queries use parameterized statements
- [ ] Authentication and authorization checks in place
- [ ] XSS prevention measures implemented
- [ ] Error messages don't expose sensitive information
- [ ] Dependencies audited for vulnerabilities
- [ ] HTTPS enforced in production
- [ ] CORS configured properly
- [ ] Security headers set (CSP, HSTS, X-Frame-Options)
- [ ] Rate limiting implemented on sensitive endpoints
- [ ] File upload validation (if applicable)
- [ ] Session management secure

---

## 🚫 Common Vulnerabilities to Avoid

1. **SQL Injection** - Use ORMs or parameterized queries
2. **XSS** - Sanitize output, use CSP
3. **CSRF** - Use CSRF tokens
4. **Insecure Direct Object References** - Verify authorization
5. **Security Misconfiguration** - Review all settings
6. **Sensitive Data Exposure** - Encrypt sensitive data
7. **Missing Access Control** - Implement proper authorization
8. **Using Components with Known Vulnerabilities** - Keep dependencies updated
9. **Insufficient Logging & Monitoring** - Log security events
10. **Unvalidated Redirects** - Validate redirect URLs

---

## 📚 Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [Node.js Security Best Practices](https://nodejs.org/en/docs/guides/security/)

---

**Remember**: Security is not optional. Follow these rules for EVERY code change.
