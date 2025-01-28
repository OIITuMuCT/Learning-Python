# Program 10.18

class Contact:
    """Класс Contact содержит контактную информацию"""

    def __init__(self, name, phone, email):
        """ Метод инициализирует атрибуты """
        self.__name = name
        self.__phone = phone
        self.__email = email

    def set_name(self, name):
        """ Метод устанавливает атрибут name """
        self.__name = name

    def set_phone(self, phone):
        """ Метод устанавливает атрибут phone """
        self.__phone = phone

    def set_email(self, email):
        """ Метод устанавливает атрибут email """
        self.__email = email

    def get_name(self):
        """ Метод возвращает атрибут name """
        return self.__name
    
    def get_phone(self):
        return self.__phone
    
    def get_email(self):
        return self.__email
    
    def __str__(self):
        """ Метод возвращает состояние объекта в виде строкового значения """
        return f'Имя: {self.__name}\n' + \
               f'Телефон: {self.__phone}\n' + \
               f'Электронная почта: {self.__email}'

