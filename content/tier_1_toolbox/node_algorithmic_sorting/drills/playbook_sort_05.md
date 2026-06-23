# Textbook: Compound Filtering and Sorting (KATA_SORT_05)

## Theoretical Foundation
This combines our filtering loop/comprehension pattern with custom key sorting. We first filter out any invalid or inactive telemetry records, then sort the remaining valid records by confidence score to isolate top hits.

---

## Step-by-Step Exercise Instructions
1. Filter the `items` list using a loop or comprehension to keep only dictionary items where `.get("status") == "active"`.
2. Sort that filtered list using `sorted(..., key=lambda x: x.get("score"), reverse=True)`.
3. Return the final sorted list of active records.
