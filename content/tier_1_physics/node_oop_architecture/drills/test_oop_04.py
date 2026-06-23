import pytest
import active_lab
def test_clean_representation():
    v1 = active_lab.Embedding([0.1, 0.2, 0.3])
    assert repr(v1) == 'Embedding(dims=3)', f"Expected 'Embedding(dims=3)', got '{repr(v1)}'"
