import pygame, sys
from pygame import *

pygame.init()

WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

counter = 0
counterIncrease = False

complexMeme = pygame.image.load('whatTheyThinkWeDo.jpg')
simpleMeme = pygame.image.load('whatWeActuallyDo.jpg')



window = pygame.display.set_mode((WIDTH, HEIGHT),0, 32)
font = pygame.font.SysFont(None,52)
text = font.render("",False,BLACK)
memeTalk = text.get_rect()


while True:

    if counterIncrease == False:
        counter -= 1
        window.blit(simpleMeme,(0,0))
        if counter <= 0:
            counterIncrease = True
            text = font.render("What they think we do.", False, WHITE)
    elif counterIncrease == True:
        counter +=1
        window.blit(complexMeme,(0,0))
        if counter >= 500:
            counterIncrease = False
            text = font.render("What we really do.", False, BLACK)

    pressed = pygame.key.get_pressed()
    if pressed[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    memeTalk.centerx = 210
    memeTalk.centery = 550
    pygame.draw.rect(window, 0, memeTalk,1)
    window.blit(text, memeTalk)
    pygame.display.update()