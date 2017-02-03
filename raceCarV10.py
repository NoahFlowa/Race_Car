# Programmer: Noah Osterhout
# Date: February 2nd 2017 12:21PM EST
# Project: raceCarV1.py

import pygame
import time
import random

pygame.init()
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

playGame = (3,155,229)
quitGame = (255,87,34)

pgHover = (255,87,34)
qgHover = (3,155,229)

block_color = (2, 119, 189)

car_width = 73
 
 
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
 
pygame.display.set_caption("Race Game")

caring = pygame.image.load('racecar.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, BLACK)
    screen.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(screen, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    screen.blit(caring,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("OpenSans-Light.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)

    game_loop()

def crash():
    message_display("You crashed!")

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(WHITE)
        largeText = pygame.font.Font("OpenSans-Light.ttf", 115)
        TextSurf, TextRect = text_objects("8 bit Racey", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        screen.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        print(mouse)

        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(screen, pgHover, (150, 450, 100, 50))
        else:
            pygame.draw.rect(screen, playGame, (150, 450, 100, 50))

        if 550 + 100 > mouse[0] > 550 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(screen, qgHover, (550, 450, 100, 50))
        else:
            pygame.draw.rect(screen, quitGame, (550, 450, 100, 50))
        
        pygame.display.update()
        
    clock.tick(15)
    
def game_loop():
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 3
    thing_width = 100
    thing_height = 100

    thing_count = 1

    dodged = 0
    
    gameExit = False
     
    clock = pygame.time.Clock()
     
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            print("y crossover")
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print("x crossover")
                crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
