import pytest
import ex_oop_02 as active_lab

def test_internal_dispatch():
    bucket = active_lab.TokenBucket()
    bucket.add_tokens(150)
    assert bucket.total_tokens == 150, "Total tokens did not accumulate correctly."
    assert bucket.total_cost == 3.0, "Cost computation mismatch. Did you remember to delegate cost calculation internally via self._calculate_cost(count)?"
