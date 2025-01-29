# Эта программа создает 
# Create table chocolate.db
# rows:
# ProductID INTEGER PRIMARY KEY NOT NULL,
# Description TEXT,
# UnitCost REAL,
# RetailPrice REAL,
# UnitsOnHand INTEGER
# add data in Chocolate

import sqlite3

def main():
    # Присоединиться к базе данных.
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()
    # Создать таблицу.
    cur.execute('''CREATE TABLE IF NOT EXISTS Chocolate (ProductID INTEGER PRIMARY KEY NOT NULL,
                Description TEXT, UnitCost REAL, RetailPrice REAL, UnitsOnHand INTEGER)''')

    # Добавить данные в таблицу.
    again = 'д'
    while again == 'д':
        # Получить описание, стоимость единицы, розничную цену, единиц в наличии:
        description = input("Описание: ")
        unit_cost = float(input("Стоимость единицы: "))
        retail_price = float(input("Розничная цена: "))
        unit_on_hand = int(input("Единиц в наличии: "))
        # Добавить позицию в таблицу Chocolate.
        cur.execute('''INSERT INTO Chocolate (Description, UnitCost, RetailPrice, UnitsOnHand)
                    VALUES (?, ?, ?, ?)''', (description, unit_cost, retail_price, unit_on_hand))
        # Добавить еще раз?
        again = input('Добавить еще одну позицию? (д/н): ')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()