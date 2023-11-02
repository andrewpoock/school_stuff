# models.py
#   Objects used for constructing scenes

from math import sin, cos, pi, sqrt, tau
from ren3d.math3d import Point, Vector
from ren3d.materials import make_material
from ren3d.textures import lerp
from ren3d.bbox import BoundingBox
import ren3d.matrix as matrix
import ren3d.trans3d as trans3d


# Surfaces for Scene Modeling
# ----------------------------------------------------------------------


def _circ2d(c, r, n):
    """ generates points of a cirlce given its center, radius, and """
    x, y = c
    dtheta = tau / n
    points = [(r * cos(i * dtheta) + x, r * sin(i * dtheta) + y) for i in range(n)]
    points.append(points[0])
    return points


class Sphere:
    """ Model of a sphere shape"""

    def __init__(self, pos=(0, 0, 0), radius=1,
                 color=(0, 1, 0), nlat=20, nlong=20, texture=None):
        """ create a sphere
        """
        self.pos = Point(pos)
        self.radius = radius
        self.color = make_material(color)
        self.nlat = nlat
        self.nlong = nlong
        self.bands = []
        self._make_bands(nlat, nlong)
        axis = Vector((0, radius, 0))
        self.northpole = self.pos + axis
        self.southpole = self.pos - axis
        self.texture = texture
        # dont check bounding box here
        self.bbox = BoundingBox((self.pos[i] - radius for i in range(3)), (self.pos[i] + radius for i in range(3)))

    def _make_bands(self, nlat, nlong):
        """helper method that creates a list of "bands"

        each band consists of a list of points encircling the sphere
        at a latitude. There are nlat evenly (angularly) spaced
        bands each with nlong points evenly spaced around the band.
        """
        cx, cy, cz = self.pos
        theta = pi/2
        dtheta = pi / (nlat+1)
        for _ in range(nlat):
            theta += dtheta
            r = self.radius * cos(theta)
            y = self.radius * sin(theta) + cy
            self.bands.append([Point((x, y, z)) for x, z in _circ2d((cx, cz), r, nlong)])

    def iter_polygons(self):
        """produces a sequence of polygons on the skin of the sphere.

        Each polygon is a Record with fields "points" (a list of points)
        color (the color of the triangle).
        normal (surface normals of the "points")
        """

        for i in range(self.nlong):
            points = [self.northpole, self.bands[0][i], self.bands[0][i+1]]
            yield Record(points=points, color=self.color, normal=[(p - self.pos).normalized() for p in points])

        for i in range(self.nlat-1):
            b0 = self.bands[i]
            b1 = self.bands[i+1]
            for j in range(self.nlong):
                points = [b0[j], b1[j], b1[j+1], b0[j+1]]
                yield Record(points=points, color=self.color, normal=[(p - self.pos).normalized() for p in points])

        for i in range(self.nlong):
            points = [self.southpole, self.bands[-1][i], self.bands[-1][i+1]]
            yield Record(points=points, color=self.color, normal=[(p - self.pos).normalized() for p in points])

    def compute_generic(self, p):
        """ compute generic texture locations of point p"""
        return [lerp(p[i], self.pos[i]-self.radius, self.pos[i]+self.radius, -1, 1) for i in range(3)]

    def intersect(self, ray, interval, info):
        """ returns a True iff ray intersects the sphere within the

        given time interval. The approriate intersection information
        is recorded into info, which is a Record containing:
          point: the point of intersection
          t: the time of the intersection
          normal: the surface normal at the point
          color: the color at the point.
        """
        a = ray.dir.mag2()
        if a == 0:
            return False
        rp_vec = ray.start - self.pos
        b = 2 * ray.dir.dot(rp_vec)
        c = rp_vec.mag2() - self.radius * self.radius
        discrim = b*b - 4*a*c
        if discrim < 0:
            return False
        t1 = (-b - sqrt(discrim)) / (2*a)
        if t1 in interval:
            self._setinfo(ray, t1, info)
            return True
        t2 = (-b + sqrt(discrim)) / (2*a)
        if t2 in interval:
            self._setinfo(ray, t2, info)
            return True
        return False

    def _setinfo(self, ray, t, info):
        """ helper method to fill in the info record """
        info.update(t=t, point=ray.point_at(t), color=self.color, texture=self.texture)
        info.uvn = self.compute_generic(info.point)
        info.normal = (info.point - self.pos).normalized()


