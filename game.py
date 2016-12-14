import pygame, sys
import pygame.event as GAME_EVENTS
from random import randint
from time import sleep
pygame.init()

frameRate= 0.05
speed = 20

posX = 250
posY = 250


window = pygame.display.set_mode((500,400))
while True:
    window.fill((0,0,0))
    pygame.draw.rect(window, (randint(0,255),randint(0,255),randint(0,255)), (0,0, 50, 30) )
    pygame.draw.circle(window, (randint(0,255),randint(0,255),randint(0,255)), (posX,posY), 20, 0 )
    pygame.draw.circle(window, (randint(0,255),randint(0,255),randint(0,255)), (posX,posY), 22, 1 )

    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                posX = posX - speed
            if event.key == pygame.K_RIGHT:
                posX = posX + speed
            if event.key == pygame.K_UP:
                posY = posY - speed
            if event.key == pygame.K_DOWN:
                posY = posY + speed
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    ##     if event.type == pygame.KEYUP:
    ##        if event.key == pygame.K_LEFT:
    ##            leftDown = True
    ##        if event.key == pygame.K_RIGHT:
    ##            rightDown = True
    ##        if event.key == pygame.K_UP:
    ##            haveJumped = True
    ##        if event.key == pygame.K_DOWN:
    ##            haveJumped = True
    
    pygame.display.update()
    sleep(frameRate)
