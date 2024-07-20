Portfolio 3
Andrew Poock

-------------

Projects:
    mergesort.py - sorts a list by first sorting its two halves, then merges them together
    quickhull.py - creates a set of random points and draws the smallest polygon that encloses all points
    quickselect.py - returns the kth smallest item in the list using lomuto partitioning
    quicksort.py - sorts a list using hoare partitioning
    tree23.py - 2-3 Tree and Node class implementation

-------------

Other:
    graphics.py - zelle graphics program used for drawing quickhulls

-------------

Usage from Portfolio3 dir:
    mergesort.py (Sorts example list) - python mergesort.py
    quickhull.py (User determines #n random points, then draws hull) - python quickhull.py
    quickselect.py (Example quickselect) - python quickselect.py
    quicksort.py (Sorts example list) - python quicksort.py
    tree23.py - python
        from tree23 import Tree23
        t = Tree23([3,1,4,5,9,2,6])
        5 in t
        10 in t
        list(t)
        t.pprint()
        t.insert(10)
        t2 = Tree23(range(1,16))
        t.pprint()