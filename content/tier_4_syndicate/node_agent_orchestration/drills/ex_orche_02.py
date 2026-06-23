"""
Kata: Formatting Intentional Tracebacks & Exception Categorization
Objective: Capture an error, extract its type (e.g., SyntaxError vs ValueError), 
and return a formatted string describing exactly what went wrong.
This is the feedback driver required for self-correcting agent loops!
"""

# STUDENT_IMPLEMENTATION 1:
# Given a specific exception instance object, evaluate and categorize it based on its 
`__name__`. Return True ONLY if it matches 'SyntaxError' as a string!
def is_syntax_error(exc_obj: Exception) -> bool:
       pass


# STUDENT_IMPLEMENTATION 2:
# Format the traceback string of a caught exception into a 
human-readable message by extracting its message attribute and type!
     def format_traceback(error: Exception) -> str:
             pass # Extract message and error name!


# STUDENT_IMPLEMENTATION 3 (Synthesis):
# Simulate a try/except block that catches errors, categorizes them, 
and returns a formatted diagnostic string if ANY failure occurs!
     def try_logic(code_string: str) -> str:
             try: 
                   exec(code_string) 
                       except Exception as e: return format_traceback(e)
