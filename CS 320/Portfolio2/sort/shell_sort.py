# shell_sort.py
# Shell Sort Algorithm
# Andrew Poock

def shell_sort(lst):
    SEQ = [797161, 265720, 88573, 29524, 9841, 3280, 1093, 364, 121, 40, 13, 4, 1]
    incr_sequence = [n for n in SEQ if n < len(lst)]
    for incr in incr_sequence:
        for i in range(incr, len(lst)):
            v = lst[i]
            j = i-incr
            while j >= 0 and lst[j] > v:
                lst[j+incr] = lst[j]
                j -= incr
            lst[j+incr] = v