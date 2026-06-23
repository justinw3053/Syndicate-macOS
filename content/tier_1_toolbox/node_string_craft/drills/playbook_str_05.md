# Textbook: Safe Substring Slicing (KATA_STR_05)

## Theoretical Foundation
Slicing strings is used to parse headers, isolate message prefixes, or truncate prompts to fit inside smaller console views. Python's slice syntax `[start:stop]` is secure and does not throw IndexErrors if the boundaries overflow the container capacity.

---

## Step-by-Step Exercise Instructions
1. Slice the `prompt` string from index 0 to `n` using `prompt[:n]`.
2. Return the sliced substring.
