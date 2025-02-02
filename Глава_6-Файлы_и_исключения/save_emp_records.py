# Эта программа получает от пользователя данные о сотрудниках 
# и сохраняет их в виде записей в файле employee.txt.

def main():
    # Получить количество записей о сотрудниках для создания.
    num_emps = int(input('Сколько записей о сотрудниках' + "Вы хотите создать? "))
    
    
    # Открыть файл для записи.
    emp_file = open('employee.txt', 'a')
    
    # Получить данные каждого сотрудника 
    # и записать их в файл.
    for count in range(1, num_emps + 1):
        # Получить данные о сотруднике.
        print(f'Введите данные о сотруднике № {count}')
        name = input('Имя: ')
        id_num = input('Идентификационный номер: ')
        dept = input('Отдел: ')
        
        # Записать в файл данные как запись.
        emp_file.write(f'{name}\n')
        emp_file.write(f'{id_num}\n')
        emp_file.write(f'{dept}\n')
        
        # Показать пустую строку.
        print()

        # Закрыть файл.
    emp_file.close()
    print('Записи о сотрудниках сохранены в employee.txt.')
    
# Call the main function
if __name__ == '__main__':
    main()

