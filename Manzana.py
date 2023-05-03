import random
import pygame, sys
from pygame.locals import *
from random import randint

def cell2coord(row,col):
    return (277+(60*row), 127+(60*col))

#Posicion aleatoria de la manzana
def generar_posicion_aleatoria(ancho, alto):
    x = random.randint(0, 10)
    y = random.randint(0, 10)

    return cell2coord(x,y)

ancho = 650
alto = 650
manzana = generar_posicion_aleatoria(ancho, alto)


#Carga imagen manzana
manzana_imagen = pygame.image.load("manzana.png")

# Dibujar la manzana
clasic.blit(manzana_imagen,(manzana))