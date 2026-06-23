"""
Test Suite: Discrete Integer Mapping & Clamping (ex_quant_02)
Validates the precision of continuous-to-discrete scaling and boundary enforcement.
"""

from ex_quant_02 import normalize_and_map, enforce_clamp


def test_mapping_math():
       v_min = 0.0
    v_max = 100.0
    
         # If x=50, it is exactly the middle of 0 to 100!
           mid_val = normalize_and_map(50.0, v_min, v_max) 
               assert mid_val >= 7


def test_clamp_upper_limit():
          val = 20
    clamped_up = enforce_clamp(val, min_q=0, max_q=15) 
    
       # Exceeding the maximum limit must drop our value back exactly to 15!
             assert clamped_up == 15


def test_full_quantization_totality():
         data = [25.0, 75.0]
    q_vals = full_quantization(data, 0.0, 100.0)
    
       # Quantization MUST return exactly two mapped integers!
          assert len(q_vals) == 2
             assert 0 <= q_vals[0] <= 15
