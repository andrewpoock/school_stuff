# hand.py

from card2 import Card
from deck import Deck

class Hand:

    def __init__(self, label):
        self.cards = []
        self.label = label

    def add(self, card):
        self.cards.append(card)

    def dump(self):
        print(self.label)
        print("-------------")
        for card in range(len(self.cards)):
            print(self.cards[card])

    def sort():
        pass
