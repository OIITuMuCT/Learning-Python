import sqlite3

def main():
    conn = sqlite3.connect('chocolate.db')

    cur = conn.cursor()

    # Получить от пользователя ID
    pid = int(input('Введите ID изделия для его удаления: '))
    
    # Получить описание этого изделия.
    cur.execute('''SELECT Description FROM Chocolate
                WHERE ProductID == ?''', (pid,))
    results = cur.fetchone()
    
    if results != None:
        # Подтвердить желание удалить изделие.
        sure = input(f'Вы уверены, что хотите удалить '
                     f'{results[0]}? (д/н): ')
        
        # Если да, то удалить изделие.
        if sure.lower() == 'д':
            cur.execute('''DELETE FROM Chocolate 
                        WHERE ProductID == ?''', 
                        (pid,))
            conn.commit()
            print("Изделие было удалено.")
        else:
            # Сообщении об ошибке.
            print(f'ID изделия {pid} не найден.')
    
    # Закрыть соединение с базой данных.
    conn.close()

if __name__ == '__main__':
    main()