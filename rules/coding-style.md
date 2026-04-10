# Coding Style Rules

**Purpose**: Maintain consistent, readable, and maintainable code across all projects.

---

## 📁 File Organization

### File Size Limits

- ✅ Keep files under **500 lines**
- ✅ Split large files into smaller, focused modules
- ✅ One component/class per file (with exceptions for small helpers)

### Directory Structure

- ✅ Group related files by feature/domain
- ✅ Keep flat structure when possible (max 3-4 levels deep)
- ✅ Use meaningful directory names

**Example Structure:**

```
src/
  features/
    auth/
      components/
        LoginForm.tsx
        RegisterForm.tsx
      hooks/
        useAuth.ts
      utils/
        validation.ts
      types.ts
      index.ts
    posts/
      components/
      hooks/
      utils/
      types.ts
      index.ts
```

---

## 🔒 Immutability

### Prefer Immutable Data Structures

- ✅ Use `const` by default
- ⚠️ Use `let` only when reassignment is necessary
- ❌ Avoid `var`
- ✅ Don't mutate function parameters
- ✅ Use immutable update patterns

### Examples

**❌ BAD (Mutation):**

```typescript
function addItem(array: string[], item: string) {
  array.push(item); // Mutates parameter
  return array;
}

const user = { name: "John", age: 30 };
user.age = 31; // Direct mutation
```

**✅ GOOD (Immutable):**

```typescript
function addItem(array: string[], item: string) {
  return [...array, item]; // Returns new array
}

const user = { name: "John", age: 30 };
const updatedUser = { ...user, age: 31 }; // New object

// For complex state updates
import { produce } from "immer";
const newState = produce(state, (draft) => {
  draft.nested.value = 42;
});
```

---

## 🏷️ Naming Conventions

### Variables & Functions

- ✅ **camelCase** for variables and functions
- ✅ Descriptive names (avoid abbreviations)
- ✅ Boolean variables start with `is`, `has`, `should`
- ❌ No single-letter names (except in loops/lambdas)

**Examples:**

```typescript
// ✅ GOOD
const userAuthenticated = true;
const hasPermission = checkUserRole(user);
function calculateTotalPrice(items: Item[]): number {}

// ❌ BAD
const ua = true;
const x = checkUserRole(user);
function calc(i: Item[]): number {}
```

### Classes & Components

- ✅ **PascalCase** for classes and React components
- ✅ Noun-based names

**Examples:**

```typescript
// ✅ GOOD
class UserRepository {}
class EmailService {}
function UserProfile() {}
function ShoppingCart() {}

// ❌ BAD
class userRepository {}
function userprofile() {}
```

### Constants

- ✅ **UPPER_SNAKE_CASE** for true constants
- ✅ Use for configuration values, magic numbers

**Examples:**

```typescript
// ✅ GOOD
const MAX_RETRY_ATTEMPTS = 3;
const API_BASE_URL = "https://api.example.com";
const DEFAULT_TIMEOUT_MS = 5000;

// ❌ BAD (not really constants)
const userList = []; // This will change
```

### Files & Directories

- ✅ **kebab-case** for file names (or match component name)
- ✅ Match exported name for components

**Examples:**

```
utils/
  date-formatter.ts      ✅
  stringHelpers.ts       ❌ (use string-helpers.ts)

components/
  UserProfile.tsx        ✅
  user-profile.tsx       ✅ (acceptable)
  userprofile.tsx        ❌
```

---

## 🎯 DRY Principle (Don't Repeat Yourself)

### Extract Repeated Code

- ✅ If code appears 3+ times, extract to function/component
- ✅ Create reusable utilities
- ✅ Use composition over duplication

### Examples

**❌ BAD (Repetition):**

```typescript
// Formatting date in multiple places
const formattedDate1 = new Date(date1).toLocaleDateString("en-US");
const formattedDate2 = new Date(date2).toLocaleDateString("en-US");
const formattedDate3 = new Date(date3).toLocaleDateString("en-US");
```

**✅ GOOD (Extracted):**

```typescript
// utils/date.ts
export function formatDate(date: string | Date): string {
  return new Date(date).toLocaleDateString("en-US");
}

// Usage
const formattedDate1 = formatDate(date1);
const formattedDate2 = formatDate(date2);
const formattedDate3 = formatDate(date3);
```

---

## 📝 Comments & Documentation

### When to Comment

- ✅ Complex algorithms (explain "why", not "what")
- ✅ Non-obvious business logic
- ✅ Workarounds for external issues
- ✅ Public API documentation (JSDoc/TSDoc)
- ❌ Obvious code (let code be self-documenting)

### Examples

**❌ BAD (Obvious Comment):**

```typescript
// Increment counter by 1
counter++;

// Loop through users
users.forEach((user) => {});
```

**✅ GOOD (Helpful Comment):**

```typescript
// Using exponential backoff to avoid rate limiting from API
const delay = Math.min(1000 * Math.pow(2, attempt), 30000);

/**
 * Calculates the compound interest for an investment.
 * Formula: A = P(1 + r/n)^(nt)
 *
 * @param principal - Initial investment amount
 * @param rate - Annual interest rate (as decimal, e.g., 0.05 for 5%)
 * @param compounds - Number of times interest is compounded per year
 * @param years - Investment period in years
 * @returns Final amount after compound interest
 */
function calculateCompoundInterest(
  principal: number,
  rate: number,
  compounds: number,
  years: number,
): number {
  return principal * Math.pow(1 + rate / compounds, compounds * years);
}
```

