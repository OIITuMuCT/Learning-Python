# Эта про грамма имитирует 10 бро ско в мо неты.
import random


# Константы.
HEADS = 1       # Орел.
TAILS = 2       # Решка.
TOSSES = 10     # Количество брос ко в.


def main():
    for toss in range(TOSSES):
        # Имитиро вать бросан ие мо неты.
        if random.randint(HEADS, TAILS) == HEADS:
            print('Орел')
        else:
            print('Решка')


# Вызвать главную функцию.
main()
