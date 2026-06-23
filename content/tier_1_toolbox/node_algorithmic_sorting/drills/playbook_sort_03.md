# Textbook: Extracting Max Indexes (KATA_SORT_03)

## Theoretical Foundation
In greedy token generation (Argmax sampling), we don't just want to know the maximum probability value—we need to know **which token position** generated that maximum value so we can decode the matching character word from our vocabulary list!

---

## Step-by-Step Exercise Instructions
1. Guard against empty lists: if `logits` is empty, return `-1`.
2. Locate the maximum value in the list using `max(logits)`.
3. Locate its index using `logits.index(max_val)`.
4. Return the index integer.
