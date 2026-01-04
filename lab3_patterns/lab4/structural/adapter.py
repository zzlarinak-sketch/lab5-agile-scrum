"""
Adapter Pattern - Адаптер для логгера
"""

from abc import ABC, abstractmethod

class ExternalLogger:
    def log_message(self, msg: str) -> None:
        print(f"External log: {msg}")

class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass

class LoggerAdapter(Logger):
    def __init__(self, external_logger: ExternalLogger):
        self.external_logger = external_logger
    
    def log(self, message: str) -> None:
        self.external_logger.log_message(message)

if __name__ == "__main__":
    external_logger = ExternalLogger()
    logger = LoggerAdapter(external_logger)

    logger.log("This is a test message.")
