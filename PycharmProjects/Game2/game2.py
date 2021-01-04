import pygame

# initiating pyGame
pygame.init()

# Creating the display for the Game Window.
win = pygame.display.set_mode((852, 480))
screenWidth = 852
screenHeight = 480

# Sets the Caption of the Game Window.
pygame.display.set_caption("First Game")

# Loading all The Images.
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
bullet_img = pygame.image.load('bullet.png')
bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')
music = pygame.mixer.music.load('music.mp3')

# Sets the Background Music
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()     # Creates a Clock
score = 0       # The Score Variable
reSpawn = True      # A boolean for re spawning


# This the Player Object.
class player(object):
    def __init__(self, x, y, height, width):    # Initiation function
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 7
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitBox = (self.x + 17, self.y + 11, 29, 52)


# This function is for drawing the player on the board and to see the direction he will be facing
    def draw(self, window):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                window.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                window.blit(walkLeft[0], (self.x, self.y))
            elif self.standing:
                window.blit(char, (self.x, self.y))
        self.hitBox = (self.x + 17, self.y + 11, 29, 52)

    def hit(self):      # This is the function which is called when the player is hit
        self.x = 0
        self.y = 405
        self.walkCount = 0
        font1 = pygame.font.SysFont('cosmicsans', 100)
        text = font1.render('-50', 1, (255, 0, 0))
        win.blit(text, ((screenWidth / 2) - (text.get_width() / 2), (screenHeight / 2) - (text.get_height() / 2)))
        pygame.display.update()
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                pygame.quit()


class enemy(object):    # This the Enemy Object.
    # this loads all the images for The Enemy
    walkRight = [pygame.image.load("R1E.png"), pygame.image.load("R2E.png"), pygame.image.load("R3E.png"),
                 pygame.image.load("R4E.png"), pygame.image.load("R5E.png"), pygame.image.load("R6E.png"),
                 pygame.image.load("R7E.png"), pygame.image.load("R8E.png"), pygame.image.load("R9E.png"),
                 pygame.image.load("R10E.png"), pygame.image.load("R11E.png")]
    walkLeft = [pygame.image.load("L1E.png"), pygame.image.load("L2E.png"), pygame.image.load("L3E.png"),
                pygame.image.load("L4E.png"), pygame.image.load("L5E.png"), pygame.image.load("L6E.png"),
                pygame.image.load("L7E.png"), pygame.image.load("L8E.png"), pygame.image.load("L9E.png"),
                pygame.image.load("L10E.png"), pygame.image.load("L11E.png")]

    def __init__(self, x, y, width, height, player_x):      # The Initiation Function
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.player_x = player_x
        self.left = True
        self.right = False
        self.vel = 3
        self.walkCount = 0
        self.hitBox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 29
        self.visible = True

    def draw(self, window):     # This Function Draws the Function
        if self.visible:
            self.move()
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.right:
                window.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.left:
                window.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(window, (255, 0, 0), (self.hitBox[0], self.hitBox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0, 128, 0),
                             (self.hitBox[0], self.hitBox[1] - 20, 50 - ((50 / 29) * (29 - self.health)), 10))
            self.hitBox = (self.x + 17, self.y + 2, 31, 57)

    def move(self):     # This Function Moves the Enemy

        if self.x < self.player_x:
            self.right = True
            self.left = False
        elif self.x > self.player_x:
            self.left = True
            self.right = False

        if self.left:
            self.x -= self.vel
        elif self.right:
            pygame.time.delay(10)
            self.x += self.vel

    def hit(self):      # This is the function called when The Enemy is hit
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


class projectile(object):       # This is the Projectile Object.
    def __init__(self, x, y, facing2):      # The Initiation Function
        self.x = x
        self.y = y
        self.facing2 = facing2
        self.vel = facing2 * 8
        self.hitBox = (self.x, self.y, 16, 16)

    def draw(self, window):     # This Function draws the projectile on the screen
        self.hitBox = (self.x, self.y + 2, 16, 13)
        window.blit(bullet_img, (self.x, self.y))


def redraw_game_window():   # This is the Function that updates the game Window
    win.blit(bg, (0, 0))
    player1.draw(win)
    text = font.render("Score: " + str(score), 1, (0, 0, 0))
    win.blit(text, (700, 10))
    enemy1.draw(win)
    for bullet2 in bullets:
        bullet2.draw(win)
    font2 = pygame.font.SysFont('cosmicsans', 100)
    text1 = font2.render('You Win. Your Score = ' + str(score), 1, (0, 128, 0))
    if not enemy1.visible:
        win.blit(text1, ((screenWidth / 2) - (text1.get_width() / 2), (screenHeight / 2) - (text1.get_height() / 2)))
        pygame.display.update()
        while not enemy1.visible:
            pygame.time.delay(8000)
            pygame.quit()

    pygame.display.update()


# This Identifies the Main Function
if __name__ == '__main__':
    # Objects created
    player1 = player(0, 405, 64, 64)
    enemy1 = enemy(800, 410, 64, 64, player1.x)
    font = pygame.font.SysFont('cosmicsans', 30, True)
    shootLoop = 0
    bullets = []
    run = True

    # Main Loop
    while run:
        clock.tick(27)
        # This checks if the enemy and Player has collided or not
        if player1.hitBox[1] < enemy1.hitBox[1] + enemy1.hitBox[3] and player1.hitBox[1] + player1.hitBox[3] > \
                enemy1.hitBox[1]:
            if player1.hitBox[0] + player1.hitBox[2] > enemy1.hitBox[0] and player1.hitBox[0] < enemy1.hitBox[0] + \
                    enemy1.hitBox[2] and enemy1.visible:
                player1.hit()
                score -= 50

        # This is the Bullet Shooting limit setter
        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 7:
            shootLoop = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # For checking if the bullet hit anything or not
        for bullet in bullets:
            if bullet.y - 16 < enemy1.hitBox[1] + enemy1.hitBox[3] and bullet.y + 16 > enemy1.hitBox[1]:
                if bullet.x + 16 > enemy1.hitBox[0] and bullet.x - 16 < enemy1.hitBox[0] + enemy1.hitBox[2] \
                        and enemy1.visible:
                    hitSound.play()
                    enemy1.hit()
                    score += 10
                    bullets.pop(bullets.index(bullet))

            if bullet.x < screenWidth:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        # This gets the keys pressed
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()[0]

        # Checks if the right mouse button has been clicked or not
        if mouse and shootLoop == 0:
            player1.standing = False
            if player1.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 5:
                bullets.append(projectile(round(player1.x + player1.width // 2), round(player1.y + player1.height // 2),
                                          facing))
                bulletSound.play()
            shootLoop = 1

        # Checks if the Movement keys has been pressed or not
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player1.x > player1.vel:
            player1.x -= player1.vel
            player1.left = True
            player1.right = False
            player1.standing = False
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player1.x < screenWidth - player1.width - player1.vel:
            player1.x += player1.vel
            player1.right = True
            player1.left = False
            player1.standing = False
        else:
            player1.standing = True
            player1.walkCount = 0

        # Checks if the Space Bar has been pressed or not
        if not player1.isJump:
            if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
                player1.isJump = True
                player1.right = False
                player1.left = False
                player1.walkCount = 0
        else:
            if player1.jumpCount >= -10:
                neg = 1
                if player1.jumpCount < 0:
                    neg = -1
                player1.y -= (player1.jumpCount ** 2) * 0.5 * neg
                player1.jumpCount -= 1
            else:
                player1.isJump = False
                player1.jumpCount = 10
        enemy1.player_x = player1.x
        redraw_game_window()

    # Ends the game
    pygame.quit()
