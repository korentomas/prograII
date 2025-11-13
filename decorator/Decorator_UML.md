# Patrón Decorator - UML

## Diagrama de Clases

```mermaid
classDiagram
    class Beverage {
        <<abstract>>
        -description: str
        -size: str = "Tall"
        +get_description()* str
        +cost()* float
        +set_size(size: str)
    }
    
    class Espresso {
        +cost() float
        +get_description() str
    }
    
    class DarkRoast {
        +cost() float
        +get_description() str
    }
    
    class HouseBlend {
        +cost() float
        +get_description() str
    }
    
    class CondimentDecorator {
        <<abstract>>
        #beverage: Beverage
        +get_description()* str
        +cost()* float
    }
    
    class Mocha {
        +cost() float
        +get_description() str
    }
    
    class Whip {
        +cost() float
        +get_description() str
    }
    
    class Soy {
        +cost() float
        +get_description() str
    }
    
    class Caramel {
        +cost() float
        +get_description() str
    }
    
    class Milk {
        +cost() float
        +get_description() str
    }
    
    class PrettyPrint {
        -beverage: Beverage
        +get_description() str
    }
    
    %% Herencias
    Beverage <|-- Espresso
    Beverage <|-- DarkRoast
    Beverage <|-- HouseBlend
    
    %% CondimentDecorator también es un Beverage
    Beverage <|-- CondimentDecorator
    
    %% Decoradores específicos
    CondimentDecorator <|-- Mocha
    CondimentDecorator <|-- Whip
    CondimentDecorator <|-- Soy
    CondimentDecorator <|-- Caramel
    CondimentDecorator <|-- Milk
    
    %% Composición: CondimentDecorator envuelve Beverage
    CondimentDecorator o-- Beverage : wraps
    
    %% PrettyPrint también envuelve Beverage
    PrettyPrint o-- Beverage : wraps
```

## Descripción del Patrón

El **Patrón Decorator** permite agregar responsabilidades dinámicamente a objetos de manera flexible. En este caso:

- **Beverage**: Clase abstracta que representa cualquier bebida
- **Espresso, DarkRoast, HouseBlend**: Bebidas concretas base
- **CondimentDecorator**: Clase abstracta que envuelve un Beverage y agrega funcionalidades
- **Mocha, Whip, Soy, Caramel, Milk**: Condimentos que decoran las bebidas
- **PrettyPrint**: Decorador adicional para formatear descripciones
