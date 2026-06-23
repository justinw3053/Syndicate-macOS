import pytest
import ex_sm_01 as active_lab

def test_transition():
    assert active_lab.transition("idle", "start") == "processing"
    assert active_lab.transition("processing", "finish") == "idle"
    assert active_lab.transition("idle", "fail") == "idle"
