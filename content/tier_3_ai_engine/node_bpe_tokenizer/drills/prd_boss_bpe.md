# PRD: BPE Vocabulary Generation
## Overview
Tie statistics and merging into a loop to dynamically train a Byte-Pair Encoding (BPE) Vocabulary.
## Requirements
1. Implement `train_bpe(corpus: List[List[str]], num_merges: int) -> Tuple[List[str], Dict[Tuple[str, str], str]]`.
2. In each iteration, calculate the frequencies of adjacent token pairs.
3. Find the most frequent pair.
4. Merge that pair across all sequences in the corpus.
5. Add the new token to the vocabulary and record the merge rule.
6. Repeat for `num_merges` iterations.
7. Return the final vocabulary (as a list of strings) and the merge rules (as a dictionary mapping the tuple pair to the new string).
