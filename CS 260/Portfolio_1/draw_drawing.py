# draw_drawing.py
# Andrew Poock

import sys
from image import Image
from painter import Painter

def draw_drawing(file, painter):
    infile = open(file, 'r')
    polylines = infile.readline()
    for i in range(int(polylines)):
        points = []
        point = infile.readline()
        for p in range(int(point)):
            x, y = infile.readline().split()
            x, y = int(x), int(y)
            points.append((x,y))
        painter.draw_lines(points)


if __name__ == '__main__':
    img = Image((700,500))
    img.clear((255,255,255))
    p = Painter(img)
    draw_drawing('drawing.dat', p)
    img.show()
