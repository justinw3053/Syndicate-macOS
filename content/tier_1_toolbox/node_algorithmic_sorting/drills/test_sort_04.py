import pytest
import active_lab

def test_sort_by_length():
    raw = ["apple", "hi", "assistant", "code"]
    assert active_lab.sort_by_length(raw) == ["hi", "code", "apple", "assistant"]
