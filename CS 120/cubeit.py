# cubeit.py
# Display cube of a number
# Andrew Poock

def cube(x):
    num = x*x*x
    return num

def main():
    print("This program computes the cube of a number")
    num = float(input("Please enter a number: "))

    print("The cube of", num, "is:", cube(num))

main()
