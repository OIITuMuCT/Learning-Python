import sqlite3

def main():
    print('Программа запущена ...')
    # Переменная управления циклом.
    again = "д"
    
    while (again == 'д'):
        #  Получить ID товара, название и цену.
        item_id = int(input('ID товара: '))
        item_name = input('Название товара: ')
        price = float(input('Цена: '))

        add_item(item_id, item_name, price)
        
        again = input('Добавить еще одну позицию? (д/н): ')

# Функция add_item добавляет позицию в базу данных.
def add_item(item_id, name, price):
    # Инициализировать переменную соединения
    conn = None
    try:
        # Подсоединиться к базе данных.
        conn = sqlite3.connect("inventory.db")

        # получить курсор.
        cur = conn.cursor()
        print('Выполняется добавление в базу данных')
        # Добавить позицию в таблицу Inventory.
        cur.execute('''INSERT INTO Inventory (ItemID, ItemName, Price) VALUES (?, ?, ?)''',
                    (item_id, name, price))
        # зафиксировать изменения.
        conn.commit()
    except sqlite3.Error as err:
        print(err)

    finally:
        if conn is not None:
            # Закрыть соединение.
            conn.close()

if __name__ == '__main__':
    main()
