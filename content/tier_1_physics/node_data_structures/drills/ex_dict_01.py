# PROBLEM: List of Dictionaries Manipulation
#
# Your Task: Implement `extract_usernames(users: list) -> list`
# Extract and return a list of usernames where 'status' is exactly "active".

def extract_usernames(users: list) -> list:
    active_users = []
    # Step 1: Iterate through user dictionaries in users
    for user in users:
        # Step 2: Check if 'status' is "active"
        if user.get("status") == "active":
            # Step 3: Append 'username' to active_users list
            active_users.append(user.get("username", ""))
    return active_users
