# Product Requirement Document (PRD) - Boss Fight: Clean Log Pipeline

## Objective
Build a zero-dependency text parser to clean raw string log list streams.

## Input Format
A list of strings. Each line represents a record in the format: `"username:status"`.
Example: `"justin:active"`

## Acceptance Criteria
1.  **Iterative Loop:** Loop over `raw_logs` using a `for` loop.
2.  **Structural Check:** Check if the line contains a colon `:` character. If it is missing, skip the line.
3.  **Splitting:** Split each line by `:` into `parts`. Verify we got exactly 2 parts (username and status).
4.  **Dictionary Construction:** Compile the parsed values into a dictionary:
    `{"username": parts[0], "status": parts[1]}`.
5.  **Output:** Append the parsed records to a list and return the final list.
