import pytest
import active_lab

def test_get_username():
    res = active_lab.get_username()
    assert isinstance(res, str), "Your username must be text wrapped in quotes!"
    assert len(res) > 0, "Your username cannot be empty!"
