# hello_graphics.py
# by: Andrew Poock

from graphics import *

def main():
    win = GraphWin("Hello", 500, 300)
    greeting = Text(Point(250,150), "Hello, CS 120")
    greeting.setSize(32)
    greeting.draw(win)
    win.getMouse()
    win.close()

main()
