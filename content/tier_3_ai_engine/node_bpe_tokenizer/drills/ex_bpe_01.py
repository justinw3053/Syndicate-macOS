# PROBLEM: Count Character Bigrams
#
# Count the frequencies of adjacent pairs of character tokens in a word dataset.
#
# Your Task: Return dictionary mapping character bigram tuples to occurrence counts.

def count_bigrams(words: dict) -> dict:
    frequencies = {}
    # Step 1: Iterate through words and their frequency counts
    for word, word_freq in words.items():
        # Step 2: Loop through characters in the word to form adjacent pairs
        for i in range(len(word) - 1):
            pair = (word[i], word[i+1])
            # Step 3: Accumulate counts into frequencies
            frequencies[pair] = frequencies.get(pair, 0) + word_freq
    return frequencies
