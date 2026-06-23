import pytest
import active_lab

def test_get_first_item():
    assert active_lab.get_first_item(["apple", "banana"]) == "apple"
    assert active_lab.get_first_item([10, 20, 30]) == 10
