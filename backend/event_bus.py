import json
import threading

class EventBus:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(EventBus, cls).__new__(cls)
                cls._instance.subscribers = []
                cls._instance.state_lock = threading.Lock()
            return cls._instance
            
    def subscribe(self, callback):
        with self.state_lock:
            self.subscribers.append(callback)
            
    def publish(self, action_type, payload):
        event = {
            "type": action_type,
            "payload": payload
        }
        event_str = json.dumps(event)
        
        with self.state_lock:
            for sub in self.subscribers:
                try:
                    sub(event_str)
                except Exception:
                    pass
