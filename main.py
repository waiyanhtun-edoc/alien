import pygame

#intilizattion of pygame
pygame.init()

#screen 
screen = pygame.display.set_mode((1000,600))

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

#draw ship on screen
def player(x,y):
    """Something"""
    screen.blit(playerImage,(x,y))


#Game Loop
running = True
while running:

    #Background color
    screen.fill((80,50,100))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_UP:
                playerY_change = -0.4
            if event.key == pygame.K_DOWN:
                playerY_change =  0.4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerY += playerY_change
    playerX += playerX_change
    player(playerX,playerY)
    pygame.display.update()