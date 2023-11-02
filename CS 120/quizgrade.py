# quizgrade.py
# Andrew Poock

def grade(score):
    scores = "FFDCBA"
    letter = scores[score]
    return letter

def main():
    print("Quiz Grader")

    s = int(input("Enter the score (0--5): "))
    print("Grade:", grade(s))

main()
