# Textbook: Object-Oriented Architecture, Class State & Representation Hooks (KATA_OOP_03)

## Theoretical Foundation
### Pointer Equality vs Value Equality.
Classes group state (attributes) and behavior (methods) into clean, logical units. In custom AI pipelines, class instances represent prompt segments, system contexts, and agent states. Understanding identity vs equality and overriding representation hooks like `__repr__` and `__str__` is critical for runtime debugging and tracing.

In modern machine learning orchestration and agent runtimes, understanding the exact lifecycle of objects and executions under the hood prevents fatal memory leaks and state decay.

---

## Syntax Anatomy
Here is the core API structure representing the target function you are implementing:
```python
# Function interface definition
def __init__(...):
  """Pointer Equality vs Value Equality."""
  # Your optimized logic here
```

Make sure your code uses standard Python idioms, is completely zero-dependency, and strictly uses local scoping variables to ensure thread-safe concurrent execution.

---

## Anti-Patterns & Common Pitfalls
*  **Defining class-level variables (static variables) when intending to define instance-level variables. Class-level lists or dicts are shared across all instances of a class, meaning any state update inside one instance will instantly mutate all other active class instances.**
*  **Leaking Global States:** Modifying outer global arrays inside local functions instead of returning newly created, decoupled structures.
*  **Failing Bound Verification:** Omitting safeguards against zero-division, index errors, or invalid key types.

---

## Step-by-Step Exercise Instructions
1. Initialize instance-level variables inside the `__init__` constructor using `self`.
2. Define custom `__eq__` hooks to assert value equality instead of pointer identity.
3. Override the `__repr__` representation hook to output clean, developers-friendly tracing logs.
4. Validate your implementation locally using standard assertions.
