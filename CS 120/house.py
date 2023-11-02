# house.py
# allows the user to make a house by clicking the screen
# by: Andrew Poock

from graphics import *

def main():
    s1 = "Create a house by clicking opposite corners of the house,"
    s2 = "the top of the door, the window, the roof, and colors"
    window = GraphWin(s1 + s2, 800, 550)
    window.setCoords(-10,-10,10,10)

    # draw rectangle
    p1 = window.getMouse()
    p2 = window.getMouse()

    if p1.getY() < p2.getY():
        bottom = Point(p1.getX(), p1.getY())
        top = Point(p2.getX(), p2.getY())
    else:
        bottom = Point(p2.getX(), p2.getY())
        top = Point(p1.getX(), p1.getY())

    rec = Rectangle(p1,p2)
    rec.draw(window)

    # draw door
    p3 = window.getMouse()
    width = (abs(p1.getX() - p2.getX())/5)
    rec2 = Rectangle(Point(1,1),Point(2,2))
    rec2.setWidth(width)
    p31 = Point(p3.getX()-width/2, p3.getY())
    p32 = Point(p3.getX()+width/2, bottom.getY())
    rec2 = Rectangle(p31, p32)
    rec2.draw(window)
    
    # draw window
    p4 = window.getMouse()
    width2 = (abs(p31.getX()-p32.getX())/2)
    rec3 = Rectangle(Point(1,1),Point(2,2))
    rec3.setWidth(width2)
    p41 = Point(p4.getX()-width2/2, p4.getY()+width2/2)
    p42 = Point(p4.getX()+width2/2, p4.getY()-width2/2)
    rec3 = Rectangle(p41, p42)
    rec3.draw(window)

    # draw roof
    p5 = Point(p1.getX(), top.getY())
    p6 = Point(p2.getX(), top.getY())
    p7 = window.getMouse()
    tri = Polygon(p5, p6, p7)
    tri.draw(window)

    # add color
    window.getMouse()
    rec.setFill("wheat")
    rec2.setFill("silver")
    rec3.setFill("cyan")
    tri.setFill("firebrick")

    text = Text(Point(0,-8), "Nice House! Click again to exit")
    text.setSize(20)
    text.draw(window)

    window.getMouse()
    window.close()

main()
