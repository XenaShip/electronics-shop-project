from src.item import Item
import pytest
from src.InstantiateCSVError import InstantiateCSVError

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
    Item.instantiate_from_csv('l')
    assert 'FileNotFoundError: Отсутствует файл l'
    Item.instantiate_from_csv('src/items_broken.csv')
    assert 'InstantiateCSVError: Файл src/items_broken.csv поврежден'


def test_item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('5.0') == 5


def test_item_repr():
    my_item= Item("Смартфон", 10000, 20)
    assert repr(my_item) == "Item('Смартфон', 10000, 20)"


def test_item_str():
    my_item = Item("Смартфон", 10000, 20)
    assert str(my_item) == 'Смартфон'


def test_add():
    my_item = Item("Смартфон", 10000, 20)
    my_item2 = Item("Смартфон", 10000, 20)
    assert my_item + my_item2 == 40