# breakout1.py
#   Simple program for a bouncing ball animation.
# Andrew Poock

from math import *
from graphics import *


class Ball:

    def __init__(self, window, center, radius, angle):
        self.radius = radius
        self.marker = Circle(Point(center[0], center[1]), radius)
        self.marker.setFill("red")
        self.marker.draw(window)
        self.angle = degrees(angle)
        self.dx = cos(self.angle)
        self.dy = sin(self.angle)

    def hTip(self):
        return (abs(self.marker.getCenter().getX()) + self.radius, self.marker.getCenter().getY())

    def vTip(self):
        return (self.marker.getCenter().getX(), abs(self.marker.getCenter().getY()) + self.radius)

    def move(self, distance):
        self.marker.move(distance*self.dx, distance*self.dy)

    def reflectX(self):
        self.dx = -self.dx
        
    def reflectY(self):
        self.dy = -self.dy

def checkSideWallContact(ball):
    leadX, y = ball.hTip()
    if abs(leadX) > 100:
        ball.reflectX()


def checkTopBottomContact(ball):
    x, leadY = ball.vTip()
    if abs(leadY) > 100:
        ball.reflectY()


def main():
    win = GraphWin("Bouncing Ball", 500, 500, autoflush=False)
    win.setCoords(-100, -100, 100, 100)
    win.setBackground("white")

    aball = Ball(win, (0, 50), 10, 40)
    while True:
        key = win.checkKey()
        if key in ["q", "Q"]:
            break
        checkSideWallContact(aball)
        checkTopBottomContact(aball)
        aball.move(3)
        update(50)

    win.close()


main()
