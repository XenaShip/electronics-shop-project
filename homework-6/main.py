from src.item import Item

if __name__ == '__main__':
    Item.instantiate_from_csv('l')
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv('src/items_broken.csv')
    # InstantiateCSVError: Файл item.csv поврежден
