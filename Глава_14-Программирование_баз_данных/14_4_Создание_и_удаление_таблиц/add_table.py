import sqlite3

def main():
    # Подсоединится к базе данных.
    conn = sqlite3.connect('inventory.db')
    
    # Получить курсор.
    cur = conn.cursor()

    # Добавить таблицу Inventory.
    cur.execute('''CREATE TABLE Inventory (ItemId INTEGER PRIMARY KEY NOT NULL,
                ItemName TEXT, Price REAL)''')
    # зафиксировать изменения.
    conn.commit()
    
    # Закрыть соединение.
    conn.close()

if __name__ == '__main__':
    main()