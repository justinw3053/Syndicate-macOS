import pytest
import active_lab
def test_value_equality():
    v1 = active_lab.Embedding([0.1, 0.2, 0.3])
    v2 = active_lab.Embedding([0.1, 0.2, 0.3])
    v3 = active_lab.Embedding([0.9, 0.8, 0.7])
    assert v1 == v2, 'CRITICAL: Identical embeddings evaluated as false.'
    assert v1 != v3, 'CRITICAL: Different embeddings evaluated as true.'
