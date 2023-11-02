# trans2d.py
#    implementation of 2d transformations in homogeneous coords
# Andrew Poock


from math import radians, sin, cos, tan
import matrix as mat


def scale(sx, sy):
    """ return a matrix that scales by sx, sy.

    >>> scale(2,3)
    [[2.0, 0.0, 0.0], [0.0, 3.0, 0.0], [0.0, 0.0, 1.0]]
    >>> 
    """
    return [[float(sx), 0.0, 0.0], [0.0, float(sy), 0.0], [0.0, 0.0, 1.0]]

def translate(dx, dy):
    """return a matrix that translates by (dx, dy)

    >>> translate(-3, 2)
    [[1.0, 0.0, -3.0], [0.0, 1.0, 2.0], [0.0, 0.0, 1.0]]
    """
    return [[1.0, 0.0, float(dx)], [0.0, 1.0, float(dy)], [0.0, 0.0, 1.0]]


def rotate(angle):
    """returns a matrix that rotates angle degrees counter-clockwise

    >>> print(rotate(30))
    [[0.8660254037844387, -0.49999999999999994, 0.0], [0.49999999999999994, 0.8660254037844387, 0.0], [0.0, 0.0, 1.0]]
    """
    rad = radians(angle)
    return [[cos(rad), -sin(rad), 0.0], [sin(rad), cos(rad), 0.0], [0.0, 0.0, 1.0]]

    
def window(box0, box1):
    """returns a transformation that maps box0 to box1

    note: a box is a tuple: (left, bottom, right, top) where
    (left,bottom) is the point at the lower-left corner and
    (right, top) is the point in the upper-right corner.

    >>> window((20, 10, 60,40), (5, 5, 9, 8))
    [[0.1, 0.0, 3.0], [0.0, 0.1, 4.0], [0.0, 0.0, 1.0]]
    >>> m=window((20, 10, 60,40), (5, 5, 9, 8))
    >>> mat.apply(m, (20,10,1))
    [5.0, 5.0, 1.0]
    >>> mat.apply(m, (60,40,1))
    [9.0, 8.0, 1.0]
    >>> mat.apply(m, (40,25,1))
    [7.0, 6.5, 1.0]

    """
    m = translate(-box0[0], -box0[1])
    sx = ((box1[2]-box1[0])/(box0[2]-box0[0]))
    sy = ((box1[3]-box1[1])/(box0[3]-box0[1]))
    m = mat.mul(scale(sx, sy), m)
    m = mat.mul(translate(box1[0], box1[1]), m)
    return m


if __name__ == '__main__':
    import doctest
    doctest.testmod()
