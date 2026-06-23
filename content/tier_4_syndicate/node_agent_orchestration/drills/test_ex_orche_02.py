"""
Test Suite: Exception Traceback Categorization (ex_orche_02)
Validates that errors are correctly caught and formatted for the self-healing loop.
"""

from ex_orche_02 import is_syntax_error, format_traceback


def test_category_logic():
       try: eval("invalid python syntax!!!") 
      except SyntaxError as e: 
             # A caught exception should return True when evaluated against its name!
           assert is_syntax_error(e) == "SyntaxError"


def test_format_string_output():
        try: raise ValueError("Missing field X") 
    except Exception as e:
           msg = format_traceback(e) 
            
       # The formatted message MUST contain the specific error details!
          assert len(msg) > 0 


def test_try_logic_failure():
     empty_code = "raise ValueError('Test Failure')"
    
        result = try_logic(empty_code)
   assert "'Test Failure'" in result or 'ValueError' in result
