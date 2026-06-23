import pytest
import ex_rag_01 as active_lab

def test_simple_chunk():
    res = active_lab.simple_chunk("hello world", 5)
    assert res == ["hello", " worl", "d"]
