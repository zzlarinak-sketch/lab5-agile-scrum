def demonstrate_strategy():
    print("=" * 60)
    print("1. STRATEGY (Стратегия)")
    print("=" * 60)
    
    from behavioral.strategy import Sorter, BubbleSortStrategy, QuickSortStrategy
    
    sorter = Sorter()
    data = [5, 3, 8, 4, 2]
    
    print(f"Исходные данные: {data}")
    
    sorter.set_strategy(BubbleSortStrategy())
    data_copy = data.copy()
    sorter.sort_array(data_copy)
    print(f"После пузырьковой сортировки: {data_copy}")
    
    sorter.set_strategy(QuickSortStrategy())
    data_copy = data.copy()
    sorter.sort_array(data_copy)
    print(f"После быстрой сортировки: {data_copy}")


def demonstrate_chain_of_responsibility():
    print("\n" + "=" * 60)
    print("2. CHAIN OF RESPONSIBILITY (Цепочка обязанностей)")
    print("=" * 60)
    
    from behavioral.chain_of_responsibility import (
        ConcreteHandlerA, ConcreteHandlerB, Request, RequestType
    )
    
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_a.set_next_handler(handler_b)
    
    requests = [
        Request(RequestType.TYPE_A),
        Request(RequestType.TYPE_B),
    ]
    
    for request in requests:
        print(f"\nОбработка {request.get_type().value}:")
        handler_a.handle_request(request)


def demonstrate_iterator():
    print("\n" + "=" * 60)
    print("3. ITERATOR (Итератор)")
    print("=" * 60)
    
    from behavioral.iterator import ArrayIterator
    
    fruits = ["Apple", "Banana", "Cherry", "Date"]
    iterator = ArrayIterator(fruits)
    
    print("Итерация по массиву фруктов:")
    while iterator.has_next():
        fruit = iterator.next()
        print(f"  - {fruit}")


def demonstrate_proxy():
    print("\n" + "=" * 60)
    print("4. PROXY (Прокси)")
    print("=" * 60)
    
    from structural.proxy import DatabaseProxy
    
    print("Тестирование доступа к базе данных:")
    
    user_db = DatabaseProxy(False)
    print("\nПользователь пытается выполнить запрос:")
    user_db.query("SELECT * FROM users")
    
    admin_db = DatabaseProxy(True)
    print("\nАдминистратор выполняет запрос:")
    admin_db.query("SELECT * FROM users")


def demonstrate_adapter():
    print("\n" + "=" * 60)
    print("5. ADAPTER (Адаптер)")
    print("=" * 60)
    
    from structural.adapter import ExternalLogger, LoggerAdapter
    
    external_logger = ExternalLogger()
    adapter = LoggerAdapter(external_logger)
    
    print("Использование адаптированного логгера:")
    adapter.log("Сообщение через адаптер")
    adapter.log("Еще одно сообщение")


def demonstrate_bridge():
    print("\n" + "=" * 60)
    print("6. BRIDGE (Мост)")
    print("=" * 60)
    
    from structural.bridge import Monitor, Printer, TextOutput, ImageOutput
    
    monitor = Monitor()
    printer = Printer()
    
    print("Текстовый вывод:")
    text_on_monitor = TextOutput(monitor)
    text_on_monitor.render("Hello World")
    
    text_on_printer = TextOutput(printer)
    text_on_printer.render("Hello World")
    
    print("\nГрафический вывод:")
    image_on_monitor = ImageOutput(monitor)
    image_on_monitor.render("101010101")
    
    image_on_printer = ImageOutput(printer)
    image_on_printer.render("101010101")


def main():
    print("=" * 70)
    print("ЛАБОРАТОРНАЯ РАБОТА №4")
    print("ПОВЕДЕНЧЕСКИЕ И СТРУКТУРНЫЕ ПАТТЕРНЫ ПРОЕКТИРОВАНИЯ")
    print("=" * 70)
    
    demonstrate_strategy()
    demonstrate_chain_of_responsibility()
    demonstrate_iterator()
    demonstrate_proxy()
    demonstrate_adapter()
    demonstrate_bridge()
    
    print("\n" + "=" * 70)
    print("Все паттерны успешно продемонстрированы!")
    print("=" * 70)


if __name__ == "__main__":
    main()
