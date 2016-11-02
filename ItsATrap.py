import random
import pygame, sys
from pygame import *

pygame.init()

WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT),0, 32)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

counter = 0


OGTrap = pygame.image.load('TrapItsATrap.jpg')
IDontAlways = pygame.image.load('TrapIDontAlways.jpg')
IheardIts = pygame.image.load('TrapIHeardItsATrap.jpg')
ImNotSaying = pygame.image.load('TrapImNotSaying.jpg')
ElaborateRuse = pygame.image.load('TrapItsAnElaborateRuse.jpg')

while True:
    counter +=1
    if counter >=750:
        counter = 0




    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    pygame.display.update()