# Эта программа считывает содержимое файла в список.

def main():
    # Open file for read
    infile = open('cities.txt', 'r')
    
    # Прочитать содержимое файла в список.
    cities = infile.readlines()

    # Close file.
    infile.close()
    
    # Удалить из каждого элемента символ \n.
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1
    
    # Напечатать содержимое списка.
    print(cities)
    
# Вызвать главную функцию.
if __name__ == '__main__':
    main()