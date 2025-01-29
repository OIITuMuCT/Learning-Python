import sqlite3

def main():
    # переменная управления циклом.
    again = 'д'
    
    # Присоединиться к базе данных.
    conn = sqlite3.connect('inventory.db')
    # получить курсор.
    cur = conn.cursor()
    
    while again == 'д':
        # Получить название и цену позиции.
        item_name = input('Название: ')
        price = float(input('Цена: '))
        
        # Добавить позицию в таблицу inventory.
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                    VALUES (?, ?)''',
                    (item_name, price))
        # Добавить еще раз?
        again = input('Добавить еще одну позицию? (д/н): ')
    
    # Зафиксировать изменения.
    conn.commit()

    # закрыть соединение.
    conn.close()

if __name__ == '__main__':
    main()