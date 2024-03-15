import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0,0)
BLANC = (255,255,255)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Cercle')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)
    pygame.draw.rect(pantalla, NEGRE, (199, 199, 201, 205))
    pygame.draw.circle(pantalla, VERMELL, (300,300),100)
    pygame.draw.polygon(pantalla, (0, 255, 170), [(305, 198), (100, 400), (369, 369)], )
    pygame.display.update()
