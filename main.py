import pygame
import random
import math

#intilizattion of pygame
pygame.init()

#score of 
score = 0

#screen 
screen = pygame.display.set_mode((1000,600))

#background image
background = pygame.image.load('backgroun.png')

#Title and icon
pygame.display.set_caption("Alien Invasion")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#player
playerImage = pygame.image.load('ship.png')
playerX  = 470
playerY  = 500
playerX_change = 0
playerY_change = 0

#enemy
enemyImage = pygame.image.load('enemy.png')
enemyX  = random.randint(0, 800)
enemyY  = random.randint(50, 150)
enemyX_change = 0.5
enemyY_change = 10

#bullet
bulletImage = pygame.image.load('bullet.png')
bulletX  = 0
bulletY  = 0
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

#draw ship on screen
def player(x,y):
    """Something"""
    screen.blit(playerImage,(x,y))

#draw enemy on screen
def enemy(x,y):
    """Something"""
    screen.blit(enemyImage,(x,y))

#bullet 
def fire_bullet(x,y):
    """Something"""
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage,(x + 15, y + 15))

#distance of enemy and bullet
def isCollision(enemyX,enemyY,bulletX,bulletY):
    """Somethings"""
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        return False



#Game Loop
running = True
while running:

    #Background color
    screen.fill((80,50,100))
    
    #Background image
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change =  1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    #set the boundaries of y coordinate
    playerY += playerY_change

    if playerY <= 0:
        playerY = 0
    elif playerY >= 535:
        playerY = 535

    #set the boundaries of x coordinate
    playerX += playerX_change

    if playerX <= 10:
        playerX = 10
    elif playerX >= 930:
        playerX = 930

    #bullet boundaries
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    #bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change


    #set the boundaries of enemy 
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.5
        enemyY += enemyY_change 
    elif enemyX >= 935:
        enemyX_change = -0.5  
        enemyY += enemyY_change
    
    #shoot enemy and add score
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX  = random.randint(0, 800)
        enemyY  = random.randint(50, 150)


    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()