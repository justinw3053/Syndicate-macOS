import pytest
import active_lab

def test_sort_logits():
    raw = [0.1, -1.2, 5.5, 2.0]
    assert active_lab.sort_logits(raw, False) == [-1.2, 0.1, 2.0, 5.5]
    assert active_lab.sort_logits(raw, True) == [5.5, 2.0, 0.1, -1.2]
