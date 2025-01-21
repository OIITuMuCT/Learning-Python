myset = set()

myset = set(['a', 'b', 'c','d', 'e', 'f'])
myset_str = set('Hello world!!!')
print(myset)
print(myset_str)
# для создания множества из строк ['one', 'two', 'three'], необходимо в качестве аргумента в функцию set() передать список, содержащий строковый значения ['one', 'two', 'three']
myset_words = set(["one", "two", "three"])
print(myset_words)

# Методы множества.
# Добавить элемент в множество
myset.add('g')
print(myset)
# Обновить множество
myset.update(['i', 'h', 'k'])
myset.update('xyz')
print(myset)
# Удаление элемента из множества метод remove() and discard(), первый метод вызывает исключение KeyError если элемент не найден, а второй исключения не вызывает
myset.discard("u")
print(myset)
myset.remove('g')

print(myset)
# Метод clear() удаляет все элементы из множества.
# myset.clear()
# print(myset)
for val in myset:
    print(val, end=', ')
print()
# Объединение множеств.
myset_new = myset.union(myset_str)
print(myset_new)

# Пересечение множеств
myset_inter = myset_new.intersection(myset)
print(myset_inter)

# Разность множеств
myset_diff = myset.difference(myset_str)
print("myset_diff = myset.difference(myset_str) =", myset_diff)

множество1 = set([i for i in range(5)])
множество2 = set([i for i in range(3, 10)])
множество3 = множество1.difference(множество2)
print('Множество3 = ', множество3)

print(myset)
# Симметричная разность symmetric_difference()
myset_sym_diff = myset_str.symmetric_difference(myset)
myset_sym_diff2 = myset.symmetric_difference(myset_words)

print('symmetric difference = ', myset_sym_diff)
print("symmetric difference 2 = ", myset_sym_diff2)
set1 = set([n for n in range(1, 5)])
set2 = set([n for n in range(3, 7)])
set3 = set1 ^ set2
print(set3)

# Подмножества и надмножества issubset() and issuperset()
set2.issubset(set1)

myset = set()
print(myset)
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
set3 = set2.difference(set1)
print(set3)

set1 = set( [ 'а' ,'б' ,'в' ] )
set2 = set( [ 'б' ,'в' , 'г' ] )
set3 = set1.symmetric_difference(set2)
print(set3)
