# PROBLEM: HTTP GET Requests (No Imports)
#
# To perform GET requests in pure Python, we use the standard urllib library:
#    import urllib.request
#    with urllib.request.urlopen(url) as response:
#        html = response.read().decode('utf-8')
#
# Your Task: Query 'url' using GET, read the response, decode to UTF-8 string, and return it.

import urllib.request

def perform_http_get(url: str) -> str:
    # Step 1: Open the URL using urllib.request.urlopen() inside a with-context
    with urllib.request.urlopen(url) as response:
        # Step 2: Read and decode the response bytes to a UTF-8 string, then return it
        content = response.read().decode("utf-8")
    return content
