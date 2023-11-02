# pingpong.py
# Simulation of pingpong games

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of pingpong between two players")
    print('called "A" and "B".  The abilities of each player are indicated')
    print("by a probability (a number between 0 and 1) that the player wins")
    print("the point when serving. Player A always has the first serve.")

def getInputs():
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
            if serviceShouldSwitch(scoreA, scoreB) == True:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
            if serviceShouldSwitch(scoreA, scoreB) == True:
                serving = "A"
    return scoreA, scoreB

def serviceShouldSwitch(scoreA, scoreB):
    totalscore = scoreA + scoreB
    return totalscore % 2 == 0 or totalscore >= 20

def gameOver(a, b):
    return (a >= 11 or b >= 11) and abs(a - b) >= 2

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()
