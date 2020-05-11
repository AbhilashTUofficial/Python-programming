import pygame
import random
import math

pygame.init()
# window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space wars!")
backimg = pygame.image.load('background.png')

# player
playerimg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy

enemyimg = pygame.image.load('alien.png')
enemyX = random.randint(1, 735)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

bulletimg = pygame.image.load('bullet.png')
bulletX_change = 0
bulletY_change = 10
bulletX = 0
bulletY = 497
bullet_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy_go(x, y):
    screen.blit(enemyimg, (x, y))


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y))


def iscolision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((bulletX - enemyX), 2) + math.pow((bulletY - enemyY), 2))
    if distance < 27:
        return True






# gameloop
notgameover = True
while notgameover:
    screen.fill((0, 0, 0))
    screen.blit(backimg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notgameover = False

        # keystrok

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

          playerX = playerX + playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 735

     enemyX = enemyX + enemyX_change
    if enemyX <= 0:
            enemyX_change = 4
            enemyY += enemyY_change
    elif enemyX >= 736:
            enemyX_change = -4
            enemyY += enemyY_change







    if bulletY <= 0:
        bulletY = 497
        bullet_state = "ready"

    if bullet_state is "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change





        colision = iscolision(enemyX, enemyY, bulletX, bulletY)
        if colision:
            bulletY = 497
            bullet_state = "ready"
            score += 1
            enemyX = random.randint(0, 800)
            enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy_go(enemyX, enemyY)
    pygame.display.update()
