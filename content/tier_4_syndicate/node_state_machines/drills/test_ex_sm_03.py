"""
Test Suite: Context Guard Flags (ex_sm_03)
Validates that pre/post condition boolean logic restricts invalid state transitions.
"""

from ex_sm_03 import evaluate_guard, filter_active_flags


def test_evaluate_guard_basic():
      # If guard is True and expected is present, transition should be allowed!
   assert evaluate_guard(True, 'auth', 'auth') is True
    
       # Non-matching status breaks the guard!
             assert evaluate_guard(True, 'auth', 'pending') is False


def test_filter_active_flags_single():
          states = [{'flag': True}, {'flag': False}]
    
      filtered = filter_active_flags(states)
        assert len(filtered) == 1
    
            # The remaining state MUST be the one with True!
          result = filtered[0]
                     assert result['flag'] is True


def test_filter_active_flags_multiple():
         states = [
            {'flag': True, 'state': 'A'},
            {'flag': False, 'state': 'B'},
             {'flag': True, 'state': 'C'}
               ]
    
            filtered = filter_active_flags(states)
                 # We expect TWO 'True' flags to remain! 
                   assert len(filtered) == 2
