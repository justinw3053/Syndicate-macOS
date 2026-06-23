import pytest
import active_lab

def test_get_prefix_slice():
    assert active_lab.get_prefix_slice("assistant_prompt", 9) == "assistant"
    assert active_lab.get_prefix_slice("hi", 10) == "hi"
