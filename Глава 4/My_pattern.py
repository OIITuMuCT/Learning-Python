# Этапрограмма выводит прямоугольную комбинацию
# звездочек
rows = int(input('Сколько строк? '))
cols = int(input('Сколько столбцов? '))
stars = int(input('Сколько звезд? '))
# star = stars
BASE_SIZE = stars 

for b in range(BASE_SIZE):
    for d in range(b + 1):
        print('*', end='')
    print()

for r in range(rows):
    for c in range(cols):
        for s in range(stars):    
            print('*', end='')
        print(' ', end='')    
    print()

for b in range(BASE_SIZE, 0 , -1):
    for d in range(b):
        print('*', end='')
    print()