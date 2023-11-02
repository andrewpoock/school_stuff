# linkedqueue.py
# linked list queue

class _Node():

    def __init__(self, item, link=None):
        self.item = item
        self.link = link

class Queue:

    def __init__(self):
        # empty node so queue is never empty
        self._front = _Node(None)
        self._back = self._front
        self._size = 0

    def enqueue(self, item):
        node = _Node(item)
        self._back.link = node
        self._back = node
        self._size += 1

    def front(self):
        return self._front.link.item

    def size(self):
        return self._size

    def dequeue(self):
        item = self._front.link.item
        self._front.link = self._front.link.link
        self._size -= 1
        if self._size == 0:
            self._back = self._front
        return item
    # can use another dummy node at back to simplify dequeue
