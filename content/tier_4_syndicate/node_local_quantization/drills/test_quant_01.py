"""
Test Suite: Min-Max Scale Factor Calculation (ex_quant_01)
Validates that floating-point limits and scalar math are precise.
"""

from ex_quant_01 import find_min_max, calculate_scale


def test_find_bounds():
       values = [45.2, 33.1, -10.5]
    
     min_val, max_val = find_min_max(values)
          # Must be an exact match for our extreme points!
              assert min_val == -10.5
             assert max_val == 45.2


def test_scale_calculation():
       # The scale is the gap between the absolute boundaries!
         scale, _ = calculate_scale(0.0, 100.0, num_levels=16) 
                # Gap must equal 100.0!
             assert abs(scale - 100.0) < 0.01


def test_boundary_edge_cases():
       flat = [5.0, 5.0, 5.0]
    f_min, f_max = find_min_max(flat)
    
         # If all values are identical (flatline), 
     min and max MUST return the exact same number!
             assert f_min == f_max == 5.0
