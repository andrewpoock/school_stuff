# msgcd.py
# Prime factorization algorithm for computing gcd
# by Andrew Poock

# Computes the floor(sqrt(n))
def floorsqrt(n):
    temp = 1
    while temp * temp <= n:
        temp = temp + 1
    return temp - 1

# Finds common elements of 2 sorted, numeric lists and combines them into 1 list
def merge_lists(l1, l2):
    result = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            result.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1
    return result

# Returns all prime numbers <= n
def sieve(n):
    a = [True for _ in range(n+1)]
    for p in range(2, floorsqrt(n)):
        if a[p]:
            j = p * p
            while j <= n:
                a[j] = False
                j = j + p
    return [i for i in range(2, n+1) if a[i]]

# Computes gcd(a, b) by finding the common primes in the 2 prime factorizations and multiplying them together
def msgcd(a, b):
    aprimes = sieve(a)
    bprimes = sieve(b)
    pfa, pfb = [], []
    # Loop through the list of primes <= a and get the ones that divide a (a's unique prime factorization)
    for i in range(len(aprimes)):
        while a % aprimes[i] == 0:
            pfa.append(aprimes[i])
            a = a / aprimes[i]
            if a == 1:
                break
    # Same algorithm as above for b
    for j in range(len(bprimes)):
        while b % bprimes[j] == 0:
            pfb.append(bprimes[j])
            b = b / bprimes[j]
            if b == 1:
                break
    result = 1
    common = merge_lists(pfa, pfb)
    # Multiply together the common primes to compute the gcd
    for k in range(len(common)):
        result = result * common[k]
    return result


def main():
    print("\nThis program computes the greatest common divisor of 2 integers\n")
    a = int(input("Enter int a: "))
    b = int(input("Enter int b: "))
    print(f"\ngcd({a}, {b}) = {msgcd(a, b)}\n")


main()