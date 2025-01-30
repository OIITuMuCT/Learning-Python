import sqlite3

def main():
    conn = None
    try:
        conn = sqlite3.connect('employees.db')
        cur = conn.cursor()

        cur.execute('PRAGMA foreign_keys=ON')
        
        cur.execute('''INSERT INTO Employees
                    (Name, Position, DepartmentID, LocationID) 
                    VALUES ("Билл Свифт", "Стажер", 99, 1)''')
        conn.commit()
        print('Сотрудник успешно добавлен.')
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    main()