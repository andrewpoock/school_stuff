# convert.py
# A program to convert celcius temps to farenheit
# by: Andrew poock

def main():
    print("This program converts celcius temps to farenheit")
    print()
    c = eval(input("what is the celsius temp? "))
    farenheit = 9/5 * c + 32
    print("the temperature is ", farenheit, "degrees farenheit")
    input("press enter to quit")

main()
