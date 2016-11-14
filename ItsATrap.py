import random
import pygame, sys
from pygame import *

pygame.init()

WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT),0, 32)


counter = 0
randomNum = random.randint(0,4)

trapMemes = [pygame.image.load('TrapItsATrap.jpg'),pygame.image.load('TrapIDontAlways.jpg'),pygame.image.load('TrapIHeardItsATrap.jpg'),pygame.image.load('TrapImNotSaying.jpg'),pygame.image.load('TrapItsAnElaborateRuse.jpg')]

while True:
    counter +=1
    if counter >=750:
        counter = 0
        randomNum = random.randint(0,4)




    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    window.blit(trapMemes[randomNum],(0,0))
    pygame.display.update()