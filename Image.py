import pygame, sys
from pygame import *

pygame.init()

xPos =400
yPos = 400

WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

corsairMeme = pygame.image.load('mousePad.jpg')
window = pygame.display.set_mode((WIDTH, HEIGHT),0, 32)
window.blit(corsairMeme, (0,0))


font = pygame.font.SysFont(None,40)
text = font.render("Corsair suddenly surrounded by darkness.",False,WHITE)
memeTalk = text.get_rect()



def greyScreen():
    pxarray = pygame.PixelArray(window)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = window.get_at((x,y)).r
            GREEN = window.get_at((x,y)).g
            BLUE = window.get_at((x,y)).b
            grey = (RED + GREEN + BLUE)/3

            pxarray[x,y] = (grey,grey,grey)

    del pxarray

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[K_ESCAPE]:
        pygame.quit()
        sys.exit()


    memeTalk.centerx = 400
    memeTalk.centery = 560


    pygame.draw.rect(window, 0, memeTalk, 10)
    window.blit(text,memeTalk)
    greyScreen()
    pygame.display.flip()
    pygame.display.update()