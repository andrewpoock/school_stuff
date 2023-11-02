# linkedqueue.py
# linked list queue

class _Node():

    def __init__(self, item, link=None):
        self.item = item
        self.link = link

class Queue:

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def enqueue(self, item):
        node = _Node(item)
        if self._back is None:
            self._front = node
        else:
            self._back.link = node
        self._back = node
        self._size += 1

    def front(self):
        return self._front.item

    def size(self):
        return self._size

    def dequeue(self):
        item = self._front.item
        self._front = self._front.link
        self._size -= 1
        if self._size == 0:
            self._back = None
        return item
