
phonebook = {"Крис": "555-1111", "Кэти": "555-2222", "Джоанна": "555-3333"}

a = phonebook
for key in a:
    print(f' ключ = {key}; значение = {a[key]}')
print(set(phonebook))

form = {'employee': {'name': 'John', 'job': 'apple'}, 'boss': {'name':'Steve', 'job':'GemDev'}}