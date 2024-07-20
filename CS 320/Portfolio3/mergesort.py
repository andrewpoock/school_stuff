# mergesort.py
# Andrew Poock


def merge(B, C, A):
    i, j, k = 0, 0, 0
    p, q = len(B), len(C)
    while i < p and j < q:
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    if i == p:
        A[k:] = C[j:]
    else:
        A[k:] = B[i:]

def mergesort(A):
    n = len(A)
    if n > 1:
        B = A[:n//2]
        C = A[n//2:]
        mergesort(B)
        mergesort(C)
        merge(B, C, A)

def main():
    lst = [32, 56, 12, 99, 82, 74, 41]
    print(f"Sorting {lst}")
    mergesort(lst)
    print(f"Sorted: {lst}")

main()