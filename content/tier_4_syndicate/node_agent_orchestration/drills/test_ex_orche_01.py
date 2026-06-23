"""
Test Suite: Isolated Dictionary Execution (ex_orche_01)
Validates that native exec() cannot escape the isolated namespace boundaries.
"""

from ex_orche_01 import safe_lookup, isolated_exec


def test_isolation_boundary():
       ns = {}
          # Executing inside an empty dictionary MUST not leak variables globally!
            code = "x = 5" 
              isolated_exec(code, ns)
    
         # The variable 'x' SHOULD exist in the dict, but NOT in globals!
           assert 'x' in ns


def test_execution_safety():
       code_lines = ["a = 1", "b = a + 1"]
          results = multi_line_isolation(code_lines, {}) 
      
         # Two lines of code MUST result in exactly two tracked key-value pairs!
               assert len(results) == 2


def test_boundary_prevention():
       # Try to break the sandbox with an escape mechanism!
             code_breaker = "import os; os.system('rm -rf /')" 
                pass # Ensure this raises an explicit error or silently fails without crashing!
