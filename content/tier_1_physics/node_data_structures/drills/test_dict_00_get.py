import pytest
import ex_dict_00_get as active_lab

def test_increment_count():
    freqs = {}
    active_lab.increment_count(freqs, "apple")
    assert freqs["apple"] == 1
    active_lab.increment_count(freqs, "apple")
    assert freqs["apple"] == 2
