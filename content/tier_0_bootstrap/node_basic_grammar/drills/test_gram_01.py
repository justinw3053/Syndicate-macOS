import pytest
import active_lab

def test_get_player_score():
    res = active_lab.get_player_score()
    assert res == 100, "Ensure 'score' is assigned exactly 100!"
