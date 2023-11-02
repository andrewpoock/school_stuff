# qgrade.py
# by: Andrew Poock

def main():
    grades = 60*"F" + 10*"D" + 10*"C" + 10*"B" + 11*"A"
    score = int(input("Enter the score: "))
    print("The grade is a", grades[score]+".")
main()
