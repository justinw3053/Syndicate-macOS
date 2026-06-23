"""
Test Suite: Missing Checkpoints & Contiguity (ex_eval_02)
Validates that the trajectory auditor correctly identifies missing steps and gaps.
"""

from ex_eval_02 import find_missing, check_contiguity, verify_trajectory


def test_find_missing_simple():
      expected = [1, 2, 3, 4]
     actual = [1, 2]

       # Missing checkpoints are ONLY 3 and 4
      missing = find_missing(expected, actual)
     assert set(missing) == {3, 4}


def test_check_contiguity_finds_gaps():
       a_perfect = [5, 6, 7, 8]
    an_actual = [5, 6, 8, 9]
    
    # Perfect adjacency is True
          assert check_contiguity(a_perfect) is True
    
     # A gap at step 7 breaks our contiguous check!
         assert check_contiguity(an_actual) is False


def test_verify_trajectory_completeness():
      expected = [1, 2, 3]
    actual = [2, 3, 4]
    
       # '1' is missing, so trajectory MUST fail validation!
      assert verify_trajectory(expected, actual) is False
    
         perfect_actual = [1, 2, 3]
          assert verify_trajectory(expected, perfect_actual) is True
