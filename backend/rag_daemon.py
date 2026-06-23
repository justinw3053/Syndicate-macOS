import sys
import os
import socket
import json
import threading
import time
import urllib.request
import urllib.error

# Force all warnings and standard library logs to stderr to keep the TCP channel unpolluted
sys.stdout = sys.stderr

def get_chroma_client():
    """Dynamically resolves the ChromaDB path across environments."""
    try:
        import chromadb
        # Fallback to the active user's RAG directory if it exists, otherwise use standard App Support
        default_vault_path = os.path.join(os.path.expanduser("~"), "RAG", "openforge_chroma_db")
        if os.path.exists(default_vault_path):
            path = default_vault_path
        else:
            home = os.path.expanduser("~")
            path = os.path.join(home, "Library", "Application Support", "OpenForge", "chroma_db")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            
        return chromadb.PersistentClient(path=path)
    except Exception as e:
        sys.stderr.write(f"ChromaDB initialization error: {e}\n")
        return None

def query_ollama_embedding(text, model="nomic-embed-text"):
    """Queries Ollama's local embedding endpoint using pure Python urllib (zero dependencies)."""
    url = "http://127.0.0.1:11434/api/embeddings"
    payload = {"model": model, "prompt": text}
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url, 
            data=data, 
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10.0) as response:
            if response.status == 200:
                resp_data = json.loads(response.read().decode("utf-8"))
                return resp_data.get("embedding", [])
    except Exception as e:
        sys.stderr.write(f"Ollama embedding query failed: {e}\n")
    return []

def perform_rag_search(query):
    """Executes vector similarity search against the local ChromaDB persistent collection."""
    chroma_client = get_chroma_client()
    if not chroma_client:
        return ["RAG offline: ChromaDB package not installed in environment."]
        
    try:
        # Get the 'vault_core' collection
        collection = chroma_client.get_collection(name="vault_core")
        
        # Get query vector from local Ollama
        query_vector = query_ollama_embedding(query)
        if not query_vector:
            # Fallback to standard word search if Ollama embeddings are unavailable
            results = collection.query(
                query_texts=[query],
                n_results=3
            )
        else:
            results = collection.query(
                query_embeddings=[query_vector],
                n_results=3
            )
            
        documents = results.get("documents", [[]])[0]
        return documents if documents else ["No offline documentation matched your query."]
        
    except Exception as e:
        sys.stderr.write(f"RAG lookup failed: {e}\n")
        return [f"RAG search error: {e}"]

def orphan_watchdog():
    """Background thread that kills the daemon if the parent Swift process terminates."""
    while True:
        # On macOS, if parent process dies, ppid becomes 1 (adopted by launchd)
        if os.getppid() == 1:
            sys.stderr.write("[RAG DAEMON] Parent process terminated. Clean self-exit.\n")
            os._exit(0)
        time.sleep(1.0)

def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: python rag_daemon.py <port>\n")
        sys.exit(1)
        
    port = int(sys.argv[1])
    
    # Start the orphan monitor thread
    watchdog_thread = threading.Thread(target=orphan_watchdog, daemon=True)
    watchdog_thread.start()
    
    # Establish connection to the Swift TCP Server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(("127.0.0.1", port))
        sys.stderr.write(f"[RAG DAEMON] Securely connected to Swift TCP host on port {port}.\n")
    except Exception as e:
        sys.stderr.write(f"Connection failed: {e}\n")
        sys.exit(1)
        
    # Read/Write loop
    buffer = ""
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                sys.stderr.write("[RAG DAEMON] Connection closed by Swift host. Exiting.\n")
                break
                
            buffer += data.decode("utf-8")
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                if not line.strip():
                    continue
                    
                try:
                    request = json.loads(line)
                    method = request.get("method")
                    params = request.get("params", {})
                    req_id = request.get("id")
                    
                    if method == "search":
                        query = params.get("query", "")
                        # Run similarity lookup
                        results = perform_rag_search(query)
                        
                        # Return JSON-RPC 2.0 Response
                        response = {
                            "jsonrpc": "2.0",
                            "result": results,
                            "id": req_id
                        }
                        sock.sendall((json.dumps(response) + "\n").encode("utf-8"))
                    else:
                        response = {
                            "jsonrpc": "2.0",
                            "error": {"code": -32601, "message": "Method not found"},
                            "id": req_id
                        }
                        sock.sendall((json.dumps(response) + "\n").encode("utf-8"))
                        
                except Exception as e:
                    sys.stderr.write(f"Error parsing request: {e}\n")
                    
    except Exception as e:
        sys.stderr.write(f"RAG daemon communication error: {e}\n")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
