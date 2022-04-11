import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from helper import *
from random import random, randint
from helper import *
from Ball import *

display = (800, 400)

num = randint(20, 30)
balls = []
colors = []
for x in range(num):
    centre, r = (randint(20, 780), randint(200, 600)), 8
    ball = Ball(centre, r, display)
    colors.append((random(), random(), random()))
    balls.append(ball)


def draw(edge, fill, color):
    # Function to plot the points of each ball (outline and filling inside)
    glPointSize(1.0)
    glBegin(GL_POINTS)
    for i in fill:
        for vertex in i:
            glColor3fv(color)
            glVertex2iv(vertex)
    glEnd()
    glPointSize(2.0)
    glBegin(GL_POINTS)
    for i in edge:
        for vertex in i:
            glColor3fv([0, 0, 0])
            glVertex2fv(vertex)
    glEnd()


def ball_draw():
    # Call the draw function and reposition them at each instance
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for i in balls:
        i.repos_ball()
        draw([i.edge], [i.generate_fill()], colors[balls.index(i)])
    pygame.display.flip()
    pygame.time.wait(1)


# Main Function
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor(1, 1, 0, 0.2)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_COLOR_MATERIAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    gluOrtho2D(0, display[0], 0, display[1])
    while True:
        for event in pygame.event.get():
            pygame. display. set_caption('Free Falling Balls')
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        ball_draw()
        pygame.time.Clock().tick(60)