# Textbook: Functions, Scoping, Closures & State Factories (KATA_FUNC_03)

## Theoretical Foundation
### Mutable Default Argument Trap.
In Python, execution scopes determine variable resolution via the LEGB rule (Local, Enclosing, Global, Built-in). Closures allow functions to retain references to variables in their enclosing lexical scope even after the outer function has finished executing. This is a powerful pattern for building lightweight, stateless factories for agent runtimes.

In modern machine learning orchestration and agent runtimes, understanding the exact lifecycle of objects and executions under the hood prevents fatal memory leaks and state decay.

---

## Syntax Anatomy
Here is the core API structure representing the target function you are implementing:
```python
# Function interface definition
def func(...):
  """Mutable Default Argument Trap."""
  # Your optimized logic here
```

Make sure your code uses standard Python idioms, is completely zero-dependency, and strictly uses local scoping variables to ensure thread-safe concurrent execution.

---

## Anti-Patterns & Common Pitfalls
*  **Unintentionally binding mutable objects (like lists or dictionaries) as default arguments in function definitions. Since default arguments are evaluated once at definition time, all function calls share the same mutable reference, causing memory leakage across independent runs.**
*  **Leaking Global States:** Modifying outer global arrays inside local functions instead of returning newly created, decoupled structures.
*  **Failing Bound Verification:** Omitting safeguards against zero-division, index errors, or invalid key types.

---

## Step-by-Step Exercise Instructions
1. Define nested functions to capture enclosing variables.
2. Use the `nonlocal` keyword if mutating state in enclosing scopes.
3. Avoid mutable default argument traps by setting default parameters to `None` and instantiating internally.
4. Validate your implementation locally using standard assertions.
