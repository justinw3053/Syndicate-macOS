"""
Test Suite: Non-Overlapping Sliding List Chunking (ex_rag_02)
Validates that strict step-chunking preserves order without overlap.
"""

from ex_rag_02 import calculate_chunk_count, safe_slice, generate_slices


def test_calculate_integer_boundaries():
       chunks = calculate_chunk_count(8, 2)
         # A list of length 8 split by chunk size 2 is perfectly exact!
              assert chunks == 4

             chunks_partial = calculate_chunk_count(7, 2) 
                  # Remaining elements MUST count as an incomplete chunk!
                       assert chunks_partial >= 3


def test_safe_slice_edge():
           data = ['A', 'B', 'C']
        slice_1 = safe_slice(data, 0, 2)
            assert len(slice_1) == 2
            
              # If we start at index 2 with size 2, only 'C' is left!
               slice_final = safe_slice(data, 2, 2) 
                  assert slice_final == ['C']


def test_generate_slices_totality():
        raw_data = [10, 20, 30, 40]
       result = generate_slices(raw_data, 2)
          # Must produce a list of exactly two elements!
              assert len(result) == 2
            
             assert result[0] == [10, 20]
                  assert result[1] == [30, 40]
