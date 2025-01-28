# Эта программа демонстрирует расконсервацию объектов.
import pickle

# Главная функция.
def main():
    end_of_file = False # Для обозначения конца файла.
    
    # Открыть файл для двоичного чтения.
    input_file = open('info.dat', 'rb')
    
    # прочитать файл до конца.
    while not end_of_file:
        try:
            # Расконсервировать следующий объект.
            person = pickle.load(input_file)
            
            # Показать объект.
            display_data(person)
        except EOFError:
            # Установить флаг, чтобы обозначить, что был достигнут конец файла.
            end_of_file = True
    # Закрыть файл.
    input_file.close()

def display_data(person):
    print('Name:', person['name'])
    print('Age:' , person['age'])
    print('weight:', person['weight'])
    print()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()