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


def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()


if __name__ == "__main__":
    main()
