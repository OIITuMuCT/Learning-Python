# Эта программа читает результаты контрольных работ из
# файла CSV и вычисляет вредний балл для каждого ученика.

def main():
    # Открыть файл.
    csv_file = open('test_scores.csv', 'r')
    # Прочитать строки файла в список.
    lines = csv_file.readlines()
    
    # Закрыть файл.
    csv_file.close()

    # Обработка строки.
    for line in lines:
        # получить результаты контрольных работ в виде лексем.
        tokens = line.split(',')
        
        # Подсчитать общее количество баллов за контрольные работы.
        total = 0.0
        for token in tokens:
            total += float(token)
        
        # Вычислить сердний балл резальтатов контрольных работ.
        avarage = total/len(tokens)
        print(f'Средний балл: {avarage}')

if __name__ == '__main__':
    main()
    print(__name__)
