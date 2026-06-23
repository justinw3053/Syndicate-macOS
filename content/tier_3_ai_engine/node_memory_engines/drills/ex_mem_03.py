# PROBLEM: Sliding Window Buffer
#
# sliding window compiles context overlap arrays across history log sequences.
#
# Your Task: Return list of all sub-lists of size 'window_size' stepping with 'stride'.

def sliding_window_buffer(history: list, window_size: int, stride: int) -> list:
    buffers = []
    i = 0
    # Step 1: Iterate using stride jumps
    while i + window_size <= len(history):
        # Step 2: Extract sliding slice window and append
        buffers.append(history[i : i + window_size])
        i += stride
    return buffers
