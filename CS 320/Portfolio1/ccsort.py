# ccsort.py
# Tests the efficiency of a sorting algorithm on a list (Compare Count Sort)
# by Andrew Poock

import time, random


# Sorting Algorithm
def ccsort(lst):
    result = [0] * len(lst)
    count = [0] * len(lst)
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] < lst[j]:
                count[j] = count[j] + 1
            else:
                count[i] = count[i] + 1
    for k in range(len(lst)):
        result[count[k]] = lst[k]
    return result


def main():
    print("\nThis program tests the efficiency of sorting a list\n")
    size = int(input("Enter the list size: "))
    trials = int(input("Enter the number of trials: "))
    print()
    total = 0
    # For each trial, create a list of random integers and find the time needed to sort it
    for trial in range(trials):
        lst = [random.randint(0, size) for n in range(size)]
        start = time.time()
        slst = ccsort(lst)
        end = time.time()
        elapsed = end - start
        total = total + elapsed
        print(f"Trial {trial}: {elapsed} seconds")
    avg = total / trials
    print(f"\nTotal Time: {total} seconds")
    print(f"Average Time: {avg} seconds\n")


main()