#turtle.py

from graphics import *
from math import sin,cos,radians

class Turtle:

    def __init__(self, window, pos=Point(0,0)):
        self._win = window
        self._pos = pos
        self._dir = 0
        self._pic = None
        self._drawTurtle()

    def move(self, d):
        newpos = self._nextPoint(d)
        drawing = Line(self._pos, newpos)
        drawing.draw(self._win)
        self._pos = newpos
        self._drawTurtle()

    def turn(self, angle):
        self._dir = self._dir + radians(angle)
        self._drawTurtle()

    def _drawTurtle(self):
        tip = self._nextPoint(10)
        body = Line(self._pos, tip)
        body.setArrow("last")
        body.draw(self._win)
        if self._pic != None:
            self._pic.undraw()
        self._pic = body

    def _nextPoint(self, d):
        dest = self._pos.clone()
        dest.move(d*cos(self._dir), d*sin(self._dir))
        return dest

def test():
    win = GraphWin("Turtle Test", 500, 500)
    win.setCoords(-250,-250,250,250)
    turt = Turtle(win)
    for i in range(4):
        turt.move(50)
        turt.turn(90)
        win.getMouse()

if __name__ == '__main__':
    test()
