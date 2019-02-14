from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
add_point(matrix, 1, 2)
add_edge(matrix, 2, 3, 0, 5, 6, 7)
add_edge(matrix, 9, 8, 7, 6, 5, 4)
print_matrix(matrix)
matrix = new_matrix()
ident(matrix)
print_matrix(matrix)

m1 = new_matrix()
m2 = new_matrix()

add_helper(m1, 1, 2, 3)
add_helper(m1, 4, 5, 6)
add_helper(m1, 7, 8, 9)
add_helper(m1, 11, 12, 13)
print("m1")
print_matrix(m1)
add_helper(m2, 6, 5, 4)
add_helper(m2, 1, 2, 3)
add_helper(m2, 13, 14, 15)
add_helper(m2, 17, 18, 19)
print("m2")
print_matrix(m2)
matrix_mult(m1, m2)
print_matrix(m2)

#draw_lines( matrix, screen, color )
#display(screen)
