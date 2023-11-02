# C curve

from graphics import *
from math import sqrt

from turtle import Turtle


def c_curve(turtle, length, level):
    if level == 0:
        turtle.move(length)
    else:
        level1 = level - 1
        len1 = length/2**(.5)
        turtle.turn(45)
        c_curve(turtle, len1, level1)
        turtle.turn(-90)
        c_curve(turtle, len1, level1)
        turtle.turn(45)


def main():
    print()
    print("Let's draw a C-curve")
    print()

    level = int(input("What level C-curve do you want? "))

    win = GraphWin("C-curve", 500, 500)
    win.setCoords(0, 0, 500, 500)
    win.setBackground("green")

    myTurtle = Turtle(win, Point(350, 125))
    myTurtle.turn(90)

    c_curve(myTurtle, 250, level)

    Text(Point(350, 250), "Click in window to close").draw(win)
    win.getMouse()
    win.close()


main()
