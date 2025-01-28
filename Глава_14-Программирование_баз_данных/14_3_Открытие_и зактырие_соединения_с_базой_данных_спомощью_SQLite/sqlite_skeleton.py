# Программа 14.1 демонстрирует исходный код Python, который выполняет эти шаги.
import sqlite3

def main():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()

    # ! Здесь вставить код для выполнения операций с базой данных.
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()