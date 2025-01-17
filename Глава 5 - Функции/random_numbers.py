# Этапрограмма показывает случайное число
# из диапазона 1 до 100.
import random

def main():
    number = random.randint(1, 100)
    # Показать число.
    print(f'Числло равняется {number}.')
    
#  Calling main
main()