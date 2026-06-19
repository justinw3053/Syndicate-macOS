# The Arsenal Contract

To ensure every component built during this journey is "Forward Compatible" and architecturally sound, all modules must adhere to the following standards:

## 1. Type Integrity
- **Mandatory Type Hinting:** Every function must have input and output type hints. No "guessing" what a function returns.
- **Pydantic/Dataclasses:** For complex data structures, use `dataclasses` or `pydantic` to define the "schema" of the data.

## 2. Documentation (The "Why")
- **PEP 257:** Every module, class, and function must have a docstring explaining its purpose.
- **Internal Comments:** Use comments to explain non-obvious logic, specifically focusing on "Why" something is done a certain way (e.g., why this specific error is caught).

## 3. Resiliency (The "Stress Test")
- **Deterministic Failure:** Functions must never crash silently. They should raise specific exceptions or return structured error objects.
- **Timeout & Retry:** Network calls must have explicit timeouts.

## 4. PEP 8 & Style
- **Naming:** `snake_case` for functions/variables, `PascalCase` for classes.
- **Consistency:** Use 4 spaces for indentation.

## 5. Interface Standard
- Every module should be testable in isolation. 
- Use `if __name__ == "__main__":` blocks for local "lab" testing.
