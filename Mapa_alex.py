import pygame, sys
from pygame.locals import *
from random import randint
pygame.init()

from Manzana import manzana_imagen
from Manzana import manzana
from Manzana import cell2coord


#COLORES
Naranja = (250, 87, 0)
Azul = (0, 113, 250)
Rojo = (227, 24, 14)
Amarillo = (219, 212, 9)
Lila = ( 153, 9, 219)
negro = (0,0,0)
Blanco = (255, 255, 255)
Verde = (0, 250, 54)
VerdeOsc = (0, 225, 3)


#PANTALLA
clasic = pygame.display.set_mode((1200,900))
pygame.display.set_caption("SNAKE")
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)


#BUCLE PANTALLA
while True:
    for evento in pygame.event.get():
        #SI SE PULSA LA X SE CIERRA
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    #BUCLE COLOR
    clasic.fill((negro))
    
    #LINEAS BORDE (650x650)
    pygame.surface.Surface
    fondo = pygame.image.load("fondo.png")
    posX= 0
    posY= 0
    #clasic.blit(fondo,(posX,posY))
    
    serpi = pygame.image.load("serpi.png")
    clasic.blit(serpi,cell2coord(5,5))

    pygame.draw.line(clasic,Rojo,(275,125),(937,125),2) #ROJO
    pygame.draw.line(clasic,Naranja,(937,125),(937,787),2) #NARANJA
    pygame.draw.line(clasic,Verde,(937,787),(275,787),2) #Verde
    pygame.draw.line(clasic,Azul,(275,787),(275,125),2) #Azul
    pygame.draw.circle(clasic, (8,70,120),(600,450),2)

    # Dibujar la manzana
    clasic.blit(manzana_imagen,(manzana))

    # Actualizar la pantalla
    pygame.display.update()