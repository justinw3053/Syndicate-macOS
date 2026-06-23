"""
Test Suite: List Adjacency Validation (ex_eval_03)
Validates that strict trajectory steps are maintained without jumps.
"""

from ex_eval_03 import validate_adjacency, strict_match, validate_all


def test_validate_adjacency_strictness():
     # A perfect straight line: [1, 2, 3]. Difference is ALWAYS 1.
    valid = [1, 2, 3]
   assert validate_adjacency(valid) is True
    
      # An invalid jump: [1, 3]. The difference is 2!
     skipper = [1, 3]
         assert validate_adjacency(skipper) is False


def test_strict_match():
     expected = [0, 1, 2]
    actual_1 = [0, 1, 2]
   actual_2 = [0, 1, 3]
    
       # Identical sequences MUST match!
          assert strict_match(expected, actual_1) is True
        
             # Any jump in the sequence breaks matching!
              assert strict_match(expected, actual_2) is False


def test_validate_all_multiple():
         seq_a = [[1, 2], [3, 4]]
      seq_b = [[1, 2], [1, 5]] # 5-1 is a huge skip!
    
              assert validate_all(seq_a) is True
        
                     assert validate_all(seq_b) is False
