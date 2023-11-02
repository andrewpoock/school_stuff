#average.py
#A program to calculate the average of 3 exam scores
# by: Andrew Poock

def main () : 
    print ("This program computes the average of three exam scores ") 
    score1, score2, score3 = eval (input ("Enter three scores separated by a comma: ")) 
    average = (score1 + score2 + score3)/3 
    print ("The average of the scores is: ", average)
    input("Press 'enter' to quit")
    
main () 
