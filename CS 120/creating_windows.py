# Andrew Poock

from graphics import *

def main():
    win = GraphWin()
    win.close()
    win = GraphWin('My Window')
    SmallWin = GraphWin('My Window', 50, 50)
    win.close()
    SmallWin.close()

main()
