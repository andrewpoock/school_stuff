# sumn.py
# Andrew Poock

def sumN(n):
    sum = 0
    for num in range(1, n+1):
        sum = sum + num
    return sum

def main():
    print("This program returns the sum of the natural")
    print("numbers from 1 to n.")

    last = int(input("\nEnter the value of n: "))
    print("The sum is:", sumN(last))

main()
