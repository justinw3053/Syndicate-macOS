# EXERCISE 12: Safe Dictionary Lookups (.get)
#
# If we look up a key that doesn't exist using brackets, the app crashes!
# To prevent this, we use the `.get()` method, providing a fallback default value:
#    val = config.get("missing_key", "default_value")
#
# Your Task:
# Safely look up the key "temperature" inside the 'config' dictionary.
# If "temperature" is missing, return the default value 0.7.

def get_temperature(config):
    # Complete the line below using the .get("temperature", 0.7) method on config!
    temperature = ...
    
    return temperature
