class Mammal:
    """Класс представляет род млекопитающих."""

    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print("Я -", self.__species)

    def make_sound(self):
        print("Грррррр")


class Dog(Mammal):
    """Класс Dog является подклассом класса Mammal."""

    def __init__(self):
        Mammal.__init__(self, "собака")

    def make_sound(self):
        print("Гав-гав")


class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self, "кот")

    def make_sound(self):
        print("Мяу!")


if __name__ == "__main__":
    mammal = Mammal("Обычное млекопитающее")
    mammal.show_species()
    mammal.make_sound()
    print()
    dog = Dog()
    dog.show_species()
    dog.make_sound()
    print()
    cat = Cat()
    cat.show_species()
    cat.make_sound()
    print()
