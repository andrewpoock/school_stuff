# quicksort.py
# Andrew Poock


def sort3(a, b, c):
    if a > b:
        if a > c:
            if b > c:
                return a, b, c
            else:
                return a, c, b
        else:
            return c, a, b
    else:
        if a > c:
            if b > c:
                return c, b, a
            else:
                return b, c, a
        else:
            return b, a, c

def hoare_partition(A, l, r):
    a, b, c = A[l], A[(r+l)//2], A[r]
    min, med, max = sort3(a, b, c)
    A[l], A[r], A[(r+l)//2] = med, max, min
    p = A[l]
    i = l
    j = r+1
    while i < j:
        i += 1
        while A[i] < p:
            i += 1
        j -= 1
        while A[j] > p:
            j -= 1
        A[i], A[j] = A[j], A[i]
    A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def quicksort(A, l, r):
    if l < r:
        s = hoare_partition(A, l, r)
        quicksort(A, l, s-1)
        quicksort(A, s+1, r)

def main():
    lst = [32, 56, 12, 99, 82, 74, 41]
    print(f"Sorting {lst}")
    quicksort(lst, 0, len(lst)-1)
    print(f"Sorted: {lst}")

main()