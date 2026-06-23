import pytest
import active_lab

def test_pure_cumulative_sum():
    original = [1, 2, 3, 4]
    result = active_lab.cumulative_sum(original)
    
    assert result == [1, 3, 6, 10], "The math is incorrect. Did you add the current number to the running total?"
    assert original == [1, 2, 3, 4], "You modified the original list! Ensure you are appending to a NEW list instead."
