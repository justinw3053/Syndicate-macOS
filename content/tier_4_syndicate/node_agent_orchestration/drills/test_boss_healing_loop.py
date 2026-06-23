import pytest
import active_lab

def test_healing_loop():
    good_code = "x = 1 + 1"
    bad_code = "x = 1 / 0"
    
    assert active_lab.execute_and_heal(good_code) == "SUCCESS"
    res = active_lab.execute_and_heal(bad_code)
    assert "ZeroDivisionError" in res
    assert "FAILED" in res
