# dice.py
# Andrew Poock

from review import MSDie


class Dice:

    def __init__(self, sides_seq):
        self._dice = [MSDie(die) for die in sides_seq]

    def values(self):
        vals = []
        for die in self._dice:
            vals.append(die.value)
        return vals

    def rollall(self):
        for die in self._dice:
            die.roll()

    def roll(self, index):
        for i in index:
            self._dice[i].roll()

    def total(self):
        return sum(self.values())
