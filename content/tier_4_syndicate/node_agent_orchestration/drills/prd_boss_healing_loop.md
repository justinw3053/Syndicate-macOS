# PRD: Self-Correcting Execution Loops
Multi-agent orchestration requires robust validation loops.
Implement `execute_and_heal(code_str: str) -> str`.
Use `exec(code_str, {})`. If it succeeds, return `"SUCCESS"`.
If it fails, catch the Exception, format the traceback using `traceback.format_exc()`, and return `"FAILED: " + tb`.
