# quickhull.py
# Andrew Poock

from graphics import *
from random import randint


def determ(a, b, c):
    return a[0]*b[1] + c[0]*a[1] + b[0]*c[1] - c[0]*b[1] - b[0]*a[1] - a[0]*c[1]

def halfhull(p1, p2, s, dets):
    if s == []:
        return [(p1, p2)]
    else:
        pivot_i = dets.index(max(dets))
        pivot = s[pivot_i]
        s.remove(pivot)
        newdets1 = [determ(p1, pivot, p) for p in s]
        s1 = [s[i] for i in range(len(s)) if newdets1[i] > 0]
        dets1 = [newdets1[i] for i in range(len(newdets1)) if newdets1[i] > 0]
        newdets2 = [determ(pivot, p2, q) for q in s]
        s2 = [s[i] for i in range(len(s)) if newdets2[i] > 0]
        dets2 = [abs(newdets2[i]) for i in range(len(newdets2)) if newdets2[i] > 0]
        return halfhull(p1, pivot, s1, dets1) + halfhull(pivot, p2, s2, dets2)

def quickhull(pts):
    inds = range(len(pts))
    minx_i = min(inds, key=pts.__getitem__)
    maxx_i = max(inds, key=pts.__getitem__)
    p1 = pts[minx_i]
    p2 = pts[maxx_i]
    s = pts[:]
    s.remove(p1)
    s.remove(p2)
    dets = [determ(p1, p2, p) for p in s]
    s1 = [s[i] for i in range(len(s)) if dets[i] > 0]
    dets1 = [dets[i] for i in range(len(dets)) if dets[i] > 0]
    uhull = halfhull(p1, p2, s1, dets1)
    s2 = [s[i] for i in range(len(s)) if dets[i] < 0]
    dets2 = [abs(dets[i]) for i in range(len(dets)) if dets[i] < 0]
    lhull = halfhull(p2, p1, s2, dets2)
    return uhull + lhull

def main():
    n = int(input("Enter the number of random points to draw and make a quickhull: "))
    points = [(randint(-80, 80),randint(-80,80)) for i in range(n)]
    hull = quickhull(points)
    win = GraphWin("QuickHull", 500, 500)
    win.setCoords(-100,-100,100,100)
    for x,y in points:
        point = Point(x, y)
        point.draw(win)
    for (x1, y1), (x2, y2) in hull:
        line = Line(Point(x1, y1), Point(x2, y2))
        line.draw(win)
    win.getMouse()
    win.close()

main()