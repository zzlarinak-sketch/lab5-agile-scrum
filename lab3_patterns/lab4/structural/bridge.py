"""
Bridge Pattern - Мост между устройствами и форматами вывода
"""

from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def print(self, data: str) -> None:
        pass

class Monitor(Device):
    def print(self, data: str) -> None:
        print(f"Displaying on monitor: {data}")

class Printer(Device):
    def print(self, data: str) -> None:
        print(f"Printing to paper: {data}")

class Output(ABC):
    def __init__(self, device: Device):
        self.device = device
    
    @abstractmethod
    def render(self, data: str) -> None:
        pass

class TextOutput(Output):
    def render(self, data: str) -> None:
        self.device.print(f"Text: {data}")

class ImageOutput(Output):
    def render(self, data: str) -> None:
        self.device.print(f"Image: [Binary data: {data}]")

if __name__ == "__main__":
    monitor = Monitor()
    printer = Printer()

    text_on_monitor = TextOutput(monitor)
    text_on_printer = TextOutput(printer)

    text_on_monitor.render("Hello, world!")
    text_on_printer.render("Hello, world!")

    image_on_monitor = ImageOutput(monitor)
    image_on_monitor.render("101010101")
