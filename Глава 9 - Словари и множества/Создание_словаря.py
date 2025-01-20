phonebook = {"Крис": "555-1111", "Кэти": "555-2222", "Джоанна": "555-3333"}

phone_book_copy1 = {k:k.endswith('11') for k in phonebook.items() }
print('phone_book_copy1 = ', phone_book_copy1)
phone_book_copy = {k:v for k, v in phonebook.items()}
a = phonebook
for key in a:
    print(f' ключ = {key}; значение = {a[key]}')
print(phonebook)

numbers = [i for i in range(1, 5)]
squares = {}
for item in numbers:
    squares[item] = item**2
print("squares = ", squares)
sqr = {item:item**3 for item in range(1, 5)}
print('sqr = ', sqr)
print(type(sqr))
print(type(numbers))
print('Phone_book_copy =', phone_book_copy)


populations = {
    'New-York': 8398748, 'Los-Angeles': 3990456,
    'Chicago': 2705994, 'Houston': 2325502, 
    'Phenix': 1660272, 'Philadelphia' :1584138}

largest = {}
for k, v in populations.items():
    if v > 2000000:
        largest[k] = v
print(largest)
smallest = {k:v for k, v in populations.items() if v < 2000000}
print(smallest)
employee = {}
employee['id'] = 54321
print(employee)
stuff = {1:'aaa', 2: 'bbb', 3:'ccc'}
print(stuff[3])
employee['job'] = 'apple corp'
print(employee.values())
k, v = employee.popitem()
# del employee['id']
print(employee)
for k in stuff:
    print(k)
print(k, v)
print(employee)

names = ['Chris', 'Katie', 'Joanna', 'Curt']
dict_names = {k: len(k) for k in names}
print(dict_names)
