# Программа 10.10
# Эта программа демонстрирует класс BankAccount

import bankaccount2

def main():
    # Получить начальный остаток.
    start_bal = float(input('Введите свой начальный остаток: '))

    # Создать объект BankAccount.
    savings = bankaccount2.BankAccount(start_bal)
    
    # Внести на счет зарплату пользователя.
    pay = float(input('Какую сумму вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счет.')
    savings.deposit(pay)
    
    # Показать остаток.
    print(savings)
    
    # Получить сумму для снятия с банковского счета.
    cash = float(input('Какую сумму Вы желаете снять со счета? '))
    print('Снимаю эту сумму с Вашего банковского счета.')
    savings.withdraw(cash)
    
    # Показываем остаток.
    print(savings)

if __name__ == '__main__':
    main()
