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

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for row in matrix:
        for element in row:
            print(element,end=" ")
        print("")

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i is j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #assuming m1 is square, 4x4
    row = 4
    col = m2[3].count(1)
    temp = []
    for i in range(row):
        temp.append([])
        for j in range(col):
            temp.append(m2[i][j])
            m2[i][j] = 0
    
    print_matrix(m2)
    print(temp)
    print("matrix")
    for i in range(row):
        for j in range(col):
            for n in range(row):
                m2[i][j] += m1[i][n] * temp[n][j]
    

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
