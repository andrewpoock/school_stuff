# selection_sort.py
# Selection Sort Algorithm
# Andrew Poock

def selection_sort(lst):
    for i in range(len(lst)-1):
        minpos = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[minpos]:
                minpos = j
        lst[i], lst[minpos] = lst[minpos], lst[i]