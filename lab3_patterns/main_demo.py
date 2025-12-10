print("=== Лаба 3: 4 паттерна ===")

from singleton.singleton import Singleton
s1 = Singleton.get_instance()
s2 = Singleton.get_instance()
print(f"1. Singleton: {s1 is s2}")

from factory_method.factory_method import FileLoggerFactory
file_factory = FileLoggerFactory()
print(f"2. Factory Method: {file_factory.log_message('test')}")

from abstract_factory.abstract_factory import WindowsFactory
windows_factory = WindowsFactory()
print(f"3. Abstract Factory: {windows_factory.create_button().paint()}")

from builder.builder import HawaiianPizzaBuilder, PizzaDirector
builder = HawaiianPizzaBuilder()
director = PizzaDirector(builder)
director.construct_pizza()
pizza = director.get_pizza()
print(f"4. Builder: {pizza}")

print("✅ Готово")
