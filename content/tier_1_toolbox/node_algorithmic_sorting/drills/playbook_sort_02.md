# Textbook: Sorting Custom Objects (KATA_SORT_02)

## Theoretical Foundation
When models return structured responses or retrieval logs, they contain keys like `score` or `metric`. Sorting arrays of dictionary blocks by custom keys is a daily requirement for AI systems. We use lightweight, inline anonymous `lambda` functions to point the sorter directly to the metric key.

---

## Syntax Anatomy
```python
sorted_data = sorted(list_dicts, key=lambda d: d["score"])
```

---

## Step-by-Step Exercise Instructions
1. Call `sorted(items, key=lambda x: x["metric"], reverse=True)`.
2. Return the sorted list of dictionary records.
