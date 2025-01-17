# Эта программа демонсстрирует использование глобальной константы
# для предоставления ставки износа компании.
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Введите зароботную плату: '))
    bonus = float(input('Введите сумму премий: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)
    
# функция show_pay_contrib принимает зароботную 
# плату в качестве аргумента и показывает взнос
# в пенсионные накопления исходя из этого размера оплаты. 
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print(f'Взнос исходя из зароботной платы: ${contrib:,.2f}.')
    
# Функция show_bonus_contrib принимает сумму премий
# в качестве аргумента и показыват взнос
# в пенсионное накопление исходя из этой суммы оплаты.
def show_bonus_contrib(bonus):
    contrib = bonus*CONTRIBUTION_RATE
    print(f'Взнос исходя из праемий: ${contrib:,.2f}.')

# Вызвать главную функцию.
main()