import pytest
import boss_transpose as active_lab

def test_transpose():
    matrix = [[1, 2], [3, 4], [5, 6]]
    ans = active_lab.transpose(matrix)
    assert ans == [[1, 3, 5], [2, 4, 6]], "Matrix transposition failed."
    assert active_lab.transpose([]) == []
