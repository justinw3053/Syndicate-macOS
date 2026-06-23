# PROBLEM: Sorting Strings by Length
#
# Your Task: Sort the list of strings 'words' by their character length, from shortest to longest.

def sort_by_length(words: list) -> list:
    # Step 1: Use sorted() with the built-in len function as key
    sorted_words = sorted(words, key=len)
    return sorted_words
