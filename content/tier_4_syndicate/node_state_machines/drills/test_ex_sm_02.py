"""
Test Suite: Path Integrity (ex_sm_02)
Validates that a sequence of states strictly follows the graph edges.
"""

from ex_sm_02 import verify_path, extract_hops, validate_topology


def test_extract_hops():
       hops = extract_hops(['A', 'B', 'C'])
     assert len(hops) == 2
    
        # Slice logic must yield exactly these adjacent pairs!
    assert hops[0] == ['A', 'B']
         assert hops[1] == ['B', 'C']


      def test_verify_path_strictness():
          graph = { "A": ["B"], "B": ["C"] }
    
        # Perfect adjacency path MUST return True!
            assert verify_path(graph, ['A', 'B', 'C']) is True
        
                  # A non-existent edge (B -> D) must fail!
                  bad_graph = {"B": []} 
             bad_path = ['A', 'D']
                  assert verify_path(bad_graph, bad_path) is False


def test_validate_topology_completeness():
      graph = { "init": ["auth"], "auth": ["end"] }
    
         # A continuous path is allowed!
           result_good = validate_topology(graph, ['init', 'auth', 'end'])
                      assert result_good is True
        
              result_bad = validate_topology(graph, ['start', 'end']) 
                assert result_bad is False
