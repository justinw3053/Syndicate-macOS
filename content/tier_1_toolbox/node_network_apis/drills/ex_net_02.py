# PROBLEM: POSTing JSON Payloads (No Imports)
#
# To POST JSON data, we serialize our dictionary to a JSON string, encode it to bytes,
# and configure a Request object with headers and method:
#    import urllib.request
#    import json
#    data = json.dumps(payload).encode("utf-8")
#    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
#
# Your Task: Perform a POST request to 'url' transmitting the 'payload' dictionary. 
# Decode and return the response string.

import urllib.request
import json

def perform_http_post(url: str, payload: dict) -> str:
    # Step 1: Serialize payload to a JSON string and encode to UTF-8 bytes
    post_data = json.dumps(payload).encode("utf-8")
    
    # Step 2: Construct the Request object with headers and POST method
    req = urllib.request.Request(
        url,
        data=post_data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    # Step 3: Open request, read and decode response, then return it
    with urllib.request.urlopen(req) as response:
        content = response.read().decode("utf-8")
    return content
