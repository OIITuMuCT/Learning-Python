# polymorphism

import animals


def main():
    # Создать объект Mammal, Dog, и объект Cat.
    mammal = animals.Mammal("обычное животное")
    dog = animals.Dog()
    cat = animals.Cat()

    # Показать информацию о каждом животном.
    print("Вот несколько животных и")
    print("звуки, которые они издают.")
    print("--------------------------")
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    show_mammal_info('Я - последовательность символов')


def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print(creature)
        print('Это не млекопитающее!')

if __name__ == "__main__":
    main()
