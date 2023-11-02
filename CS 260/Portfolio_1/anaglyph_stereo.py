# anaglyph_stereo.py
# Andrew Poock

import sys

from image import Image


def anaglyph_stereo(img, img2, animate=False):
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r1, g1, b1 = img[x, y]
            r2, g2, b2 = img2[x, y]
            l1 = .229*r1 + .589*g1 + .114*b1
            l2 = .229*r2 + .589*g2 + .114*b2
            img[x, y] = (round(l1), 0, round(l2))
        if animate:
            img.show()


def main():

    if len(sys.argv) != 4:
        print("Usage: python sunset.py leftppm rightppm newppm")
        sys.exit()

    in_image = sys.argv[1]
    in_image2 = sys.argv[2]
    out_image = sys.argv[3]

    im = Image(in_image)
    im2 = Image(in_image2)
    anaglyph_stereo(im, im2, False)
    im.save(out_image)


if __name__ == "__main__":
    main()
