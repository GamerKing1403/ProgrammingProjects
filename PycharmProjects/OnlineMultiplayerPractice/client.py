import pygame
from network import Network

width = 500
height = 500
win: pygame.display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Player")


def redrawWindow(window, player):
    window.fill((255, 255, 255))
    for p in player:
        p.draw(window)
    pygame.display.update()


def main():
    run = True
    n = Network()
    clock = pygame.time.Clock()
    p = n.getP()

    while run:
        clock.tick(60)
        p2 = n.send(p)
        players = [p, p2]
        p.move()
        redrawWindow(win, players)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()
