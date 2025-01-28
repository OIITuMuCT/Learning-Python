def main():
    try:
        # Получить количество отработаннь часов.
        hours = int (input('Сколько часов вы отработали? '))
        
        # Получитьпочасовую ставку оплаты труда.
        pay_rate =float(input ( 'Bвeдитe свою почасовую ставку: ' ))
        
        # Вычислить заработную плату до удержаний.
        gross_pay = hours * pay_rate
        
        # Показать заработную плату.
        print(f'Заработная плата: ${gross_pay:,.2f})')
    except ValueError as err:
        print(err)



# Вызвать главную функцию.
if __name__ == '__main__':
    main()