# linkedstack.py

class _Node:

    def __init__(self, item, link=None):
        self.item = item
        self.link = link

class Stack:

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, x):
        node = _Node(x, self._top)
        self._top = node
        self._size += 1

    def pop(self):
        item = self._top.item
        self._top = self._top.link
        self._size -= 1
        return item

    def top(self):
        return self._top.item

    def size(self):
        return self._size
