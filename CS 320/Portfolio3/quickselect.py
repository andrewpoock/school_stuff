# quickselect.py
# Andrew Poock


def lomuto_partition(A, l, r):
    p = A[l]
    s = l
    for i in range(l+1, r+1):
        if A[i] < p:
            s += 1
            A[i], A[s] = A[s], A[i]
    A[l], A[s] = A[s], A[l]
    return s

def quickselect(A, k, l, r):
    s = lomuto_partition(A, l, r)
    if s == k-1:
        return A[s]
    elif s > k-1:
        return quickselect(A, k, l, s-1)
    else:
        return quickselect(A, k, s+1, r)

def main():
    lst = [32, 56, 12, 99, 82, 74, 41]
    k = 3
    print(f"Performing quickselect to find {k}th smallest element in this list: {lst}")
    print(f"The {k}th smallest item is: {quickselect(lst, k, 0, len(lst)-1)}")

main()