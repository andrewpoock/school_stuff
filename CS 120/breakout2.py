# breakout2.py
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
        if self.dx > 0:
            return (self.marker.getCenter().getX() + self.radius, self.marker.getCenter().getY())
        if self.dx < 0:
            return (self.marker.getCenter().getX() - self.radius, self.marker.getCenter().getY())

    def vTip(self):
        if self.dy > 0:
            return (self.marker.getCenter().getX(), self.marker.getCenter().getY() + self.radius)
        if self.dy < 0:
            return (self.marker.getCenter().getX(), self.marker.getCenter().getY() - self.radius)

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

class BoundingBox:

    def __init__(self, xlow, ylow, xhigh, yhigh):
        self.xlow = xlow
        self.ylow = ylow
        self.xhigh = xhigh
        self.yhigh = yhigh

    def isInside(self, xy):
        x, y = xy
        if (self.xlow <= x <= self.xhigh) and (self.ylow <= y <= self.yhigh):
            return True
        else:
            return False

    def bounce(self, ball):
        if self.isInside(ball.hTip()):
            ball.reflectX()
            print("BOUNCE")
            return True
        if self.isInside(ball.vTip()):
            ball.reflectY()
            print("BOUNCE")
            return True
        
        return False

class BreakoutGame:
    def __init__(self):
        self.win = GraphWin("Bouncing Ball", 500, 500, autoflush=False)
        self.win.setCoords(-100, -100, 100, 100)
        self.win.setBackground("white")
        self.aball = Ball(self.win, (0, 50), 10, 25)
        self.boundingBox = BoundingBox(-40,-40,40,40)

    def run(self):
        while True:
            key = self.win.checkKey()
            if key in ["q", "Q"]:
                break
            checkSideWallContact(self.aball)
            checkTopBottomContact(self.aball)
            self.boundingBox.bounce(self.aball)
            self.aball.move(4)
            update(30)

        self.win.close()


game = BreakoutGame()
game.run()
