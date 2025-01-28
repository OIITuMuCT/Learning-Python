# Эта программа выводит ступенчатую коомбинацию.
NUM_STEPS = 15

for r in range(NUM_STEPS):
    for c in range(r):
        print(' ', end='')
    print('#')