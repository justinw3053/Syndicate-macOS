# PROBLEM: Mocking External Server Requests Safely
#
# In unit testing, we mock network calls to prevent slow, flaky external calls.
#
# Your Task: Return a mock dictionary simulating a standard server response.
# Mock output: {"status": "mock_success", "payload": data}

def mock_server_query(data: dict) -> dict:
    # Step 1: Wrap input data in a standard simulated payload dictionary structure
    simulated_response = {
        "status": "mock_success",
        "payload": data
    }
    return simulated_response
