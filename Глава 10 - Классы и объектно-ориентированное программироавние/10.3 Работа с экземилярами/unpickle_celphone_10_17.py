# Эта программа расконсервирует объекты CellPhone.
import pickle
import cellphone_10_12

FILENAME = 'cellphones.dat'

def main():
    end_of_file = False
    
    input_file = open('cellphones.dat', 'rb' )

    while not end_of_file:
        try:
            phone = pickle.load(input_file)
            # Показать данные о сотовом телефоне.
            display_data(phone)
        except EOFError:
            # Установить флаг, чтобы обозначить, что 
            # был достигнут конец файла.
            end_of_file = True
    # закрыть файл.
    input_file.close()

def display_data(phone):
    print(f'Производитель: {phone.get_manufact()}')
    print(f'Номер модели: {phone.get_model()}')
    print(f'Розничная цена: {phone.get_retail_price():,.2f}')
    print()

if __name__ == '__main__':
    main()