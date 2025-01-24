# Эта программа применяет 
# рекурсию для вычисления факториала числа.

def main():
    number = int(input('Введите неотрицательное целое число: '))

    fact = factorial(number)
    
    # Показать факториал
    print(f'Факториал числа {number} равняется {fact}.')

def factorial(num):
    if num == 0:
        return 1
    else: return num * factorial(num - 1)

if __name__ == '__main__':
    main()