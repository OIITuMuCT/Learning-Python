# Эта программа записывает цифры в num_10.txt от 1 до 10 
# с помощью цикла for

def main():
    # Открыть файл num_10.txt для записи.
    num_file = open('num_10.txt', 'w')
    
    for num in range(1, 15):
        num_file.write(f'{num}\n')

    # close num_file
    num_file.close()
    
if __name__ == '__main__':
    main()