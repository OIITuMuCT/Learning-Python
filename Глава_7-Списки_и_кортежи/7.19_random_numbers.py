# Эта программа присваивает случайные числа 
# двумерному списку.
import random

# Константы для строк и столбцов
ROWS = 3
COLS = 4

def main():
    # Создать двумерный список.
    values = [[0]*4, [0]*4, [0]*4]
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)
    # Выведем числа из списка.
    for row in values:
        for item in row: 
            print(item, end=' ')
    # Показать случайные числа. 
    print(values)
    
# Вызвать главную функцию.
if __name__ == '__main__':
    main()