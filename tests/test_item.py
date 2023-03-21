from src.item import Item
import pytest


@pytest.fixture
def x():
    return Item('computer', 100, 10)


def test_item_init(x):
    assert x.name == 'computer'
    assert x.price == 100
    assert x.quantity == 10
    assert Item.all[0] is x


def test_item_apply_discount(x):
    Item.pay_rate = 0.95
    x.apply_discount()
    assert x.price == 95


def test_item_calculate_total_price(x):
    assert x.calculate_total_price() == 1000

def test_item_property(x):
    x.name = 'IphoneXR'
    assert x.name == 'IphoneXR'


def test_item_instantiate_from_csv():
    helper = len(Item.all)
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert (len(Item.all) - helper) == 5


def test_item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('5.0') == 5