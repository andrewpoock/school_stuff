# acronym.py
# Andrew Poock

def acro(phrase):
    ans = ""
    for word in phrase.split():
        ans = ans + word[0].upper()
    return ans

def main():
    print("This program makes an acronym from user input")
    words = input("Enter a phrase of words: ")

    print("The acronym is:", acro(words))

main()
