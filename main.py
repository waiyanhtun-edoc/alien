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
playerImg_Change = 0

#draw ship on screen
def player(x,y):
    """Something"""
    screen.blit(playerImage,(x,y))


#Game Loop
running = True
while running:

    #Background color
    screen.fill((80,50,100))
    playerY -= 0.1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        

    player(playerX,playerY)
    pygame.display.update()