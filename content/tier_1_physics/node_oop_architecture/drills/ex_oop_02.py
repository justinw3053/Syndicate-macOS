# PROBLEM: Class State Mutation Leakage
#
# Your Task: Complete the ConfigManager class. Ensure values don't leak into class-level state.

class ConfigManager:
    def __init__(self, initial_settings: dict = None):
        # Step 1: Safely initialize self.settings as a copy of initial_settings or empty dict
        self.settings = (initial_settings or {}).copy()
        
    def update_setting(self, key: str, value):
        # Step 2: Update local settings instance attribute
        self.settings[key] = value
        
    def get_setting(self, key: str, default=None):
        # Step 3: Get setting safely with default
        return self.settings.get(key, default)
