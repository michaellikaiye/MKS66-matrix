from display import *
from matrix import *


def draw_lines(matrix, screen, color):
    for i in range(int(len(matrix) / 2)):
        start = matrix[i * 2]
        end = matrix[i * 2 + 1]
        if start == end:
            plot(screen, color, start[0], start[1])
        else:
            draw_line(start[0], start[1], end[0], end[1], screen, color)


def add_edge(matrix, x0, y0, z0, x1, y1, z1):
    add_one(matrix, x0, y0, z0)
    add_one(matrix, x1, y1, z1)
    pass


def add_point(matrix, x, y, z=0):
    add_one(matrix, x, y, z)
    add_one(matrix, x, y, z)


def add_one(matrix, x, y, z):
    point = [x, y, z, 1]
    length = len(matrix)
    points = 0
    for i in range(length):
        if matrix[i][3] > 0:
            points = i + 1
    if points == length:
        matrix.append(point)
    else:
        matrix[points] = point


def draw_line(x0, y0, x1, y1, screen, color):

    # swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    # octants 1 and 8
    if (abs(x1 - x0) >= abs(y1 - y0)):

        # octant 1
        if A > 0:
            d = A + B / 2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y += 1
                    d += B
                x += 1
                d += A
            # end octant 1 while
            plot(screen, color, x1, y1)
        # end octant 1

        # octant 8
        else:
            d = A - B / 2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y -= 1
                    d -= B
                x += 1
                d += A
            # end octant 8 while
            plot(screen, color, x1, y1)
        # end octant 8
    # end octants 1 and 8

    # octants 2 and 7
    else:
        # octant 2
        if A > 0:
            d = A / 2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x += 1
                    d += A
                y += 1
                d += B
            # end octant 2 while
            plot(screen, color, x1, y1)
        # end octant 2

        # octant 7
        else:
            d = A / 2 - B

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x += 1
                    d += A
                y -= 1
                d -= B
            # end octant 7 while
            plot(screen, color, x1, y1)
        # end octant 7
    # end octants 2 and 7
# end draw_line
