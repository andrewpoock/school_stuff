# stack.py
#   in-class stack implementation using a Python list

class Stack:

    def __init__(self):
        """Create an empty stack
        """
        self._items = []

    def push(self, x):
        """pushes x on the stack
        """
        self._items.append(x)

    def pop(self):
        """pops item from stack
        """
        return self._items.pop()

    def top(self):
        """returns top item of stack
        """
        return self._items[-1]

    def size(self):
        """returns number of items in stack
        """
        
        return len(self._items)
    
