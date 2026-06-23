import pytest
import ex_accumulator_02 as active_lab

def test_factorial():
    assert active_lab.factorial == 720, "Factorial check failed. Ensure you are multiplying by the loop variable sequentially."
