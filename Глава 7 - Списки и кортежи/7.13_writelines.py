# Эта программа применяет метод writelines() для сохранения 
# списка строковых значений в файл.

def main():
    # Создать список строковых значений.
    cities = ['Нью-Йорк', 'Бостон', 'Атланта', 'Даллас']
    
    # Открыть файл для записи.
    outfile = open('cities.txt', 'w')
    
    # Записать список в файл.
    outfile.writelines(cities)
    
    # Закрыть файл.
    outfile.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()