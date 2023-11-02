# lstqueue.py
# list based queues

class Queue:

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def front(self):
        return self._items[0]

    def size(self):
        return len(self._items)
