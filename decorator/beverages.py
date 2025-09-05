# beverages.py
# Contiene el Componente y los Componentes Concretos del patrón.

from abc import ABC, abstractmethod

# --- Componente Abstracto ---
class Beverage(ABC):
    """
    La clase base para todas las bebidas. Utiliza el módulo abc para
    definir que es una clase abstracta.
    """
    def __init__(self):
        self.description = "Bebida Desconocida"
        self._size="Tall"

    def get_description(self) -> str:
        """
        Devuelve la descripción de la bebida con su tamaño correspondiente.
        """
        return self.description + f" ({self._size})"
    def get_size(self) -> str:
        """
        Devuelve el tamaño de la bebida.
        """
        return self._size
    def set_size(self,size:str):
        self._size=size
        
         
    
    
    

    @abstractmethod
    def cost(self) -> float:
        """
        Método abstracto que las subclases deben implementar para devolver
        el costo de la bebida.
        """
        pass

# --- Componentes Concretos ---
class HouseBlend(Beverage):
    """
    Café de la casa, un tipo específico de bebida.
    """
    def __init__(self):
        super().__init__()
        self.description = "Café de la Casa"

    def cost(self) -> float:
        return 0.89

class DarkRoast(Beverage):
    """
    Café Dark Roast, un tipo específico de bebida.
    """
    def __init__(self):
        super().__init__()
        self.description = "Café Dark Roast"

    def cost(self) -> float:
        return 0.99

class Decaf(Beverage):
    """
    Café Descafeinado, un tipo específico de bebida.
    """
    def __init__(self):
        super().__init__()
        self.description = "Café Descafeinado"

    def cost(self) -> float:
        return 1.05

class Espresso(Beverage):
    """
    Café Espresso, un tipo específico de bebida.
    """
    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99
