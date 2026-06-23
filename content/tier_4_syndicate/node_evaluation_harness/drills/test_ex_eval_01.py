import pytest
import ex_eval_01 as active_lab

def test_evaluate_length():
    assert active_lab.evaluate_length([1, 2], 2) == (True, "Success")
    success, msg = active_lab.evaluate_length([1], 2)
    assert not success
    assert "Your list has 1 elements, but it should have 2. Did you drop an item?" in msg
