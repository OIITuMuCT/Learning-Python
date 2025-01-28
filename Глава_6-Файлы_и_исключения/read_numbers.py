# Эта программа демонстрирует, как прочитанные из файла 
# числа конвертируются из строкового представления 
# перд тем как они используются в математической операциию

def main():
    # Открыть файл для чтения.
    infile = open('numbers.txt', 'r')
    
    # Прочитать три числа из файла.
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    
    # Close file.
    infile.close()
    
    # Сложить три числа.
    total = num1 + num2 + num3
    
    # Показать числа и их сумму.
    print(f'Числа: {num1}, {num2}, {num3}')
    print(f'Их сумма: {total}')
    
# Calling main
if __name__ == '__main__':
    main()