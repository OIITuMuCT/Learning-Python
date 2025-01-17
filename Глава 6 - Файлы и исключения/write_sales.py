# Эта программа предлагает пользователю ввести суммы 
# продаж и записывает эти суммы в файл sales.txt.

def main():
    # Get the numbers of days.
    num_days = int(input('За какое колво дней ' + 
                         'Вы располагаете продажами? '))
    
    # Open a new file named sales.txt.
    sales_file = open('sales.txt', 'w')
    
    # get the amounth of sales for each and write 
    # it to the file.
    for count in range(1, num_days + 1):
        # get the sales for a day.
        sales = float(input(f'Введите продажи за день № {count}: '))
        # записать сумму продаж в файл.
        sales_file.write(f'{sales}\n')
    
    # Закрыть файл.
    sales_file.close()
    print('Данные записанны в sales.txt.')
    
# Call the main func.
if __name__ == '__main__':
    main()
        
         