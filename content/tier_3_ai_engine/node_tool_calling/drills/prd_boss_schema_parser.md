# PRD: Signature-to-Schema Parser
Implement function_to_schema(func) -> dict using inspect.
It must parse __name__, __doc__, and type hint annotations, mapping python types (str, int, float, bool) to JSON types (string, integer, number, boolean).
Parameters without defaults must be added to the required array.
