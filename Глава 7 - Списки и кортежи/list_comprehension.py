list1 = [1, 2, 3, 4]
list2 = [item for item in list1]

for item in list1:
    list2.append(item**2)

print(list2)

for item in list1:
    list2.append(item**2)

list1 = [1, 2, 3, 4]
list2 = [item**2 for item in list1]
print(list2)


str_list = ['Моргнуть', 'Мигнуть', 'Кивнуть']
len_list = []

for s in str_list:
    len_list.append(len(s))
print(str_list, len_list)

lst1 = [1, 12, 2, 20, 3, 15, 4]
lst2 = []
for n in lst1:
    if n < 10:
        lst2.append(n)
print(lst1, lst2)
lst2 = [item for item in lst1 if item >= 4]
print(lst2)

last_names = ['Джексон', 'Смит', 'Хильдебрандт', 'Джонс']
short_names = [name for name in last_names if len(name) < 6]
print(short_names)

students = [["Джо", "Ким"], ["Сэм", "Сью"], ["Келли", "Крис"] ]
print(students)

scores = [[0, 0, 0],
          [0, 4, 0],
          [0, 0, 0]]
print(scores[1][1])
print(students[2][1])