# PROBLEM: Trimming & Padding Text
#
# Strings often carry trailing whitespaces, newlines, or require padding.
# In Python, we clean edges using `.strip()`, `.lstrip()`, or `.rstrip()`.
# To pad text to a exact length, we use `.ljust(width, char)` or `.rjust(width, char)`.
#
# Your Task:
# 1. Trim all leading and trailing whitespaces from 'raw_text'.
# 2. Left-pad the result to exactly 10 characters using the dash character '-' as padding.

def clean_and_pad_text(raw_text: str) -> str:
    # Step 1: Trim whitespaces using .strip()
    trimmed = raw_text.strip()
    
    # Step 2: Left-pad to width 10 with '-' using .rjust()
    padded = trimmed.rjust(10, "-")
    return padded
