# deck.py - implements a simple deck of cards

from card2 import Card
from random import randrange

class Deck:

    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(rank, suit)
                self.cards.append(card)

    def size(self):
        return len(self.cards)

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        for i in range(len(self.cards)-1):
            pos = randrange(i, len(self.cards))
            self.cards[i], self.cards[pos] = self.cards[pos], self.cards[i]

        # for i, card in enumerate(self.cards):
            # pos = randrange(i, len(self.cards))
            # self.cards[i] = self.cards[pos]
            # self.cards[pos] = card

    def __iter__(self):
        for c in self.cards:
            yield c
        # OR: return iter(self.cards)
            
            
