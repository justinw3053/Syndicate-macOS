import pytest
import active_lab

def test_filter_positives():
    assert active_lab.filter_positives([1, -5, 2, 0, -3]) == [1, 2]
    assert active_lab.filter_positives([-1, -2]) == []
