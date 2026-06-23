import pytest
import active_lab

def test_find_justin():
    assert active_lab.find_justin(["Carl", "Justin", "Leonidas"]) == "Found!"
    assert active_lab.find_justin(["Carl", "Leonidas"]) == "Not Found"
