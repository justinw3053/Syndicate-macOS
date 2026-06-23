import pytest
import active_lab

def test_return_scope():
    ans = active_lab.square(5)
    assert ans is not None, "The function returned None. Did you forget the 'return' keyword?"
    assert ans == 25.0, f"Expected 25.0, got {ans}"
