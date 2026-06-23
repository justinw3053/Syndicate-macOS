import asyncio
import json
import os
import sys

async def handle_client(reader, writer):
    while True:
        line = await reader.readline()
        if not line:
            break
        try:
            payload = json.loads(line.decode('utf-8'))
            if "method" in payload and payload["method"] == "execute":
                params = payload.get("params", {})
                req_id = payload.get("id", 1)
                code = params.get("code", "")
                assertions = params.get("assertions", "")
                default_ws = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                workspace = params.get("workspacePath", default_ws)
                
                # Awaiting this serializes executions, preventing race conditions
                await run_execution(req_id, code, assertions, workspace, writer)
        except Exception as e:
            # Drop malformed requests cleanly
            pass

async def run_execution(req_id, code, assertions, workspace, writer):
    active_lab_path = os.path.join(workspace, "active_lab.py")
    test_lab_path = os.path.join(workspace, "test_active_lab.py")
    
    with open(active_lab_path, "w") as f:
        f.write(code)
    with open(test_lab_path, "w") as f:
        f.write(assertions)
        
    bin_dir = os.path.dirname(sys.executable)
    pytest_path = os.path.join(bin_dir, "pytest")
    if not os.path.exists(pytest_path):
        pytest_path = os.path.join(workspace, ".venv", "bin", "pytest")
        
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONPATH"] = f"{workspace}:{workspace}/.pi"

    sandbox_path = os.path.join(workspace, "backend", "sandbox.sb")
    with open(sandbox_path, "w") as f:
        f.write(f'''(version 1)
(allow default)
(deny file-write*)
(allow file-write* 
    (subpath "/private/var/folders")
    (subpath "{os.path.join(workspace, '.pytest_cache')}")
    (subpath "{os.path.join(workspace, 'backend', '__pycache__')}")
    (subpath "{os.path.join(workspace, '__pycache__')}")
    (literal "{active_lab_path}")
    (literal "{test_lab_path}")
    (literal "{sandbox_path}")
    (literal "/dev/null")
    (literal "/dev/dtracehelper")
    (literal "/dev/stdout")
    (literal "/dev/stderr")
    (literal "/dev/tty")
)
(deny network-outbound)
(allow network-outbound (local ip "localhost:*"))
(allow network-outbound (literal "/private/var/run/mDNSResponder"))
''')

    process = await asyncio.create_subprocess_exec(
        "sandbox-exec", "-f", sandbox_path, pytest_path, "-v", "--color=yes", "--tb=short", "-p", "no:cacheprovider", test_lab_path,
        cwd=workspace,
        env=env,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
        preexec_fn=os.setsid
    )
    
    async def send_output():
        while True:
            data = await process.stdout.read(4096)
            if not data:
                break
            msg = json.dumps({"id": req_id, "output": data.decode('utf-8', errors='replace')})
            writer.write(msg.encode('utf-8') + b'\n')
            await writer.drain()

    success = False
    try:
        # Enforce strict 5.0 second CPU/I/O timeout
        await asyncio.wait_for(send_output(), timeout=5.0)
        await asyncio.wait_for(process.wait(), timeout=1.0)
        success = process.returncode == 0
    except asyncio.TimeoutError:
        try:
            os.killpg(os.getpgid(process.pid), 15)
            await asyncio.sleep(0.5)
            os.killpg(os.getpgid(process.pid), 9)
        except Exception:
            pass
        msg = json.dumps({"id": req_id, "output": "\n[TIMEOUT] CPU limit exceeded. Process terminated.\n"})
        writer.write(msg.encode('utf-8') + b'\n')
        await writer.drain()
        success = False
    finally:
        if os.path.exists(test_lab_path):
            try: os.remove(test_lab_path)
            except: pass
            
    done_msg = json.dumps({"id": req_id, "done": True, "success": success})
    writer.write(done_msg.encode('utf-8') + b'\n')
    await writer.drain()

async def main(port):
    sys.stdout.write(f"[ExecutionDaemon] Connecting to Swift on 127.0.0.1:{port}\n")
    sys.stdout.flush()
    try:
        reader, writer = await asyncio.open_connection('127.0.0.1', port)
        await handle_client(reader, writer)
    except Exception as e:
        sys.stderr.write(f"[ExecutionDaemon] Connection failed: {e}\n")
        sys.stderr.flush()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    asyncio.run(main(port))
