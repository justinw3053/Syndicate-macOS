# Textbook: Vector Embeddings & Cosine Similarity Metrics (KATA_EMBED_01)

## Theoretical Foundation
### Cosine Similarity.
Embeddings translate raw text strings into high-dimensional geometric coordinates representing semantic meaning. The cosine similarity measures the angular alignment between two semantic vectors in embedding space, returning a score from -1.0 to 1.0 that dictates contextual proximity.

In modern machine learning orchestration and agent runtimes, understanding the exact lifecycle of objects and executions under the hood prevents fatal memory leaks and state decay.

---

## Syntax Anatomy
Here is the core API structure representing the target function you are implementing:
```python
# Function interface definition
def cosine_similarity(...):
  """Cosine Similarity."""
  # Your optimized logic here
```

Make sure your code uses standard Python idioms, is completely zero-dependency, and strictly uses local scoping variables to ensure thread-safe concurrent execution.

---

## Anti-Patterns & Common Pitfalls
*  **Confusing standard Dot product with Cosine Similarity. Cosine similarity requires dividing the dot product by the product of both vectors' L2 norms. Forgetting to normalization-scale results in amplitude-corrupted scores.**
*  **Leaking Global States:** Modifying outer global arrays inside local functions instead of returning newly created, decoupled structures.
*  **Failing Bound Verification:** Omitting safeguards against zero-division, index errors, or invalid key types.

---

## Step-by-Step Exercise Instructions
1. Calculate the dot product of two semantic float vectors.
2. Compute the L2 Norm (Euclidean magnitude) of both vectors.
3. Divide the dot product by the product of the magnitudes, handling zero-division safeguards.
4. Validate your implementation locally using standard assertions.
