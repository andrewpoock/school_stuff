#jumpyyy.py
# Andrew Poock

from graphics import *

def moveTo(obj, newcenter):
    center = obj.getCenter()
    dx = newcenter.getX() - center.getX()
    dy = newcenter.getY() - center.getY()
    obj.move(dx, dy)

def main():
    window = GraphWin("Click Window", 400, 400)
    shape = Circle(Point(50, 50), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(window)
    for i in range(10):
        p = window.getMouse()
        moveTo(shape, p)
    window.close()

main()
