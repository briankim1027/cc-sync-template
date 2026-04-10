# Testing Rules

**Requirement**: All code must be developed using Test-Driven Development (TDD) with minimum 80% coverage.

---

## 🔴🟢🔄 Test-Driven Development (TDD)

### The Red-Green-Refactor Cycle

**Always follow this cycle:**

1. **🔴 RED** - Write a failing test
2. **🟢 GREEN** - Write minimal code to pass
3. **🔄 REFACTOR** - Improve code while keeping tests green

### TDD Process

#### 1. RED - Write Failing Test First

**Before writing any implementation code:**

- Define expected behavior through tests
- Write test that describes the desired functionality
- Run test and confirm it fails
- Review the failure message

**Example:**

```typescript
// sum.test.ts
describe("sum", () => {
  it("should add two positive numbers", () => {
    expect(sum(2, 3)).toBe(5);
  });
});

// Run: npm test
// Expected: Test FAILS (function doesn't exist yet)
```

#### 2. GREEN - Make Test Pass

**Write the simplest code to pass the test:**

- Don't add extra features
- Don't over-engineer
- Just make it work

**Example:**

```typescript
// sum.ts
export function sum(a: number, b: number): number {
  return a + b; // Simplest implementation
}

// Run: npm test
// Expected: Test PASSES
```

#### 3. REFACTOR - Improve Code

**Clean up while keeping tests green:**

- Improve structure
- Remove duplication
- Optimize if needed
- Run tests after each change

**Example:**

```typescript
// Add validation (refactor)
export function sum(a: number, b: number): number {
  if (typeof a !== "number" || typeof b !== "number") {
    throw new Error("Arguments must be numbers");
  }
  return a + b;
}

// Add test for new behavior
it("should throw error for non-numbers", () => {
  expect(() => sum("2" as any, 3)).toThrow("Arguments must be numbers");
});

// Run: npm test
// Expected: All tests PASS
```

---

## 📊 Coverage Requirements

### Minimum Coverage: 80%

**Coverage Metrics:**

- ✅ **Statements**: 80% minimum
- ✅ **Branches**: 80% minimum
- ✅ **Functions**: 80% minimum
- ✅ **Lines**: 80% minimum

### Critical Paths: 100% Coverage

**Require 100% coverage for:**

- Authentication/authorization logic
- Payment processing
- Data validation
- Security-critical code
- Business logic calculations

### Running Coverage

**JavaScript/TypeScript:**

```bash
# Jest
npm test -- --coverage

# Vitest
npm run test:coverage

# Check coverage thresholds
```

**Python:**

```bash
# pytest
pytest --cov=. --cov-report=html --cov-report=term

# Check coverage
coverage report
```

**Coverage Configuration (Jest):**

```json
{
  "jest": {
    "coverageThreshold": {
      "global": {
        "branches": 80,
        "functions": 80,
        "lines": 80,
        "statements": 80
      },
      "src/auth/**/*.ts": {
        "branches": 100,
        "functions": 100,
        "lines": 100,
        "statements": 100
      }
    }
  }
}
```

---

## 📁 Test Organization

### File Naming

**JavaScript/TypeScript:**

```
src/
  utils/
    sum.ts                  ← Implementation
    sum.test.ts            ← Unit test
    sum.integration.test.ts ← Integration test
  components/
    Button.tsx
    Button.test.tsx
```

**Python:**

```
src/
  utils/
    calculator.py          ← Implementation
  tests/
    test_calculator.py     ← Unit test
    integration/
      test_calculator_integration.py
```

### Test Types

1. **Unit Tests** - `*.test.ts` or `test_*.py`
   - Test individual functions/classes in isolation
   - Mock external dependencies
   - Fast execution

2. **Integration Tests** - `*.integration.test.ts`
   - Test multiple components together
   - May use real databases (test DB)
   - Slower than unit tests

3. **E2E Tests** - `*.e2e.test.ts`
   - Test complete user workflows
   - Use real browser (Playwright, Cypress)
   - Slowest, but most realistic

---

## ✍️ Writing Good Tests

### Test Structure: Arrange-Act-Assert (AAA)

```typescript
it("should calculate discounted price correctly", () => {
  // Arrange - Setup test data
  const basePrice = 100;
  const discountPercent = 20;

  // Act - Execute the function
  const result = calculateDiscount(basePrice, discountPercent);

  // Assert - Verify the result
  expect(result).toBe(80);
});
```

### Descriptive Test Names

**✅ GOOD:**

```typescript
describe("User Authentication", () => {
  it("should return JWT token when credentials are valid", () => {});
  it("should throw error when password is incorrect", () => {});
  it("should lock account after 5 failed attempts", () => {});
});
```

**❌ BAD:**

```typescript
describe("Auth", () => {
  it("works", () => {});
  it("test1", () => {});
  it("handles error", () => {}); // Which error?
});
```

### One Assertion Per Test (When Possible)

**✅ GOOD:**

```typescript
it("should return user name", () => {
  expect(user.getName()).toBe("John Doe");
});

it("should return user email", () => {
  expect(user.getEmail()).toBe("john@example.com");
});
```

**⚠️ ACCEPTABLE (Related Assertions):**

