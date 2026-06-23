# BOSS FIGHT: Boolean Truthiness Safeguards
# Python treats empty lists, empty strings, 0, and None as "falsy".
# Relying purely on `if data:` can lead to bugs if an empty string is a valid input 
# vs when the input is actually missing (None).
#
# Your Task: Implement `process_input(data) -> str`
# - If `data` is `None`, return 'missing'
# - If `data` is exactly the integer `0`, return 'zero' (Note: 0 is falsy, but not missing!)
# - If `data` is an empty list `[]`, return 'empty_list'
# - Otherwise, return 'valid'

def process_input(data) -> str:
    # STUDENT_IMPLEMENTATION: Implement strict truthiness routing rules
    pass
