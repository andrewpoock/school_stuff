# bqueue.py
#   implementattion of a Bounded Queue using a circular list technique
# Andrew Poock


class BoundedQueue:

    def __init__(self, capacity):
        self._capacity = capacity  # Capacity of the queue
        self._size = 0             # number of items in the queue
        self._items = [None] * capacity   # list containing the items
        self._head = 0             # position of the front of the queue
        self._tail = capacity - 1  # position of the back of the queue

    def size(self):
        """returns number of items in queue"""
        return self._size

    def capacity(self):
        """returns the capacity of the queue"""
        return self._capacity

    def enqueue(self, item):
        """add item to the back of the queue"""

        # this is the error handling, see last test case
        assert self._size < self._capacity, "Queue is full"
        # code to add the item goes here
        self._tail = (self._tail + 1) % self._capacity
        self._items[self._tail] = item
        self._size += 1

    def front(self):
        """returns item at the front of the queue"""
        return self._items[0]

    def dequeue(self):
        """removes and returns item at front of the queue"""
        item = self._items[self._head]
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return item

    def isfull(self):
        """returns whether the queue is at capacity (a Boolean)"""
        return self._size == self._capacity
