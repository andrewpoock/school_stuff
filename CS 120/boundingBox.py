# boundingBox.py
# Andrew Poock

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
