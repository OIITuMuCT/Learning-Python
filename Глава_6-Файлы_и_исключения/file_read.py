# Эта программа читает показывает содержимое 
# файла philosophers.txt
def main():
    # Открыть файл с именем philosophers.txt.
    infile = open('philosophers.txt', 'r')
    
    # Прочитать содержимое файла.
    file_contents = infile.read()
    
    # Close file.
    infile.close()
    
    # Напечатать данные, считанные
    # в оперативвную память.
    print(file_contents)

#  Calling main
if __name__ == '__main__':
    main()