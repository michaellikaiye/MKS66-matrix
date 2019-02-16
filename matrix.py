"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

# print the matrix such that it looks like
# the template in the top comment


def print_matrix(matrix):

    for j in range(4):
        for point in matrix:
            print(point[j], end=" ")
        print("")

# turn the paramter matrix into an identity matrix
# you may assume matrix is square


def ident(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

# multiply m1 by m2, modifying m2 to be the product
# m1 * m2 -> m2


def matrix_mult(m1, m2):
    # m1 must be 4points by 4
    # m2 bpoints by 4
    m1rows = []
    m2cols = []
    for j in range(4):
        row = [i[j] for i in m1]
        m1rows.append(row)
    for i in range(len(m2)):
        col = m2[i][:]
        m2cols.append(col)
    rows = len(m1rows)
    cols = len(m2cols)
    for i in range(rows):
        for j in range(cols):
            m2[j][i] = dot(m1rows[i], m2cols[j])


def dot(row, col):
    # same sized vectors
    return sum([row[k] * col[k] for k in range(len(row))])


def new_matrix(rows=4, cols=4):
    m = []
    for c in range(cols):
        m.append([])
        for r in range(rows):
            m[c].append(0)
    return m
