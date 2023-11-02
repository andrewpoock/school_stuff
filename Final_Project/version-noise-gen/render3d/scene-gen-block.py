# scene-gen-block.py

from ren3d.scenedef import *
from perlin_noise import PerlinNoise

noise_gen = PerlinNoise(octaves=.1, seed=69)

def add_house():
    # house
    scene.add(Box(pos=(4, 4, -4), size=(5, 1, 5), color=(0.5, 0.5, 0.5))) # Stone Base

    scene.add(Box(pos=(2, 6, -2), size=(1, 3, 1), color=(0.5,0.5,0.5))) # Stone Pillars
    scene.add(Box(pos=(6, 6, -2), size=(1, 3, 1), color=(0.5,0.5,0.5)))
    scene.add(Box(pos=(2, 6, -6), size=(1, 3, 1), color=(0.5,0.5,0.5)))
    scene.add(Box(pos=(6, 6, -6), size=(1, 3, 1), color=(0.5,0.5,0.5)))

    scene.add(Box(pos=(4, 8, -4), size=(5, 1, 5), color=(0.23, 0.15, 0.05))) # Log Top

    scene.add(Box(pos=(5, 6,-2), size=(1,4,1), color=(0.7,0.54,0.32))) # Front Door
    scene.add(Box(pos=(3, 6,-2), size=(1,4,1), color=(0.7,0.54,0.32)))
    scene.add(Box(pos=(4, 7,-2), size=(1,1,1), color=(0.7,0.54,0.32)))

    scene.add(Box(pos=(5, 6, -6), size=(1,4,1), color=(0.7,0.54,0.32))) # Back Window
    scene.add(Box(pos=(3, 6, -6), size=(1,4,1), color=(0.7,0.54,0.32)))
    scene.add(Box(pos=(4, 7,-6), size=(1,1,1), color=(0.7,0.54,0.32)))
    scene.add(Box(pos=(4, 5,-6), size=(1,1,1), color=(0.7,0.54,0.32)))

    scene.add(Box(pos=(2, 6, -3), size=(1, 4, 1), color=(0.7,0.54,0.32))) # Left Wall
    scene.add(Box(pos=(2, 6, -5), size=(1, 4, 1), color=(0.7,0.54,0.32)))
    scene.add(Box(pos=(2, 7,-4), size=(1,1,1), color=(0.7,0.54,0.32)))
    scene.add(Box(pos=(2, 5,-4), size=(1,1,1), color=(0.7,0.54,0.32)))

    scene.add(Box(pos=(6, 6, -3), size=(1, 4, 1), color=(0.7,0.54,0.32))) # Right Wall
    scene.add(Box(pos=(6, 6, -5), size=(1, 4, 1), color=(0.7,0.54,0.32)))
    scene.add(Box(pos=(6, 7,-4), size=(1,1,1), color=(0.7,0.54,0.32)))
    scene.add(Box(pos=(6, 5,-4), size=(1,1,1), color=(0.7,0.54,0.32)))

    scene.add(Box(pos=(4, 3.75, -1), size=(1, 0.5, 1), color=(0.5, 0.5, 0.5))) # Stone Steps
    scene.add(Box(pos=(4, 4.25, -1.25), size=(1, 0.5, 0.5), color=(0.5, 0.5, 0.5)))

def add_tree():
    scene.add(Box(pos=(-6, 5, -1), size=(1, 4, 1), color=(0.23, 0.15, 0.05))) # Log
    scene.add(Box(pos=(-6, 8, -1), size=(5, 2, 5), color=(0.13,0.54,0.13))) # Leaves
    scene.add(Box(pos=(-6, 10, -1), size=(1, 2, 1), color=(0.13,0.54,0.13)))
    scene.add(Box(pos=(-7, 10, -1), size=(1, 2, 1), color=(0.13,0.54,0.13)))
    scene.add(Box(pos=(-5, 10, -1), size=(1, 2, 1), color=(0.13,0.54,0.13))) 
    scene.add(Box(pos=(-6, 10, 0), size=(1, 2, 1), color=(0.13,0.54,0.13))) 
    scene.add(Box(pos=(-6, 10, -2), size=(1, 2, 1), color=(0.13,0.54,0.13)))

def gen_block(x, z, noise):
    y = round(noise([x, z]) * 10)
    return Box(pos=(x, y, z), texture=Boxtexture("textures/grass2.ppm"))


for i in range(-30, 30):
    for j in range(-30, 30):
        block = gen_block(i, j, noise_gen)
        scene.add(block)
        
add_house()
add_tree()

scene.background = (1, 1, 1)
scene.ambient = (.5, .5, .5)
scene.textures = True
# scene.shadows = True
scene.set_light(pos=(0, 50, -10))
camera.set_view(eye=(0, 8, 18), lookat=(0, 0, -15))
camera.set_perspective(60, 1.33, 5)
