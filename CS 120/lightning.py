# lightning.py
# A program to help the user calculate the distance to lightning
# by: Andrew Poock

def main () : 
    print ("This program calculates the distance in miles to a lighning strike ") 
    s = eval (input ("Enter the number of seconds between the lightning and the thunder: ")) 
    miles = (1125*s)/5280
    print ("The distance to the lightning is ", miles, "miles")
    input("Press 'enter' to quit")
    
main () 
