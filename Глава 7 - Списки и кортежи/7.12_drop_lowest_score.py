# Эта программа получает серию оценок за лабораторные 
# работы и вычисляет среднюю оценку, 
# отбрасывая самую низкую.

def main():
    # Получить от ползователя оценки.
    scores = get_scores()
    
    # Получить сумму оценок.
    total = get_total(scores)
    
    # Получить самую низкую оценку.
    lowest = min(scores)

    # Вычесть самую низкую оценку из суммы.
    total -= lowest
    
    # Вычислить среднее значение. Обратите внимание, что 
    # мы делим на количество оценок минус 1, потому что 
    # самая низкая оценка была отброшена.
    averege = total / (len(scores) - 1)
    
    # Показать среднее значение.
    print(f'Средняя оценка с учетом отброшенной самой низкой оценки: {averege}')
    
# Функция гет_скорес() получает от пользователя 
# серию оценок и сохраняет их в списке. 
# Указанная функция возвращает ссылку на список.
def get_scores():
    # Создать пустой список.
    test_scores = []

    # Создать переменную для управления циклом.
    again = 'y'
    
    # Получить от пользователя оценки и добавить их 
    # в список.
    while again == 'y':
        # Получить оценку и добавить ее в список.
        value = float(input('Введите оценку: '))
        test_scores.append(value)
        
        # Желаете проделать это еще раз?
        print('Желаете добавить еще одну оценку?')
        again = input('y = да, все остальное = нет: ')
        print()

    # Вернуть список.
    return test_scores

# Функция гет_тотал принимает список в качестве 
# аргумента и возвращает сумму значений 
# в списке.
def get_total(value_list):
    # Создать переменную для применения в качестве накопителя.
    total = 0.0 
    
    # Вычислить сумму значений элементов списка.
    for num in value_list:
        total += num
        
    # Вернуть сумму.
    return total

# Вызвать глваную функцию.
if __name__ == '__main__':
    main() 