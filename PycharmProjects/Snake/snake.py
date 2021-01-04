import pygame
import random
import threading

pygame.init()

pygame.display.set_caption("Snake")

win = pygame.display.set_mode((512, 512), 0, 32)
scrSide = 512
block_size = 32
clock = pygame.time.Clock()

font1 = pygame.font.SysFont('cosmicsans', 100)
text = font1.render('Game Over', 1, (255, 0, 0))


class snake(object):

    def __init__(self, x, y, contact, count, not_crashed=True):
        self.x = x
        self.y = y
        self.contact = contact
        self.count = count
        self.vel = 32
        self.not_crashed = not_crashed
        self.facingLeft = False
        self.facingRight = True
        self.facingUp = False
        self.facingDown = False

    def draw(self):
        pygame.draw.rect(win, (255, 0, 0), (self.x + 1, self.y + 1, block_size - 2, block_size - 2))

    def continuous_mov(self):
        if self.not_crashed:
            pygame.time.delay(500)
            if self.facingRight:
                self.x += self.vel
            if self.facingLeft:
                self.x -= self.vel
            if self.facingUp:
                self.y -= self.vel
            if self.facingDown:
                self.y += self.vel
            self.crash_checker()

    def crash_checker(self):
        if self.x >= scrSide + block_size or self.y >= scrSide + block_size or self.x < 0 or self.y < 0:
            self.not_crashed = False
            win.blit(text, ((scrSide / 2) - (text.get_width() / 2), (scrSide / 2) - (text.get_height() / 2)))


class collectable(object):

    def __init__(self):
        self.x = random.randrange(0, scrSide, block_size)
        self.y = random.randrange(0, scrSide, block_size)
        self.visible = True

    def draw(self):
        if self.visible:
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, block_size - 2, block_size - 2))
        self.visibility()

    def visibility(self):
        if snake1.x == self.x and snake1.y == self.y:
            self.visible = False


def windraw():
    pygame.display.set_mode((512, 512), 0, 32)
    for y in range(scrSide):
        for x in range(scrSide):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            pygame.draw.rect(win, (255, 255, 255), rect, 1)


def redraw():
    snake1.draw()
    coin1.draw()
    snake1.continuous_mov()
    pygame.display.update()


snake1 = snake(0, 0, False, 0)
coin1 = collectable()
t1 = threading.Thread(windraw())

t1.start()

run = True
while run:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if key[pygame.K_UP] or key[pygame.K_w]:
        snake1.y -= block_size
        if not snake1.facingUp:
            snake1.facingUp = True
            snake1.facingLeft = False
            snake1.facingRight = False
            snake1.facingDown = False

    if key[pygame.K_DOWN] or key[pygame.K_s]:
        snake1.y += block_size
        if not snake1.facingDown:
            snake1.facingUp = False
            snake1.facingLeft = False
            snake1.facingRight = False
            snake1.facingDown = True

    if key[pygame.K_LEFT] or key[pygame.K_a]:
        snake1.x -= block_size
        if not snake1.facingLeft:
            snake1.facingUp = False
            snake1.facingLeft = True
            snake1.facingRight = False
            snake1.facingDown = False

    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        snake1.x += block_size
        if not snake1.facingRight:
            snake1.facingUp = False
            snake1.facingLeft = False
            snake1.facingRight = True
            snake1.facingDown = False

    redraw()


pygame.quit()
