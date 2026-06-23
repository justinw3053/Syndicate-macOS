import pytest
import active_lab

def test_add_numbers():
    assert active_lab.add_numbers(5, 10) == 15
    assert active_lab.add_numbers(-3, 3) == 0
