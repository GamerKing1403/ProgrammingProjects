import pygame, sys, pymunk

pygame.init()  # Initializing pygame
screen = pygame.display.set_mode((800, 800))  # setting a display
clock = pygame.time.Clock()  # Clock
space = pymunk.Space()  # Creating a f
ball = pymunk.Circle(pymunk.Body(1, 1000), 5)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((217, 217, 217))
    space.step(1 / 50)

    pygame.display.update()
    clock.tick(60)
