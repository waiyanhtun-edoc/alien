from tkinter import font
import pygame
import random
import math
from pygame import mixer

#intilizattion of pygame
pygame.init()

#score of 
score_value = 0
font = pygame.font.Font('RobotoSlab-Medium.ttf',32)

textX = 10
textY = 10
 

#screen 
screen = pygame.display.set_mode((1000,600))

#background image
background = pygame.image.load('backgroun.png')

#background sond
background_song = mixer.Sound('background.mp3')
background_song.play(-1)

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


#enemy list
enemyImage = []
enemyX  = []
enemyY  = []
enemyX_change = []
enemyY_change = []
number_enemy = 100

#enemy
for i in range(number_enemy):
    enemyImage.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(10)

#bullet
bulletImage = pygame.image.load('bullet.png')
bulletX  = 0
bulletY  = 0
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#show text of score

def show_score(x,y):
    score = font.render("Score :) " + str(score_value),True,(250,200,255))
    screen.blit(score,(x,y))



#draw ship on screen
def player(x,y):
    """Something"""
    screen.blit(playerImage,(x,y))

#draw enemy on screen
def enemy(x,y,i):
    """Something"""
    screen.blit(enemyImage[i],(x,y))

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
    if distance < 50:
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
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_UP:
                playerY_change = -4
            if event.key == pygame.K_DOWN:
                playerY_change =  4
            if event.key == pygame.K_SPACE:
                bullet_song = mixer.Sound('pbullet.wav')
                bullet_song.play()
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
    for i in range(number_enemy):

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change [i]
        elif enemyX[i] >= 935:
            enemyX_change[i] = -3 
            enemyY[i] += enemyY_change[i]

            
    
        #shoot enemy and add score
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_song = mixer.Sound('explosion1.wav')
            explosion_song.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i]  = random.randint(0, 800)
            enemyY[i]  = random.randint(50, 150)
        
        enemy(enemyX[i],enemyY[i],i)


    show_score(textX,textY)
    player(playerX,playerY)
    pygame.display.update()