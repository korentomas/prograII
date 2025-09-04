# main.py
# Script principal para probar el patrón Decorator.

from beverages import Espresso, DarkRoast, HouseBlend
from condiments import Mocha, Whip, Soy,Caramel
from builder import build_beverage

def main():
    """
    Función principal que simula la preparación de cafés en Starbuzz.
    """
    print("Bienvenido a Starbuzz Coffee!")
    print("--- Preparando pedidos ---")

    # Pedido 1: Un Espresso simple, sin condimentos.
    beverage1 = Espresso()
    print(f"Pedido 1: {beverage1.get_description()} ${beverage1.cost():.2f}")

    # Pedido 2: Un DarkRoast con doble Mocha y Crema.
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)  # Envolvemos con el primer Mocha
    beverage2 = Mocha(beverage2)  # Envolvemos con el segundo Mocha
    beverage2 = Whip(beverage2)   # Envolvemos con Crema
    beverage2 = Caramel(beverage2) # Envolvemos con caramel
    print(f"Pedido 2: {beverage2.get_description()} ${beverage2.cost():.2f}")

    # Pedido 3: Un HouseBlend con Soja, Mocha y Crema.
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"Pedido 3: {beverage3.get_description()} ${beverage3.cost():.2f}")

    beverage4 = HouseBlend()
    beverage4 = Soy(beverage4)
    beverage4 = Soy(beverage4)
    beverage4 = Soy(beverage4)
    beverage4 = Caramel(beverage4)
    beverage4 = Caramel(beverage4)
    beverage4 = Whip(beverage4)
   
    print(f"Pedido 4: {beverage4.get_description()} ${beverage4.cost():.2f}")


    beverage5 = HouseBlend()
    beverage5.set_size("Venti")
    beverage5 = Soy(beverage5)
    print(f"Pedido 5: {beverage5.get_description()} ${beverage5.cost():.2f}")

    beverage6 = DarkRoast()
    beverage6.set_size("Venti")
    beverage6 = Mocha(beverage6)
    beverage6 = Mocha(beverage6)
    beverage6 = Soy(beverage6)
    print(f"Pedido 6: {beverage6.get_description()} ${beverage6.cost():.2f}")


   # pedido7 = build_beverage(DarkRoast, "Grande", [Mocha, Mocha,Mocha])
   # print(f"Pedido 7: {pedido7.get_description()} ${pedido7.cost():.2f}")


    
    beverage8 = DarkRoast()
    beverage8.set_size("Venti")
    beverage8 = Soy(beverage8)
    beverage8 = Mocha(beverage8)
    beverage8 = Mocha(beverage8)
    print(f"Pedido 8: {beverage8.get_description()} ${beverage8.cost():.2f}")








if __name__ == "__main__":
    main()