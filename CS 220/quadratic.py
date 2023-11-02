# quadratic.py
# Andrew Poock

from math import sqrt

def calc_discrim(a, b, c):
    ans = b**2 - 4*a*c
    return ans

def print_intro():
    print("This program calculates the real roots of a quadratic equation")

def get_coeffs():
    a, b, c = input("Enter the coefficients (a b c): ").split()
    return float(a), float(b), float(c)

def main():
    print_intro()
    a, b, c = get_coeffs()

    discrim = calc_discrim(a, b, c)
    if discrim > 0:
        discrt = sqrt(discrim)
        root1 = (-b + discrt)/(2*a)
        root2 = (-b - discrt)/(2*a)
        print("The roots are: ", root1, root2)
    elif discrim == 0:
        print("The root is", -b/(2*a))
    else:
        print("No real roots")

main()
    
