# render_oo.py

"""FrameBuffer that keeps the z coordinates of points to implement a
depth buffer for hidden surface removal.

"""


from math import inf as math_inf

from collections import namedtuple, defaultdict
import ren3d.matrix as mat


def render_wireframe(scene, img):
    """
    Render wireframe view of scene into img
    """
    # put your render_wireframe here and tweak it to use the new FB
    img.clear(scene.background.quantize(255))
    fb = FrameBuffer(img, scene.camera.window)
    d = -scene.camera.distance
    for poly in scene.surface.iter_polygons():
        points = [p.trans(scene.camera.trans) for p in poly.points]
        points = [(d * (p.x / p.z), d * (p.y / p.z), p.z) for p in points]

        fb.draw_polygon(points, poly.color.diffuse)


# ---------------------------------------------------------------------------
# Helper class
pixloc = namedtuple("pixloc", "x y z")


class FrameBuffer:
    """ Wrapper for images to provide a window mapping and drawing primitives.
    This is a stripped down combination of elements from our Painter
    and Render2d projects

    This version is updated to keep the z component of the points to use for 
    depth buffering.
    """

    def __init__(self, img, window):
        self.img = img
        self.size = img.size
        # viewport dimensions are 1 unit larger than pixel dimensions
        w, h = self.size[0] + 1, self.size[1] + 1
        l, b, r, t = window
        self.transform = [[w/(r-l), 0.0, 0.0, (-.5*r-(w-.5)*l)/(r-l)],
                          [0.0, h/(t-b), 0.0, (-.5*t-(h-.5)*b)/(t-b)],
                          [0.0, 0.0, 1.0, 0.0],
                          [0.0, 0.0, 0.0, 1.0]]

        self._depth_buff = defaultdict(lambda: -math_inf)

    def transpt(self, point):
        # Transform point from window (world) coordinates to pixel coordinates
        # x and y are ints, z is a float indicating depth
        x, y, z, _ = mat.apply(self.transform, point+(1,))
        return pixloc(int(x + .5), int(y + .5), z)

    def depth_buff(self, x, y, z=None):
        if z:
            self._depth_buff[(x, y)] = z
            return
        return self._depth_buff[(x, y)]

    def set_pixel(self, loc, z, color):
        w, h = self.size
        if 0 <= loc[0] < w and 0 <= loc[1] < h and z > self.depth_buff(loc[0], loc[1]):
            self.img[loc] = color.quantize(255)
            self.depth_buff(loc[0], loc[1], z)

    def draw_line(self, a, b, rgb):
        # pre: a and b are pixel locations (int, int, float)
        if a[:2] == b[:2]:   # handle degenerate case same pixel location
            self.set_pixel(a[:2], a.z, rgb)
            return
        # Otherwise, handle the general case
        dx = b.x - a.x
        dy = b.y - a.y
        dz = b.z - a.z 
        if abs(dx) > abs(dy):  # x changes faster, walk it
            if a.x > b.x:
                a, b = b, a
            yinc = dy/dx
            y = a.y
            zinc = dz/dx
            z = a.z
            for x in range(a.x, b.x + 1):
                self.set_pixel((x, round(y)), z, rgb)
                y += yinc
                z += zinc
        else:
            if a.y > b.y:
                a, b = b, a
            xinc = dx/dy
            x = a.x
            zinc = dz/dy
            z = a.z
            for y in range(a.y, b.y + 1):
                self.set_pixel((round(x), y), z, rgb)
                x += xinc
                z += zinc

    def draw_polygon(self, points, color):
        # points are 3D window points (tuple of floats)
        pixels = [self.transpt(p) for p in points]
        for i in range(len(pixels) - 1):
            self.draw_line(pixels[i], pixels[i+1], color)
        self.draw_line(pixels[-1], pixels[0], color)
