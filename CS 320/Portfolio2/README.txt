Portfolio 2
Andrew Poock

-------------

Projects are sorted into respective folders: graph and sort

-------------

Required Projects:
    bubble_sort.py - bubble sort algorithm to sort lists
    selection_sort.py - selection sort algorithm to sort lists
    DFS.py - class to implement depth first search algorithm
    listgraph.py - graph subclass using adjacency list structure
    insertion_sort.py - insertion sort algorithms to sort lists and arrays
    sort_wars.py - run timing trials on all sort types using sorttime.py
        -results are in sort_wars.txt

-------------
    
Optional Projects:
    BFS.py - class to implement breadth first search algorithm
    shell_sort.py - shell sort algorithm to sort lists

-------------

Other:
    sorttime.py - functions to test and time sorting algorithms
    example_graphs.py - pre built graphs to test BFS, DFS, and listgraph
    graph.py - graph class, super class for listgraph and matrixgraph
    matrixgraph.py - matrix implementation of a graph used to test BFS and DFS

-------------

Usage:
    sorts -     from {sortname} import {sortname}
                l = {list of values}
                {sortname}(l)
                l
    DFS/BFS -   from {DFS/BFS} import {DFS/BFS}
                from example_graphs import g310
                search = {DFS/BFS}(graph)
                search.entrymarks, search.exitmarks (DFS)
                seach.marks (BFS)
        (can change between listgraph and matrixgraph in example_graphs)
        (listgraph is currently implemented)
    sort_wars - python sort_wars.py
