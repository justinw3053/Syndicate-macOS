import pytest
import active_lab

def test_clean_and_pad():
    assert active_lab.clean_and_pad_text("   justin   ") == "----justin"
    assert active_lab.clean_and_pad_text("agent") == "-----agent"
