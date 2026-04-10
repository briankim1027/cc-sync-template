# N8N Expression Syntax Reference

Quick reference for n8n expression syntax and validation.

## Expression Format

**Syntax**: `={{expression}}`

**Examples**:
```javascript
={{$json["fieldName"]}}
={{$json["field1"]}} and {{$json["field2"]}}
={{new Date().toISOString()}}
```

## Common Patterns

### Accessing Data

```javascript
// Current item field
={{$json["fieldName"]}}

// Nested field
={{$json["user"]["email"]}}

// Array element
={{$json["items"][0]}}

// All items
={{$items}}
```

### String Operations

```javascript
// Lowercase
={{$json["email"].toLowerCase()}}

// Uppercase
={{$json["name"].toUpperCase()}}

// Trim
={{$json["text"].trim()}}

// Substring
={{$json["text"].substring(0, 100)}}

// Replace
={{$json["text"].replace("old", "new")}}

// Concatenate
={{$json["first"]}} {{$json["last"]}}

// Template
={{`Hello ${$json["name"]}`}}
```

### Number Operations

```javascript
// Arithmetic
={{$json["price"] * 1.2}}
={{$json["total"] - $json["discount"]}}

// Rounding
={{Math.round($json["value"])}}
={{Math.floor($json["value"])}}

// Min/Max
={{Math.max($json["a"], $json["b"])}}
```

### Date/Time

```javascript
// Current timestamp
={{new Date().toISOString()}}

// Format date
={{new Date($json["date"]).toLocaleDateString()}}

// Unix timestamp
={{Date.now()}}

// Add days
={{new Date(Date.now() + 86400000).toISOString()}}
```

### Conditionals

```javascript
// Ternary
={{$json["premium"] ? "VIP" : "Standard"}}

// Null coalescing
={{$json["field"] || "default"}}

// Comparison
={{$json["age"] >= 18 ? "adult" : "minor"}}
```

### Array Operations

```javascript
// Length
={{$json["items"].length}}

// Join
={{$json["tags"].join(", ")}}

// Map
={{$json["items"].map(i => i.name)}}

// Filter
={{$json["items"].filter(i => i.active)}}

// Find
={{$json["items"].find(i => i.id === 123)}}
```

### Object Operations

```javascript
// Keys
={{Object.keys($json)}}

// Values
={{Object.values($json)}}

// Merge
={{Object.assign({}, $json, {newField: "value"})}}
```

## Validation Rules

### Syntax Check

✅ **Valid**:
```javascript
={{$json["field"]}}
={{$json["email"].toLowerCase()}}
={{new Date().toISOString()}}
```

❌ **Invalid**:
```javascript
={{$json[field]}}              // Missing quotes
={{$json.field.toLowerCase()}} // Incorrect bracket notation
={{Date.now}}                  // Missing ()
```

### Common Errors

**Error**: `"field" is not defined`
**Fix**: Use proper field access: `$json["field"]`

**Error**: Unexpected token
**Fix**: Check quote matching, parentheses, brackets

**Error**: Cannot read property of undefined
**Fix**: Add null check: `={{$json["field"] || "default"}}`

## Expression Testing

**Test Pattern**:
```javascript
// Safe access with default
={{$json["field"] !== undefined ? $json["field"] : "default"}}

// Type checking
={{typeof $json["field"] === "string" ? $json["field"] : ""}}

// Null-safe chaining
={{$json["user"] && $json["user"]["email"]}}
```

## Best Practices

1. **Always quote field names**: `$json["field"]` not `$json.field`
2. **Use default values**: `{{$json["field"] || "default"}}`
3. **Validate before operations**: Check undefined/null
4. **Escape special characters**: In strings
5. **Test expressions**: In n8n test mode before deployment
