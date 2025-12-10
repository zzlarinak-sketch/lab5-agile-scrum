"""
Паттерн Factory Method (Фабричный метод)
"""
from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass
    
    @abstractmethod
    def attack(self) -> str:
        pass

class Warrior(Character):
    def __init__(self):
        self.name = "Воин"
        self.health = 150
    
    def get_info(self) -> str:
        return f"{self.name} (здоровье: {self.health})"
    
    def attack(self) -> str:
        return f"{self.name} наносит удар мечом!"

class Mage(Character):
    def __init__(self):
        self.name = "Маг"
        self.mana = 100
    
    def get_info(self) -> str:
        return f"{self.name} (мана: {self.mana})"
    
    def attack(self) -> str:
        return f"{self.name} бросает огненный шар!"

class CharacterFactory(ABC):
    @abstractmethod
    def create_character(self) -> Character:
        pass

class WarriorFactory(CharacterFactory):
    def create_character(self) -> Character:
        return Warrior()

class MageFactory(CharacterFactory):
    def create_character(self) -> Character:
        return Mage()
