import pytest
import active_lab

def test_multiply_values():
    assert active_lab.multiply_values(5, 3) == 15
    assert active_lab.multiply_values(-2, 4) == -8
