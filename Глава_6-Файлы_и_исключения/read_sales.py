# эта программа читает все значения из 
# файла sales.txt

def main():
    # Open the sales.txt file for reading.
    sales_file = open('sales.txt', 'r')
    
    # прочитать первую строку из файла, но 
    # пока не конвертировать в число. Сначала нужно 
    # выполнить проверку на пустое строковое значение.
    line = sales_file.readline()
    
    # Продолжить обработку до тех пор, пока из redline 
    # не будет возвращена пустая строка.
    while line != '':
        amount = float(line)
        
        # Отформатировать и показать сумму.
        print(f'{amount:.2f}')
        
        # Прочитать следующую строку.
        line = sales_file.readline()
        
    # Закрываем файл.
    sales_file.close()
        
# Вызываем главную функцию.
if __name__ == '__main__':
    main()