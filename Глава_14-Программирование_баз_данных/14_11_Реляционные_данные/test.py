import sqlite3


conn = sqlite3.connect('employees.db')
conn.close()
print(type(conn))