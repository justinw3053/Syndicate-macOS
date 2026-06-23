# BOSS FIGHT: Schema Validation Contract
# Before sending data to an LLM, we must ensure it matches the expected schema.
# 
# Your Task: Implement `validate_tool_schema(payload: dict) -> bool`
# The payload MUST be a dictionary containing exactly the following keys:
# - 'id': must be a string
# - 'name': must be a string
# - 'params': must be a list
#
# Return True if the payload matches the contract exactly. 
# Return False if keys are missing, extra keys exist, or if types do not match.

def validate_tool_schema(payload: dict) -> bool:
    # STUDENT_IMPLEMENTATION: Implement strict dictionary validation
    pass
