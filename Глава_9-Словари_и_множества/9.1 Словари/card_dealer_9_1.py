# Эта программа применяет словарь  в качестве колоды карт.
import random

def main():
    # Создать колоду карт.
    deck = create_deck()
    
    # Получить количество карт для раздачи.
    num_cards = int(input('Сколько карт раздать? '))

    # Раздать карты.
    deal_cards(deck, num_cards)

# Функция create_deck возвращает словарь, представляющий колоду карт.

def create_deck():
    deck = {
    "2 spades": 2,
    "2 diamond": 2,
    "2 hearts": 2,
    "2 clubs": 2,
    "3 spades": 3,
    "3 diamond": 3,
    "3 hearts": 3,
    "3 clubs": 3,
    "4 spades": 4,
    "4 diamond": 4,
    "4 hearts": 4,
    "4 clubs": 4,
    "5 spades": 5,
    "5 diamond": 5,
    "5 hearts": 5,
    "5 clubs": 5,
    "6 spades": 6,
    "6 diamond": 6,
    "6 hearts": 6,
    "6 clubs": 6,
    "7 spades": 7,
    "7 diamond": 7,
    "7 hearts": 7,
    "7 clubs": 7,
    "8 spades": 8,
    "8 diamond": 8,
    "8 hearts": 8,
    "8 clubs": 8,
    "9 spades": 9,
    "9 diamond": 9,
    "9 hearts": 9,
    "9 clubs": 9,
    "10 spades": 10,
    "10 diamond": 10,
    "10 :hearts": 10,
    "10 clubs": 10,
    "J spades": 10,
    "J diamond": 10,
    "J hearts": 10,
    "J clubs": 10,
    "Q spades": 10,
    "Q diamond": 10,
    "Q hearts": 10,
    "Q clubs": 10,
    "K spades": 10,
    "K diamond": 10,
    "K hearts": 10,
    "K clubs": 10,
    "A spades": 1,
    "A diamond": 1,
    "A hearts": 1,
    "A clubs": 1,
}
    
    return deck
# функция deal_cards раздает заданное количество карт из колоды.
def deal_cards(deck, number):
    # Инициализировать накопитель для количества карт на руках.
    hand_value = 0
    # Убедитесь, что количество карт для раздачи не больше 
    # количества карт в колоде.
    if number >len(deck):
        number = len(deck)
    
    # Раздать карты и накопить их значения.
    for count in range(number):
        card = random.choice(list(deck))
        print(card)
        hand_value +=deck[card]
    
    # Показать величину карт на руках.
    print(f'Величина карт на руках: {hand_value}')


if __name__ == '__main__':
    main()