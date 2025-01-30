import sqlite3

DATABASE = 'inventory.db'
MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

def main():
    """Главная функция выполняет операции CRUD с базой данных Inventory"""
    choice = 0
    while choice is not EXIT:
        display_menu()
        choice = get_menu_choice()

        if choice == CREATE:
            create()
        if choice == READ:
            read()
        if choice == UPDATE:
            update()
        if choice == DELETE:
            delete()


def display_menu():
    """Функция выводит на экран главное меню"""
    print('\n----- Меню ведения учета инструментов -----')
    print('1. Создать новую позицию')
    print('2. Прочитать позицию')
    print('3. Обновить позицию')
    print('4. Удалить позицию')
    print('5. Выйти из программы')

def get_menu_choice():
    """ Получает от пользователя пункт меню. """
    # Получить от пользователя вариант действий
    choice = int(input('Введите ваш вариант: '))
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Допустимые варианты таковы: {MIN_CHOICE} - {MAX_CHOICE}.')
        choice = int(input('Введите ваш вариант: '))

    return choice

def create():
    """Создает новую позицию в базе данных"""
    print('Создать новую позицию')
    name = input('Название позиции: ')
    price = input('Цена: ')
    insert_row(name, price)

def read():
    """Функция читает существующую позицию """
    name = input('Введите название искомой позиции: ')
    num_found = display_item(name)
    print(f'{num_found} строк(а) найдено.')

def update():
    """ Функция обновляет данные существующей позиции."""
    # Сначала показать пользователю найденные строки.
    read()
    # Получить ID выбранной позиции.
    selected_id = int(input('Выберите ID обновляемой позиции: '))

    # Получить новые значения для названия и цены.
    name = input('Введите новое название для позиции: ')
    price = input('Введите новую цену: ')
    
    # Обновить строку.
    num_updated = update_row(selected_id, name, price)
    print(f'{num_updated} строк(а) обновлено.')

def delete():
    """Функция удаляет позицию"""
    # Сначала показать пользователю найденные строки.
    read()
    
    # Получить ID выбранной позиции.
    selected_id = int(input('Выберите ID удаляемой позиции: '))

    # Подтвердить удаление.
    sure = input('Вы уверены, что хотите удалить эту позицию? (д/н): ')
    if sure.lower() == 'д':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} строк(а) удалено.')

def insert_row(name, price):
    """ вставляет строку в таблицу Inventory """
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                    VALUES (?, ?)''',
                    (name, price))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn is not None:
            conn.close()

def display_item(name):
    """функция выводит на экран все позиции с совпадающими названиями позиций. """
    conn = None
    results = []
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Inventory
                    WHERE ItemName == ?''',
                    (name,))
        results = cur.fetchall()

        for row in results:
            print(f'ID: {row[0]:<3} Название: {row[1]:<15} '
                  f'Цена: {row[2]:<6}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn is not None:
            conn.close()
        # Вернуть число совпавших строк.
    return len(results)

def update_row(id, name, price):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute('''UPDATE Inventory
                    SET ItemName = ?, Price = ?
                    WHERE ItemID == ?''',
                    (name, price, id))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn is not None:
            conn.close()

        return num_updated

def delete_row(id):
    conn = None
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Inventory
                    WHERE ItemID == ?''',
                    (id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn is not None:
            conn.close()

        return num_deleted

if __name__ == '__main__':
    main()
