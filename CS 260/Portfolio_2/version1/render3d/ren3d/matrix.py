# matrix.py
#    A set of functions for operating on matrices, where a matrix is
#    a list of lists.
# Andrew Poock


def unit(n):
    """return nxn identity matrix

    >>> unit(2)
    [[1.0, 0.0], [0.0, 1.0]]
    >>> unit(3)
    [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    >>> unit(4)
    [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]
    """
    m = []
    for r in range(0, n):
        row = []
        for c in range(0, n):
            if (r == c):
                row.append(1.0)
            else:
                row.append(0.0)
        m.append(row)
    return m
    

def nrows(mat):
    """ returns the number of rows in mat

    >>> m1 = [ [1,2], [3,4] ]
    >>> nrows(m1)
    2
    >>> m2 = [ [1,2], [3,4], [5,6] ]
    >>> nrows(m2)
    3
    """
    return len(mat)


def ncols(mat):
    """ returns the number of columns in mat

    >>> m1 = [ [1,2], [3,4] ]
    >>> m2 = [ [1,2], [3,4], [5,6] ]
    >>> ncols(m1)
    2
    >>> ncols(m2)
    2
    >>> m3 = [ [1], [2], [3] ]
    >>> ncols(m3)
    1
    """
    return len(mat[0])


def mul(m1, m2):
    """ returns the matrix product of m1 and m2

    >>> m1 = [[1,2],[3,4]]
    >>> m2 = [[-2,3], [1,-1]]
    >>> mul(m1,m2)
    [[0, 1], [-2, 5]]
    >>> mul(m2,m1)
    [[7, 8], [-2, -2]]
    >>> mul(m1,unit(2))
    [[1.0, 2.0], [3.0, 4.0]]
    >>> mul(unit(2), m2)
    [[-2.0, 3.0], [1.0, -1.0]]
    >>> mul(m1, [[2], [2]])
    [[6], [14]]
    """
    assert ncols(m1) == nrows(m2)
    rows = []
    for r in range(nrows(m1)):
        row = []
        for c in range(ncols(m2)):
            entry = 0
            for k in range(ncols(m1)):
                entry += m1[r][k] * m2[k][c]
            row.append(entry)
        rows.append(row)
    return rows


def transpose(m):
    """ return the transpose of matrix m

    >>> m1 = [[1,2],[3,4]]
    >>> m2 = [[-2,3], [1,-1]]
    >>> transpose(m1)
    [[1, 3], [2, 4]]
    >>> transpose(m2)
    [[-2, 1], [3, -1]]
    """
    t = unit(nrows(m))
    for i in range(nrows(m)):
        for j in range(ncols(m)):
            t[j][i] = m[i][j]
    return t

    
def dotprod(a, b):
    """ return dotproduct of sequences a and b

    >>> dotprod([1,2,3],[4,5,6])
    32
    """
    tot = 0
    for i in range(len(a)):
        x = a[i]*b[i]
        tot += x
    return tot


def apply(m, seq):
    """return the result of applying m to seq

    seq is treated as a column. The result is returned as a (flat) list.
    >>> m1 = [[1,2],[3,4]]
    >>> m2 = [[-2,3], [1,-1]]
    >>> apply(m1, [-1,1])
    [1, 1]
    >>> apply(m2, [-1,1])
    [5, -2]
    >>> apply(unit(3), [1,2,3])
    [1.0, 2.0, 3.0]

    """
    rows = []
    for r in range(nrows(m)):
        row = 0
        for c in range(len(seq)):
            entry = 0
            entry += m[r][c] * seq[c]
            row += entry
        rows.append(row)
    return rows


if __name__ == '__main__':
    import doctest
    doctest.testmod()
