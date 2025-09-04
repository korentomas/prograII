# condiments.py
# Contiene el Decorador Abstracto y los Decoradores Concretos.

from abc import ABC, abstractmethod
from beverages import Beverage

# --- Decorador Abstracto ---
class CondimentDecorator(Beverage, ABC):
    """
    Clase base para los decoradores de condimentos.
    Hereda de Beverage para tener el mismo tipo.
    Mantiene una referencia a la bebida que está envolviendo.
    """
    def __init__(self, beverage: Beverage):
        super().__init__()
        self._beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        pass
    
    def get_size(self) -> str:
        return self._beverage.get_size()

# --- Decoradores Concretos ---
class Milk(CondimentDecorator):
    """
    Decorador para añadir Leche a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Leche"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10

class Mocha(CondimentDecorator):
    """
    Decorador para añadir Mocha a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20
class Caramel(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description()+", Caramel"
    def cost(self):
        return self._beverage.cost()+0.25

class Soy(CondimentDecorator):
    """
    Decorador para añadir Soja a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soja"

    def cost(self) -> float:
        size=self._beverage.get_size()
        costo_fijo=0.15
        if size == "Tall":
            extra = 0.15
        elif size == "Grande":
            extra = 0.20
        elif size == "Venti":
            extra = 0.25
        
        return self._beverage.cost()+ extra+costo_fijo
        

class Whip(CondimentDecorator):
    """
    Decorador para añadir Crema a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Crema"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10
