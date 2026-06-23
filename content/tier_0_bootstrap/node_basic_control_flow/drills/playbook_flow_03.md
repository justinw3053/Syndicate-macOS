# Textbook: Repeating Actions - for loop (KATA_FLOW_03)

## Theoretical Foundation
A `for` loop repeats a block of code for every item inside a list sequence. It sequentially binds each item in the list to a temporary loop variable.

Example:
```python
for name in ["Carl", "Justin"]:
    print(name)
```

---

## Step-by-Step Exercise Instructions
1. Iterate through the `names` list using a `for` loop: `for name in names:`.
2. Inside the loop, write a conditional check: if the current `name` is equal to `"Justin"`, return `"Found!"` immediately.
3. If the loop completes and "Justin" was never found, return `"Not Found"`.
