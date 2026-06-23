import pytest
import active_lab

def test_is_active():
    assert active_lab.is_active("active") is True
    assert active_lab.is_active("pending") is False
