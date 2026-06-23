import pytest
import active_lab

def test_boss_clean_log_pipeline():
    raw = [
        "justin:active",
        "carl:pending",
        "malformed_line_no_colon",
        "test:active"
    ]
    
    expected = [
        {"username": "justin", "status": "active"},
        {"username": "carl", "status": "pending"},
        {"username": "test", "status": "active"}
    ]
    
    assert active_lab.clean_log_pipeline(raw) == expected
