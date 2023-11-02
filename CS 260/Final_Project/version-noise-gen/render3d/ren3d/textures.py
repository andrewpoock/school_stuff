# texture.py
#  simple implementation of texture mapping.

from math import atan2, tau, pi, asin

from ren3d.image import Image
from ren3d.rgb import RGB


def _pixrgb(img, loc):
    return RGB([v/255 for v in img[loc]])


def lerp(v, low0, high0, low1, high1):
    return low1 + (v-low0)*(high1-low1)/(high0-low0)


class Boxtexture:

    def __init__(self, imagefile):
        self.image = Image(imagefile)

    def __call__(self, uvn):
        # skip largest value (mapping to nearest plane)
        coords = list(uvn)
        coords.remove(max(uvn, key=abs))
        u, v = coords
        w, h = self.image.size
        # div 2 could be      (u+1)>>1                (v+1)>>1
        pixel = round((w-1) * (u+1)/2), round((h-1) * (v+1)/2)
        # print("texture pixel", uvn, u, v, pixel)
        return _pixrgb(self.image, pixel)


class Spheretexture:

    def __init__(self, imagefile):
        self.image = Image(imagefile)

    def __call__(self, uvn):
        x, y, z = uvn
        w, h = self.image.size
        phi = atan2(-z, x) if z > 0 else atan2(-z, x)  # + tau  # <-- put this back
        theta = asin(y)
        px = lerp(phi, 0, tau, 0, w-1)
        py = lerp(theta, -pi / 2, pi / 2, 0, h - 1)
        return _pixrgb(self.image, (round(px), round(py)))
