# wavefns.py
#    Simple periodic waveform functions.

import math
from math import pi as pi
import random

def sinewave(t):
    """ standard periodic sine wave generator """
    return math.sin(t)

def squarewave(t):
    """ Standard periodic square wave generator.

    pre: t >= 0
    post: returns amplitude of standard square wave at time t.
          (1.0 for 0 <= t < pi and -1.0 for pi <= t < 2*pi)
    """
    p = t % math.tau
    if p >= 0 and p < pi:
        return 1
    elif p >= pi and p < math.tau:
        return -1

def trianglewave(t):
    """ Standard periodic triangle wave generator.

    pre: t >= 0
    post: returns amplitude of standard triangle wave at time t.
          (0.0 at t=0, 1.0 at t=pi/2, 0.0 at t=pi, -1.0 at t=1.5*pi)
    """
    p = t % math.tau
    if p >= 0 and p < pi/2:
        return p*(2/pi)
    elif p >= pi/2 and p < 3*pi/2:
        return p*(-2/pi)+2
    elif p >= 3*pi/2 and p < math.tau:
        return p*(2/pi)-4
    
def sawtoothwave(t):
    """ Standard periodic sawtooth wave generator.

    pre: t >= 0
    post: returns amplitude of standard sawtooth wave at time t.
          (0.0 at t=0, rises to 1 near t=pi, -1.0 at t=pi, rises to 0.0 at t=pi)
    """
    p = t % math.tau
    if p >= 0 and p < pi:
        return p*(1/pi)
    if p >= pi and p < math.tau:
        return p*(1/pi)-2


def whitenoise(t):
    """ White noise "wave" generator

    post: returns random value in range -1 to 1
    """
    return random.random()*2-1

def _plot(wavefn):
    # test function plots 2 cycles of wavefn
    win = GraphWin(wavefn.__name__, 600, 200, autoflush=False)
    win.setCoords(-1, -1.3, 2*math.tau+1, 1.2)
    for y in [-1, 0, 1]:
        Line(Point(0, y), Point(2*math.tau, y)).draw(win)
        Text(Point(-.5, y), str(y)).draw(win)

    Text(Point(math.tau, -1.15), "2*pi").draw(win)
    Line(Point(math.tau, -1), Point(math.tau, 1.1)).draw(win)
    Text(Point(2*math.tau, -1.15), "4*pi").draw(win)
    Line(Point(2*math.tau, -1), Point(2*math.tau, 1.1)).draw(win)

    npoints = 300
    dt = 2*math.tau/npoints
    t = 0
    last = Point(t, wavefn(t))
    for i in range(npoints):
        t += dt
        p = Point(t, wavefn(t))
        segment = Line(last, p).draw(win)
        segment.setFill("red")
        segment.setWidth(2)
        last = p
    win.getMouse()
    win.close()


if __name__ == "__main__":
    from graphics import *
    _plot(sinewave)
    _plot(squarewave)
    _plot(trianglewave)
    _plot(sawtoothwave)
    _plot(whitenoise)
