# Эта программа показывает итоговый объем
# продаж из файла sales data.txt.

def main():
    # Инициализировать накопитель.
    total = О.О
    
    try:
        # Открыть файл sales_data.txt.
        infile = open('sales_data.txt', 'r')
        
        # Прочитать значения из файла
        # и накопить их в переменной.
        for line in infile:
            arnount = float(line)
            total += arnount
            
        # Закрыть файл.
        infile. close ()
    except Exception as err:
        print(err)
    else:
    # Напечатать итог.
    print(f'{total:,.2f}')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()