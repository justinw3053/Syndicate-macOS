# Textbook: Scaled Dot-Product Attention Mechanics (KATA_ATTN_01)

## Theoretical Foundation
### The Vanishing Gradient (Score Scaling).
Transformers use Attention mechanisms to dynamically route focus. Query (Q), Key (K), and Value (V) projections represent questions, keys, and values. By computing the dot-product similarity of Queries and Keys, scaling by the square root of the dimensions, and applying Softmax, we determine how strongly to weight Values.

In modern machine learning orchestration and agent runtimes, understanding the exact lifecycle of objects and executions under the hood prevents fatal memory leaks and state decay.

---

## Syntax Anatomy
Here is the core API structure representing the target function you are implementing:
```python
# Function interface definition
def scale_scores(...):
  """The Vanishing Gradient (Score Scaling)."""
  # Your optimized logic here
```

Make sure your code uses standard Python idioms, is completely zero-dependency, and strictly uses local scoping variables to ensure thread-safe concurrent execution.

---

## Anti-Patterns & Common Pitfalls
*  **Forgetting the scaling factor `1 / sqrt(d_k)`. High-dimensional dot products explode in magnitude, driving Softmax into regions with near-zero gradients. This prevents successful training or smooth focus distribution.**
*  **Leaking Global States:** Modifying outer global arrays inside local functions instead of returning newly created, decoupled structures.
*  **Failing Bound Verification:** Omitting safeguards against zero-division, index errors, or invalid key types.

---

## Step-by-Step Exercise Instructions
1. Multiply Query and transposed Key matrices to calculate similarity scores.
2. Scale all scores by the square root of the key dimension.
3. Pass scaled scores through Softmax and multiply by the Value matrix.
4. Validate your implementation locally using standard assertions.
