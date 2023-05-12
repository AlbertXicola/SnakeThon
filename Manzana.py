import random
import pygame, sys
from pygame.locals import *
from random import randint
CELLSIZE=50
# Calculadora de posicion cuadriculada
def cell2coord(row,col):
    return (275+(CELLSIZE*row), 125+(CELLSIZE*col))

# Posicion aleatoria de la manzana
def generar_posicion_aleatoria():
    x = random.randint(0, 12)
    y = random.randint(0, 12)

    return cell2coord(x,y)



#Carga imagen manzana
manzana_imagen = pygame.image.load("images/comida.png")

