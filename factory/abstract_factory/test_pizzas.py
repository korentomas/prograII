from .store import NYPizzaStore, ChicagoPizzaStore

# Test #1: Verificar que NYPizzaStore crea una pizza estilo NY
def test_ny_pizza_store_creates_ny_style_pizza():
    # Arrange
    store = NYPizzaStore()
    # Act
    pizza = store.order_pizza("cheese")
    # Assert
    assert pizza.name == "NY Style Cheese Pizza"

# Test #2: Verificar que ChicagoPizzaStore crea una pizza estilo Chicago

def test_chicago_pizza_store_creates_chicago_style_pizza():
    # Arrange
    store = ChicagoPizzaStore()
    # Act
    pizza = store.order_pizza("cheese")
    # Assert
    assert pizza.name == "Chicago Style Cheese Pizza"

# Test #3: Verificar que una pizza de queso de NY contiene los ingredientes correctos de NY
def test_ny_cheese_pizza_has_correct_ingredients():
    # Arrange
    store = NYPizzaStore()
    # Act
    pizza = store.order_pizza("cheese")
    # Assert
    assert pizza.dough.name == "Thin Crust Dough"
    assert pizza.sauce.name == "Marinara Sauce"
    assert pizza.cheese.name == "Reggiano Cheese"

# Test #4: Verificar que una pizza de almejas de Chicago contiene los ingredientes correctos de Chicago
def test_chicago_clam_pizza_has_correct_ingredients():
    # Arrange
    store = ChicagoPizzaStore()
    # Act
    pizza = store.order_pizza("clam")
    # Assert
    assert pizza.dough.name == "Extra Thick Crust Dough"
    assert pizza.sauce.name == "Chunky Tomato Sauce"
    assert pizza.cheese.name == "Shredded Mozzarella Cheese"
    assert pizza.clam.name == "Lake Michigan Clams"