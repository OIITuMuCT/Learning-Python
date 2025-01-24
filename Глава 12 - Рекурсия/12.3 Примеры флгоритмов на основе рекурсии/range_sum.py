# Эта программа демонстрирует функцию range_sum.

def main():
    # Создать список чисел.
    numbers = [i for i in range(1, 10)]
    
    my_sum = range_sum(numbers, 2, 5)
    
    print(f'Сумма значений со 2 до 5 равняется {my_sum}')

def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)

if __name__ == '__main__':
    main()