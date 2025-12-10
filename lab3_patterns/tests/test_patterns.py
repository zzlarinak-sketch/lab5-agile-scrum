"""
Тесты для паттернов
"""
from singleton.game_logger import GameLogger
from factory_method.character_factory import Warrior, WarriorFactory
from builder.character_builder import WarriorBuilder, CharacterDirector

def test_singleton():
    logger1 = GameLogger()
    logger2 = GameLogger.get_instance()
    
    assert logger1 is logger2
    
    logger1.log("Тест")
    assert len(logger2.get_logs()) == 1
    print("✅ Singleton тест пройден")

def test_factory_method():
    factory = WarriorFactory()
    warrior = factory.create_character()
    
    assert isinstance(warrior, Warrior)
    assert warrior.health == 150
    print("✅ Factory Method тест пройден")

def test_builder():
    builder = WarriorBuilder()
    director = CharacterDirector(builder)
    character = director.construct("Тест")
    
    assert character.name == "Тест"
    assert character.character_class == "Воин"
    print("✅ Builder тест пройден")

def run_all_tests():
    print("Запуск всех тестов...")
    test_singleton()
    test_factory_method()
    test_builder()
    print("\n✅ Все тесты пройдены успешно!")

if __name__ == "__main__":
    run_all_tests()
