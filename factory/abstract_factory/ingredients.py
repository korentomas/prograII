from abc import ABC, abstractmethod

# Ingredient products
class Dough:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Sauce:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Cheese:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Clams:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Pepperoni:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Veggies:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Onion:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Mushroom:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class SlicedPepperoni:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class RedPepper:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class ShreddedEgg:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Olives:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Anchovies:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class HeartOfPalm:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

# Abstract Factory
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough: ...
    @abstractmethod
    def create_sauce(self) -> Sauce: ...
    @abstractmethod
    def create_cheese(self) -> Cheese: ...
    @abstractmethod
    def create_clam(self) -> Clams: ...
    @abstractmethod
    def create_pepperoni(self) -> Pepperoni: ...
    @abstractmethod
    def create_veggies(self) -> Veggies: ...
    @abstractmethod
    def create_onion(self) -> Onion: ...
    @abstractmethod
    def create_mushroom(self) -> Mushroom: ...
    @abstractmethod
    def create_sliced_pepperoni(self) -> SlicedPepperoni: ...
    @abstractmethod
    def create_red_pepper(self) -> RedPepper: ...
    @abstractmethod
    def create_shredded_egg(self) -> ShreddedEgg: ...
    @abstractmethod
    def create_olives(self) -> Olives: ...
    @abstractmethod
    def create_anchovies(self) -> Anchovies: ...
    @abstractmethod
    def create_heart_of_palm(self) -> HeartOfPalm: ...

# Concrete factories
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  return Dough("Thin Crust Dough")
    def create_sauce(self) -> Sauce:  return Sauce("Marinara Sauce")
    def create_cheese(self) -> Cheese: return Cheese("Reggiano Cheese")
    def create_clam(self) -> Clams:   return Clams("Fresh Long Island Clams")
    def create_pepperoni(self) -> Pepperoni: return Pepperoni("Pepperoni")
    def create_veggies(self) -> Veggies: return Veggies("NY Seasonal Veggies")
    def create_onion(self) -> Onion: return Onion("Onion")
    def create_mushroom(self) -> Mushroom: return Mushroom("White Mushrooms")
    def create_sliced_pepperoni(self) -> SlicedPepperoni: return SlicedPepperoni("Sliced Pepperoni")
    def create_red_pepper(self) -> RedPepper: return RedPepper("Red Pepper")
    def create_shredded_egg(self) -> ShreddedEgg: return ShreddedEgg("Shredded Egg")
    def create_olives(self) -> Olives: return Olives("Olives")
    def create_anchovies(self) -> Anchovies: return Anchovies("Italian Anchovies")
    def create_heart_of_palm(self) -> HeartOfPalm: return HeartOfPalm("Heart Of Palm")

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  return Dough("Extra Thick Crust Dough")
    def create_sauce(self) -> Sauce:  return Sauce("Chunky Tomato Sauce")
    def create_cheese(self) -> Cheese: return Cheese("Shredded Mozzarella Cheese")
    def create_clam(self) -> Clams:   return Clams("Lake Michigan Clams")
    def create_pepperoni(self) -> Pepperoni: return Pepperoni("Pepperoni")
    def create_veggies(self) -> Veggies: return Veggies("Chicago Seasonal Veggies")
    def create_onion(self) -> Onion: return Onion("Onion")
    def create_mushroom(self) -> Mushroom: return Mushroom("Portobello Mushrooms")
    def create_sliced_pepperoni(self) -> SlicedPepperoni: return SlicedPepperoni("Sliced Pepperoni")
    def create_red_pepper(self) -> RedPepper: return RedPepper("Chicago Red Pepper")
    def create_shredded_egg(self) -> ShreddedEgg: return ShreddedEgg("Shredded Egg")
    def create_olives(self) -> Olives: return Olives("Olives")
    def create_anchovies(self) -> Anchovies: return Anchovies("Lake Michigan Anchovies")
    def create_heart_of_palm(self) -> HeartOfPalm: return HeartOfPalm("Heart Of Palm")  