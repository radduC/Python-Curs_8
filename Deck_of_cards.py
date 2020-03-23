from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return self.value + ' of ' + self.suit 


class Deck:
    def __init__(self):
        value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, color) for rank in value for color in suit]
    
    def __repr__(self):
        return 'Deck of {} cards'.format(len(self.cards))
    
    def count(self):
        return len(self.cards)

    def _deal(self, number):
        if self.count() == 0:
            raise ValueError('All cards have been dealt')
        elif number <= self.count():
            cards = self.cards[-number:]
            self.cards = self.cards[:-number]
            return cards
        else:
            cards = self.cards
            self.cards = []
            return cards
    
    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full cardss can be shuffled')
        shuffle(self.cards)
        return self.cards
    
    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, number):
        return self._deal(number)


def Curs_7_Ex_1():    
    pachet = Deck()
    return pachet
    # print(pachet.cards, '\n')
    # pachet.shuffle()
    # print(pachet.cards, '\n')
    # print(pachet.deal_hand(4))
    # pachet._deal(2)
    # pachet._deal(2)
    # pachet._deal(2)
    # print(pachet.count(), '\n')
    # pachet._deal(2)
    # print(pachet.cards, '\n')
    # print(pachet.count())


if __name__ == "__main__":
    deck = Deck()
    pachet = Deck()
    print(pachet.cards, '\n')
    pachet.shuffle()
    print(pachet.cards, '\n')
    print(pachet.deal_hand(4))
    pachet._deal(2)
    pachet._deal(2)
    pachet._deal(2)
    print(pachet.count(), '\n')
    pachet._deal(2)
    print(pachet.cards, '\n')
    print(pachet.count())