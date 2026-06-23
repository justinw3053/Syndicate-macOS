import pytest
import active_lab

def test_split_parameters():
    assert active_lab.split_parameters("USER:justin|STATUS:active") == ["USER:justin", "STATUS:active"]
