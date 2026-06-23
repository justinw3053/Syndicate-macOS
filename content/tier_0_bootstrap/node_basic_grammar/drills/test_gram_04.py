import pytest
import active_lab

def test_get_simple_list():
    res = active_lab.get_simple_list()
    assert res == ["hello", "world"], "Make sure your list is exactly [\"hello\", \"world\"]"
