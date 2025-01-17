# Эта программа демонстирирует преобразование 
# числвых значений в строковые перед их 
# записью в текстовый файл.

def main():
    # Открыть файл для записи.
    outfile = open('numbers.txt', 'w')
    
    # Получить от пользователя три числа.
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите число еще одно: '))
    num3 = int(input('Введите число еще одно: '))

    # Записать эти числа в файл.
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')
    
    # Close file.
    outfile.close()
    print('Данные записанны в numbers.txt')
    
# Calling main
if __name__ == '__main__':
    main()