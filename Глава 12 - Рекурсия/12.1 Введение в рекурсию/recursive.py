# Эта программа имеет рекурсивную функцию.

def main():
    # Передав аргумент 5 в функцию message,
    # мы сообщим ей, что нужно показать 
    # сообщение пять раз.
    message(5)
    
def message(times):
    if times > 0:
        print('Это рекурсивная функция.')
        message(times - 1)


if __name__== '__main__':
    main()