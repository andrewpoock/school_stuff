# math3d.py
# implementation of points and vectors in 3-space


from math import sqrt as math_sqrt

from ren3d.matrix import apply as mat_apply


class Point:
    """A location in 2- or 3-space"""

    def __init__(self, coords):
        """ A point in 2- or 3-space
        >>> p2 = Point([1,2])
        >>> p3 = Point([1,2,3])
        """
        self._coords = [float(v) for v in coords]

    def __repr__(self):
        """ 
        >>> Point([1,2,3])
        Point([1.0, 2.0, 3.0])
        """
        return "Point(" + str(self._coords) + ")"

    @property
    def x(self):
        return self._coords[0]

    @x.setter
    def x(self, v):
        self._coords[0] = float(v)

    @property
    def y(self):
        return self._coords[1]

    @y.setter
    def y(self, v):
        self._coords[1] = float(v)

    @property
    def z(self):
        return self._coords[2]

    @z.setter
    def z(self, v):
        self._coords[2] = float(v)

    def __getitem__(self, i):
        return self._coords[i]

    def __setitem__(self, i, value):
        self._coords[i] = float(value)

    def __iter__(self):
        """ Point is a sequence of its coordinates
        >>> p = Point([1,2,3])
        >>> tuple(p)
        (1.0, 2.0, 3.0)
        >>> list(p)
        [1.0, 2.0, 3.0]
        >>> for v in p: print(v)
        1.0
        2.0
        3.0
        >>> x, y, z = p
        >>> x, y, z
        (1.0, 2.0, 3.0)
        """
        return iter(self._coords)

    def __sub__(self, other):
        """ Difference of Point with another Point or a Vector

        A point minus a point produces a vector.
        A point minus a vector produces a point.
        
       >>> Point([1,2,3]) - Point([5,-3,2])
       Vector([-4.0, 5.0, 1.0])
        >>> Point([1,2,3]) - Vector([5,-3,2])
        Point([-4.0, 5.0, 1.0])
        >>>

        """
        restype = Vector if type(other) == Point else Point
        return restype([a-b for a, b in zip(self, other)])

    def trans(self, t):
        """ returns a new point with transformation applied """
        return Point(mat_apply(t, tuple(self) + (1,))[:3])


class Vector:
    """A vector in 2- or 3-space"""

    def __init__(self, coords):
        """
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4.3, 5.2])
        """
        self._coords = [float(v) for v in coords]
        
    def __repr__(self):
        """
        >>> Vector([1,2,3])
        Vector([1.0, 2.0, 3.0])
        """
        return "Vector(" + str(self._coords) + ")"

    @property
    def x(self):
        return self._coords[0]

    @x.setter
    def x(self, v):
        self._coords[0] = float(v)

    @property
    def y(self):
        return self._coords[1]

    @y.setter
    def y(self, v):
        self._coords[1] = float(v)

    @property
    def z(self):
        return self._coords[2]

    @z.setter
    def z(self, v):
        self._coords[2] = float(v)

    def __iter__(self):
        """
        >>> list(Vector([1,2,3]))
        [1.0, 2.0, 3.0]
        """
        return iter(self._coords)

    def __getitem__(self, i):
        """ get ith item 
        >>> v = Vector((1, 3, 5))
        >>> v[0]
        1.0
        >>> v[2]
        5.0
        """
        return self._coords[i]

    def __setitem__(self, i, v):
        """ set ith item 

        >>> v = Vector((1, 3, 5))
        >>> v[1] = 4
        >>> v[1]
        4.0
        """
        self._coords[i] = float(v)

    def __rmul__(self, s):
        """ multiplication by a preceeding scalar

        >>> 3 * Vector([1,2,3])
        Vector([3.0, 6.0, 9.0])
        """
        return Vector([s * n for n in self])

    def __mul__(self, s):
        """ multiplication by a succeeding scalar
        >>> Vector([1,2,3]) * 3
        Vector([3.0, 6.0, 9.0])
        """
        return s * self
   
    def __add__(self, other):
        """ vector addition with other on right
        the result type depends on other: 
            vector + point --> point
            vector + vector --> vector

        >>> Vector([3, -1, 2]) + Point([1, 2, 3])
        Point([4.0, 1.0, 5.0])
        >>> Vector([3, -1, 2]) + Vector([1, 2, 3])
        Vector([4.0, 1.0, 5.0])
        """
        restype = Vector if type(other) == Vector else Point
        return restype([a + b for a, b in zip(self, other)])

    def __radd__(self, other):
        """ vector addition with other (point or vector) on left (see __add__)

        >>> Vector([1,2,3]) + Vector([4,5,6])
        Vector([5.0, 7.0, 9.0])
        """
        return self + other

    def __neg__(self):
        """negation
        >>> -Vector([1,-2,3])
        Vector([-1.0, 2.0, -3.0])
        """
        return Vector([-n for n in self])

    def __sub__(self, other):
        """vector subtraction
        >>> Vector([1,2,3]) - Vector([-3,1,2.5])
        Vector([4.0, 1.0, 0.5])
        """
        return Vector([a - b for a, b in zip(self, other)])

    def trans(self, t):
        """ applies transformation to a Vector """
        return Vector(mat_apply(t, tuple(self) + (0,))[:3])

    def dot(self, other):
        """ Vector dot product

        >>> Vector([1,2,3]).dot(Vector([2,3,4]))
        20.0
        """
        return sum(a * b for a, b in zip(self, other))

    def cross(self, other):
        """ Vector cross product

        >>> Vector([1,2,3]).cross(Vector([4,5,6]))
        Vector([-3.0, 6.0, -3.0])

        formula: a x b = (ay*bz - by*az)*i -(ax*bz - bx*az)*j + (ax*by - bx*ay)*k
            aka: a x b = (ay*bz - by*az)*i +(bx*az - ax*bz)*j + (ax*by - bx*ay)*k
        i, j, k are respective unit vectors in x,y,z
        This formula is similar to det of matrix of form [i,j,k, [a.x,a.y,a.z], [b.x,b.y,b.z]]
        with cofactor expansion
        """
        return Vector((self.y * other.z - other.y * self.z,
                       other.x * self.z - self.x * other.z,
                       self.x * other.y - other.x * self.y))

    def reflect(self, n):
        """ returns vector of a reflection ray n onto self """
        return self - 2 * (self.dot(n)) * n

    def mag2(self):
        """ Square of magnitude

        >>> Vector([1,2,3]).mag2()
        14.0
        """
        return sum(n * n for n in self)

    def mag(self):
        """ Magnitude
        >>> Vector([1,2,3]).mag()
        3.7416573867739413
        """
        return math_sqrt(sum(n * n for n in self))

    def normalize(self):
        """ make this vector unit length

        >>> v = Vector([1,2,3])
        >>> v.normalize()
        >>> v
        Vector([0.2672612419124244, 0.5345224838248488, 0.8017837257372732])
        """
        mag = self.mag()
        self._coords = [n/mag for n in self]

    def normalized(self):
        """ return normalized version of this vector
        >>> v = Vector([1,2,3])
        >>> v.normalized()
        Vector([0.2672612419124244, 0.5345224838248488, 0.8017837257372732])
        >>> v
        Vector([1.0, 2.0, 3.0])
        """
        mag = self.mag()
        return Vector([n/mag for n in self])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
