# PROBLEM: Replacing Substrings
#
# We rewrite words or anonymize keys using the `.replace(old, new)` method.
# Example: `"hello world".replace("world", "student")` returns `"hello student"`.
#
# Your Task: Complete the function to replace all occurrences of "Leonidas" with "Justin".

def replace_student_name(text: str) -> str:
    # Step 1: Replace "Leonidas" with "Justin" using .replace()
    cleaned_text = text.replace("Leonidas", "Justin")
    return cleaned_text
