# Эта программа демонстрирует аргумент,
# передаваемый в функцию.

def main():
    value = 5
    show_double(value)

# функция show_double принимает аргумент 
# и показывает его удвоенное значение.
def show_double(number):
    result = number * 2
    print(result)

# Вызвать главную функцию.
main()