# review.py
# Andrew Poock

from random import randrange

class MSDie:

    def __init__(self, sides):
        self._sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self._sides+1)
