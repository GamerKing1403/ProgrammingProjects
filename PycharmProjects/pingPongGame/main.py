import pygame
from network import Network
from ball import Ball
import sys
import pymunk.pygame_util

winDimension = [1080, 720]
win = pygame.display.set_mode(winDimension)
pygame.display.set_caption("Ping Pong Game")
space = pymunk.Space()
space.debug_draw(pymunk.pygame_util.DrawOptions(win))


def redrawWindow(window, player):
    window.fill((255, 255, 255))
    for p in player:
        p.draw(window)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    p = n.getP()
    b = Ball(space, winDimension[0]/2, winDimension[1]/2, 5, 2, 3)

    while run:
        clock.tick(60)
        p2 = n.send(p)
        players = [p, p2, b]
        p.move()
        redrawWindow(win, players)
        space.step(0.01)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False


if __name__ == '__main__':
    sys.exit(main())
