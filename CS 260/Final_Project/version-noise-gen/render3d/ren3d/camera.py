# camera.py
#    Implementation of simple camera for describing views

from math import tan, radians
from ren3d.math3d import Point, Vector
from ren3d.ray3d import Ray

from ren3d.trans3d import to_uvn as trans3d_to_uvn
from ren3d.matrix import unit as mat_unit


class Camera:
    """Camera is used to specify the view of the scene.
    >>> c = Camera()
    >>> c.set_perspective(60, 1.333, 20)
    >>> c.set_view(eye=(1, 2, 3), lookat=(0, 0, -10))
    >>> c.trans[0]
    [0.9970544855015816, 0.0, -0.07669649888473705, -0.7669649888473704]
    >>> c.trans[1]
    [-0.01162869315077414, 0.9884389178158018, -0.15117301096006383, -1.5117301096006381]
    >>> c.trans[2]
    [0.07580980435789034, 0.15161960871578067, 0.9855274566525744, -3.335631391747175]
    >>> c.trans[3]
    [0, 0, 0, 1]
    >>> c.set_resolution(400, 300)
    >>> r = c.ij_ray(0, 0)
    >>> r.start
    Point([1.0, 2.0, 3.0])
    >>> r.dir
    Vector([-12.900010270830052, -11.566123962675615, -17.521989305329008])
    >>> r = c.ij_ray(100, 200)
    >>> r.start
    Point([1.0, 2.0, 3.0])
    >>> r.dir
    Vector([-7.277823674777881, -0.14976036620738498, -19.7108288275589])
    """

    def __init__(self):
        self.eye = Point([0, 0, 0])
        self.window = -10.0, -10.0, 10.0, 10.0
        self.distance = 10
        self.dx, self.dy = 0, 0
        self.u, self.v, self.n = Vector([1, 0, 0]), Vector([0, 1, 0]), Vector([0, 0, 1])
        self.trans = mat_unit(4)

    def set_view(self, eye, lookat, up=(0, 1, 0)):
        self.eye = Point(eye)
        self.n = (self.eye - Point(lookat)).normalized()
        self.u = Vector(up).cross(self.n).normalized()
        self.v = self.n.cross(self.u).normalized()

        self.trans = trans3d_to_uvn(self.u, self.v, self.n, eye)

    def set_perspective(self, hfov, aspect, distance):
        """ Set up perspective view
        hfov is horizontal field of view (in degrees)
        aspect is the aspect ratio horizontal/vertical
        distance is distance from eye to focal plane.

        >>> c = Camera()
        >>> c.set_perspective(60, 1.333, 20)
        >>> c.eye
        Point([0.0, 0.0, 0.0])
        >>> c.distance
        20
        >>> c.window
        (-11.547005383792515, -8.662419642755076, 11.547005383792515, 8.662419642755076)
        """
        self.distance = distance
        half_width = tan(radians(hfov)/2) * distance
        self.window = -half_width, -half_width/aspect, half_width, half_width/aspect

    # ------------------------------------------------------------
    # These methods used for ray tracing

    def set_resolution(self, width, height):
        """ Set resolution of pixel sampling across the window."""
        self.dx = (self.window[2] - self.window[0]) / width
        self.dy = (self.window[3] - self.window[1]) / height

    def ij_ray(self, i, j):
        """ return the ray from the eye through the ijth pixel.

        >>> c = Camera()
        >>> c.set_resolution(400, 300)
        >>> c.ij_ray(-0.5, -0.5)
        Ray(Point([0.0, 0.0, 0.0]), Vector([-10.0, -10.0, -10.0]))
        >>> c.ij_ray(399.5, 299.5)
        Ray(Point([0.0, 0.0, 0.0]), Vector([10.0, 10.0, -10.0]))
        >>> c.ij_ray(0, 0)
        Ray(Point([0.0, 0.0, 0.0]), Vector([-9.975, -9.966666666666667, -10.0]))
        >>> c.ij_ray(399/2, 299/2)
        Ray(Point([0.0, 0.0, 0.0]), Vector([0.0, 0.0, -10.0]))
        """
        x = (self.window[0] + self.dx * (.5 + i)) * self.u
        y = (self.window[1] + self.dy*(.5+j)) * self.v
        z = -self.distance * self.n

        return Ray(self.eye, x+y+z)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
