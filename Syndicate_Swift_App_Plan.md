# Syndicate 3.0: Native macOS App Blueprint

## 🎯 The Vision
Convert the raw, terminal-based "Syndicate 3.0" Python curriculum into a premium, standalone macOS application designed for an adult developer. The app will serve as a dedicated, AI-powered IDE for learning Generative AI architecture from first principles.

## 🏗 Core Architecture Pivot

### 1. The Execution Engine: Native Python Interop
*   **Abandon:** WebAssembly (Pyodide) and Flask backends.
*   **Adopt:** `PythonKit` or Swift `Process()` API.
*   **Why:** For an adult developer on a trusted machine, we do not need browser sandboxing. Native execution hooks directly into the local `venv`, runs `pytest` natively, and executes Python code instantly without overhead.

### 2. The AI Engine: Apple Silicon MLX
*   **Abandon:** Background HTTP server daemons (Ollama).
*   **Adopt:** `mlx-swift`.
*   **Why:** Embed the "Sebastian" Socratic tutor directly into the Swift application natively. Runs bare-metal on Apple Silicon unified memory for maximum performance, offline capability, and zero external dependencies.

### 3. The UI/UX: The "Adult" Interface
*   **Aesthetic:** Clean, minimalist macOS native (San Francisco typography, SF Symbols, translucency, dark mode).
*   **Layout:**
    *   **Left Sidebar:** Syllabus map (Prep Phase to Phase 10) acting as the curriculum progression tree.
    *   **Center Stage (The Forge):** A native code editor pane with rich Markdown rendering above it for the "Discovery Lab" interactive lectures.
    *   **Right Panel (Comms Array):** Native MLX-powered chat interface. Crucially, the chat context will automatically read the active state of the Center Stage editor to provide seamless Socratic guidance.

## 🚀 Next Steps
1. Initialize the macOS Swift project.
2. Establish the `PythonKit` bridge to the local Syndicate Python virtual environment.
3. Integrate the `mlx-swift` package and load a local model.
4. Build the core UI shell.
