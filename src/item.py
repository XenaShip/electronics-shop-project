import csv
from src.InstantiateCSVError import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception ("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, fn='src/items.csv'):
        try:
            csvfile = open(fn, newline='')
            csvfile.reader = csv.DictReader(csvfile)
            fieldnames = csvfile.reader.fieldnames
            if len(fieldnames) != 3:
                raise InstantiateCSVError
            for row in csvfile.reader:
                # print(row['name'], row['price'], row['quantity'])
                if (row['name'] is None) or (row['price'] is None) or (row['quantity'] is None):
                    raise InstantiateCSVError
                else:
                    Item(row['name'], row['price'], row['quantity'])
        except FileNotFoundError as e:
            print(f'FileNotFoundError: Отсутствует файл {fn}')
        except InstantiateCSVError as e:
            print(f'{e}: Файл {fn} поврежден')

    @staticmethod
    def string_to_number(s):
        s = float(s)
        return int(s)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        return self.quantity + other.quantity

