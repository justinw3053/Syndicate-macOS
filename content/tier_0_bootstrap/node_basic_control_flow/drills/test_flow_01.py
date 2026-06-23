import pytest
import active_lab

def test_check_passing_score():
    assert active_lab.check_passing_score(0.7) == "PASS"
    assert active_lab.check_passing_score(0.3) == "FAIL"
    assert active_lab.check_passing_score(0.5) == "PASS"
