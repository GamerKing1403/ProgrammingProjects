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
        self.direction = bool(randint(0, 2))
        self.theta = randint(0, 90)
        self.velx = self.vel * np.cos(np.radians(self.theta))
        self.vely = self.vel * np.sin(np.radians(self.theta))
        self.start = True
        self.xorY = None

    def move(self, players, winDimension):
        self.collision(players, winDimension)
        if self.direction:
            if self.xorY == 0:
                self.x -= self.velx
                self.y += self.vely
                self.start = False
            elif self.xorY == 1:
                self.x += self.velx
                self.y -= self.vely
                self.start = False
            elif self.start:
                self.x += self.velx
                self.y += self.vely
        else:
            if self.xorY == 0:
                self.x += self.velx
                self.y -= self.vely
                self.start = False
            elif self.xorY == 1:
                self.x -= self.velx
                self.y += self.vely
                self.start = False
            elif self.start:
                self.x -= self.velx
                self.y -= self.vely
        self.update()

    def collision(self, players, winDimension):
        self.xorY = 0
        if self.x + 2 * self.r >= winDimension[0]:
            self.xorY, self.direction = 0, not self.direction
        elif self.x <= 0:
            self.xorY, self.direction = 0, not self.direction
        elif self.y <= 0:
            self.xorY, self.direction = 1, not self.direction
        elif self.y + 2 * self.r >= winDimension[1]:
            self.xorY, self.direction = 1, not self.direction

    def update(self):
        self.pos = (self.x, self.y)

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.pos, self.r)
