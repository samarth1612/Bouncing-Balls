from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


def octet(h, k, x, y):
    # Return the points in the eight octets
    return [(h+x, k+y), (h+y, k+x), (h+y, k-x), (h+x, k-y), (h-x, k-y), (h-y, k-x), (h-y, k+x), (h-x, k+y)]


# Mid point circle drawing algorithm
def mcd(c, r):
    h, k = c
    p = 1 - r
    x, y = 0, r
    points = octet(h, k, x, y)
    while y > x:
        if p < 0:
            points += octet(h, k, x+1, y)
            p += 2 * x + 3
            x += 1
        else:
            points += octet(h, k, x+1, y-1)
            p += 2 * x - 2 * y + 5
            x += 1
            y -= 1
    return points