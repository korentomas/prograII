from condiments import Mocha, Soy, Whip, Caramel
from beverages import Espresso, DarkRoast, HouseBlend   

def build_beverage(bass_class,size:str,condiments:list[str]):
    """
    Función que construye una bebida(cafe) con el tamaño y los condimentos especificados.
    Argumentos:
    bass_class: Clase base de la bebida (Espresso, DarkRoast, HouseBlend).
    size: Tamaño de la bebida.Opciones posibles: ("Tall", "Grande", "Venti").
    condiments: Lista de condimentos(decoradores) a añadir.Opciones posibles: (Mocha, Soy, Whip, Caramel)."""

    beverage=bass_class()
    beverage.set_size(size) 
    for condiment in condiments:
        beverage=condiment(beverage)
    return beverage