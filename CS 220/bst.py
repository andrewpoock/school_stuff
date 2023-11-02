# bst.py
# Andrew Poock

class _BSTNode:

    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def insert(self, item):
        if item < self.item: # goes in left
            if self.left: # if left tree exists
                self.left.insert(item)
            else:
                self.left = _BSTNode(item)
        elif item > self.item:
            if self.right:
                self.right.insert(item)
            else:
                self.right = _BSTNode(item)
        else:
            print("Item already in Tree")

    def __iter__(self):
        if self.left:
            for i in self.left:
                yield i
        yield self.item
        if self.right:
            for j in self.right:
                yield j

    def find(self, item):
        if self.item == item:
            return self.item
        if item < self.item:
            if self.left:
                return self.left.find(item)
        else:
            if self.right:
                return self.right.find(item)
        return None

class BST:

    def __init__(self):
        self.root = None
        
    def insert(self, item):
        if self.root:
            self.root.insert(item)
        else:
            self.root = _BSTNode(item)

    def find(self, item):
        if self.root:
            return self.root.find(item)

    def __iter__(self):
        if self.root:
            for item in self.root:
                yield item

def main():
    tree = BST()
    for x in [10,6,13,2,7,11,18,12,14]:
        tree.insert(x)
    for x in tree:
        print(x)

if __name__ == "__main__":
    main()
