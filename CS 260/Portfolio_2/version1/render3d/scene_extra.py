# scene_extra.py
# Andrew Poock
# a person

from random import random
from ren3d.scenedef import *

camera.set_perspective(30, 1.3333, 5)
scene.background = (0, .8, .8)
# torso
scene.add(Box(pos=(0, 0, -20), size=(1.5, 3, 2), color=(1, .8, .6)))
# head
scene.add(Sphere(pos=(0, 2.5, -20), radius=1, color=(1, .8, .6)))
# legs
scene.add(Box(pos=(-.8, -2.5, -20), size=(.5, 2, 2), color=(1, .8, .6)))
scene.add(Box(pos=(.8, -2.5, -20), size=(.5, 2, 2), color=(1, .8, .6)))
# arms
scene.add(Box(pos=(-1.5, 2.25, -20), size=(.5, 2, 2), color=(1, .8, .6)))
scene.add(Box(pos=(1.5, 2.25, -20), size=(.5, 2, 2), color=(1, .8, .6)))
# shoulders
scene.add(Box(pos=(1, 1.25, -20), size=(1, .5, 2), color=(1, .8, .6)))
scene.add(Box(pos=(-1, 1.25, -20), size=(1, .5, 2), color=(1, .8, .6)))
# eyes
scene.add(Sphere(pos=(-.25, 2.75, -19), radius=.25, color=(0, 0, 0)))
scene.add(Sphere(pos=(.25, 2.75, -19), radius=.25, color=(0, 0, 0)))
# mouth
scene.add(Sphere(pos=(-.2, 2, -19), radius=.3, color=(255, 255, 255)))
