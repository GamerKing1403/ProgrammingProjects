from player import Player
import pygame

players = []
win_width = 1080
win_height = 720
win = pygame.display.set_mode((win_width, win_height))
player1 = Player(0, win_height/2-50, 20, 100, (0, 0, 0), win)
player2 = Player(win_width-20, win_height/2-50, 20, 100, (0, 0, 0), win)
players.append(player1)
players.append(player2)


def redrawWindow(window, player):
    window.fill((255, 255, 255))
    for p in player:
        p.draw()
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for p in players:
            p.move()
        redrawWindow(win, players)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False


if __name__ == '__main__':
    main()

