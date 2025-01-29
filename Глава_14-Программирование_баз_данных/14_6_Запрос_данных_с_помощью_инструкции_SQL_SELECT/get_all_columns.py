import sqlite3

def main():
    # connect to db
    conn = sqlite3.connect('chocolate.db')
    # Get cursor
    cur = conn.cursor()
    # Выбрать все столбцы из каждой строки таблицы Chocolate
    cur.execute('SELECT * FROM Chocolate')
    
    result = cur.fetchall()
    
    for row in result:
        print(f'{row[0]:2} {row[1]:35} {row[2]:5} {row[3]:6} {row[4]:5}')
    
    conn.close()

if __name__ == '__main__':
    main()