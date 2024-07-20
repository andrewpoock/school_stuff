# tree23.py
# Andrew Poock


class _Node23:
    def __init__(self, key=None, trees=[]):
        self.keys = [key] if key is not None else []
        self.trees = list(trees)

    def _keyscan(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] >= key:
                return i
        return len(self.keys)

    def __contains__(self, key):
        if key in self.keys:
            return True
        for node in self.trees:
            if key in node:
                return True
        return False
    
    def __iter__(self):
        tkeys = []
        for node in self.trees:
            for key in node:
                tkeys.append(key)
        for key in self.keys:
            tkeys.append(key)
        yield from sorted(tkeys)

    def pprint(self, depth=0):
        print("\t" * depth + str(self.keys))
        for tree in self.trees:
            tree.pprint(depth + 1)

    def __repr__(self):
        return f"_Node23({self.keys},{self.trees})"
    
    def insert(self, key):
        i = self._keyscan(key)
        if i != len(self.keys):
            if key == self.keys[i]:
                raise Exception("Duplicate Key Error")
        if self.trees == []:
            self.keys.insert(i, key)
        else:
            result = self.trees[i].insert(key)
            if result is not None:
                newkey, nltree, nrtree = result
                self.keys.insert(i, newkey)
                self.trees[i:i+1] = nltree, nrtree
        if len(self.keys) > 2:
            lkey, mkey, rkey = self.keys[0], self.keys[1], self.keys[2]
            ltrees = self.trees[:2] if self.trees else []
            rtrees = self.trees[2:] if self.trees else []
            self.keys = [mkey]
            self.trees = [_Node23(lkey, ltrees), _Node23(rkey, rtrees)]
            return mkey, self.trees[0], self.trees[1]
        return None
            
class Tree23:
    def __init__(self, keys=[]):
        self.root = None
        if keys:
            for key in keys:
                self.insert(key)

    def insert(self, key):
        if self.root is None:
            self.root = _Node23(key)
        else:
            result = self.root.insert(key)
            if result is not None:
                med, ltree, rtree = result
                self.root = _Node23(med, [ltree, rtree])

    def __contains__(self, key):
        return key in self.root

    def __iter__(self):
        return iter(self.root)

    def pprint(self):
        self.root.pprint()

    def __repr__(self):
        return repr(self.root)