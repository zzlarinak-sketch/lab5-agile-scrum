"""
Strategy Pattern - Разные алгоритмы сортировки
"""

from abc import ABC, abstractmethod
from typing import List

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, array: List[int]) -> None:
        pass

class BubbleSortStrategy(SortingStrategy):
    def sort(self, array: List[int]) -> None:
        print("Sorting using Bubble Sort")
        n = len(array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

class QuickSortStrategy(SortingStrategy):
    def sort(self, array: List[int]) -> None:
        print("Sorting using Quick Sort")
        self._quick_sort(array, 0, len(array) - 1)
    
    def _quick_sort(self, array: List[int], low: int, high: int) -> None:
        if low < high:
            pi = self._partition(array, low, high)
            self._quick_sort(array, low, pi - 1)
            self._quick_sort(array, pi + 1, high)
    
    def _partition(self, array: List[int], low: int, high: int) -> int:
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

class Sorter:
    def __init__(self):
        self.strategy = None
    
    def set_strategy(self, strategy: SortingStrategy) -> None:
        self.strategy = strategy
    
    def sort_array(self, array: List[int]) -> None:
        if self.strategy is None:
            raise ValueError("Стратегия не установлена")
        self.strategy.sort(array)

if __name__ == "__main__":
    sorter = Sorter()
    
    sorter.set_strategy(BubbleSortStrategy())
    array1 = [5, 3, 8, 4, 2]
    print(f"До сортировки: {array1}")
    sorter.sort_array(array1)
    print(f"После сортировки: {array1}")
    
    print()
    
    sorter.set_strategy(QuickSortStrategy())
    array2 = [5, 3, 8, 4, 2]
    print(f"До сортировки: {array2}")
    sorter.sort_array(array2)
    print(f"После сортировки: {array2}")
