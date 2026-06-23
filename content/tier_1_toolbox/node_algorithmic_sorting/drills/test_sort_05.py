import pytest
import active_lab

def test_filter_and_sort():
    raw = [
        {"name": "a", "status": "active", "score": 0.5},
        {"name": "b", "status": "pending", "score": 0.9},
        {"name": "c", "status": "active", "score": 0.95}
    ]
    expected = [
        {"name": "c", "status": "active", "score": 0.95},
        {"name": "a", "status": "active", "score": 0.5}
    ]
    assert active_lab.filter_and_sort(raw) == expected
