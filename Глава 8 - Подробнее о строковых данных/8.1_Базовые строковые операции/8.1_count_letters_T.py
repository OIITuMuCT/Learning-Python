# Эта программа подсчитывает количество появлений
# буквы Т (в верхнем регистре)
# в строковом значении.

def main():
    # Создать переменную, в которой будет храниться количество.
    # Значение переменной должно начинаться с 0.
    count = 0
    
    # Получить от пользователя строковое значение.
    my_string = input('Введите предложение: ')

    # Посчитать буквы Т.
    for ch in my_string:
        if ch == 'Т' or ch == 'Т':
            count += 1
    
    # Напечатать результат.
    print(f'Буква Т появляется {count} раз(а).')

if __name__ == '__main__':
    main()