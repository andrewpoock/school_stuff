# Koch snowflake
# Andrew Poock and Ian Barry
from graphics import *
from turtle import Turtle


def koch(turtle, length, level):
    if level == 0:
        turtle.move(length)
    else:
        dist = length/3
        level1 = level-1
        koch(turtle, dist, level1)
        turtle.turn(60)
        koch(turtle, dist, level1)
        turtle.turn(-120)
        koch(turtle, dist, level1)
        turtle.turn(60)
        koch(turtle, dist, level1)


def main():

    print()
    print("Let's draw a Koch snowflake")
    print()

    level = int(input("What level of Koch flake do you want? "))

    win = GraphWin("Koch", 500, 500)
    win.setCoords(0, 0, 500, 500)
    win.setBackground("lightgreen")

    myTurtle = Turtle(win, Point(100, 150))
    myTurtle.turn(60)

    # The Koch snowflake is based on applying the Koch
    # algorithm to each side of an equilateral triangle
    for i in range(3):
        koch(myTurtle, 300, level)
        myTurtle.turn(-120)

    Text(Point(250, 250), "Click in window to close").draw(win)
    win.getMouse()
    win.close()


main()
