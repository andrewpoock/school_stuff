# scenedef.py
#    A scene is a collection of modeling elements.
#    This file is the basic "header" needed to define scenes


from ren3d.models import Sphere, Box, Square, Transformable, Group
from ren3d.mesh import Triangle, Mesh
from ren3d.camera import Camera
from ren3d.math3d import Point
from ren3d.materials import *
from ren3d.textures import *
from ren3d.bvh import make_BVH


# ----------------------------------------------------------------------
class Scene:

    def __init__(self):
        self.camera = Camera()
        self.objects = []
        self.background = RGB((0, 0, 0))
        self.ambient = .1, .1, .1
        self.shadows = False
        self.textures = False
        self.reflections = 0
        self.lights = [(self.camera.eye, RGB((1, 1, 1)))]
        self._surface = None

    def add(self, obj):
        self.objects.append(obj)
        self._surface = None

    def add_light(self, pos=(0, 0, 0), color=(1, 1, 1)):
        self.lights.append((Point(pos), RGB(color)))

    def set_light(self, pos=(0, 0, 0), color=(1, 1, 1)):
        self.lights[-1] = (Point(pos), RGB(color))

    @property
    def light(self):
        return self.lights[-1]

    @property
    def surface(self):
        if self._surface is None:
            self._surface = make_BVH(self.objects)
        return self._surface

    @property
    def ambient(self):
        return self._ambient

    @ambient.setter
    def ambient(self, color):
        if type(color) == float:
            color = [color] * 3
        self._ambient = RGB(color)

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, color):
        self._background = RGB(color)

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
