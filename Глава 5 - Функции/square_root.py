# Эта программа демонстрирует функцию sqrt.
import math

def main():
    # получить число
    number = float(input('Введите число: '))
    
    # получить квадратный корень числа.
    square_root = math.sqrt(number)
    
    # показать квадратный корень.
    print(f'Квадратный корень из {number} составляет {square_root}')
    
# вызвать главную функцию.
main()