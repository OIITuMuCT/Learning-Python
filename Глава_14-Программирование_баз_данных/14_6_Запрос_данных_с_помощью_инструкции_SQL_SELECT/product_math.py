import sqlite3

def main():
    # Connect to db
    conn = sqlite3.connect('chocolate.db')

    cur = conn.cursor()

    cur.execute('SELECT MIN(RetailPrice) FROM Chocolate')
    lowest = cur.fetchone()[0]
    
    cur.execute('SELECT MAX(RetailPrice) FROM Chocolate')
    highest = cur.fetchone()[0]

    cur.execute('SELECT AVG(RetailPrice) FROM Chocolate')
    average = cur.fetchone()[0]

    # Показать результаты.
    print(f'Минимальная цена: ${lowest:.2f}')
    print(f'Максимальная цена: ${highest:.2f}')
    print(f'Средняя цена: ${average:.2f}')
    
    # Close connect to db
    conn.close()

if __name__ == '__main__':
    main()


