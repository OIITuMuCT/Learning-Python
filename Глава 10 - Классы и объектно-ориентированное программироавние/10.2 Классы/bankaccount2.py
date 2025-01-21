# программа 10.9
# Класс BankAccount имитирует банковский счет.

class BankAccount:

    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Ошибка: недостаточно средств.')

    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return f'Остаток составляет ${self.__balance:,.2f}'
