class CellPhone:
    """
    Класс CellPhone содержит данные о сотовом телефоне.
    """

    def __init__(self, manufact, model, price):
        """Метод __init__ инициализирует атрибуты."""
        self.__manufact = manufact
        self.__model = model
        self.__price = price

    def set_manufact(self, manufact):
        """Метод  set_manufact принимает аргумент для производителя телефона."""
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, price):
        """Метод set_retail_price принимает аргумент для розничной цены телефона."""
        self.__price = price

    def get_manufact(self):
        """Метод get_manufact возвращает производителя телефона"""
        return self.__manufact

    def get_model(self):
        """Метод возвращает номер модели телефона."""
        return self.__model

    def get_retail_price(self):
        """Метод возвращает розничную цену телефона."""
        return self.__price
