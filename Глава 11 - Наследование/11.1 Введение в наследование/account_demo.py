# Эта программа создает экземпляр класса SavingsAccount
# и экземпляр класса CD

import accounts

def main():
    # Получить номер счета, процентную ставку,
    # и остаток сберегательного счета.
    print('Введите данные о сберегательном счете.')
    acct_num = input('Номер счета: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))

    # создать объект SavingsAccount.
    savings = accounts.SavingsAccount(acct_num, int_rate, balance)

    # Получить номер счета, процентную ставку,
    # остаток счета и дату погашения CD.
    print('Введите данные о счете CD.')
    acct_num = input('Номер счета: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))
    maturity = input('Дата погашения: ')
    cd = accounts.CD(acct_num, int_rate, balance, maturity)

    # Показать введенные Вами данные.
    print('Вот введенные Вами данные: ')
    print()
    print('Сберегательный счет')
    print('-------------------')
    print(f'Номер счета: {savings.get_account_num()}')
    print(f'Процентная ставка: {savings.get_interest_rate()}')
    print(f"Остаток: {savings.get_balance():,.2f}")
    print()
    print('Счет депозитарного сертификата (CD)')
    print("-" * len("Счет депозитарного сертификата (CD)"))
    print(f"Номер счета: {cd.get_account_num()}")
    print(f"Процентная ставка: {cd.get_interest_rate()}")
    print(f"Остаток: {cd.get_balance():,.2f}")
    print(f'Дата погашения: {cd.get_maturity_date()}')

if __name__ == '__main__':
    main()