import sqlite3


def main():
    # Присоединяемся к базе данных.
    conn = sqlite3.connect("inventory.db")

    # Получить курсор.
    cur = conn.cursor()
    # Добавить строку в таблицу Inventory.
    cur.execute(
        '''INSERT INTO Inventory (ItemName, Price)
                VAlUES ("Отвертка", 4.99)'''
    )
    cur.execute(
        """INSERT INTO Inventory (ItemName, Price)
                VALUES ('Молоток', 12.99)"""
    )
    cur.execute(
        '''INSERT INTO Inventory (ItemName, Price) 
                VALUES ("Плоскогубцы", 14.99)'''
    )
    # Сохранить изменения.
    conn.commit()
    # Закрыть базу данных.
    conn.close()


if __name__ == "__main__":
    main()
