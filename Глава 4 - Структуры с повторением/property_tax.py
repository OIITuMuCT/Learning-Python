# Эта программа показывает налоги на имущество.

TAX_FACTOR = 0.0065 # Представляет налоговый коэффициент.

# Получить номер первоно лота.
print('Введите номер имушественного лота либо 0, чтобы завершить.')
lot = int(input('Номер лота: '))

# Продолжить обработку, пока ползователь
# не введет номер лота 0.
while lot != 0:
    # Получить стоимость имущества.
    value = float(input('Введите стоимость имущества: '))

     #  Исчислить налог на имущество.
    tax = value * TAX_FACTOR
    
    # Показать налог на имущество.
    print(f'Налог на имущество: ${tax:,.2f}')

    # получить следующий номер лота.
    print('Введите следующий номер либо 0, чтобы завершить.') 
    lot = int(input('Номер лота: '))