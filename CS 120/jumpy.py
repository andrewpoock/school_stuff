# jumpy.py
# Andrew Poock

from graphics import *

def main():
    window = GraphWin("Click Window", 400, 400)
    shape = Rectangle(Point(40,40),Point(60,60))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(window)
    for i in range(10):
        p = window.getMouse()
        center = shape.getCenter()
        dx = p.getX() - center.getX()
        dy = p.getY() - center.getY()
        shape = shape.clone()
        shape.draw(window)
        shape.move(dx,dy)
    window.close()

main()
