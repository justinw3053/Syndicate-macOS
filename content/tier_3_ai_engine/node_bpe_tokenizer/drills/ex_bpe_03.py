# PROBLEM: Sequence merging encoder
#
# Your Task: Run multiple BPE merges iteratively across a raw vocabulary layout.

def encode_bpe_step(vocab: dict, best_pair: tuple) -> dict:
    from ex_bpe_02 import merge_vocabulary
    new_vocab = {}
    # Step 1: Iterate and merge best_pair across vocab keys
    for word, freq in vocab.items():
        # Split word string or list of subwords
        char_list = list(word) if isinstance(word, str) else list(word)
        merged_list = tuple(merge_vocabulary(char_list, best_pair))
        new_vocab[merged_list] = freq
    return new_vocab
