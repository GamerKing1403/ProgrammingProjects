import pygame
from network import Network
from ball import Ball

winDimension = [1080, 720]
win = pygame.display.set_mode(winDimension)
pygame.display.set_caption("Ping Pong Game")


def redrawWindow(window, player, ball):
    window.fill((255, 255, 255))
    ball.draw(window)
    ball.collision(player, winDimension)
    for p in player:
        p.draw(window)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    p = n.getP()
    b = Ball(winDimension[0]/2, winDimension[1]/2, 5, 5)

    while run:
        clock.tick(60)
        p2 = n.send(p)
        players = [p, p2]
        p.move()
        b.move()
        redrawWindow(win, players, b)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False


if __name__ == '__main__':
    main()

