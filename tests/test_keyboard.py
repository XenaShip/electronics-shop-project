from src.keyboard import KeyBoard
import pytest


def test_language():
    my_keyboard = KeyBoard('KeyBoard', 9600, 5)
    assert my_keyboard.language == 'EN'
    my_keyboard.change_lang()
    assert my_keyboard.language == 'RU'