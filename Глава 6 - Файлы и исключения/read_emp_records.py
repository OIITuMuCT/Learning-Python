# Эта программа показывает записи, которые 
# находятся в файле employee.txt.

def main():
    # Открыть файл employee.txt.
    emp_file = open('employee.txt', 'r')
    
    # Прочитать первую строку в файле, т.е. 
    # поле с именем сотркдника первой записи.
    name = emp_file.readline()
    
    # Если поле прочитанно, то продолжить обработку.
    while name != '':
        # Прочитать поле с идентификационным номером.
        id_num = emp_file.readline()
        
        # Прочитать поле с названием отдела.
        dept = emp_file.readline()
        
        # удалить символы новой строки из полей.
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')
        
        # Показать запись.
        print(f'Имя: {name}')
        print(f'ID: {id_num}')
        print(f'Отдел: {dept}') 
        print()
        
        # Прочитать поле с именем следующей записи.
        name = emp_file.readline()
        
    # Закрыть файл.
    emp_file.close()
    
# Вызвать главную функцию.
if __name__ == '__main__':
    main()