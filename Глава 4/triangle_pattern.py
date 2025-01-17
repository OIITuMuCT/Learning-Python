# This  program displays a trianglre pattern
BASE_SIZE = 50 

for r in range(BASE_SIZE):
    for c in range(r + 1):
        print('*', end='')
    print()
