# scenedef.py
#    A scene is a collection of modeling elements.
#    This file is the basic "header" needed to define scenes

from ren3d.math3d import Point
from ren3d.rgb import RGB
from ren3d.models import Sphere, Group, Box
from ren3d.camera import Camera


# ----------------------------------------------------------------------
class Scene:

    def __init__(self):
        self.camera = Camera()
        self.objects = Group()
        self.background = (0, 0, 0)
        self.light = Point((0,0,0))

    def add(self, object):
        self.objects.add(object)

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, color):
        self._background = RGB(color)

    def set_light(self, pos=(0,0,0)):
        self.light = Point(pos)

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
