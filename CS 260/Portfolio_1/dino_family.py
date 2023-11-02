# dino_family.py
# Andrew Poock

from render2d import Render2d
from draw_drawing import draw_drawing
import random as rand

def draw_drawing(file, r):
    infile = open(file, 'r')
    polylines = infile.readline()
    for i in range(int(polylines)):
        points = []
        point = infile.readline()
        for p in range(int(point)):
            x, y = infile.readline().split()
            x, y = int(x), int(y)
            points.append((x,y))
        r.lines(points)

def dino(r, length, width, angle, pos):
    r.push_matrix()
    r.translate(*pos)
    r.rotate(angle)
    r.scale(length, width)
    draw_drawing('drawing.dat', r)
    r.pop_matrix()

def main():
    r = Render2d((600, 600))
    for i in range(0, 6):
        size = .3*rand.random()+.2
        dino(r, size, size, rand.randrange(0,360),
             (rand.randrange(100, 500),rand.randrange(100,500)))
    r.image.show()
    r.image.save('dinos.ppm')


if __name__ == "__main__":
    main()
