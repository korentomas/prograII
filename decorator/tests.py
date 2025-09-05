from beverages import HouseBlend, Espresso, DarkRoast
from condiments import Mocha, Whip, Soy, Caramel, PrettyPrint
from builder import build_beverage


def test_double_mocha_darkroast_soy_grande():
    """Funcion que testea el caso de DarkRoast con doble Mocha y Soy (grande)"""
    drink = build_beverage(DarkRoast, "Grande", [Mocha, Mocha, Soy])
    cost = drink.cost()
    expected_cost = 0.99 + 0.20 * 2 + 0.35
    assert round(cost, 2) == round(expected_cost, 2)


def test_triple_mocha_whip_houseblend_venti():
    """Funcion que testea el caso de un HouseBlend con triple Mocha y Whip"""
    drink = build_beverage(HouseBlend, "Venti", [Mocha, Mocha, Mocha, Whip])
    desc = drink.get_description()
    cost = drink.cost()
    assert desc.count("Mocha") == 3
    expected_cost = 0.89 + 0.20 * 3 + 0.10
    assert round(cost, 2) == round(expected_cost, 2)


def test_double_whip_espresso_tall():
    """Funcion que testea el caso de un Espresso con doble Whip y triple Caramel"""
    drink = build_beverage(Espresso, "Tall", [Whip, Whip, Caramel, Caramel, Caramel])
    cost = drink.cost()
    expected_cost = 1.99 + 0.10 * 2 + 0.25 * 3
    assert cost == expected_cost


def test_mocha_whip_houseblend_grande():
    """Funcion que testea el caso de un HouseBlend con Mocha y Whip"""
    drink = build_beverage(HouseBlend, "Grande", [Mocha, Whip])
    cost = drink.cost()
    expected_cost = 0.89 + 0.20 + 0.10
    assert cost == expected_cost


def test_pretty_print_multiple_condiments():
    """Funcion que testea el PrettyPrint con varios condimentos repetidos"""
    drink1 = build_beverage(DarkRoast, "Tall", [Mocha, Mocha])
    pretty1 = PrettyPrint(drink1)
    assert "Double Mocha" in pretty1.get_description()
    assert "Mocha, Mocha" not in pretty1.get_description()

    drink2 = build_beverage(Espresso, "Grande", [Whip, Whip, Whip])
    pretty2 = PrettyPrint(drink2)
    assert "Triple Crema" in pretty2.get_description()

    drink3 = build_beverage(HouseBlend, "Venti", [Mocha, Mocha, Soy, Soy, Caramel])
    pretty3 = PrettyPrint(drink3)
    desc = pretty3.get_description()
    assert "Double Mocha" in desc
    assert "Double Soja" in desc
    assert "Caramel" in desc

    assert drink3.cost() == pretty3.cost()
