# futval2.py
# A program to compute the value of an investment carried 10 years into
# the future
# by: Andrew Poock

def main():
    print("This program calculates the future value on a multi-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual intrest rate: "))
    years = eval(input("Enter the number of years of the investment: "))
    print("Enter how often it is compounded per year: ")
    periods = eval(input("(1 = annually, 4 = quarterly, 12 = monthly)\n"))

    for i in range(years*periods):
        principal = principal * (1 + apr/periods)

    print("The value in", years, "years is:", principal)

main()
