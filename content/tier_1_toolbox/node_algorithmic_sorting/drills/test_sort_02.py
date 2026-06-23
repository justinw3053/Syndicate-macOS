import pytest
import active_lab

def test_sort_by_metric():
    raw = [
        {"name": "a", "metric": 0.5},
        {"name": "b", "metric": 0.95},
        {"name": "c", "metric": 0.1}
    ]
    expected = [
        {"name": "b", "metric": 0.95},
        {"name": "a", "metric": 0.5},
        {"name": "c", "metric": 0.1}
    ]
    assert active_lab.sort_by_metric(raw) == expected
