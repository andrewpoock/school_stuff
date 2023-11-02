# image_processing.py
# Andrew Poock

import sys

from image import Image


def color_negative(img, animate=False):
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b = img[x, y]
            img[x, y] = (255-r, 255-g, 255-b)
        if animate:
            img.show()

def greyscale(img, animate=False):
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b = img[x, y]
            l = .229*r + .589*g + .114*b
            img[x, y] = (round(l), round(l), round(l))
        if animate:
            img.show()
    
def sepia_tint(img, animate=False):
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b = img[x, y]
            newr = .393*r + .769*g + .189*b
            newg = .349*r + .686*g + .168*b
            newb = .272*r + .534*g + .131*b
            if newr > 255:
                newr = 255
            if newg > 255:
                newg = 255
            if newr > 255:
                newb = 255
            img[x, y] = (round(newr), round(newg), round(newb))
        if animate:
            img.show()

def blue_light_filter(img, animate=False):
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b = img[x, y]
            img[x, y] = (r, g, round(.25*b))
        if animate:
            img.show()

def main():

    print("Usage: python image_processing.py oldppm newppm filter")
    print("for filter use keywords negative, grey, sepia, or blue")
    if len(sys.argv) != 4:
        print("Usage: python image_processing.py oldppm newppm filter")
        print("for filter use negative, grey, sepia, or blue")
        sys.exit()

    in_image = sys.argv[1]
    out_image = sys.argv[2]
    method = sys.argv[3]
    
    if method == 'negative':
        im = Image(in_image)
        color_negative(im, False)
        im.save(out_image)
    if method == 'grey':
        im = Image(in_image)
        greyscale(im, False)
        im.save(out_image)
    if method == 'sepia':
        im = Image(in_image)
        sepia_tint(im, False)
        im.save(out_image)
    if method == 'blue':
        im = Image(in_image)
        blue_light_filter(im, False)
        im.save(out_image)


if __name__ == "__main__":
    main()
