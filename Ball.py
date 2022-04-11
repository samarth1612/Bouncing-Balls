from helper import *
import math

g = 9.8


class Ball():
    def __init__(self, centre, radius, display):
        self.centre = centre
        self.radius = radius
        self.height = centre[1]
        self.display = display
        self.dir = -1
        self.u = 0
        self.edge = mcd(self.centre, self.radius)

    def in_mat(self):
        # Creating matrix of the size around the polygon drawn
        x, y = zip(*self.edge)
        return (min(x), max(x)), (min(y), max(y))

    def generate_fill(self):
        # Generating fill points
        fill = []
        rng = self.in_mat()
        for x in range(rng[0][0], rng[0][1]):
            for y in range(rng[1][0], rng[1][1]):
                if (x-self.centre[0])**2 + (y-self.centre[1])**2 < self.radius**2:
                    fill.append((x, y))
        return fill

    def velocity(self):
        # Velocity of each ball
        self.u = math.sqrt(self.u**2 + 2 * g * (self.centre[1]) * 0.001)
        return self.u

    def displacement(self):
        # Updated height of the ball
        v = self.velocity()
        t = v / g
        return round(0.5 * g * t**2)

    def repos_ball(self):
        if self.centre[1] <= self.radius and self.dir == -1:
            self.dir *= -1
            self.height *= 0.9
        if self.centre[1] >= 0.9 * self.height and self.dir == 1:
            self.dir *= -1
        dist = self.dir * self.displacement()
        if self.height > 1:
            if self.centre[1] + dist < self.radius:
                dist = self.radius - self.centre[1]
            self.centre = (self.centre[0], self.centre[1] + dist)
            for i in range(len(self.edge)):
                self.edge[i] = (self.edge[i][0], self.edge[i][1] + dist)