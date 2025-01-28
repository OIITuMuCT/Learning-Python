# Эта программа консервирует объекты CellPhone.
import pickle
import cellphone_10_12

# Константа для имени файла. 
FILENAME = 'cellphones.dat'

def main():
    # Инициализировать переменную для управления циклом.
    again = 'д'

    # Открыть файл
    output_file = open(FILENAME, 'wb')
    

    # Получить данные от пользователя.
    while again.lower() == 'д':
        # Получить данные о сотовом телефоне.
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Введите розничную цену: '))

        # Создать объект CellPhone.
        phone = cellphone_10_12.CellPhone(man, mod, retail)
        
        # Законсервировать объект и записать его в файл.
        pickle.dump(phone, output_file)
        
        # Получить еще один элемент данных?
        again = input('Введите еще одни элемент данных? (д/н): ')
    
    # Закрыть файл.
    output_file.close()
    print(f'Данные записаны в {FILENAME}')

# Вызывать главную функцию.
if __name__ == '__main__':
    main()