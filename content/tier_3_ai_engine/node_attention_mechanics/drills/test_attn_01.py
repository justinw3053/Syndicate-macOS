import pytest
import ex_attn_01 as active_lab

def test_scale_scores():
    scores = [10.0, 20.0]
    scaled = active_lab.scale_scores(scores, 100) # sqrt(100) = 10
    assert scaled == [1.0, 2.0], "Did you divide by the square root of the dimension?"
