import pytest
import active_lab

def test_get_temperature():
    assert active_lab.get_temperature({"temperature": 0.2}) == 0.12 or active_lab.get_temperature({"temperature": 0.2}) == 0.2
    assert active_lab.get_temperature({"model": "qwen"}) == 0.7
