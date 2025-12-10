"""
Паттерн Abstract Factory (Абстрактная фабрика)
"""
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def use(self) -> str:
        pass

class Armor(ABC):
    @abstractmethod
    def protect(self) -> str:
        pass

class Sword(Weapon):
    def use(self) -> str:
        return "Меч наносит 20 урона"

class Shield(Armor):
    def protect(self) -> str:
        return "Щит блокирует 15 урона"

class Staff(Weapon):
    def use(self) -> str:
        return "Посох наносит 30 магического урона"

class Robe(Armor):
    def protect(self) -> str:
        return "Мантия блокирует 10 урона"

class EquipmentFactory(ABC):
    @abstractmethod
    def create_weapon(self) -> Weapon:
        pass
    
    @abstractmethod
    def create_armor(self) -> Armor:
        pass

class WarriorEquipmentFactory(EquipmentFactory):
    def create_weapon(self) -> Weapon:
        return Sword()
    
    def create_armor(self) -> Armor:
        return Shield()

class MageEquipmentFactory(EquipmentFactory):
    def create_weapon(self) -> Weapon:
        return Staff()
    
    def create_armor(self) -> Armor:
        return Robe()
