total = 0
for i in range(1, 6):
    total = i # Attempt to accumulate by assigning directly

print(f"Result: {total}") # Expected 15, but got 5! The state history is wiped out.

# TODO: Correct the loop using the Rosetta Stone equation to accumulate state sequentially.
total = 0
N = 5
# Your loop code here:
for i in range(1, N + 1):
    total += i
    
assert total == (N * (N + 1)) // 2, f"Expected {(N * (N + 1)) // 2}, got {total}"
print("Success! Accumulator pattern mastered.")

# TODO: Write a loop to calculate the factorial of 6.
# Expected output for 6! = 720
factorial = 1

# Your code here:
for i in range(1,7):
    factorial *= i

assert factorial == 720, f"Expected 720, got {factorial}
print(f"Success! 6! is indeed {factorial}.")

# TODO: Write a loop that accumulates tokens into a single prompt string.
tokens = ["The", "quick", "brown", "agent", "jumps", "over", "the", "lazy", "node", ".", "It", "compiled", ",", "sir", "."]
result_prompt = "
# Your accumulator loop here:
punct = [",", "."]
parts = []
for i, token in enumerate(tokens):
    if i > 0 and token not in punct:
        parts.append(f" {token}") # Space before non-punctuation tokens
    else:
        parts.append(token) #no space for first token or punctuation

result_prompt = ''.join(parts) # Join once at the end


expected = "The quick brown agent jumps over the lazy node. It compiled, sir.
assert result_prompt == expected, f"Expected: '{expected}'
Got: '{result_prompt}'
print("Success! String accumulator logic is flawless.")

# TODO: Calculate sum, min, and max in a single loop without built-ins.
scores = [2.3, -1.5, 4.2, 0.0, -3.1, 1.8]
running_sum = 0.0
min_score = float('inf')
max_score = float('-inf')

# Your loop code here:
for score in scores:
    running_sum += score
    if score < min_score:
        min_score = score
    if score > max_score:
        max_score = score


assert abs(running_sum - sum(scores)) < 1e-9
assert min_score == -3.1
assert max_score == 4.2
print(f"Success! Sum: {running_sum}, Min: {min_score}, Max: {max_score}")

# TODO: Accumulate tokens and calculate running USD costs.
interactions = [
    {"prompt": 150, "completion": 45},
    {"prompt": 230, "completion": 110},
    {"prompt": 95, "completion": 30},
    {"prompt": 412, "completion": 220}
]

total_prompt_tokens = 0
total_completion_tokens = 0
total_cost_usd = 0.0

# Your cost tracking loop here:
for interaction in interactions:
    p = interaction.get("prompt", 0)
    c = interaction.get("completion", 0)

    total_prompt_tokens += p
    total_completion_tokens += c
p_cost = total_prompt_tokens * 0.0000015
c_cost = total_completion_tokens * 0.0000020
total_cost_usd = p_cost + c_cost
print(total_prompt_tokens)
print(total_completion_tokens)
print(total_cost_usd)

assert total_prompt_tokens == 887
assert total_completion_tokens == 405
assert abs(total_cost_usd - 0.0021405) < 1e-9
print(f"Success! Total tokens accumulated: {total_prompt_tokens + total_completion_tokens}. USD spent: ${total_cost_usd:.7f}")