class Box:

    def __init__(self, pos=(0, 0, 0), size=(1, 1, 1), color=(1, 0, 0), texture=None):
        self.pos = Point(pos)
        self.size = Vector(size)
        self.color = make_material(color)
        self.planes = self._make_vertices()
        self.texture = texture
        # bbox doesn't provide speedup in box class
        self.bbox = BoundingBox([self.planes[a][0] for a in range(3)], [self.planes[a][1] for a in range(3)])

    def __repr__(self):
        return f"{tuple(self.pos)}"

    def _make_vertices(self):
        """ makes the vertices requried for the box corners """
        sx, sy, sz = self.size * 0.5
        cx, cy, cz = self.pos
        planes = [(cx - sx, cx + sx), (cy - sy, cy + sy), (cz - sz, cz + sz)]  # -z is closer
        return planes

    def iter_polygons(self):
        """ returns the polygons that make up the skin of a box """
        x_p, y_p, z_p = self.planes
        # front, back, left, right, top, bot
        yield Record(points=[Point((x_p[0], y_p[0], z_p[1])), Point((x_p[1], y_p[0], z_p[1])),
                             Point((x_p[1], y_p[1], z_p[1])), Point((x_p[0], y_p[1], z_p[1]))], color=self.color,
                     normal=[Vector((0, 0, 1)) for _ in range(4)])
        yield Record(points=[Point((x_p[0], y_p[0], z_p[0])), Point((x_p[1], y_p[0], z_p[0])),
                             Point((x_p[1], y_p[1], z_p[0])), Point((x_p[0], y_p[1], z_p[0]))], color=self.color,
                     normal=[Vector((0, 0, -1)) for _ in range(4)])
        yield Record(points=[Point((x_p[0], y_p[0], z_p[1])), Point((x_p[0], y_p[0], z_p[0])),
                             Point((x_p[0], y_p[1], z_p[0])), Point((x_p[0], y_p[1], z_p[1]))], color=self.color,
                     normal=[Vector((-1, 0, 0)) for _ in range(4)])
        yield Record(points=[Point((x_p[1], y_p[0], z_p[1])), Point((x_p[1], y_p[0], z_p[0])),
                             Point((x_p[1], y_p[1], z_p[0])), Point((x_p[1], y_p[1], z_p[1]))], color=self.color,
                     normal=[Vector((1, 0, 0)) for _ in range(4)])
        yield Record(points=[Point((x_p[0], y_p[1], z_p[1])), Point((x_p[1], y_p[1], z_p[1])),
                             Point((x_p[1], y_p[1], z_p[0])), Point((x_p[0], y_p[1], z_p[0]))], color=self.color,
                     normal=[Vector((0, 1, 0)) for _ in range(4)])
        yield Record(points=[Point((x_p[0], y_p[0], z_p[1])), Point((x_p[1], y_p[0], z_p[1])),
                             Point((x_p[1], y_p[0], z_p[0])), Point((x_p[0], y_p[0], z_p[0]))], color=self.color,
                     normal=[Vector((0, -1, 0)) for _ in range(4)])

    def compute_generic(self, p):
        """ compute generic coords for point p"""
        return [lerp(p[i], self.planes[i][0], self.planes[i][1], -1, 1) for i in range(3)]

    def intersect(self, ray, interval, info):
        """ returns a True iff ray intersects the box within the

        given time interval. The approriate intersection information
        is recorded into info, which is a Record containing:
          point: the point of intersection
          t: the time of the intersection
          normal: the surface normal at the point
          color: the color at the point.
        """
        # there are 6 "planes" to check
        hit = False
        for a in range(len(self.planes)):
            if ray.dir[a] == 0:
                continue
            for lh in range(2):
                t = (self.planes[a][lh] - ray.start[a]) / ray.dir[a]
                if t not in interval:
                    continue
                if self._in_rect(ray.point_at(t), a):
                    hit = True
                    interval.high = t
                    info.update(t=t, point=ray.point_at(t), color=self.color, texture=self.texture)
                    info.uvn = self.compute_generic(info.point)
                    info.normal = Vector((0, 0, 0))
                    info.normal[a] = -1.0 if lh == 0 else 1.0
        return hit

    def _in_rect(self, p, axis):
        for a in range(len(self.planes)):
            if a == axis:
                continue
            low, high = self.planes[a]
            if not low <= p[a] <= high:
                return False
        return True


