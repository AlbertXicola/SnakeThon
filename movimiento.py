import pygame
import sys
from pygame.locals import *
from random import randint
#Velocidad de movimiento del gusano:
velocidad=20
#Izquierda o derecha:
Direccion=True
#posicion de inicio de partida:
posX, posY =randint(1,400), randint(1,300)



#posicionar la serpiente en el mapeado inicial:
pygame.draw.rect(ventana,colorFigura, (posX,posY,40,40))
#indicador de donde esta la serpiente y direccion a la que va:
    elif evento.type== pygame.KEYDOWN:
        if evento.key == K_LEFT:
            posX-=velocidad
            if posX<0:
                posX=0
        elif evento.key == K_RIGHT:
            posX+=velocidad
            if posX<500-40:
                    posX=500-40
        elif evento.key == K_UP:
            posY-=velocidad
            if posY<0:
                posy=0
        elif evento.key== K_DOWN:
            posY+=velocidad
            if posY>(400-40):
                posY=400-40
