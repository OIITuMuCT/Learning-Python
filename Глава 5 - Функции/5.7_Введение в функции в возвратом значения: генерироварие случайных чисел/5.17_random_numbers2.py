# Эта программа показывает пять случайных чисел
# из диапазона 1 до 100.
import random

def main():
    for count in range(5):
        # Получить случайное число.
        number = random.randint(1, 100)
        print(number) 


# Вызвать главную функцию.
main() 
