import pytest
import active_lab

def test_argmax():
    assert active_lab.extract_argmax_index([0.1, 5.5, -2.0, 1.2]) == 1
    assert active_lab.extract_argmax_index([]) == -1
