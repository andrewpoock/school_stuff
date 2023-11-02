# rgb.py
#    Calculations on color values

# ----------------------------------------------------------------------


class RGB:

    def __init__(self, rgb):
        """ representaiton of color using 3 floating point values

        >>> c = RGB((.3, .3, .75))
        >>> c.values
        (0.3, 0.3, 0.75)
        >>> c = RGB((1, 0, 1))
        >>> c.values
        (1.0, 0.0, 1.0)
        >>>
        """
        r, g, b = rgb
        self.values = (float(r), float(g), float(b))

    def __repr__(self):
        """
        >>> RGB((.5, .5, 1))
        RGB((0.5, 0.5, 1.0))
        """
        return ('RGB(' + str(self.values) + ')')

    def __iter__(self):
        """ iterate through components in r,g,b order
        >>> c = RGB((1, 2, 3))
        >>> list(c)
        [1.0, 2.0, 3.0]
        """
        return iter(self.values)

    def quantize(self, top):
        """ return a tuple of ints all in range(top+1)
        >>> RGB((.3, .3, .75)).quantize(255)
        (76, 76, 191)
        >>> RGB((.5, .8, 1.1)).quantize(255)
        (128, 204, 255)
        """
        new_rgb = [0]*3
        for i in range(len(self.values)):
            if 0 <= self.values[i]*top <= top:
                new_rgb[i] = round(self.values[i]*top)
            if self.values[i]*top < 0:
                new_rgb[i] = 0
            if self.values[i]*top > top:
                new_rgb[i] = top
        return tuple(new_rgb)

    def __mul__(self, i):
        """ return a new RGB that is scaled by i

        >>> .25*RGB((.8, .5, .4))
        RGB((0.2, 0.125, 0.1))
        """
        new_rgb = [0]*3
        for j in range(len(self.values)):
            new_rgb[j] = self.values[j]*i
        return RGB(tuple(new_rgb))

    def __rmul__(self, i):
        """ return a new RGB that is scaled by i

        >>> RGB((.8, .5, .4))*(.25)
        RGB((0.2, 0.125, 0.1))
        """
        new_rgb = [0]*3
        for j in range(len(self.values)):
            new_rgb[j] = self.values[j]*i
        return RGB(tuple(new_rgb))

    def __add__(self, other):
        """
        >>> RGB((.8, .5, .4)) + RGB((.1, .2, .3))
        RGB((0.9, 0.7, 0.7))
        """
        new_rgb = [0]*3
        for j in range(len(self.values)):
            new_rgb[j] = self.values[j] + other.values[j]
        return RGB(tuple(new_rgb))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
