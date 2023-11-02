# scene_extra.py
# Andrew Poock
# a smiley

from random import random
from ren3d.scenedef import *

camera.set_perspective(30, 1.3333, 5)
scene.background = (1, .2, .6)

# eyes
scene.add(Sphere(pos=(-2, 2.5, -20), radius=1, color=(random(), random(), random())))
scene.add(Sphere(pos=(2, 2.5, -20), radius=1, color=(random(), random(), random())))
# smile
scene.add(Box(pos=(-.5, -2, -20), size=(1, 1, 2), color=(random(), random(), random())))
scene.add(Box(pos=(.5, -2, -20), size=(1, 1, 2), color=(random(), random(), random())))
scene.add(Box(pos=(-1.5, -1.75, -20), size=(1, 1, 2), color=(random(), random(), random())))
scene.add(Box(pos=(1.5, -1.75, -20), size=(1, 1, 2), color=(random(), random(), random())))
scene.add(Box(pos=(-2.5, -1.25, -20), size=(1, 1, 2), color=(random(), random(), random())))
scene.add(Box(pos=(2.5, -1.25, -20), size=(1, 1, 2), color=(random(), random(), random())))
