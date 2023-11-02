# breakout3.py
# Andrew Poock

from math import *
from graphics import *
from random import *

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

class BoundingBox:

    def __init__(self, x1, y1, x2, y2):
        if x1 < x2:
            self.xlow = x1
            self.xhigh = x2
        elif x1 > x2:
            self.xlow = x2
            self.xhigh = x1
        if y1 < y2:
            self.ylow = y1
            self.yhigh = y2
        elif y1 > y2:
            self.ylow = y2
            self.yhigh = y1

    def isInside(self, xy):
        x, y = xy
        if (self.xlow <= x <= self.xhigh) and (self.ylow <= y <= self.yhigh):
            return True
        else:
            return False

    def bounce(self, ball):
        if self.isInside(ball.hTip()):
            ball.reflectX()
            return True
        if self.isInside(ball.vTip()):
            ball.reflectY()
            return True
        
        return False

class Wall:

    def __init__(self, win, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        self.bbox = BoundingBox(x1, y1, x2, y2)
        self.marker = Rectangle(Point(x1, y1), Point(x2, y2))
        self.marker.draw(win)
        self.marker.setFill("blue")

    def bounce(self, ball):
        return self.bbox.bounce(ball)

class Brick:
    def __init__(self, win, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        self.bbox = BoundingBox(x1, y1, x2, y2)
        self.color = color_rgb(randrange(50, 256), randrange(50, 256), randrange(50, 256))
        self.brick = Rectangle(Point(x1, y1), Point(x2, y2))
        self.brick.setFill(self.color)
        self.brick.draw(win)
        
    def bounce(self, ball):
        if self.bbox.bounce(ball) == True:
            self.brick.undraw()
            return True
        return False

class BreakoutGame:
    def __init__(self):
        self.win = GraphWin("Bouncing Ball", 1024, 768, autoflush=False)
        self.win.setCoords(-200, -150, 200, 150)
        self.win.setBackground("black")
        self.aball = Ball(self.win, (0, -100), 10, 45)
        self.w1 = Wall(self.win, (-200, -150), (-190, 150))
        self.w2 = Wall(self.win, (200, -150), (190, 150))
        self.w3 = Wall(self.win, (-200, 150), (200, 140))
        self.w4 = Wall(self.win, (-200, -150), (200, -140))
        self.walls = [self.w1, self.w2, self.w3, self.w4]
        b1 = Brick(self.win, (randrange(-180, 180), randrange(-75, 130)), (randrange(-180, 180), randrange(-75, 130)))
        b2 = Brick(self.win, (randrange(-180, 180), randrange(-75, 130)), (randrange(-180, 180), randrange(-75, 130)))
        b3 = Brick(self.win, (randrange(-180, 180), randrange(-75, 130)), (randrange(-180, 180), randrange(-75, 130)))
        b4 = Brick(self.win, (randrange(-180, 180), randrange(-75, 130)), (randrange(-180, 180), randrange(-75, 130)))
        self.bricks = [b1, b2, b3, b4]

    def run(self):
        while True:
            key = self.win.checkKey()
            if key in ["q", "Q"] or self.bricks == []:
                break
            for wall in self.walls:
                if wall.bounce(self.aball):
                    print("BOUNCE!")
            for brick in self.bricks:
                if brick.bounce(self.aball):
                    print("BOOM")
                    self.bricks.remove(brick)
            self.aball.move(5)
            update(30)

        self.win.close()


game = BreakoutGame()
game.run()