---

## 🧩 Function Design

### Keep Functions Small

- ✅ One function = one responsibility (Single Responsibility Principle)
- ✅ Max ~30 lines per function (guideline, not rule)
- ✅ Extract complex logic into separate functions

### Function Parameters

- ✅ Max 3-4 parameters
- ✅ Use object for multiple related parameters
- ✅ Required parameters first, optional last

**Examples:**

**❌ BAD (Too Many Parameters):**

```typescript
function createUser(
  name: string,
  email: string,
  age: number,
  city: string,
  country: string,
  phone: string,
) {
  // ...
}
```

**✅ GOOD (Object Parameter):**

```typescript
interface CreateUserParams {
  name: string;
  email: string;
  age: number;
  address: {
    city: string;
    country: string;
  };
  phone?: string;
}

function createUser(params: CreateUserParams) {
  // ...
}
```

---

## 🎨 Code Formatting

### Use Automated Formatting

- ✅ Use Prettier for consistent formatting
- ✅ Configure in `.prettierrc`
- ✅ Run on pre-commit (husky + lint-staged)

**Example `.prettierrc`:**

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "arrowParens": "avoid"
}
```

### Indentation & Spacing

- ✅ 2 spaces for indentation (no tabs)
- ✅ Blank line between logical blocks
- ✅ No trailing whitespace

---

## 📦 Import Organization

### Order Imports

1. External libraries
2. Internal modules
3. Relative imports
4. Types (if separate)

**Example:**

```typescript
// 1. External libraries
import React, { useState, useEffect } from "react";
import { useRouter } from "next/router";
import axios from "axios";

// 2. Internal modules
import { Button } from "@/components/ui";
import { apiClient } from "@/lib/api";

// 3. Relative imports
import { UserForm } from "./UserForm";
import { validation } from "../utils/validation";

// 4. Types
import type { User, Post } from "@/types";
```

---

## 🔧 TypeScript Best Practices

### Use Types Properly

- ✅ Define interfaces for object shapes
- ✅ Use type unions instead of enums (when appropriate)
- ✅ Avoid `any` - use `unknown` if truly unknown
- ✅ Enable strict mode

**Examples:**

**❌ BAD:**

```typescript
function processData(data: any) {
  // Avoid 'any'
  return data.value;
}

const user = {
  // Missing type
  name: "John",
  age: 30,
};
```

**✅ GOOD:**

```typescript
interface User {
  name: string;
  age: number;
  email?: string;
}

function processData(data: unknown) {
  if (typeof data === "object" && data !== null && "value" in data) {
    return data.value;
  }
  throw new Error("Invalid data");
}

const user: User = {
  name: "John",
  age: 30,
};
```

---

## ⚡ Performance Considerations

### Avoid Premature Optimization

- ✅ Write clear code first
- ✅ Profile before optimizing
- ✅ Optimize hot paths only

### Common Optimizations

- ✅ Memoize expensive calculations
- ✅ Use lazy loading for large components
- ✅ Debounce/throttle frequent operations

---

## ✅ Code Style Checklist

Before committing:

- [ ] Files are under 500 lines
- [ ] Using `const` by default
- [ ] No parameter mutations
- [ ] Descriptive variable/function names
- [ ] No code duplication (DRY)
- [ ] Functions have single responsibility
- [ ] Comments explain "why", not "what"
- [ ] Imports are organized
- [ ] Code is formatted with Prettier
- [ ] TypeScript strict mode enabled
- [ ] No `any` types (use `unknown` if needed)

---

## 🎯 Examples of Well-Structured Code

**✅ EXCELLENT:**

```typescript
// utils/price-calculator.ts
interface PriceCalculationParams {
  basePrice: number;
  taxRate: number;
  discount?: number;
}

interface PriceBreakdown {
  subtotal: number;
  tax: number;
  discount: number;
  total: number;
}

export function calculatePrice(params: PriceCalculationParams): PriceBreakdown {
  const { basePrice, taxRate, discount = 0 } = params;

  const subtotal = basePrice;
  const discountAmount = calculateDiscount(subtotal, discount);
  const taxableAmount = subtotal - discountAmount;
  const taxAmount = calculateTax(taxableAmount, taxRate);
  const total = taxableAmount + taxAmount;

  return {
    subtotal,
    tax: taxAmount,
    discount: discountAmount,
    total,
  };
}

function calculateDiscount(amount: number, discountRate: number): number {
  return amount * (discountRate / 100);
}

function calculateTax(amount: number, taxRate: number): number {
  return amount * (taxRate / 100);
}
```

**Key Features:**

- ✅ Clear, descriptive names
- ✅ Single responsibility functions
- ✅ Immutable operations
- ✅ Type safety
- ✅ Easy to test
- ✅ Easy to understand

---

**Remember**: Consistent style makes code easier to read, maintain, and collaborate on.
