def main():
    # Передать символьное значение в функцию show_mammal_info 
    show_mammal_info('Я - последовательность символов')
    
def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

if __name__ == '__main__':
    main()