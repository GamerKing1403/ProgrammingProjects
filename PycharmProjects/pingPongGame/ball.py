from random import randint
import numpy as np
import pygame
import pymunk
import pymunk.pygame_util


class Ball:
    def __init__(self, space, x, y, r, vel, mass):
        self.r = r
        self.p = (x, y)
        self.mass = mass
        self.vel = vel
        self.color = (0, 0, 0)
        self.space = space
        self.body = pymunk.Body()
        self.shape = pymunk.Circle(self.body, self.r)
        self.shape.mass = self.mass
        self.space.add(self.body, self.shape)

    def draw(self, screen):
        return pymunk.pygame_util.DrawOptions(screen)
