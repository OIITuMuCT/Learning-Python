# Эта программа демонстрирует класс Car.

import vehicles_11_1

def main():
    # Создать объект на основе Car. 
    # Легковое авто: 2007 Audi c 12500 милями пробега,
    # ценой $ 21500.00 и с 4 дверьми.
    used_car = vehicles_11_1.Car('Audi', 2007, 12500, 21500.0, 4) 

    # Показать данные легкового авто.
    print('Изготовитель: ', used_car.get_make())
    print('Модель:', used_car.get_model())
    print('Пробег:', used_car.get_mileage())
    print('Цена:', used_car.get_price())
    print('Количество дверей:', used_car.get_doors())

if __name__ == '__main__':
    main()