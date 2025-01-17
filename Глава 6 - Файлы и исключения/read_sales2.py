# Эта программа применяет цикл for для чтения 
# всез значений из файла sales.txt.

def main():
    # открыть файл для чтения.
    sales_file = open('sales.txt', 'r')
    
    # Прочитать все строки из файла.
    for line in sales_file:
        # Конвертировать строку в число с плавающей точкой.
        amount = float(line)
        # Отформатировать и показать сумму.
        print(f'{amount:.2f}')
        
    # закрыть файл.
    sales_file.close()
    
# Вызвать главную функцию.
if __name__ == '__main__':
    main()