from random import randint
import numpy as np
import pygame


class Ball:
    def __init__(self, x, y, r, vel):
        self.x = x
        self.y = y
        self.r = r
        self.vel = vel
        self.color = (0, 0, 0)
        self.pos = (x, y)
        self.startDirection = bool(randint(0, 2))
        self.theta = randint(0, 90)

    def move(self):
        if self.startDirection:
            self.x += self.vel * np.cos(np.radians(self.theta))
            self.y += self.vel * np.sin(np.radians(self.theta))
        else:
            self.x -= self.vel * np.cos(np.radians(self.theta))
            self.y -= self.vel * np.sin(np.radians(self.theta))
        self.update()

    def collision(self, players, win):
        if self.x + 2*self.r == win[0]:
            self.x -= 2 * self.vel * np.cos(np.radians(self.theta))

    def update(self):
        self.pos = (self.x, self.y)

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.pos, self.r)
