class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.topping = ""
    
    def set_dough(self, dough):
        self.dough = dough
    
    def set_sauce(self, sauce):
        self.sauce = sauce
    
    def set_topping(self, topping):
        self.topping = topping
    
    def __str__(self):
        return f"Pizza: {self.dough}, {self.sauce}, {self.topping}"

class PizzaBuilder:
    def build_dough(self):
        pass
    
    def build_sauce(self):
        pass
    
    def build_topping(self):
        pass
    
    def get_result(self):
        pass

class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()
    
    def build_dough(self):
        self.pizza.set_dough("cross")
    
    def build_sauce(self):
        self.pizza.set_sauce("mild")
    
    def build_topping(self):
        self.pizza.set_topping("ham+pineapple")
    
    def get_result(self):
        return self.pizza

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder
    
    def construct_pizza(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()
    
    def get_pizza(self):
        return self.builder.get_result()
