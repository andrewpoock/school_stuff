# bounce2.py
#   Simple program for a bouncing circle animation.
# Andrew Poock


from graphics import *


def main():
    win = GraphWin("Bounce!", 500, 500, autoflush=False)
    win.setCoords(-100, -100, 100, 100)
    win.setBackground("white")
    radius = 10
    c = Circle(Point(25, 30), radius)
    c.setFill("red")
    c.draw(win)
    dx = 3/5
    dy = 4/5

    while True:
        key = win.checkKey()
        if key in ["q", "Q"]:
            break
        center = c.getCenter()
        if abs(center.getX()) > (100-radius):
            dx = -dx
        if abs(center.getY()) > (100-radius):
            dy = -dy
        c.move(2*dx, 2*dy)
        update(50)

    win.close()


main()
