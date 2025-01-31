import sqlite3


def __get_employees():
    employee_list = []
    conn = None
    try:
        # Присоединиться к базе данных.
        conn = sqlite3.connect('employees.db')
        cur = conn.cursor()
        # Исполнить запрос SELECT
        cur.execute('''SELECT Name FROM Employees''')

        # Получить результаты запроса в виде списка.
        employee_list = [n[0] for n in cur.fetchall()]
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn is not None:
            conn.close()
        return employee_list


if __name__ == '__main__':

    print('SELECT Name \n',__get_employees())
