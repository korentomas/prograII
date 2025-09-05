from beverages import HouseBlend, Espresso, DarkRoast
from condiments import Mocha, Whip,Soy,Caramel
from builder import build_beverage

def test_double_mocha_darkroast_soy_grande():
    ''' Funcion que testea el caso de DarkRoast con doble Mocha y Soy (grande)'''
    drink = build_beverage(DarkRoast, "Grande", [Mocha, Mocha,Soy])
    cost = drink.cost()
    expected_cost = 0.99 + 0.20*2+0.35
    assert round(cost,2) == round(expected_cost,2)

def test_triple_mocha_whip_houseblend_venti():
    ''' Funcion que testea el caso de unHouseBlend con triple Mocha y Whip'''
    drink = build_beverage(HouseBlend, "Venti", [Mocha, Mocha, Mocha, Whip])
    desc = drink.get_description()
    cost = drink.cost()
    assert desc.count("Mocha") == 3
    expected_cost = 0.89 + 0.20*3 + 0.10  
    assert round(cost,2) == round(expected_cost,2)

def test_double_whip_espresso_tall():
    ''' Funcion que testea el caso de un HouseBlend con doble Whip'''
    drink = build_beverage(Espresso, "Tall", [Whip, Whip,Caramel,Caramel,Caramel])
    cost = drink.cost()
    expected_cost = 1.99 + 0.10*2+0.25*3  
    assert cost == expected_cost

def test_mocha_whip_houseblend_grande():
    ''' Funcion que testea el caso de un HouseBlend con Mocha y Whip'''
    drink = build_beverage(HouseBlend, "Grande", [Mocha, Whip])
    cost = drink.cost()
    expected_cost = 0.89 + 0.20 + 0.10  
    assert cost == expected_cost
