import pytest
import boss_dual_bounds as active_lab

def test_dual_bounds():
    assert abs(active_lab.running_sum - sum(active_lab.scores)) < 1e-9, "The running sum does not match the sum of all elements."
    assert active_lab.min_score == -3.1, "Minimum score tracking failed. Are you updating the min_score when a smaller element is found?"
    assert active_lab.max_score == 4.2, "Maximum score tracking failed. Are you updating the max_score when a larger element is found?"
