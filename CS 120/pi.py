# pi.py
# Program to estimate pi
# by: Andrew Poock
import math

def main():
    n = int(input("Enter the number of terms to estimate pi: "))
    num = 4
    denom = 1
    x = 0
    for denom in range(1,2*n,2):
        x = x + num/denom
        num = -num
    error = abs(x - math.pi)
    print("The estimate of pi is: ", x)
    print("The error is: ", error)

main()
