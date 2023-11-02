# cipher.py
# description
# by: Andrew Poock

def main():
    message = input("Enter a message of lowercase letters and spaces to translate: ")
    key = int(input("Enter a key to shift the message by: "))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    words = message.split()
    for word in words:
        newword = ""
        for letter in word:
            pos = alphabet.find(letter)
            newpos = (pos+key) % len(alphabet)
            newletter = alphabet[newpos]
            newword += newletter
        words[i] = newword
        i = i+1
    newmessage = " ".join(words)
    print(newmessage)
    
main()
