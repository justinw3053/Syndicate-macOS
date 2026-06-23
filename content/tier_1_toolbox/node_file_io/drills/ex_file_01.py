# PROBLEM: Reading Files Securely
#
# We open files cleanly using the `with open(path, "r") as f` statement, which
# guarantees the file is closed automatically even if the code crashes.
#
# Your Task: Read the entire content of the text file at 'file_path' and return it.

def read_text_file(file_path: str) -> str:
    # Step 1: Open file at file_path in read mode "r"
    with open(file_path, "r", encoding="utf-8") as f:
        # Step 2: Read content using f.read() and return it
        content = f.read()
    return content
