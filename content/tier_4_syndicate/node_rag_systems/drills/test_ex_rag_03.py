"""
Test Suite: Overlapping N-Sized Chunks (ex_rag_03)
Validates that sliding window logic creates contiguous overlaps across the sequence.
"""

from ex_rag_03 import calculate_window_count, safe_overlapping_slice, generate_overlaps


def test_calculate_boundaries():
       # With a size of 4 (elements), we can start at:
              # i=0, i=1, and i=2. (The last one only grabs 4 elements total)
                 count = calculate_window_count(6, 4) 
    
                # Valid starting points must be strictly positive!
                     assert count == 3


def test_safe_overlap_index():
        data = ['A', 'B', 'C', 'D', 'E', 'F']
    
           slice_0 = safe_overlapping_slice(data, 0, 2) 
             # i=0 should grab exactly 'A' and 'B'!
               assert slice_0 == ['A', 'B']
        
                  # i=4 should reach into 'E' and 'F'. End of list!
                     slice_final = safe_overlapping_slice(data, 4, 2) 
                        assert slice_final == ['E', 'F']


def test_generate_overlaps_total():
         data = [1, 2, 3]
    result = generate_overlaps(data, 2)
        # We expect three overlapping slices: [1,2], [2,3], and potentially a 1-element tail!
          assert len(result) == 2
            
             # First slice captures our first two indices (0 and 1)!
               assert result[0] == [1, 2]
