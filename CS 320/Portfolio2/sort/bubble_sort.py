# bubble_sort.py
# Bubble Sort Algorithm
# Andrew Poock

def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        swapped = False
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break