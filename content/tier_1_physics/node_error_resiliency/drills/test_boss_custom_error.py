import pytest
import boss_custom_error as active_lab

def test_rate_limit():
    assert active_lab.check_rate_limit(50) == True, "Valid queries under threshold should return True without throwing exceptions."
