import pytest
import active_lab

def test_join_tokens():
    assert active_lab.join_tokens(["hello", "from", "the", "forge"]) == "hello from the forge"
