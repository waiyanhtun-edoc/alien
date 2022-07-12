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

#draw ship on screen
def player():
    """Something"""
    screen.blit(playerImage,(playerX,playerY))


#Game Loop
running = True
while running:

    #Background color
    screen.fill((80,50,100))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        

    player()
    pygame.display.update()