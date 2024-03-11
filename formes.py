import pygame
import sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE, ALT)
BLANC = (255, 255, 255)
VERMELL = (255, 0, 0)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Rectangle')

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)

    # Dibujar la letra "E" usando rectángulos rojos
    pygame.draw.rect(pantalla, VERMELL, pygame.Rect(100, 100, 400, 100))  # Parte horizontal superior de la "E"
    pygame.draw.rect(pantalla, VERMELL, pygame.Rect(100, 100, 100, 400))  # Parte vertical izquierda de la "E"
    pygame.draw.rect(pantalla, VERMELL, pygame.Rect(100, 250, 400, 100))  # Parte horizontal del medio de la "E"
    pygame.draw.rect(pantalla, VERMELL, pygame.Rect(100, 400, 400, 100))  # Parte horizontal inferior de la "E"

    pygame.display.update()
