# PRD: Strict JSON Schema Validator
Implement `validate_tool_arguments(arguments: dict, schema: dict) -> list[str]`.
Returns a list of error strings. Check for required keys, evaluate data types against `schema["properties"]`, and apply `min_val` limits safely.
