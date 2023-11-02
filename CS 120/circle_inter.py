# cirlce_inter.py
# Problem 4.7
# by: Andrew Poock

from graphics import *
import math

def main():
    print("This program computes and shows the intersection of a circle")
    print("with a horizontal line.")

    radius = float(input("Enter the radius of the circle (0 < r <= 10): "))
    y = float(input("Enter the y intercept of the line: "))

    # compute the x values of the intersection
    x1 = math.sqrt(radius**2 - y**2)
    x2 = -x1
    print("Point 1: (", x1, ",", y, ")")
    print("Point 2: (", x2, ",", y, ")")

    win = GraphWin("Circle Intersection", 400, 400)
    win.setCoords(-10,-10,10,10)

    circle = Circle(Point(0,0), radius)
    circle.draw(win)

    line = Line(Point(-10,y), Point(10,y))
    line.draw(win)

    p1 = Point(x1, y)
    m1 = Circle(p1, .25)
    m1.setFill("cyan")
    m1.setOutline("cyan")
    m1.draw(win)

    p2 = Point(x2, y)
    m2 = Circle(p2, .25)
    m2.setFill("cyan")
    m2.setOutline("cyan")
    m2.draw(win)

    win.getMouse()
    win.close()

main()
                
