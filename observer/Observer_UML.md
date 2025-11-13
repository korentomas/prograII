# Patrón Observer - UML

## Diagrama de Clases

```mermaid
classDiagram
    class Subject {
        <<abstract>>
        -observers: List~Observer~
        +register_observer(observer: Observer)*
        +remove_observer(observer: Observer)*
        +notify_observers()*
    }
    
    class Observer {
        <<interface>>
        +update(temp: float, humidity: float, pressure: float)*
    }
    
    class WeatherData {
        -temperature: float
        -humidity: float
        -pressure: float
        +get_temperature() float
        +get_humidity() float
        +get_pressure() float
        +set_measurements(t: float, h: float, p: float)
        +register_observer(observer: Observer)
        +remove_observer(observer: Observer)
        +notify_observers()
    }
    
    class CurrentConditionsDisplay {
        -temperature: float
        -humidity: float
        +update(temp: float, humidity: float, pressure: float)
        +display()
    }
    
    class StatisticsDisplay {
        -min_temp: float
        -max_temp: float
        -temp_sum: float
        -num_readings: int
        +update(temp: float, humidity: float, pressure: float)
        +display()
    }
    
    class ForecastDisplay {
        -last_pressure: float
        -trend: str
        +update(temp: float, humidity: float, pressure: float)
        +display()
    }
    
    class WeatherLog {
        -log_file: str
        +update(temp: float, humidity: float, pressure: float)
        +log_data()
    }
    
    %% Relaciones
    Subject <|-- WeatherData
    Observer <|.. CurrentConditionsDisplay
    Observer <|.. StatisticsDisplay
    Observer <|.. ForecastDisplay
    Observer <|.. WeatherLog
    
    WeatherData o-- Observer : notifies
```

## Componentes Principales

1. **Subject (WeatherData)**
   - Mantiene una lista de observadores
   - Notifica a todos cuando su estado cambia
   - Permite registrar y desregistrar observadores

2. **Observer (Interfaz)**
   - Define el método `update()` que será llamado por el Subject
   - Los observadores concretos implementan esta interfaz

3. **Observadores Concretos**
   - `CurrentConditionsDisplay`: Muestra condiciones actuales
   - `StatisticsDisplay`: Calcula estadísticas
   - `ForecastDisplay`: Predice tendencias futuras
   - `WeatherLog`: Registra datos en un archivo
