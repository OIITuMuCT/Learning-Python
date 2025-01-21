# Эта программа тестирует класс CellPhone.

import cellphone_10_12

def main():
    # Получить данные о телефоне.
    man = input('Введите производителя: ')
    mod = input('Введите номер модели: ')
    retail = input('Введите розничную цену: ')

    # Создать экземпляр класса CellPhone.
    phone = cellphone_10_12.CellPhone(man, mod, retail)
    
    # Показать введенные данные. 
    print('Вот введенные вами данные: ')
    print(f'Производитель: {phone.get_manufact()}')
    print(f'Номер модели: {phone.get_model()}')
    print(f'Розничная цена: {phone.get_retail_price()}')

if __name__ == '__main__':
    main()