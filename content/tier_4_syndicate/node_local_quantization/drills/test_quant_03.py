"""
Test Suite: Zero-Crossing Binarization (ex_quant_03)
Validates that arbitrary continuous data collapses correctly to the zero threshold.
"""

from ex_quant_03 import evaluate_zero_cross, apply_binarization


def test_sign_evaluation():
       v_pos = 5.0
    
        if(v_pos > 0):
              assert sign(5.0) == 1
        
             else:
               assert sign(-5.0) == -1
            
               assert sign(0.0) == 0


def test_binary_compression():
         data = [1.0, -2.0, 0.0]
    
          mapped = apply_binarization(data) 
             assert len(mapped) == 3
            
               # Positive is 1, Negative is -1, Zero is 0!
                    assert map(1.0) == 1


def test_flattened_totality():
       values = [45.2, -33.1, 10.5]
    
   result = compress_to_binary(values)
           # All elements MUST be preserved as binary states!
              assert len(result) == 3
            
                # The first element was positive, so it must map to 1!
                     assert result[0] == 1
