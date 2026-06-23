import pytest
import ex_vector_04 as active_lab

def test_euclidean_distance():
    # 3-4-5 triangle logic
    ans = active_lab.euclidean_distance([0, 0], [3, 4])
    assert abs(ans - 5.0) < 1e-9, f"Expected 5.0, got {ans}. Did you remember to take the square root?"
