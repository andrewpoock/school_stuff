# bounce.py
# Andrew Poock

from graphics import *

def main():
    win = GraphWin("Bounce!", 500, 500)
    win.setCoords(0, 0, 100, 100)
    r = 5
    ball = Circle(Point(25, 67), r)
    ball.setFill("red")
    ball.setOutline("red")
    ball.draw(win)
    vx = 2
    vy = -1
    key = win.checkKey()
    while key not in ['q', 'Q']:
        center = ball.getCenter()
        if (center.getX() + r) > 100 or (center.getX() - r) < 0:
            vx = -vx
        if (center.getY() + r) > 100 or (center.getY() - r) < 0:
            vy = -vy
        ball.move(vx, vy)
        update(30)
        key = win.checkKey()
    win.close()


main()
