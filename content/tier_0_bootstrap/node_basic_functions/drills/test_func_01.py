import pytest
import active_lab

def test_get_model_name():
    assert active_lab.get_model_name({"model": "qwen-2.5", "temp": 0.7}) == "qwen-2.5"
