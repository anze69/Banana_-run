import pygame
import sys
import math

pygame.init()

win = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

bg = pygame.image.load('pixil-frame-0(20).png')

# music

music = pygame.mixer.music.load("6434875305885696.mp3")
pygame.mixer.music.play(-1)

# player
playerImg = pygame.image.load('pixil-frame-0(14).png')
px = 50
py = 440
hight = 60
widh = 40
vel = 3

# Title and ja
pygame.display.set_caption("Bannana run")
Icon = pygame.image.load('pixil-frame-0(14).png')
pygame.display.set_icon(Icon)

# Coin
coinImg = pygame.image.load('pixil-frame-0(7).png')
coinX = 100
coinY = 440
hight = 60
widh = 40

# varnostnik
varnostnikImg = pygame.image.load('pixil-frame-0(26).png')
varnostnikX = 470
varnostnikY = 440
varnostnikHight = 70
varnostnikWidh = 50

# Chest
chestImg = pygame.image.load('pixil-frame-0(21).png')
chstX = 190
chestY = 460
hight = 60
chestWidh = 50

# gun
gunImg = pygame.image.load('pixil-frame-0(26).png')
gunX = 50
gunY = 50
gunWidh = 60
gunHight = 40

kkkl = pygame.mixer.Sound("20210321_170809.mp3")
kkkl.play()

def coin():
    win.blit(coinImg, (coinX, coinY))


def player():
    win.blit(playerImg, (px, py))

def chest():
    win.blit(chestImg, (chstX, chestY))

def gun():
    win.blit(gunImg, (gunX, gunY))

def varnostnik():
    win.blit(varnostnikImg, (varnostnikX, varnostnikY))

    pygame.display.update()


def isCollision(x, y, coinX, coinY):
    distance = math.sqrt(math.pow(coinX - x, 2) + (math.pow(coinY - y, 2)))
    if distance < 27:
        return True
    else:
        return False


def isCollision2(x, y, chstX, chestY):
    distance2 = math.sqrt(math.pow(chstX - x, 2) + (math.pow(chestY - y, 2)))
    if distance2 < 27:
        return True
    else:
        return False


def isCollision3(x, y, gunX, gunY):
    distance3 = math.sqrt(math.pow(gunX - x, 2) + (math.pow(gunY - y, 2)))
    if distance3 < 27:
        return True
    else:
        return False

def isCollision4(varnostnikX, varnostnikY, px, py):
    distance4 = math.sqrt(math.pow(px - varnostnikX, 2) + (math.pow(py - varnostnikY, 2)))
    if distance4 < 27:
        return True
    else:
        return False

run = True
while run:

    win.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and px > vel:
        px -= vel
    elif keys[pygame.K_RIGHT] and px < 500 - widh - vel:
        px += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0

    collision = isCollision(coinX, coinY, px, py)
    if collision:
        bulletSound = pygame.mixer.Sound("Game_bullet.mp3")
        bulletSound.play()
        coinImg = pygame.image.load('pixil-frame-0(26).png')
        if keys[pygame.K_UP] and py > vel:
            py -= vel
        if keys[pygame.K_DOWN] and py < 500 - hight - vel:
            py += vel

    collision2 = isCollision2(chstX, chestY, px, py)
    if collision2:
        varnostnikImg = pygame.image.load('pixil-frame-0(32).png')
        chestImg = pygame.image.load('pixil-frame-0(24).png')
        gunX = 210
        gunY = 450
        gunImg = pygame.image.load('pixil-frame-0(23).png')

    collision3 = isCollision3(gunX, gunY, px, py)
    if collision3:
        gunImg = pygame.image.load('pixil-frame-0(26).png')
        playerImg = pygame.image.load('pixil-frame-0(29).png')

    coin()
    player()
    chest()
    gun()
    varnostnik()

pygame.quit()
