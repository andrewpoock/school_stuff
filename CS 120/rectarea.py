# number 9
from graphics import *

def main():
    win = GraphWin("Rectangle Infor", 400, 400)
    win.setCoords(-10,-10,10,10)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p1.undraw()

    rect = Rectangle(p1,p2)
    rect.draw(win)

    length = abs(p2.getX() - p1.getX())
    width = abs(p2.getY() - p1.getY())

    area = round(length * width, 2)

    Text(rect.getCenter(), "area = " + str(area)).draw(win)

    win.getMouse()
    win.close()

main()
