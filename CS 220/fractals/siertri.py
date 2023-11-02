# Program to draw a Sierpinski triangle recursively
# Andrew Poock, Ian Barry

from graphics import *


def sierpinskiT(a, b, c, level, win):
    if level == 0:
        t = Polygon(a, b, c)
        t.setFill('black')
        t.draw(win)
    else:
        e = getmid(a, b)
        f = getmid(b, c)
        g = getmid(a, c)
        sierpinskiT(a, e, g, level-1, win)
        sierpinskiT(e, b, f, level-1, win)
        sierpinskiT(g, c, f, level-1, win)

def getmid(p1, p2):
    return Line(p1, p2).getCenter()


if __name__ == '__main__':
    print("Let's draw a Sierpinski triangle")
    level = int(input("What level tirangle should we draw? "))
    win = GraphWin('Sierpinski Triangle', 800, 800, autoflush=False)
    win.setCoords(20, -10, 80, 50)
    sierpinskiT(Point(25, 0), Point(50, 43.3), Point(75, 0), level, win)
    win.getMouse()