```typescript
it("should create user with correct properties", () => {
  const user = createUser({ name: "John", email: "john@example.com" });

  expect(user.name).toBe("John");
  expect(user.email).toBe("john@example.com");
  expect(user.id).toBeDefined();
});
```

---

## 🎭 Mocking & Test Isolation

### Mock External Dependencies

**Example with Jest:**

```typescript
// user-service.test.ts
import { getUserById } from "./user-service";
import { database } from "./database";

jest.mock("./database");

describe("getUserById", () => {
  it("should fetch user from database", async () => {
    // Arrange - Mock database response
    const mockUser = { id: 1, name: "John" };
    (database.query as jest.Mock).mockResolvedValue(mockUser);

    // Act
    const result = await getUserById(1);

    // Assert
    expect(result).toEqual(mockUser);
    expect(database.query).toHaveBeenCalledWith(
      "SELECT * FROM users WHERE id = ?",
      [1],
    );
  });
});
```

### Don't Mock What You Don't Own

**✅ GOOD (Mock your own code):**

```typescript
jest.mock("./database"); // Your database module
jest.mock("./email-service"); // Your email service
```

**❌ BAD (Avoid mocking libraries directly):**

```typescript
// Avoid mocking axios, prisma, etc. directly
// Instead, wrap them in your own modules and mock those
```

---

## 🧪 Test Coverage Best Practices

### What to Test

**✅ Always Test:**

- Public API/interfaces
- Business logic
- Edge cases
- Error conditions
- Boundary values

**❌ Don't Test:**

- Third-party libraries
- Framework internals
- Trivial getters/setters
- Private implementation details

### Edge Cases & Boundary Testing

**Example:**

```typescript
describe("validateAge", () => {
  it("should return true for age 18 (minimum)", () => {
    expect(validateAge(18)).toBe(true);
  });

  it("should return true for age 120 (maximum)", () => {
    expect(validateAge(120)).toBe(true);
  });

  it("should return false for age 17 (below minimum)", () => {
    expect(validateAge(17)).toBe(false);
  });

  it("should return false for age 121 (above maximum)", () => {
    expect(validateAge(121)).toBe(false);
  });

  it("should throw error for negative age", () => {
    expect(() => validateAge(-1)).toThrow();
  });

  it("should throw error for non-integer", () => {
    expect(() => validateAge(18.5)).toThrow();
  });
});
```

---

## 🔄 Testing Async Code

### Promises & Async/Await

**✅ GOOD:**

```typescript
it("should fetch user data", async () => {
  const user = await fetchUser(1);
  expect(user.name).toBe("John");
});

it("should handle fetch errors", async () => {
  await expect(fetchUser(999)).rejects.toThrow("User not found");
});
```

**❌ BAD:**

```typescript
it("should fetch user data", () => {
  fetchUser(1).then((user) => {
    expect(user.name).toBe("John"); // May not run!
  });
});
```

---

## 🎯 Testing Patterns

### Testing React Components

**Example with React Testing Library:**

```typescript
import { render, screen, fireEvent } from '@testing-library/react';
import { LoginForm } from './LoginForm';

describe('LoginForm', () => {
  it('should display error message for invalid credentials', async () => {
    // Arrange
    const mockLogin = jest.fn().mockRejectedValue(new Error('Invalid credentials'));
    render(<LoginForm onLogin={mockLogin} />);

    // Act
    fireEvent.change(screen.getByLabelText('Email'), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText('Password'), { target: { value: 'wrong' } });
    fireEvent.click(screen.getByRole('button', { name: 'Login' }));

    // Assert
    expect(await screen.findByText('Invalid credentials')).toBeInTheDocument();
  });
});
```

### Testing API Routes

**Example with Next.js:**

```typescript
import { createMocks } from "node-mocks-http";
import handler from "./api/users";

describe("/api/users", () => {
  it("should return 401 when not authenticated", async () => {
    const { req, res } = createMocks({
      method: "GET",
    });

    await handler(req, res);

    expect(res._getStatusCode()).toBe(401);
    expect(JSON.parse(res._getData())).toEqual({ error: "Unauthorized" });
  });
});
```

---

## ✅ Testing Checklist

Before committing code:

- [ ] All features have tests written **before** implementation (TDD)
- [ ] Tests follow Red-Green-Refactor cycle
- [ ] Overall coverage is ≥80%
- [ ] Critical paths have 100% coverage
- [ ] All edge cases are tested
- [ ] Error conditions are tested
- [ ] Tests are independent (can run in any order)
- [ ] External dependencies are mocked
- [ ] Test names are descriptive
- [ ] Tests follow AAA pattern
- [ ] Async tests use async/await
- [ ] Tests run in CI/CD pipeline

---

## 🚀 CI/CD Integration

### Run Tests on Every Commit

**GitHub Actions Example:**

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18
      - run: npm ci
      - run: npm test -- --coverage
      - run: npm run test:e2e
```

---

## 📚 Testing Resources

- [Jest Documentation](https://jestjs.io/)
- [React Testing Library](https://testing-library.com/react)
- [Vitest](https://vitest.dev/)
- [Pytest](https://docs.pytest.org/)
- [Martin Fowler - Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)

---

**Remember**: Tests are not optional. They are part of the definition of "done".
If the code doesn't have tests, it's not finished.
