BACKGROUND_IMAGE = 'assets/Espacio.png'
AMPLADA = 1280
ALTURA = 720
import pygame
pygame.init()
#screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
screen = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Hello, World!")
background = pygame.image.load(BACKGROUND_IMAGE).convert()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        screen.blit(background, (0,0))
        pygame.display.update()