class Square(Box):

    def __init__(self, color=(0, 1, 0)):
        super().__init__(color=color)


class Transformable:
    """ A wrapper to add transforms to surfaces"""

    def __init__(self, model):
        self.model = model
        self.trans = matrix.unit(4)
        self.itrans = matrix.unit(4)
        self.ntrans = matrix.unit(4)
        self.bbox = model.bbox

    def iter_polygons(self):
        for poly in self.model.iter_polygons():
            for i, p in enumerate(poly.points):
                poly.points[i] = p.trans(self.trans)
                poly.normal[i] = poly.normal[i].trans(self.ntrans)
            yield poly

    def intersect(self, ray, interval, info):
        if not self.bbox.hit(ray, interval):
            return False

        if self.model.intersect(ray.trans(self.itrans), interval, info):
            info.point = info.point.trans(self.trans)  # test ray.point_at(t) that would be way faster than mat.apply
            info.normal = info.normal.trans(self.ntrans).normalized()
            return True
        return False

    def _update(self, trans, itrans):
        self.trans = matrix.mul(trans, self.trans)
        self.itrans = matrix.mul(self.itrans, itrans)
        self.ntrans = matrix.transpose(self.itrans)
        self.bbox = self.model.bbox.transform(self.trans)
        return self

    def scale(self, sx, sy, sz):
        return self._update(trans3d.scale(sx, sy, sz), trans3d.scale(1/sx, 1/sy, 1/sz))

    def translate(self, dx, dy, dz):
        return self._update(trans3d.translate(dx, dy, dz), trans3d.translate(-dx, -dy, -dz))

    def rotate_x(self, angle):
        return self._update(trans3d.rotate_x(angle), trans3d.rotate_x(-angle))

    def rotate_y(self, angle):
        return self._update(trans3d.rotate_y(angle), trans3d.rotate_y(-angle))

    def rotate_z(self, angle):
        return self._update(trans3d.rotate_z(angle), trans3d.rotate_z(-angle))


class Group:
    """ Model comprised of a group of other models.
    The contained models may be primitives (such as Sphere) or other groups.
    """

    def __init__(self):
        self.objects = []
        self.bbox = BoundingBox()

    def add(self, model):
        """ Add model to the group """
        self.objects.append(model)
        self.bbox.include_box(model.bbox)

    def iter_polygons(self):
        """ Produce all polygons in the group"""
        for obj in self.objects:
            for rec in obj.iter_polygons():
                yield rec

    def intersect(self, ray, interval, info):
        """Returns True iff ray intersects some object in the group

        If so, info is the record of the first (in time) object hit, and
        interval.max is set to the time of the first hit.
        """
        if not self.bbox.hit(ray, interval):
            return False
        hit = False
        for obj in self.objects:
            if obj.intersect(ray, interval, info):
                hit = True
                interval.high = info.t
        return hit


# ----------------------------------------------------------------------
class Record:
    """ conveience for bundling a bunch of info together. Basically
    a dictionary that can use dot notatation

    >>> info = Record()
    >>> info.point = Point([1,2,3])
    >>> info
    Record(point=Point([1.0, 2.0, 3.0]))
    >>> info.t = 3.245
    >>> info
    Record(point=Point([1.0, 2.0, 3.0]), t=3.245)
    >>> info.update(point=Point([-1,0,0]), t=5)
    >>> info.t
    5
    >>> info
    Record(point=Point([-1.0, 0.0, 0.0]), t=5)
    >>> info2 = Record(whatever=53, whereever="Iowa")
    >>> info2.whereever
    'Iowa'
    """

    def __init__(self, **items):
        self.__dict__.update(items)

    def update(self, **items):
        self.__dict__.update(**items)

    def __repr__(self):
        d = self.__dict__
        fields = [k+"="+str(d[k]) for k in sorted(d)]
        return "Record({})".format(", ".join(fields))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
