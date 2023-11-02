# painter.py
# Andrew Poock

"""
Class for simple 2D drawing

A Painter wraps a raw raster image to make drawing into the image
more convenient. Whereas pixel coordinates are integers, a painter allows
floating point coordinates and provides methods for drawing geometric figures.
"""


from collections import namedtuple
from math import pi, sin, cos, floor, ceil


location2d = namedtuple("location2d", 'x y')
# named tuple to represent locations in an image
#   A location2d is a tuple (x, y) and functions like a
#   regular tuple, but also allows access via attributes x and y
#   example:
#      p = location2d(3, 5)
#      x, y = p
#      total = x + y
#    or
#      total = p.x + p.y


def _pixloc(loc):
    """returns the pixloc that is closest to Painter location

    Note: Painter locations are in natural image coordinates (x, y)
          where x and y are floats: -0.5 < x < width - 0.5 and -0.5 <
          y < height - 0.5

    """
    x, y = loc
    return location2d(round(x), round(y))


class Painter:
    """Tool for drawing geometric figures into images

    A Painter wraps an Image and supplies two conveniences
    1) A continuous image coordinate system (location coords can be floats)
    2) Drawing primitives for points, lines, circles, triangles, and polygons
    """

    def __init__(self, image):
        self.color = (0, 0, 0)  # default drawing color is black
        self.image = image
        w, h = image.size
        self.viewport = (0,0,w-1,h-1)

    def draw_point(self, loc):
        """draw point at loc"""
        pixloc = _pixloc(loc)
        if (self.viewport[0] <= pixloc.x < self.viewport[2]
            and self.viewport[1] <= pixloc.y < self.viewport[3]):
            self.image[pixloc] = self.color

    def draw_line(self, a, b):
        """  draw line segment from point a to point b """
        a, b = _pixloc(a), _pixloc(b)
        dx = b.x - a.x
        dy = b.y - a.y
        if abs(dx) >= abs(dy) and dx != 0:
            if a.x > b.x:
                a, b = b, a
            dx = b.x - a.x
            dy = b.y - a.y
            y = a.y
            yinc = (b.y-a.y)/(b.x-a.x)
            for x in range(a.x, b.x):
                self.draw_point((x,y))
                y = y+yinc
        if abs(dy) > abs(dx):
            if a.y > b.y:
                a, b = b, a
            dx = b.x - a.x
            dy = b.y - a.y
            x = a.x
            xinc = (b.x-a.x)/(b.y-a.y)
            for y in range(a.y, b.y):
                self.draw_point((x,y))
                x = x+xinc
        if abs(dy) == abs(dx) and dx == 0:
            # print("error: same point")
            pass
            ''' got erros while trying to do the dinosaur drawing because
                there were a few duplicate points next to eachother, which made
                dx and dy both 0, so I added this condition to skip those'''

    def draw_lines(self, points):
        """draw polyline that connects the given points"""
        curr = points[0]
        for p in points[1:]:
            self.draw_line(curr, p)
            curr = p

    def draw_polygon(self, vertices):
        """ draw polygon with given vertices """
        self.draw_lines(vertices)
        self.draw_line(vertices[-1], vertices[0])

    def draw_circle(self, center, radius, segments=50):
        """draw a cricle with the given center and radius 

        note: actually draws a regular polygon having segments sides
        """
        cx, cy = center
        dtheta = (2*pi)/segments
        theta = 0
        points = []
        while theta < 2*pi:
            x = radius*cos(theta) + cx
            y = radius*sin(theta) + cy
            points.append((x,y))
            theta += dtheta
        self.draw_polygon(points)

    def genlinefunc(self, p, p0, p1):
        x, y = p
        x0, y0 = p0
        x1, y1 = p1
        return ((y0-y1)*x + (x1-x0)*y + x0*y1-x1*y0)

    def draw_filled_triangle(self, a, b, c):
        """ draw filled triangle with vertices a, b, and c """
        a, b, c = _pixloc(a), _pixloc(b), _pixloc(c)
        xmin, xmax = min(a[0],b[0],c[0]), max(a[0],b[0],c[0])
        ymin, ymax = min(a[1],b[1],c[1]), max(a[1],b[1],c[1])
        for x in range(xmin, xmax+1):
            for y in range(ymin, ymax+1):
                alpha = (self.genlinefunc((x,y),b,c))/(self.genlinefunc(a,b,c))
                beta = (self.genlinefunc((x,y),a,c))/(self.genlinefunc(b,a,c))
                gamma = 1 - alpha - beta
                if alpha >= 0 and beta >= 0 and gamma >= 0:
                    self.draw_point((x,y))

    def draw_filled_polygon(self, vertices):
        """draw filled polygon with the given vertices

        note: vertices should describe a convex polygon
        """
        cx, cy, i = 0, 0, 0
        for i in range(len(vertices)):
            cx += vertices[i][0]
            cy += vertices[i][1]
            i += 1
        cx, cy = cx/i, cy/i
        for j in range(len(vertices)):
            self.draw_filled_triangle(vertices[j-1], (cx,cy), vertices[j])
            j += 1

    def draw_filled_circle(self, center, radius, segments=50):
        center = _pixloc(center)
        cx, cy = center
        xmin, xmax = (cx - radius), (cx + radius)
        ymin, ymax = (cy - radius), (cy + radius)
        for x in range(xmin, xmax+1):
            for y in range(ymin, ymax+1):
                if ((x-cx)**2 + (y-cy)**2 - radius**2) < 0:
                    self.draw_point((x,y))

        
if __name__ == "__main__":
    from image import Image
    img = Image((400, 300))
    img.clear((255, 255, 255))
    s = Painter(img)
    s.draw_point((100, 25))
    s.color = (255, 0, 0)
    s.draw_point((200.7, 295.3))
    s.draw_line((0.5, 0), (200, 30.4))
    s.draw_line((50.2, 100.6), (60, 250))
    s.draw_circle((200.4, 150.1), 100, 50)
    s.color = (0, 255, 0)
    s.draw_lines([(0, 0), (10.3, 30), (10, 50)])
    s.draw_polygon([(50, 50.1), (100, 50), (100, 100), (50, 100)])
    s.color = (255, 0, 0)
    s.draw_filled_triangle((150.3, 150), (230, 120.2), (200, 200))
    s.color = (128, 46, 243)
    s.draw_filled_circle((350.5, 75.2), 30)
    s.color = (86, 37, 28)
    s.draw_filled_polygon([(380, 225.25), (359, 254), (326, 243),
                           (326, 207), (359, 196)])
    
    img.save("painter_test.ppm")
    img.show()
