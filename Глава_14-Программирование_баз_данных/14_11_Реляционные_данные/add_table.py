import sqlite3

def main():
    conn = None
    try:
        conn = sqlite3.connect('employees.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE Employees(EmployeeID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT,
                                        Position TEXT,
                                        DepartmentID INTEGER,
                                        LocationID INTEGER,
                                        FOREIGN KEY (DepartmentID) REFERENCES
                                                Departments(DepartmentID),
                                        FOREIGN KEY (LocationID) REFERENCES
                                                Locations(LocationID))''')
        conn.commit()

    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    main()