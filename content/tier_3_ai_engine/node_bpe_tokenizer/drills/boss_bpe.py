# BOSS FIGHT: BPE Vocabulary Generation
# Combine the statistical frequency counting and the merging mechanism to "train" a tokenizer.
#
# Your Task: Implement train_bpe(corpus: list[list[str]], num_merges: int) -> list[list[str]]
# 1. Loop num_merges times.
# 2. Inside the loop, get the frequency stats of all pairs.
# 3. If there are no pairs, break early.
# 4. Find the pair with the highest frequency.
# 5. Merge that pair in the corpus.
# 6. Return the fully merged corpus.

def get_stats(corpus: list[list[str]]) -> dict[tuple[str, str], int]:
    pass

def merge_pair(pair: tuple[str, str], corpus: list[list[str]]) -> list[list[str]]:
    pass

def train_bpe(corpus: list[list[str]], num_merges: int) -> list[list[str]]:
    # STUDENT_IMPLEMENTATION: Tie statistics and merging into a loop
    pass
