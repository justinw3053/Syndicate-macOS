import pytest
import ex_prob_02 as active_lab

def test_stable_softmax():
    # Large numbers that would normally cause OverflowError in exp()
    logits = [1000.0, 1000.0, 1000.0]
    probs = active_lab.stable_softmax(logits)
    assert abs(probs[0] - 0.333333) < 1e-4, "Did you subtract the max logit properly to prevent overflow?"
