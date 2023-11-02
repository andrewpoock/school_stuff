# convert.py
# Andrew Poock

def main():
    #print an intro
    print("This program converts celsius to Fahrenheit")

    #calculations
    c = float(input("Enter celsius temp: "))
    f = 9/5*c + 32
    print("The temp is", f, "degrees Fahrenheit")

    if f > 90:
        print("It's really hot out there!")
    elif f < 20:
        print("It's really cold out there!")

    print("Thanks for using the amazing megaconverter!")

if __name__ == "__main__":
    main()