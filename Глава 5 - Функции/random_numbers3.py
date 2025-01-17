# Эта программа показывает пять случайных чисел
# из диапазона 1 до 100.
import random

def main():
    for count in range(5):
        print(random.randint(1, 100)) 


# Вызвать главную функцию.
main() 
