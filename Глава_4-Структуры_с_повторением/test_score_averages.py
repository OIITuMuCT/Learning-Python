# эта программа усредняет оценки. Она запращивает кол-во
# студентов и кол-во оценок в расчете на студента.

# Получить кол-во студентов.
num_students = int(input('Сколько у вас студентов?'))

# Получить кол-во оценок в расчете на студента.
num_test_score = int(input('Сколько оценок в расчете на студента?'))

# Определить средний бал каждого студента.
for student in range(num_students):
    # Инициализировать накопитель оценок.
    total = 0.0

    # Получить номер студента.
    print('Номер студента', student + 1)
    print('-----------------')
   
    # Получить оценки за лабораторные работы 
    for test_num in range(num_test_score):
        print(f'Номер лабораторной работы {test_num + 1}', end=' ')
        score = float(input(': '))

        # Прибавить оценку в на копитель.
        total += score
    # Рассчитать средний балл этого студента.
    average = total / num_test_score

    # Показать средний балл.
    print(f'Средний балл студента номер {student + 1} '
          f'состовляет: {average:.1f}')
    print()
