"""
Паттерн Singleton (Одиночка)
"""
class GameLogger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.messages = []
        return cls._instance
    
    def log(self, message: str):
        self.messages.append(message)
        print(f"[LOG] {message}")
    
    def get_logs(self):
        return self.messages
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = GameLogger()
        return cls._instance
