import pytest
import active_lab
def test_scaled_dot_product_attention():
    q = [[1.0, 0.0]]
    k = [[1.0, 0.0], [0.0, 1.0]]
    v = [[10.0], [20.0]]
    output = active_lab.scaled_dot_product_attention(q, k, v)
    assert len(output) == 1
    assert abs(output[0][0] - 13.3015) < 1e-3
