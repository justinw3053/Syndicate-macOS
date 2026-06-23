# Textbook: Making Decisions - if/else (KATA_FLOW_01)

## Theoretical Foundation
Python uses `if` and `else` blocks to let the computer make decisions. 
*   **if:** Checks if a condition is True. If it is, the code inside the block executes.
*   **else:** Runs only if the `if` condition was False.

### The Rule of Indentation (4 Spaces)
Unlike other programming languages that use curly braces `{}` to group code, Python relies strictly on **indentation (exactly 4 spaces)**. Any line indented by 4 spaces under an `if` or `else` statement belongs inside that block.

---

## Syntax Anatomy
```python
if score >= 0.5:
    return "PASS"
else:
    return "FAIL"
```

---

## Step-by-Step Exercise Instructions
1. Locate `check_passing_score(score)`.
2. Write an `if` statement to check if `score` is greater than or equal to `0.5`.
3. If True, return `"PASS"`.
4. Write an `else` statement, and return `"FAIL"`.
