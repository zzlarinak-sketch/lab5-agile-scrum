"""
Chain of Responsibility Pattern - Цепочка обязанностей
"""

from abc import ABC, abstractmethod
from enum import Enum

class RequestType(Enum):
    TYPE_A = "TYPE_A"
    TYPE_B = "TYPE_B"

class Request:
    def __init__(self, request_type: RequestType):
        self.type = request_type
    
    def get_type(self) -> RequestType:
        return self.type

class Handler(ABC):
    def __init__(self):
        self.next_handler = None
    
    @abstractmethod
    def handle_request(self, request: Request) -> None:
        pass
    
    def set_next_handler(self, next_handler: 'Handler') -> None:
        self.next_handler = next_handler

class ConcreteHandlerA(Handler):
    def handle_request(self, request: Request) -> None:
        if request.get_type() == RequestType.TYPE_A:
            print("ConcreteHandlerA handled the request.")
        elif self.next_handler is not None:
            self.next_handler.handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request: Request) -> None:
        if request.get_type() == RequestType.TYPE_B:
            print("ConcreteHandlerB handled the request.")
        elif self.next_handler is not None:
            self.next_handler.handle_request(request)

if __name__ == "__main__":
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    
    handler_a.set_next_handler(handler_b)
    
    request_a = Request(RequestType.TYPE_A)
    request_b = Request(RequestType.TYPE_B)
    
    handler_a.handle_request(request_a)
    handler_a.handle_request(request_b)
