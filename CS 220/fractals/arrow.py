# arrow.py
# Andrew Poock

from graphics import *

from turtle import Turtle


def arrow(turtle, length, level):
    if level == 0:
        turtle.move(length)
    else:
        level1 = level - 1
        len1 = length/2
        turtle.turn(60)
        worra(turtle, len1, level1)
        turtle.turn(-60)
        arrow(turtle, len1, level1)
        turtle.turn(-60)
        worra(turtle, len1, level1)
        turtle.turn(60)


def worra(turtle, length, level):
    if level == 0:
        turtle.move(length)
    else:
        level1 = level - 1
        len1 = length/2
        turtle.turn(-60)
        arrow(turtle, len1, level1)
        turtle.turn(60)
        worra(turtle, len1, level1)
        turtle.turn(60)
        arrow(turtle, len1, level1)
        turtle.turn(-60)


def main():
    print("Arrow")
    n = int(input("What level do you want? "))
    w = GraphWin("Arrow", 500, 500)
    w.setCoords(0, 0, 499, 499)
    t = Turtle(w, Point(100, 250))
    arrow(t, 300, n)
    w.getMouse()
    w.close()


if __name__ == "__main__":
    main()
