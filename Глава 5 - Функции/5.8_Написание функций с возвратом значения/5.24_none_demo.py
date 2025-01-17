# эта программа демонстриирует ключевое слово None.

def main():
    # Получить от ползователя два числа.
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите еще одно число: '))
    
    # calling func /
    quotient = divide(num1, num2)
    
    # вывести результат на экран.
    if quotient is None:
        print('Деление на ноль не возможно.')
    else:
        print(f'{num1} поделить на {num2} равняется {quotient}')
        
# Функция divide делит numl на num2 и возвращает
# результат. Если num2 равно О, то указанная функция
# возвращает None.
def divide(num1, num2):
    if num2 == 0:
        result = None
    else:
        result = num1 / num2
    return result 
    
# Исполнить главную функцию.
main()
    