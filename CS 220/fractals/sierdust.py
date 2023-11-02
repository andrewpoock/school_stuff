# Program to draw Sierpinski triangle using
#  a "fractal dust" approach

from graphics import *
from random import choice


def sierpinskidust(a, b, c, n, win):
    lastPoint = getmid(a, b)
    for i in range(n):
        vertex = choice((a, b, c))
        lastPoint = getmid(lastPoint, vertex)
        lastPoint.draw(win)


def getmid(p1, p2):
    return Line(p1, p2).getCenter()


def main():
    print("Let's draw a Sierpinski triangle.")
    npoints = int(input("How many points should we use? "))
    win = GraphWin('Sierpinski Triangle', 800, 800, autoflush=False)
    win.setCoords(20, -10, 80, 50)
    win.update()
    sierpinskidust(Point(25, 0), Point(50, 43.3), Point(75, 0), npoints, win)
    win.getMouse()


if __name__ == '__main__':
    main()
