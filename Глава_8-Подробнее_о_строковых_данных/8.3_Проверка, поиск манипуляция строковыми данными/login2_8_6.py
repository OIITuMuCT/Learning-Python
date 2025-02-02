# Функция get_login_name принимает, имя и фамилию
# и идентификационный номер в качестве аргументов.
# Она возвращает ися для входа в систему.
print(f'Импорт происходит из файла {__name__}.py')

def get_login_name(first, last, id_number):
    # Получить первые три буквы имени.
    # Если длина имени меньше 3, то
    # срез вернет все имя целиком.
    set1 = first[0:3]

    # Получить первые три буквы фамилии.
    # Если длина фамилии меньше 3 букв,
    # то срез вернет всю фамилию целиком.
    set2 = last[0:3]
    
    # Получить последние три буквы фамилии идентификатора.
    # Если длина идентификатора меньше 3, то
    # срез вернет всю фамилию целиком.
    set3 = id_number[0:3]
    
    # Собрать воедино наборы символов
    login_name = set1 + set2 + set3
    
    # Вернуть имя для входа в систему.
    return login_name

# Функция valid_password принимает пароль
# в качестве аргумента и возвращает истину либо ложь,
# сообщая о его допустимости или недопустимости. Допустимый
# пароль должен состоять как минимум из 7 символов,
# иметь как минимум один символ в верхнем регистре,
# один символ в нижнем регистре и одну цифру.

def valid_password(password):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    
    # приступить к валидации.
    # Начать с проверки длины пароля.
    if len(password) > 7:
        correct_length = True
    # Проанализировать каждый символ и установить 
    # соответствующий флаг, когда требуемый символ найден.
    for ch in password:
        if ch.isupper():
            has_uppercase = True
        if ch.islower():
            has_lowercase = True
        if ch.isdigit():
            has_digit = True
    
    # Определить, удовлетворены ли все требования.
    # Если это так, то назначить is_valid  значение True.
    # В противном случае назначь is_valid значение False
    if correct_length and has_uppercase and has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False
    
    # Вернуть переменную is_valid.
    return is_valid
