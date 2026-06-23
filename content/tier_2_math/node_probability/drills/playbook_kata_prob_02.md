# Textbook: Probability, Logits, Softmax & Top-K Sampling (KATA_PROB_02)

## Theoretical Foundation
### Softmax Numerical Stability.
AI models output unnormalized log-probability values called logits. To turn these into true probability distributions, we pass them through the Softmax function. To control generation creativity and prevent repetitive or nonsensical tokens, we apply Top-K masking before sampling.

In modern machine learning orchestration and agent runtimes, understanding the exact lifecycle of objects and executions under the hood prevents fatal memory leaks and state decay.

---

## Syntax Anatomy
Here is the core API structure representing the target function you are implementing:
```python
# Function interface definition
def stable_softmax(...):
  """Softmax Numerical Stability."""
  # Your optimized logic here
```

Make sure your code uses standard Python idioms, is completely zero-dependency, and strictly uses local scoping variables to ensure thread-safe concurrent execution.

---

## Anti-Patterns & Common Pitfalls
*  **Numerical instability inside Softmax. Raising high logits (e.g., `80.0` or higher) to exponentials triggers `OverflowError` in float representation. You must subtract the maximum value from all logits (the log-sum-exp trick) before exponentiating.**
*  **Leaking Global States:** Modifying outer global arrays inside local functions instead of returning newly created, decoupled structures.
*  **Failing Bound Verification:** Omitting safeguards against zero-division, index errors, or invalid key types.

---

## Step-by-Step Exercise Instructions
1. Subtract the max value of the input logit list from all elements to guarantee numerical stability.
2. Compute exponents and normalize values to sum up to exactly 1.0.
3. Apply Top-K masking to retain only the top largest logits, setting all others to negative infinity.
4. Validate your implementation locally using standard assertions.
