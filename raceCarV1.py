# Programmer: Noah Osterhout
# Date: February 2nd 2017 12:21PM EST
# Project: raceCarV1.py

import pygame

pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
# Set the width and height of the screen [width, height]
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
 
pygame.display.set_caption("Race Game")

#Image

caring = pygame.image.load('racecar.png')

# Funtion

def car(x,y):
    screen.blit(caring,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0 

# Loop until the user clicks the close button.
crashed = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not crashed:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    
    x += x_change
    
    screen.fill(WHITE)
    car(x,y)

    pygame.display.update()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
