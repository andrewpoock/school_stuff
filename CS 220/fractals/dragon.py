# dragon.py

from graphics import *

from turtle import Turtle
from math import sqrt


def dragon(turtle, length, level):
    if level == 0:
        turtle.move(length)
    else:
        level1 = level - 1
        len1 = length/2**(.5)
        turtle.turn(45)
        dragon(turtle, len1, level1)
        turtle.turn(-90)
        nogard(turtle, len1, level1)
        turtle.turn(45)


def nogard(turtle, length, level):
    if level == 0:
        turtle.move(length)
    else:
        level1 = level - 1
        len1 = length/2**(.5)
        turtle.turn(-45)
        dragon(turtle, len1, level1)
        turtle.turn(90)
        nogard(turtle, len1, level1)
        turtle.turn(-45)


def main():
    print("Dragon Curve")
    n = int(input("What level do you want? "))
    w = GraphWin("Dragon Curve", 500, 500)
    w.setCoords(0, 0, 499, 499)
    w.setBackground("lightgreen")
    t = Turtle(w, Point(125, 250))
    dragon(t, 300, n)
    w.getMouse()
    w.close()


if __name__ == "__main__":
    main()
