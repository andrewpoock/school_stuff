
from ren3d.image import Image
from time import sleep


if __name__ == "__main__":
    im = Image("textures/grass.ppm")
    # im.save("textures/grass2.ppm")
    for x in range(512):
        for y in range(5):
            im[(x, y)] = (0, 0, 0)
            im[(x, 512-y)] = (0, 0, 0)

    for y in range(512):
        for x in range(5):
            im[(x, y)] = (0, 0, 0)
            im[(512-x, y)] = (0, 0, 0)
    im.save("textures/grass2.ppm")
    im.show()
