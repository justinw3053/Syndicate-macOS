import pytest
import active_lab

def test_add_eof_token():
    assert active_lab.add_eof_token(["hello", "world"]) == ["hello", "world", "EOF"]
