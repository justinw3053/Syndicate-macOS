import pytest
import active_lab
import numpy as np
def test_vectorized_cosine():
    matrix = np.array([[4.0, 0.0], [1.0, 1.0], [0.0, 2.0]])
    query = np.array([1.0, 0.0])
    results = active_lab.vectorized_cosine_similarity(matrix, query)
    expected = np.array([1.0, 0.70710678, 0.0])
    assert np.allclose(results, expected, atol=1e-5)
