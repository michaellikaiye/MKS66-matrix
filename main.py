from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [200, 200, 200]

print("Testing MATRICES")
print("Testing m2 = new_matrix(4,2)")
m2 = new_matrix(4, 2)
print_matrix(m2)
print("Testing add edge (1, 2, 3), (4, 5, 6)")
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)
print("Testing identity matrix m0")
m0 = new_matrix()
ident(m0)
print_matrix(m0)
print("m1 =")
m1 = new_matrix()
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 7, 8, 9, 10, 11, 12)
print_matrix(m1)
print("Testing multiplication m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)
print("Testing add point (1, 2, 3)")
add_point(m2, 1, 2, 3)
print_matrix(m2)

art = new_matrix()
f = open("in.txt", 'r')
lines = f.read().split('\n')
for line in lines:
    locs = line.split('/')
    for i in range(len(locs) - 1):
        words = locs[i].split(',')
        start = [int(x) for x in words]
        words = locs[i + 1].split(',')
        end = [int(x) for x in words]
        add_edge(art, start[0] - 100, 500 - start[1],
                 0, end[0] - 100, 500 - end[1], 0)
f.close()
draw_lines(art, screen, color)
display(screen)
save_extension(screen, 'img.png')

