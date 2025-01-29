import sqlite3

def main():
    conn = sqlite3.connect('chocolate.db')

    cur = conn.cursor()

    pid = int(input('Введите ID изделия: '))
    
    cur.execute('''SELECT Description, RetailPrice FROM Chocolate 
                WHERE ProductID == ?''', (pid,))
    results = cur.fetchone()
    
    # Если ID изделия найден, то продолжить...
    if results != None:
        # Напечатать текущую цену.
        print(f'Текущая цена для {results[0]}: '
              f'$ {results[1]:.2f}')
        # Получить новую цену.
        new_price = float(input('Введите новую цену: '))
        # Обновить новую цену в таблице.
        cur.execute('''UPDATE Chocolate
                    SET RetailPrice = ?
                    WHERE ProductID == ?''',
                    (new_price, pid))
        # Зафиксировать изменения.
        conn.commit()
        print('Цена была изменена.')
    else:
        # Сообщение об ошибке.
        print(f'ID изделия {pid} не найден.')
    # закрыть соединение с базой данных.
    conn.close()

if __name__ == "__main__":
    main()