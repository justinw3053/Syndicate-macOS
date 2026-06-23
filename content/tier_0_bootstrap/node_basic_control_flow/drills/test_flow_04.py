import pytest
import active_lab

def test_sum_all_numbers():
    assert active_lab.sum_all_numbers([1.5, 2.5, 3.0]) == 7.0
    assert active_lab.sum_all_numbers([]) == 0.0
