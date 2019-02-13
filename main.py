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

#draw_lines( matrix, screen, color )
#display(screen)
