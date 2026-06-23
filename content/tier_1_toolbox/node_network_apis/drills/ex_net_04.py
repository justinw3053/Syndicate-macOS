# PROBLEM: Managing API Connection Timeout Barriers
#
# Sockets can hang indefinitely if a server is overloaded.
# We enforce connection timeouts by passing the 'timeout' parameter (floats):
#    urllib.request.urlopen(url, timeout=2.5)
# If the timeout limit is exceeded, an socket.timeout (or urllib.error.URLError) is raised.
#
# Your Task: Perform a GET request to 'url' enforcing a 'timeout_seconds' limit.
# If the connection times out, return "timeout_exceeded".

import urllib.request
import urllib.error
import socket

def perform_get_with_timeout(url: str, timeout_seconds: float) -> str:
    try:
        # Step 1: Open URL passing the timeout parameter
        with urllib.request.urlopen(url, timeout=timeout_seconds) as response:
            return response.read().decode("utf-8")
    except (urllib.error.URLError, socket.timeout):
        # Step 2: Handle connection timeout exception gracefully
        return "timeout_exceeded"
