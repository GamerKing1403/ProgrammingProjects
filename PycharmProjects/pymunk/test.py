import sys
import pygame
import pymunk #1

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()

    space = pymunk.Space() #2
    space.gravity = (0.0, 900.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        screen.fill((255,255,255))

        space.step(1/50.0) #3

        pygame.display.flip()
        clock.tick(50)

if __name__ == '__main__':
    sys.exit(main())