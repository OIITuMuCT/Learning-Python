# Эта программа применяет словарь для хранения 
# имен и дней рождения друзей.

# Глобальные константы для пунктов меню.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Главная функция.
def main():
    # Создать пустой словарь.
    birthdays = {}
    # Инициализировать переменную для выбора пользователя.
    choice = 0
    while choice != QUIT:
        # Получите выбранный пользователем пункт меню.
        choice = get_menu_choice()
        # Отобразить выбранный вариант действий.
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)
# Функция get_menu_choice выводит меню и получает
# проверенный на допустимость выбранный пользователем пункт.
def get_menu_choice():
    print()
    print('Друзья и их дни рождения')
    print('------------------------')
    print('1. Найти день рождения')
    print('2. Добавить новый день рождения')
    print('3. Изменить день рождения')
    print('4. Удалить день рождения')
    print('5. Выйти из программы')
    print()
    
    # Получить выбранный пользователем пункт.
    choice = int(input('Введите выбранный пункт: '))
    # Проверить выбранный пункт на допустимость.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт: '))

    # Вернуть выбранный пользователем пункт.
    return choice

# Функция look_up отыскивает имя в словаре birthdays.
# Получить искомое имя.
def look_up(birthdays):
    name = input('Введите имя: ')
    
    # Отыскать его в словаре.
    print(birthdays.get(name, 'Не найдено.'))

def add(birthdays):
    # Получить имя и день рождения.
    name = input('Введите имя: ')
    bday = input('Введите день рождения: ')

    # Если имя не существует, то добавить его.
    if name not in birthdays:
        birthdays[name]= bday
    else:
        print('Эта запись уже существует.')

def change(birthdays):
    # Получить искомое имя.
    name = input('Введите имя: ')

    if name in birthdays:
        # Получить новый день рождения.
        bday = input('Введите новый день рождения: ')
        # Обновить запись.
        birthdays[name] = bday
    else:
        print('Это имя не найдено.')

def delete(birthdays):
    # Получить искомое имя.
    name = input('Введите имя: ')

    # Если имя найдено, то удалить эту запись.
    if name in birthdays:
        del birthdays[name]
    else:
        print('Это имя не найдено.')
# Вызвать главную функцию.
if __name__ == '__main__':
    main()