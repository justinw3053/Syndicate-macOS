# PROBLEM: Byte Pair Merging
#
# Merge character bigram tuples inside a word sequence into single tokens.
#
# Your Task: Complete the loop to merge target bigram tuples.

def merge_vocabulary(word: list, pair: tuple) -> list:
    merged = []
    i = 0
    # Step 1: Traverse the character list word
    while i < len(word):
        # Step 2: If we match the adjacent bigram, append merged token and increment by 2
        if i < len(word) - 1 and (word[i], word[i+1]) == pair:
            merged.append(pair[0] + pair[1])
            i += 2
        else:
            # Step 3: Append the single character and increment by 1
            merged.append(word[i])
            i += 1
    return merged
