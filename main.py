from cProfile import run
from numpy import diff
import pygame

#intilizattion of pygame
pygame.init()

#screen 
screen = pygame.display.set_mode((1000,600))

#Title and icon
pygame.display.set_caption("Alien Invasion")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Background color
        screen.fill((250,200,255))
        pygame.display.update()