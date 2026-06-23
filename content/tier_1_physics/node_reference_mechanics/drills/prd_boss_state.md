# PRD: StateManager

## Overview
The `StateManager` class must hold an internal configuration dictionary.

## Requirements
1. **Initialization**: `StateManager(initial_state: dict)`
2. **Retrieval**: `get_state() -> dict`
   - Must return a copy of the state. Modifying the returned dictionary must NOT modify the internal state.
3. **Updating**: `update_state(new_state: dict)`
   - Must completely replace the internal state with `new_state`. Modifying `new_state` after calling `update_state` must NOT modify the internal state.

## Rules
- You may use the standard library `copy` module.
- Do not use any other imports.
