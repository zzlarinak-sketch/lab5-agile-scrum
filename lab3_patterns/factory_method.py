from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        return f"Logging to file: {message}"

class ConsoleLogger(Logger):
    def log(self, message):
        return f"Logging to console: {message}"

class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self):
        pass
    
    def log_message(self, message):
        logger = self.create_logger()
        return logger.log(message)

class FileLoggerFactory(LoggerFactory):
    def create_logger(self):
        return FileLogger()

class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self):
        return ConsoleLogger()
