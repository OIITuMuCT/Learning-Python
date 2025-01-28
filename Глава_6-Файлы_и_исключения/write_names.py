# Эта программа получает от ползователя три имени 
# и пишет их в файл.

def main():
    # Получить три имени.
    print('Введите имена трех друзей.')
    name1 = input('Друг # 1: ')
    name2 = input('Друг # 2: ')
    name3 = input('Друг # 3: ')
    
    # Открыть файл с именем freinds.txt
    myfile = open('freinds.txt', 'w')
    
    # записать имя в файл.
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')
    
    # close file.
    myfile.close()
    print('Имена были записаны в freinds.txt.')
    
# Calling main()
if __name__ == '__main__':
    main()