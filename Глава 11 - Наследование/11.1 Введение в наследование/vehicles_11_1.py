class Automobile:
    """Класс содержит общие данные об автомобиле на складе."""

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price


class Car(Automobile):
    """Класс представляет собой легковой автомобиль.
    Он является подклассом класса Automobile.
    """

    # Метод __init__ принимает аргументы для фирмы-изготовителя,
    # модели, пробега, цены и количества дверей.
    def __init__(self, make, model, mileage, price, doors):
        # Вызвать метод __init__ надкласса и передать
        # требуемые аргументы. Обратите внимание, что мы также
        # передаем self в качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)
        # Инициализировать атрибут __doors.
        self.__doors = doors

    # Метод set_doors является методом-мутатором атрибута __doors.
    def set_doors(self, doors):
        self.__doors = doors

    def get_doors(self):
        return self.__doors
