# Эта программа читает содержимое файла 
# philosophers.txt построчно.
def main():
    # Open file philosophers.txt.
    infile = open('philosophers.txt', 'r')
    
    # Ппочитать три строки из файла.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # delete \n из каждого строкого значения.
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    # Close file.
    infile.close()
    
    # Напечатать данные, прочитанные в оперативную память.
    print(line1)
    print(line2)
    print(line3)
    
# Calling main
if __name__ == '__main__':
    main()