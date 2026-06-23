import pytest
import ex_prob_01 as active_lab

def test_softmax_temp():
    logits = [2.0, 1.0, 0.1]
    probs = active_lab.softmax_temp(logits, 1.0)
    assert abs(sum(probs) - 1.0) < 1e-4, "Probabilities must sum to exactly 1.0."
    assert probs[0] > probs[1] and probs[1] > probs[2], "Higher logits must result in higher probabilities."
