# Product Requirement Document (PRD) - Boss Fight: Local Document Scraper

## Objective
Build a local document scraping and database compilation pipeline. The pipeline recursively scans folders for raw `.txt` documents, cleans the strings, simulates metadata API association, and serializes the structured records into a static JSON database file.

## Input Requirements
*   `workspace_dir`: The root directory to scan recursively.
*   `metadata_api_url`: A dummy metadata API endpoint string to attach to records.
*   `output_filepath`: The destination file path where the final compiled JSON database will be written.

## Acceptance Criteria
1.  **Recursive Search:** Traverse the entire `workspace_dir` directory tree recursively, identifying all files ending in `.txt`.
2.  **String Sanitization:** 
    *   Trim all leading and trailing whitespaces.
    *   Replace any carriage return (`\r`) or newline (`\n`) characters with a single space `" "` to flatten text lines.
3.  **Structured Record Construction:** Compile each file into a structured dictionary:
    *   `id`: An incremental integer ID.
    *   `file_name`: The filename string.
    *   `file_path`: The absolute path to the file.
    *   `content`: The sanitized content string.
    *   `meta`: A dictionary containing `source_api` and `char_count` (character length of sanitized content).
4.  **JSON Serialization:** Write the compiled list of records as indented, formatted JSON to the `output_filepath`. Create any parent directories if missing.
5.  **Output:** Return the count of successfully processed documents as an integer.
