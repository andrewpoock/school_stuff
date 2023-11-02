# scenedef.py
#    A scene is a collection of modeling elements.
#    This file is the basic "header" needed to define scenes
# by: John Zelle

from materials import *
from ren3d.rgb import RGB
from ren3d.models import Box, Sphere, Group
from ren3d.camera import Camera
from ren3d.math3d import Point
from ren3d.textures import *
import ren3d.trans3d as trans3d
import ren3d.matrix as mat
from ren3d.ray3d import Ray
from ren3d.bvh import make_BVH
from ren3d.bbox import BoundingBox
from ren3d.mesh import Mesh


# ----------------------------------------------------------------------
class Scene:

    def __init__(self):
        self.camera = Camera()
        self.objects = []
        self.background = (0, 0, 0)
        self.ambient = (.1, .1, .1)
        self.lights = [(Point((0,0,0)), RGB((1, 1, 1)))]
        self.shadows = False
        self.reflections = 0
        self.textures = False
        self._surface = None

    def add(self, obj):
        self.objects.append(obj)
        self._surface = None

    @property
    def surface(self):
        if self._surface is None:
            self._surface = make_BVH(self.objects)
        return self._surface

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, color):
        self._background = RGB(color)

    @property
    def ambient(self):
        return self._ambient

    @ambient.setter
    def ambient(self, color):
        if type(color) == float:
            color = [color] * 3
        self._ambient = RGB(color)

    @property
    def light(self):
        return self.lights[-1]

    def set_light(self, pos=(0,0,0), color=(1, 1, 1)):
        self.lights[-1] = (Point(pos), RGB(color))

    def add_light(self, pos=(0,0,0), color=(1,1,1)):
        self.lights.append((Point(pos), RGB(color)))

class Transformable:

    # A wrapper to add transforms to surfaces
    '''
    >>> s = Transformable(Sphere(color=(0, 0, 0)))
    >>> x = s.scale(2, 3, 4).rotate_y(30).translate(5, -3, 8)
    >>> s.trans[0]
    [1.7320508075688774, 0.0, 1.9999999999999998, 5.0]
    >>> s.trans[1]
    [0.0, 3.0, 0.0, -3.0]
    >>> s.trans[2]
    [-0.9999999999999999, 0.0, 3.464101615137755, 8.0]
    >>> s.trans[3]
    [0.0, 0.0, 0.0, 1.0]
    >>> s.itrans[0]
    [0.43301270189221935, 0.0, -0.24999999999999997, -0.16506350946109705]
    >>> s.itrans[1]
    [0.0, 0.3333333333333333, 0.0, 1.0]
    >>> s.itrans[2]
    [0.12499999999999999, 0.0, 0.21650635094610968, -2.357050807568877]
    >>> s.itrans[3]
    [0.0, 0.0, 0.0, 1.0]
    >>> s.ntrans[0]
    [0.43301270189221935, 0.0, 0.12499999999999999, 0.0]
    >>> s.ntrans[1]
    [0.0, 0.3333333333333333, 0.0, 0.0]
    >>> s.ntrans[2]
    [-0.24999999999999997, 0.0, 0.21650635094610968, 0.0]
    >>> s.ntrans[3]
    [-0.16506350946109705, 1.0, -2.357050807568877, 1.0]
    >>>
    '''
	
    def __init__(self, surface):
        self.surface = surface
        self.trans = mat.unit(4)
        self.itrans = mat.unit(4)
        self.ntrans = mat.unit(4)
        self.bbox = surface.bbox

    def scale(self, sx, sy, sz):
        trans = trans3d.scale(sx, sy, sz)
        self.trans = mat.mul(trans, self.trans)
        itrans = trans3d.scale(1/sx, 1/sy, 1/sz)
        self.itrans = mat.mul(self.itrans, itrans)
        self.ntrans = mat.transpose(self.itrans)
        self.bbox = self.surface.bbox.transform(self.trans)
        return self

    def translate(self, dx, dy, dz):
        trans = trans3d.translate(dx, dy, dz)
        self.trans = mat.mul(trans, self.trans)
        itrans = trans3d.translate(-dx, -dy, -dz)
        self.itrans = mat.mul(self.itrans, itrans)
        self.ntrans = mat.transpose(self.itrans)
        self.bbox = self.surface.bbox.transform(self.trans)
        return self

    def rotate_x(self, angle):
        trans = trans3d.rotate_x(angle)
        self.trans = mat.mul(trans, self.trans)
        itrans = trans3d.rotate_x(-angle)
        self.itrans = mat.mul(self.itrans, itrans)
        self.ntrans = mat.transpose(self.itrans)
        self.bbox = self.surface.bbox.transform(self.trans)
        return self

    def rotate_y(self, angle):
        trans = trans3d.rotate_y(angle)
        self.trans = mat.mul(trans, self.trans)
        itrans = trans3d.rotate_y(-angle)
        self.itrans = mat.mul(self.itrans, itrans)
        self.ntrans = mat.transpose(self.itrans)
        self.bbox = self.surface.bbox.transform(self.trans)
        return self

    def rotate_z(self, angle):
        trans = trans3d.rotate_z(angle)
        self.trans = mat.mul(trans, self.trans)
        itrans = trans3d.rotate_z(-angle)
        self.itrans = mat.mul(self.itrans, itrans)
        self.ntrans = mat.transpose(self.itrans)
        self.bbox = self.surface.bbox.transform(self.trans)
        return self

    def iter_polygons(self):
        for poly in self.surface.iter_polygons():
            newpts = []
            for i, pt in enumerate(poly.points):
                poly.points[i] = pt.trans(self.trans)
            yield poly

    def intersect(self, ray, interval, info):
        tray = ray.trans(self.itrans)
        if self.surface.intersect(tray, interval, info):
            info.point = info.point.trans(self.trans)
            info.normal = info.normal.trans(self.ntrans).normalized()
            return True
        return False

# ----------------------------------------------------------------------
# global scene
#   for files that define a scene use: from scenedef import *


scene = Scene()
camera = scene.camera

# ----------------------------------------------------------------------
# use this function to load scene modules for rendering


def load_scene(modname):
    if modname.endswith(".py"):
        modname = modname[:-3]
    scene = __import__(modname).scene
    return scene, modname

if __name__ == "__main__":
    import doctest
    doctest.testmod()
