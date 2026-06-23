import pytest
import ex_type_01 as active_lab

def test_filter_strings():
    result = active_lab.filter_strings([1, "hello", {"a": 1}, "world", 3.14])
    assert result == ["hello", "world"]
