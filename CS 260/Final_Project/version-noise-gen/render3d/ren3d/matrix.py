# matrix.py
#    A set of functions for operating on matrices, where a matrix is
#    a list of lists.


def unit(n):
    """return nxn identity matrix

    >>> unit(2)
    [[1.0, 0.0], [0.0, 1.0]]
    >>> unit(3)
    [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    >>> unit(4)
    [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]
    """
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    
def nrows(mat):
    """ returns the number of rows in mat

    >>> m1 = [[1,2], [3,4]]
    >>> nrows(m1)
    2
    >>> m2 = [[1,2], [3,4], [5,6]]
    >>> nrows(m2)
    3
    """
    return len(mat)


def ncols(mat):
    """ returns the number of columns in mat

    >>> m1 = [[1,2], [3,4]]
    >>> m2 = [[1,2], [3,4], [5,6]]
    >>> ncols(m1)
    2
    >>> ncols(m2)
    2
    >>> m3 = [[1], [2], [3]]
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
    # matrix is of size n x m where m1 * m2 is n x k * k * m
    m2_t = transpose(m2)
    return [[dotprod(m1[row], m2_t[col]) for col in range(ncols(m2))] for row in range(nrows(m1))]


def transpose(m):
    """ return the transpose of matrix m

    >>> m1 = [[1,2],[3,4]]
    >>> m2 = [[-2,3], [1,-1]]
    >>> transpose(m1)
    [[1, 3], [2, 4]]
    >>> transpose(m2)
    [[-2, 1], [3, -1]]

    # below was added myself
    >>> transpose([[1, 2 ,3]])
    [[1], [2], [3]]
    >>> transpose([[1], [2], [3]])
    [[1, 2, 3]]
    """
    return [[m[row][col] for row in range(nrows(m))] for col in range(ncols(m))]


def dotprod(a, b):
    """ return dotproduct of sequences a and b

    >>> dotprod([1,2,3],[4,5,6])
    32
    """
    assert len(a) == len(b)  # extra safety
    return sum(a[i] * b[i] for i in range(len(a)))


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
    assert nrows(m) == len(seq)  # i added this since it does need to be true
    return [row[0] for row in mul(m, transpose([seq]))]  # row is always a list of size 1 so just take it
    # note below also works, I just hadn't implimented mul yet
    # mult = [[m[col][row]*seq[row] for col in range(ncols(m))] for row in range(nrows(m))]
    # mult_t = transpose(mult)
    # return [sum(mult_t[col]) for col in range(ncols(mult))]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
