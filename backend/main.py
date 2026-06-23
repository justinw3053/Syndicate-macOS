import os
import sys
import threading
import time
from flask import Flask, jsonify, send_from_directory, request, Response
import backend.state_manager as state_manager
import backend.llm_bridge as llm_bridge
import backend.content_engine as content_engine
from backend.event_bus import EventBus
import queue

def orphan_watchdog():
    """Background watchdog thread that terminates the Flask server if the parent Swift app exits."""
    while True:
        # On macOS, if the parent Swift process dies, this process is adopted by launchd (PID 1)
        if os.getppid() == 1:
            sys.stderr.write("[BACKEND] Parent process died. Clean self-exit.\n")
            os._exit(0)
        time.sleep(0.5)

def create_app(test_config=None):
    # Start the orphan monitor watchdog thread
    watchdog_thread = threading.Thread(target=orphan_watchdog, daemon=True)
    watchdog_thread.start()

    # create and configure the app, pointing static to the frontend folder
    app = Flask(__name__, instance_relative_config=True, static_folder="../frontend", static_url_path="")

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.after_request
    def add_security_headers(response):
        response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
        response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
        return response

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    @app.route('/api/health')
    def health():
        return jsonify({"status": "ok"})

    @app.route('/api/lessons')
    def lessons():
        return jsonify(content_engine.list_lessons())

    @app.route('/api/lessons/<path:lesson_id>')
    def lesson_detail(lesson_id):
        content = content_engine.get_lesson_content(lesson_id)
        if content is None:
            return jsonify({"error": "Lesson not found"}), 404
        return jsonify(content)
        
    @app.route('/api/track', methods=['POST'])
    def track():
        data = request.json
        if not data or 'lesson' not in data:
            return jsonify({"error": "Bad Request"}), 400
            
        success = state_manager.update_progress(data['lesson'])
        return jsonify({"status": "updated", "success": success})

    @app.route('/api/chat', methods=['POST'])
    def chat():
        data = request.json
        if not data or 'message' not in data:
            return jsonify({"error": "Bad Request"}), 400
            
        message = data['message']
        context = data.get('context', '')
        lesson_id = data.get('lessonId', '')
        
        return Response(llm_bridge.stream_chat(message, context, lesson_id), mimetype='text/event-stream')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(threaded=True, host='127.0.0.1', port=5050)

    @app.route('/api/events')
    def events():
        def event_stream():
            q = queue.Queue()
            
            def on_event(event_data):
                q.put(event_data)
                
            bus = EventBus()
            bus.subscribe(on_event)
            
            try:
                while True:
                    # Block until an event is published
                    event_data = q.get()
                    yield f"data: {event_data}\n\n"
            except GeneratorExit:
                # Clean up if client disconnects
                with bus.state_lock:
                    if on_event in bus.subscribers:
                        bus.subscribers.remove(on_event)
        
        return Response(event_stream(), mimetype='text/event-stream')
