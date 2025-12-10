import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from singleton.singleton import Singleton
    from factory_method.factory_method import FileLoggerFactory
    from builder.builder import HawaiianPizzaBuilder, PizzaDirector
    print("✅ Все модули импортированы")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    sys.exit(1)

def test_singleton():
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()
    assert s1 is s2
    print("✅ Singleton тест пройден")

def test_factory_method():
    factory = FileLoggerFactory()
    result = factory.log_message("test")
    assert "Logging to file" in result
    print("✅ Factory Method тест пройден")

def test_builder():
    builder = HawaiianPizzaBuilder()
    director = PizzaDirector(builder)
    director.construct_pizza()
    pizza = director.get_pizza()
    assert "cross" in str(pizza)
    assert "ham+pineapple" in str(pizza)
    print("✅ Builder тест пройден")

def run_all_tests():
    print("Запуск тестов...")
    test_singleton()
    test_factory_method()
    test_builder()
    print("\n✅ Все тесты пройдены")

if __name__ == "__main__":
    run_all_tests()
