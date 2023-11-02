# cipherfile.py
# Andrew Poock

def encoded_word(word, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newword = ""
    for letter in word:
        pos = alphabet.find(letter)
        newpos = (pos+key) % len(alphabet)
        newletter = alphabet[newpos]
        newword += newletter
    return newword

def encoded_line(line, key):
    newline = ""
    for word in line.split():
        newline += encoded_word(word, key)
        newline += " "
    return newline

def encode_file(infile_name, outfile_name, key):
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w")
    for line in infile:
        print(encoded_line(line, key), file= outfile)
    infile.close()
    outfile.close()

def main():
    print("This program encrypts a message from a file to another file")
    infileName = input("Enter the name of the file to translate: ")
    outfileName = input("Enter the name of the file to write the new message on: ")
    key = int(input("Enter the key in which to encode the message: "))
    encode_file(infileName, outfileName, key)
    print("Success!", infileName, "has been encrypted to", outfileName)

main()
