# Issues: Syndicate 3.0 Native macOS Socratic IDE

This roadmap breaks down the production-grade, hardened `PRD.md` into seven vertical, independent, and logically ordered slices of development. Each issue contains explicit, technical Acceptance Criteria.

---

## Issue 1: Foundation Setup & Dynamic Lesson Crawling/Sorting
*   **Description:** Set up the basic macOS project structure and refactor the python parsing helper to recursively discover and numerically sort all 18 Syndicate 3.0 playroom notebooks under `/content/`.
*   **Acceptance Criteria:**
    *   A clean macOS SwiftUI application structure is created.
    *   macOS App Sandboxing is strictly disabled in the entitlements file: `com.apple.security.app-sandbox = NO`.
    *   `backend/content_engine.py` recursively walks `content/` and filters out `.ipynb` files (ignoring hidden check folders and `.eng.ipynb`).
    *   `content_engine.py` implements a robust regex-based float-key extractor (`dir_float`, `file_float`) to ensure `phase_10_syndicate` sorts *after* `phase_9_local`, and `playroom_p1_5_linalg` sorts between `p1` and `p2`.
    *   Running `PYTHONPATH=. .venv/bin/pytest` validates all core parser tests successfully with zero errors.

---

## Issue 2: The Forge Shell: SwiftUI Triple-Pane Window Layout
*   **Description:** Design the premium, dark-themed, translucent native macOS SwiftUI window shell.
*   **Acceptance Criteria:**
    *   The window implements a native macOS triple-pane sidebar-detail-inspector split layout.
    *   The window styling uses the dark-themed, translucent native look (e.g., standard SwiftUI window materials).
    *   **Left Sidebar (Syllabus):** Dynamically displays the sequential list of phases and sub-playbooks fetched from the parsed content model, styled with SF Symbols.
    *   **Center Stage:** Displays two stacked panels: an interactive Markdown lecture viewer on top (using native Markdown rendering), and a Code Stage (text editor pane) on the bottom.
    *   **Right Sidebar (Comms Array):** Displays Carl's chat panel with an input bar and a scrollable message log.

---

## Issue 3: Asynchronous Subprocess Execution with POSIX Process Group Kills & Detach Safety
*   **Description:** Implement Swift's `Process` execution engine to run the Python verification scripts in isolation, safely capturing output logs and preventing CPU spins.
*   **Acceptance Criteria:**
    *   Clicking "Verify" writes the active cell's code to `verify_lab.py` and spawns a background `Process` targeting `/Users/justin/python-ai-academy/.venv/bin/python`.
    *   The subprocess runs asynchronously in a dedicated background `DispatchQueue` to ensure the SwiftUI main thread remains responsive.
    *   Python is invoked with the `-u` flag (`PYTHONUNBUFFERED=1`) to prevent buffer lag.
    *   Chronological logging is enforced at the OS level by merging standard error into standard output (`process.standardError = process.standardOutput`).
    *   `FileHandle.readabilityHandler` streams execution logs. If the incoming data block length is `0` (EOF), the handler is immediately set to `nil` to prevent spinning CPU lock cycles.
    *   All UI state updates are strictly dispatched onto the `@MainActor`.
    *   The process executes inside a new **POSIX Process Group** (using `setpgid`). A **5-second watchdog timer** escalates from `SIGTERM` to `SIGKILL` on the entire group (`-pgid`) on timeout, cleanly killing parent and orphaned child processes.

---

## Issue 4: Hybrid Code Editor & FSEvents Watcher with State Hash Lock
*   **Description:** Build the native code editor in SwiftUI and implement the bi-directional file watcher to support external editing in VS Code/Vim without race conditions.
*   **Acceptance Criteria:**
    *   Selecting a lesson writes the starter code to `active_lab.py` inside the workspace.
    *   The app runs an asynchronous `FSEvents` directory watcher on `active_lab.py` with strict path filtering (`eventPath == active_lab.py`).
    *   SwiftUI's local disk saves are debounced by 1.5 seconds.
    *   A SHA-256 State Hash Match compares the file's current hash against SwiftUI's last written hash to suppress self-save events.
    *   If the file watcher detects an external modification while the local SwiftUI text buffer has unsaved changes, the app displays a non-destructive conflict modal prompting: *"File modified externally. Would you like to Keep My Changes or Load Disk Version?"*.

---

## Issue 5: Local Ollama Comms Array Integration with Loopback IP & Cold Start Gating
*   **Description:** Connect the Comms Array to local Ollama via the high-speed loopback IP, implementing model switching, context packaging, and cold-start progress indicators.
*   **Acceptance Criteria:**
    *   Chat requests query local Ollama using the loopback IP literal `127.0.0.1:11434` to bypass DNS resolution delays.
    *   The UI displays a dropdown listing available local models (by querying `/api/tags` on boot).
    *   The context compiler packages truncated conversation history (last 10 messages), active file code, error logs, and requirements into Carl's prompt.
    *   On boot, the app verifies the presence of both the chat model and the RAG embedding model, alerting the user of any missing local assets before they go offline.
    *   HTTP request timeout is set to 60 seconds. If a model cold-start is detected, the app polls `/api/show` to display an active *"Carl is waking up (loading model)..."* UI loader.

---

## Issue 6: Carl's Self-Updating Long-Term Memory Ledger
*   **Description:** Build the parsing engine that allows Carl to update the student's persistent memory ledger (`.pi/memory.txt` or `.pi/Learning_Memory.md`).
*   **Acceptance Criteria:**
    *   The app dynamically parses incoming chat tokens for `<memory_update>...</memory_update>` tags.
    *   On matching, the app extracts the inner text and appends/updates the local memory ledger file inside `.pi/`.
    *   The memory tags are stripped from the visible chat panel bubble so they remain hidden from the UI.
    *   On subsequent chat turns, the contents of the memory ledger are automatically prepended to the system context prompt.

---

## Issue 7: Hardware-Accelerated Local RAG Daemon over TCP Loopback
*   **Description:** Build the background Python RAG daemon that connects to the SwiftUI app over an ephemeral TCP Loopback port, generating offline vectors via local Ollama.
*   **Acceptance Criteria:**
    *   On application boot, the SwiftUI app spawns a persistent Python RAG daemon.
    *   The Swift parent binds to `127.0.0.1` on port `0` to allocate an ephemeral free port, passing it to the Python daemon as an argument.
    *   Communication is established via a clean JSON-RPC 2.0 protocol over the TCP socket, bypassing Unix Domain Socket (UDS) path length limits.
    *   All Python internal logs and warnings are redirected to `sys.stderr` to keep the TCP socket stream unpolluted.
    *   The Python daemon queries Ollama's local `/api/embeddings` using `nomic-embed-text` to generate vector coordinates, running semantic lookups against `~/Library/Application Support/Syndicate/chroma_db` completely offline.
    *   The Python daemon runs an Orphan Watchdog thread checking `os.getppid() == 1` and exits immediately if it becomes orphaned, preventing zombie background processes.
