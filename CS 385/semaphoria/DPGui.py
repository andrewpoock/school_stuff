# DPGui.py -- Simple graphical display for dinining philosophers problem
# Code shamefully borrowed from Dr. John Zelle. Thanks, Dr. Zelle!

from graphics_threaded import *
from math import pi, cos, sin, sqrt

PRAD = 2
PDIST = 7

FLEN = 1.5
FWIDTH = 2

COLOR_INUSE = "red"
COLOR_FREE = "green"

COLOR_THINKING = ""
COLOR_HUNGRY = "yellow"
COLOR_EATING = "red"

class DPDisplay:

    def __init__(self, n=5):
        self.n = n
        win = self.win = GraphWin("Dining Philosophers", 300, 300)
        win.setCoords(-10,-10,10,10)
        win.setBackground("honeydew")
        dt = pi*2.0 / n
        cs = self.philosophers = []
        fs = self.forks = []
        r = PDIST
        for i in range(n):
            theta = dt * i
            x = r*cos(theta)
            y = r*sin(theta)
            c = Circle(Point(x,y), PRAD)
            c.draw(win)
            cs.append(c)
            thetaf = theta - dt/2.0
            x = r * cos(thetaf)
            y = r * sin(thetaf)
            if abs(x) < .01:
                dx = 0
                dy = FLEN
            else:
                s = y/x
                dx = FLEN/sqrt(s*s+1)
                dy = (s*dx)
            p1 = Point(x+dx,y+dy)
            p2 = Point(x-dx,y-dy)
            l = Line(p1,p2)
            l.setWidth(FWIDTH)
            l.draw(win)
            fs.append(l)
            
    def setFork(self, i, state):
        assert(0<=i<self.n)
        assert(state in ["inuse","free"])
        fork = self.forks[i]
        if state == "inuse":
            fork.setFill(COLOR_INUSE)
        else:
            fork.setFill(COLOR_FREE)
        self.win.flush()

    def setPhil(self, i, state):
        assert(0<=i<self.n)
        assert(state in ["eating", "thinking", "hungry"])
        p = self.philosophers[i]
        if state == "eating":
            p.setFill(COLOR_EATING)
        elif state == "thinking":
            p.setFill(COLOR_THINKING)
        else:
            p.setFill(COLOR_HUNGRY)
        self.win.flush()

    def pause(self):
        self.win.getMouse()
