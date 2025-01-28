import random
phonebook = {"Крис": "555-1111", "Кэти": "555-2222", "Джоанна": "555-3333"}
print(phonebook.rand_pop())
def main(key, value):
    
    key = input('Введите  ключ: ')
    value = input('Введите значение: ')
    phonebook[key] = value
    return print(phonebook)

if __name__ == '__main__':
    main('name', 'Johnny')
