import pygame

width = 500
height = 500

win = pygame.display.set_mode((width, height))


def reDrawWindow(win):
    win.fill((0, 0, 0))
    pygame.display.update()


