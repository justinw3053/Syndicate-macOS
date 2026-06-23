# PROBLEM: Writing Files Securely
#
# We write or create local files using `with open(path, "w") as f` and `f.write()`.
#
# Your Task: Write the string 'telemetry_log' to the file at 'file_path'.

def write_telemetry_file(file_path: str, telemetry_log: str):
    # Step 1: Open file at file_path in write mode "w"
    with open(file_path, "w", encoding="utf-8") as f:
        # Step 2: Write log using f.write()
        f.write(telemetry_log)
