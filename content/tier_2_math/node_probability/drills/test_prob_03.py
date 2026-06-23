import pytest
import ex_prob_03 as active_lab

def test_mask_top_k():
    probs = [0.1, 0.6, 0.2, 0.05, 0.05]
    masked = active_lab.mask_top_k(probs, 2)
    assert masked == [0.0, 0.6, 0.2, 0.0, 0.0], "Top-K masking logic is incorrect. Only top 2 elements should remain."
