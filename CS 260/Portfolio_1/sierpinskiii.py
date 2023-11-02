# sierpinskiii.py
# Andrew Poock

import sys
from image import Image
from painter import Painter

def draw_sierpinski(a, b, c, level, painter):
    if level == 0:
        painter.draw_filled_triangle(a, b, c)
    else:
        ab = ((a[0]+b[0])/2, (a[1]+b[1])/2)
        bc = ((b[0]+c[0])/2, (b[1]+c[1])/2)
        ac = ((a[0]+c[0])/2, (a[1]+c[1])/2)
        draw_sierpinski(a,ab,ac,level-1, p)
        draw_sierpinski(ab,b,bc,level-1, p)
        draw_sierpinski(ac,bc,c,level-1, p)
        

if __name__ == '__main__':
    level = int(input("What level sierpinski triangle should we draw? "))
    img = Image((400,400))
    img.clear((255,255,255))
    p = Painter(img)
    draw_sierpinski((25, 50), (200, 324.75), (375, 50), level, p)
    img.show()
