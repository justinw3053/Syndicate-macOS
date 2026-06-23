import pytest
import ex_accumulator_01 as active_lab

def test_accumulator():
    assert active_lab.total == 15, "The running sum is incorrect. Did you reassign the variable instead of accumulating (total += i)?"
