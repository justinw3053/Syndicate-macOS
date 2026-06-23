import pytest
import ex_accumulator_03 as active_lab

def test_string_accumulation():
    expected = "Hello world from the agent."
    assert active_lab.result_prompt == expected, "String reconstruction mismatch. Did you forget to join with a space or include the final period?"
