# Эта программа преобразует скорости от 60
# до 130 км/ч (с праращением в 10 км)
# в mph.

START_SPEED = 60            # Начальна скорость.
END_SPEED = 131             # Конечная скорость.
INNCREMENT = 10             # Приращение скорости.
CONVERSION_FACTOR = 0.6214  # Коэффициент перерасчета.

# Напечаттаем заголовки таблицы.
print('KPH\tMPH') 
print('---------------')

# Напечатаем скорости.
for kph in range(START_SPEED, END_SPEED, INNCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(f'{kph}\t{mph:.1f}')
