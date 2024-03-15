import pygame                                                         
import sys                                                            
from pygame.locals import *                                           
                                                                      
AMPLE = 800                                                           
ALT = 600                                                             
TAMANY = (AMPLE, ALT)                                                 
NEGRE = (0, 0, 0)                                                     
VERMELL = (255, 0, 0, 0)                                              
BLANC = (255, 255, 255)                                               
VERDE = (0, 255, 0)                                                   
BLAU = (0, 0, 255)                                                    
                                                                      
pygame.init()                                                         
pantalla = pygame.display.set_mode(TAMANY)                            
pygame.display.set_caption('Rectángulo')                              
                                                                      
while True:  # main game loop                                         
    for event in pygame.event.get():                                  
        if event.type == QUIT:                                        
            pygame.quit()                                             
            sys.exit()                                                
                                                                      
    pantalla.fill(BLANC)                                              
    pygame.draw.rect(pantalla, NEGRE, (105, 180, 600, 230))           
    pygame.draw.rect(pantalla, BLANC, (128, 210, 550, 170))           
    pygame.draw.rect(pantalla, BLAU, (150, 230, 500, 130))            
    pygame.draw.rect(pantalla, VERDE, (174, 250, 450, 90))            
    pygame.draw.rect(pantalla, VERMELL, (200, 270, 400, 50))          
                                                                      
                                                                      
    pygame.display.update()                                           
