# Эта программа демонстрирует оператор повторения.
def main():
    # Напечатать девять строк, увеличивающихся по длине.
    for count in range(1, 10):
        print('Z' * count)
    
    for count in range(8, 0, -1):
        print('Z' * count)
    
# Вызвать главную функцию
if __name__ == '__main__':
    main()
