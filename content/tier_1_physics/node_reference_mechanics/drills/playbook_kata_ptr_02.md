# Textbook: Reference Mechanics, Pointer Aliasing & Memory Isolation (KATA_PTR_02)

## Theoretical Foundation
### Implement deep copy decoupling.
In Python, variables do not store values directly; they store pointer references to objects in memory. When you assign `b = a`, you copy the memory address pointer, not the underlying data. This results in pointer aliasing. Understanding the exact boundaries of shallow copies vs deep copies is fundamental to preventing state corruption in AI runtime pipelines.

In modern machine learning orchestration and agent runtimes, understanding the exact lifecycle of objects and executions under the hood prevents fatal memory leaks and state decay.

---

## Syntax Anatomy
Here is the core API structure representing the target function you are implementing:
```python
# Function interface definition
def get_deep_copy(...):
  """Implement deep copy decoupling."""
  # Your optimized logic here
```

Make sure your code uses standard Python idioms, is completely zero-dependency, and strictly uses local scoping variables to ensure thread-safe concurrent execution.

---

## Anti-Patterns & Common Pitfalls
*  **Mutating nested lists or dictionaries within a shallow copy. Since a shallow copy only duplicates the top-level container, inner containers are still coupled by reference pointer. A downstream mutation inside the nested dictionary will leak and corrupt your original base configuration state.**
*  **Leaking Global States:** Modifying outer global arrays inside local functions instead of returning newly created, decoupled structures.
*  **Failing Bound Verification:** Omitting safeguards against zero-division, index errors, or invalid key types.

---

## Step-by-Step Exercise Instructions
1. Import the built-in copy module.
2. Create a fully isolated copy of the data structure.
3. Return the decoupled structure without leaking references to original memory blocks.
4. Validate your implementation locally using standard assertions.
