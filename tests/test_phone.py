from src.phone import Phone
import pytest


def test_init():
    my_phone = Phone('Iphone', 40000, 20, 2)
    assert my_phone.name == 'Iphone'
    assert my_phone.price == 40000
    assert my_phone.quantity == 20
    assert my_phone.number_of_sim == 2


def test_repr():
    my_phone = Phone('Iphone', 40000, 20, 2)
    assert repr(my_phone) == "Phone('Iphone', 40000, 20, 2)"
