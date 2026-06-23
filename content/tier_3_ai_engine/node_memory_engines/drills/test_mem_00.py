import pytest
import ex_mem_00 as active_lab

def test_truncate_oldest():
    hist = [1, 2, 3, 4, 5]
    assert active_lab.truncate_oldest(hist, 3) == [3, 4, 5]
    assert active_lab.truncate_oldest(hist, 10) == [1, 2, 3, 4, 5]
