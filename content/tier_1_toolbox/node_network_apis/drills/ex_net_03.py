# PROBLEM: API HTTP Response Status Validation
#
# HTTP status codes declare request success or failure (e.g., 200 = Success, 404 = Not Found, 500 = Server Error).
# We read the response status code using the `.status` (or `.getcode()`) attribute.
#
# Your Task: Perform a GET request to 'url'. Return the HTTP status code (integer).

import urllib.request

def get_http_status_code(url: str) -> int:
    try:
        # Step 1: Open the URL inside a with block
        with urllib.request.urlopen(url) as response:
            # Step 2: Extract response status code
            return response.status
    except urllib.error.HTTPError as e:
        # Step 3: If an HTTP error occurs (like 404/500), return its status code
        return e.code
