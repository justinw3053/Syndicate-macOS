import pytest
import ex_vector_03 as active_lab

def test_dot_product():
    assert active_lab.dot_product([1, 2, 3], [4, 5, 6]) == 32.0, "Math is incorrect. Expected (1*4 + 2*5 + 3*6) = 32"
    
    with pytest.raises(ValueError, match="length"):
        active_lab.dot_product([1, 2], [1, 2, 3])
