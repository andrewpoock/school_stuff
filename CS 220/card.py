# Card.py
class Card(object):
    '''A simple playing card. A Card is characterized by two components:
    rank: an integer value in the range 1-13, inclusive (Ace-King)
    suit: a character in 'cdhs' for clubs, diamonds, hearts, and
    spades.'''

    SUITS = 'cdhs'
    SUITNAMES = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    RANKS = list(range(1,14))
    RANKNAMES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                  'Seven', 'Eight', 'Nine', 'Ten', 
                  'Jack', 'Queen', 'King']

    def __init__(self, rank, suit):
        '''Constructor
        pre: rank in range(1,14) and suit in 'cdhs'
        post: self has the given rank and suit'''
        assert rank in range(1,14)
        assert suit in ['c', 'd', 'h', 's']
        self._rank = rank
        self._suit = suit

    def suit(self):
        '''Card suit
        post: Returns the suit of self as a single character'''

        return self._suit

    def rank(self):
        '''Card rank
        post: Returns the rank of self as an int'''

        return self._rank
        
    def suitName(self):
        '''Card suit name
        post: Returns one of ('clubs', 'diamonds', 'hearts',
              'spades') corrresponding to self's suit.'''
        
        index = self.SUITS.index(self._suit)
        return self.SUITNAMES[index]        

    def rankName(self):
        '''Card rank name
        post: Returns one of ('ace', 'two', 'three', ..., 'king')
              corresponding to self's rank.'''

        index = self.RANKS.index(self._rank)
        return self.RANKNAMES[index]

    def __str__(self):
        '''String representation
        post: Returns string representing self, e.g. 'Ace of Spades' '''

        return self.rankName() + ' of ' + self.suitName()

def main():
    for suit in "cdhs":
        for rank in range(1, 14):
            card = Card(rank, suit)
            print(card)
