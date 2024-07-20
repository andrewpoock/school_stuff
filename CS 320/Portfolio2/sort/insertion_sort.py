# insertion_sort.py
# Insertion Sort Algorithm
# Andrew Poock

# Textbook/Arrays Version
def insertion_sort(lst):
    for i in range(1, len(lst)):
        v = lst[i]
        j = i-1
        while j >= 0 and lst[j] > v:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = v

# Python List Version
def insertion_sort2(lst):
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[j] > lst[i]:
                break
        else:
            j = i
        lst.insert(j, lst.pop(i))