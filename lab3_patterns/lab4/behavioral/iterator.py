"""
Iterator Pattern - Итератор для массива
"""

from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

T = TypeVar('T')

class Iterator(ABC, Generic[T]):
    @abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abstractmethod
    def next(self) -> T:
        pass

class ArrayIterator(Iterator[T]):
    def __init__(self, items: List[T]):
        self.items = items
        self.position = 0
    
    def has_next(self) -> bool:
        return self.position < len(self.items)
    
    def next(self) -> T:
        if self.has_next():
            item = self.items[self.position]
            self.position += 1
            return item
        raise IndexError("Нет больше элементов")

if __name__ == "__main__":
    items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    iterator = ArrayIterator(items)
    
    print("Итерация по массиву:")
    while iterator.has_next():
        item = iterator.next()
        print(f"  - {item}")
    
    print("\nПопытка получить элемент после конца:")
    try:
        iterator.next()
    except IndexError as e:
        print(f"  Поймано исключение: {e}")
