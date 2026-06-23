import pytest
import boss_nearest_neighbor as active_lab

def test_find_nearest():
    db = [[0, 0], [10, 10], [3, 4]]
    assert active_lab.find_nearest([2, 2], db) == [3, 4], "Failed to find nearest vector."
    assert active_lab.find_nearest([1, 1], []) == [], "Empty database should return empty list."
