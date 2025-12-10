"""
Демонстрация 4 порождающих паттернов
"""
from singleton.game_logger import GameLogger
from factory_method.character_factory import WarriorFactory, MageFactory
from abstract_factory.equipment_factory import (
    WarriorEquipmentFactory, MageEquipmentFactory
)
from builder.character_builder import (
    WarriorBuilder, MageBuilder, CharacterDirector
)

def demo_singleton():
    print("=" * 50)
    print("1. SINGLETON (Одиночка)")
    print("=" * 50)
    
    logger1 = GameLogger()
    logger2 = GameLogger.get_instance()
    
    print(f"Один и тот же объект: {logger1 is logger2}")
    
    logger1.log("Первое сообщение")
    logger2.log("Второе сообщение")

def demo_factory_method():
    print("\n" + "=" * 50)
    print("2. FACTORY METHOD (Фабричный метод)")
    print("=" * 50)
    
    warrior_factory = WarriorFactory()
    mage_factory = MageFactory()
    
    warrior = warrior_factory.create_character()
    mage = mage_factory.create_character()
    
    print(f"Воин: {warrior.get_info()}")
    print(f"Атака: {warrior.attack()}")
    
    print(f"\nМаг: {mage.get_info()}")
    print(f"Атака: {mage.attack()}")

def demo_abstract_factory():
    print("\n" + "=" * 50)
    print("3. ABSTRACT FACTORY (Абстрактная фабрика)")
    print("=" * 50)
    
    warrior_factory = WarriorEquipmentFactory()
    mage_factory = MageEquipmentFactory()
    
    warrior_weapon = warrior_factory.create_weapon()
    warrior_armor = warrior_factory.create_armor()
    
    mage_weapon = mage_factory.create_weapon()
    mage_armor = mage_factory.create_armor()
    
    print("Воинская экипировка:")
    print(f"  Оружие: {warrior_weapon.use()}")
    print(f"  Броня: {warrior_armor.protect()}")
    
    print("\nМагическая экипировка:")
    print(f"  Оружие: {mage_weapon.use()}")
    print(f"  Броня: {mage_armor.protect()}")

def demo_builder():
    print("\n" + "=" * 50)
    print("4. BUILDER (Строитель)")
    print("=" * 50)
    
    warrior_builder = WarriorBuilder()
    mage_builder = MageBuilder()
    
    director = CharacterDirector(warrior_builder)
    warrior = director.construct("Александр")
    
    director.builder = mage_builder
    mage = director.construct("Мерлин")
    
    print("Воин:")
    print(warrior)
    
    print("\nМаг:")
    print(mage)

def main():
    print("=" * 50)
    print("ЛАБОРАТОРНАЯ РАБОТА 3")
    print("ПОРОЖДАЮЩИЕ ПАТТЕРНЫ ПРОЕКТИРОВАНИЯ")
    print("=" * 50)
    
    demo_singleton()
    demo_factory_method()
    demo_abstract_factory()
    demo_builder()
    
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 50)

if __name__ == "__main__":
    main()
