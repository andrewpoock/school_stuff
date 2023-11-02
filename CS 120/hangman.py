# Program: final_project.py
# Author: Andrew Poock
# Last date modified: 08/02/20
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random


# creates Hangman game where the user must guess the dessert before they run out of tries.

class Hangman:

    def __init__(self):
        self.word_list = ["PIE", "FUDGE", "COOKIE", "CAKE", "ICECREAM", "PUDDING", "BROWNIE", "CUPCAKE", "MUFFIN",
                          "DOUGHNUT",
                          "POPSICLE", "CINNAMONROLL"]
        self.photos = [PhotoImage(file='images/hang0.png'), PhotoImage(file='images/hang1.png'),
                       PhotoImage(file='images/hang2.png'),
                       PhotoImage(file='images/hang3.png'), PhotoImage(file='images/hang4.png'),
                       PhotoImage(file='images/hang5.png'),
                       PhotoImage(file='images/hang6.png'), PhotoImage(file='images/hang7.png'),
                       PhotoImage(file='images/hang8.png'),
                       PhotoImage(file='images/hang9.png'), PhotoImage(file='images/hang10.png'),
                       PhotoImage(file='images/hang11.png')]
        self.space_word = ''
        self.guesses = 0
        self.setup()

    def reset(self):
        self.guesses = 0
        self.imgLabel.config(image=self.photos[0])
        self.word = random.choice(self.word_list)
        self.space_word = " ".join(self.word)
        self.lblWord.set(" ".join("_" * len(self.word)))

    def guess(self, letter):
        if self.guesses < 11:
            txt = self.space_word
            guessed = list(self.lblWord.get())
            if self.space_word.count(letter) > 0:
                for x in range(len(txt)):
                    if txt[x] == letter:
                        guessed[x] = letter
                    self.lblWord.set("".join(guessed))
                    if self.lblWord.get() == self.space_word:
                        messagebox.showinfo("Hangman", "You win!! :D")
                        self.reset()
            else:
                self.guesses += 1
                self.imgLabel.config(image=self.photos[self.guesses])
                if self.guesses == 11:
                    messagebox.showwarning("Hangman", "Game Over :( , the word was: " + self.word)

    def setup(self):
        self.imgLabel = Label(window)
        self.imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
        self.imgLabel.config(image=self.photos[0])
        self.lblWord = StringVar()
        Label(window, textvariable=self.lblWord, font="Consolas 24 bold").grid(row=0, column=3, columnspan=6, padx=10)
        guessLabel = Label(window, text='Guess the dessert!', font='Helivtica 18').grid(row=0, column=3, columnspan=3,
                                                                                        sticky='N')

        n = 0
        for c in ascii_uppercase:
            Button(window, text=c, command=lambda c=c: self.guess(c), font="Helivtica 18", width=4).grid(row=1 + n // 9,
                                                                                                         column=n % 9,
                                                                                                         sticky='NSWE')
            n += 1

        Button(window, text='New\nGame', command=lambda: self.reset(), font='Helivtica 12 bold').grid(row=3, column=8,
                                                                                                      sticky='NSWE')


# driver
window = Tk()
window.title("Hangman")
game = Hangman().reset()
window.mainloop()
