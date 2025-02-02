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
    """
    Класс представляет собой легковой автомобиль.
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

class Truck(Automobile):
    """ 
    Класс Truck представляет пикап. 
    Он является подклассом класса Automobile. 
    """
    def __init__(self, make, model, mileage, price, drive_type):
        """
        Метод __init__ принимает аргументы для
        изготовителя, модели, пробега, цены и типа привода пикапа.
        """
        # вызвать метод __init__ надкласса и передать
        # требуемые аргументы. Обратите внимание, что мы также
        # передаем self в качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)

        # Инициализировать атрибут __drive_type
        self.__drive_type = drive_type

    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    def get_drive_type(self):
        return self.__drive_type


class SUV(Automobile):
    """
    Класс SUV представляет джип. 
    Он является подклассом Automobile.  
    """
    def __init__(self, make, model, mileage, price, pass_cap):
        Automobile.__init__(self, make, model, mileage, price)
        self.__pass_cap = pass_cap
        
    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap
    
    def get_pass_cap(self):
        return self.__pass_cap
