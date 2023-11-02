# File: chaos.py
# A simple program illustrating chaotic behavior
# by: Andrew Poock

def main():
    n = eval(input("How many numbers should I print? ")) #use .5
    print("This program illustrates a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        x = 3.9*x-3.9*x*x
        print(x)
    x = .5
    for i in range(n):
        x = 3.9*x*(1-x)
        print(x)
    x = .5
    for i in range(n):
        x = 3.9*(x-x*x)
        print(x)

main()

# The first number is the same, but the other numbers appear to be slightly
# different. the second number last decimal place changes from 5 to 8 to 13
# which causes the other numbers to be slightly different.
# However, I am not sure why the second number would change.
# Maybe something to do with how the computer stores the values?
