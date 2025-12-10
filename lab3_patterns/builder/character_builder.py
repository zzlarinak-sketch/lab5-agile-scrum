"""
Паттерн Builder (Строитель)
"""
from abc import ABC, abstractmethod

class Character:
    def __init__(self):
        self.name = ""
        self.character_class = ""
        self.health = 0
        self.strength = 0
    
    def __str__(self):
        return (f"Персонаж: {self.name}\n"
                f"Класс: {self.character_class}\n"
                f"Здоровье: {self.health}\n"
                f"Сила: {self.strength}")

class CharacterBuilder(ABC):
    def __init__(self):
        self.character = Character()
    
    @abstractmethod
    def set_name(self, name: str):
        pass
    
    @abstractmethod
    def set_class(self):
        pass
    
    @abstractmethod
    def set_stats(self):
        pass
    
    def get_character(self):
        return self.character

class WarriorBuilder(CharacterBuilder):
    def set_name(self, name: str):
        self.character.name = name
    
    def set_class(self):
        self.character.character_class = "Воин"
    
    def set_stats(self):
        self.character.health = 200
        self.character.strength = 30

class MageBuilder(CharacterBuilder):
    def set_name(self, name: str):
        self.character.name = name
    
    def set_class(self):
        self.character.character_class = "Маг"
    
    def set_stats(self):
        self.character.health = 100
        self.character.strength = 15

class CharacterDirector:
    def __init__(self, builder: CharacterBuilder):
        self.builder = builder
    
    def construct(self, name: str):
        self.builder.set_name(name)
        self.builder.set_class()
        self.builder.set_stats()
        return self.builder.get_character()
