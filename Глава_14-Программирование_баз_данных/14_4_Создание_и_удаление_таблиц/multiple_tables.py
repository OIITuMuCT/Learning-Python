

import sqlite3

def main():
    # Присоединиться к базе данных.
    conn = sqlite3.connect('company.db')
    
    # Получить курсор.
    cur = conn.cursor()

    # Добавить таблицу Customers.
    cur.execute('''CREATE TABLE Customers (
        CustomerID INTEGER PRIMARY KEY NOT NULL,
        Name TEXT,
        Email TEXT)''')
    # Добавить таблицу Employees.
    cur.execute('''CREATE TABLE Employees (EmployeesID INTEGER PRIMARY KEY NOT NULL,
                Name TEXT,
                Position TEXT)''')
    # Зафиксировать изменения.
    conn.commit()
    
    # Закрыть соединение.
    conn.close()

if __name__ == '__main__':
    main()