import sqlite3

def main():
    # Connect to db
    conn = sqlite3.connect('chocolate.db')
    # Get cursor
    cur = conn.cursor()
    cur.execute('SELECT Description, RetailPrice FROM Chocolate')
    # Извлечь первую строку результатов.
    row = cur.fetchone()
    
    while row != None:
        # Show first row.
        print(f'{row[0]:35} {row[1]:5}')
        
        row = cur.fetchone()
    # Connect close.
    conn.close()

if __name__ == '__main__':
    main()
