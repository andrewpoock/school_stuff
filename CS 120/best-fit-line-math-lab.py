#practice

from graphics import *
from statistics import mean

def isDone(point):
    x = point.getX()
    y = point.getY()
    xlow, xhigh = 7, 10
    ylow, yhigh = -10, -8
    if (xlow <= x <= xhigh) and (ylow <= y <= yhigh):
        return True
    else:
        return False
    

def main():
    win = GraphWin("Click points to find the best fit line", 500, 500)
    win.setCoords(-10,-10,10,10)
    button = Rectangle(Point(10, -10), Point(7,-8))
    button.draw(win)

    xvalues = []
    yvalues = []
    n = 0
    xy_sum = 0
    x2_sum = 0

    while True:
        p1 = win.getMouse()
        if isDone(p1) == True:
            break
        n = n + 1
        x = p1.getX()
        y = p1.getY()
        xvalues.append(x)
        yvalues.append(y)
        p1.draw(win)

    for i in range(len(xvalues)):
        xy_sum += xvalues[i]*yvalues[i]
        x2_sum += xvalues[i]*xvalues[i]
        
    xmean = round(mean(xvalues), 5)
    ymean = round(mean(yvalues), 5)

    m = round((xy_sum-n*xmean*ymean)/(x2_sum-n*xmean**2), 5)
    equation = 'y = {ymean} + {m} * (x - {xmean})'.format(ymean=ymean, xmean=xmean, m=m)
    message = Text(Point(0,-8), equation)
    message.draw(win)

main()
        
