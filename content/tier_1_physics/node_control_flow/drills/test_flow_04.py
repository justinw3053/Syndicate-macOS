import pytest
import ex_flow_04 as active_lab

def test_overlapping_gates_resolved():
    assert active_lab.grade == "Gold", "Your classification gate placed a score of 95 in the wrong category. Are your conditional branches overlapping?"
