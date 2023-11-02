# craps.py
# Andrew Poock

from random import *

def roll_for_point(point_to_make):
    # if needed, rolls until point is made or 7 is rolled
    rollagain = roll_dice()
    while rollagain != point_to_make and rollagain != 7:
        rollagain = roll_dice()
    if rollagain == point_to_make:
        return True
    elif rollagain == 7:
        return False

def roll_dice():
    # rolls a pair of dice
    roll = randrange(1, 7) + randrange(1, 7)
    return roll

def sim_craps():
    # simulates a game of craps
    roll = roll_dice()
    if roll == 2 or roll == 3 or roll == 12:
        return False
    elif roll == 7 or roll == 11:
        return True
    else:
        return roll_for_point(roll)

def sim_n_games(n):
    # uses sim_craps to sim n games, adds number of wins, and returns win %
    wins = 0.0
    for i in range(n):
        if sim_craps() == True:
            wins = wins + 1
    winpercent = (wins/n)*100
    return winpercent, wins

def print_intro():
    # prints an intro to the program
    print("This program simulates games of craps by rolling 2 dice.")
    print("Rolling a 2,3, or 12 is a loss, and rolling a 7 or 11 is a win.")
    print("If you roll a different number, you roll until you win by")
    print("rolling the same number, or lose by rolling a 7.")

def main():
    #main function
    print_intro()
    n = int(input("Enter the number of games to simulate: "))
    winpercent, wins = sim_n_games(n)
    print("You won", int(wins), "of", n, "games, or", winpercent, "%")
    

main()
