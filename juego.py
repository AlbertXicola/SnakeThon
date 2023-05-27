import pygame, sys
from pygame.locals import *
from random import randint
import random
def cell2coord(row,col):
    return (275+(CELLSIZE*row), 125+(CELLSIZE*col))
CELLSIZE=50

def generar_posicion_aleatoria():
    x = random.randint(0, 12)
    y = random.randint(0, 12)
    return x, y



serpiente = ""

fila=6
col=1
serpiente_direccion = 'derecha'

def pintar_cabeza(ventana):
    global serpiente
    global serpiente_direccion
    # SERPIENTE , IMAGEN Y POSICION y
    if serpiente_direccion == 'derecha':
            serpiente = pygame.image.load("images/serpiente/cd.png")
    elif serpiente_direccion == 'izquierda':
            serpiente = pygame.image.load("images/serpiente/ci.png")
    elif serpiente_direccion == 'arriba':
            serpiente = pygame.image.load("images/serpiente/cb.png")
    elif serpiente_direccion == 'abajo':
            serpiente = pygame.image.load("images/serpiente/ca.png")
    pos=cell2coord(col,fila)
    posX = pos[0]
    posY = pos[1]
    ventana.blit(serpiente, (posX, posY))



manzana = ""
manzpos = [6,1]

colman = random.randint(0, 12)
filaman = random.randint(0, 12)


def pintar_manzana(ventana):
    # global posicionmanzana
    global manzana
    manzana = pygame.image.load("images/comida.png")
    pos=cell2coord(colman,filaman)
    posX = pos[0]
    posY = pos[1]
    ventana.blit(manzana, (posX, posY))

def crear_manzana(serp):
   
    manzpos = generar_posicion_aleatoria()
    if manzpos in serp:
        return crear_manzana(serp)
    else:
        return manzpos








def abrir_juego():
    global serpiente
    global serpiente_direccion
    global fila
    global col
    # global posicionmanzana
    global manzana
    global  manzpos
    

    # INICIACION DE PYGAME
    pygame.init()
    # VENTANA TAMAÑO
    ventana = pygame.display.set_mode((1200,900))


    # VELOCIDAD POR SEGUNDO A CUANTO SE MUEVE LA SERPIENTE
    FPS = 10
    reloj = pygame.time.Clock()


    pintar_cabeza(ventana)
    
    # CUADRICULA, IMAGEN Y POSICION
    cuadricula = pygame.image.load("images/cuadricula.png")
    cuadriculpos = (275, 125)

    # FONDO, IMAGEN Y POSICION
    superfondo = pygame.image.load("images/superfondo.png")
    superfondopos = (0, 0)

    # BORDE, IMAGEN Y POSICION
    borde = pygame.image.load("images/borde.png")
    bordepos = (266,116)

    # PRUEBA MANZANA, IMAGEN Y POSICION
    manzana = pygame.image.load("images/comida.png")
    manzanapos = (688, 538)
    
    # PRUEBA BOTON QUIT, IMAGEN Y POSCION
    quit = pygame.image.load("images/quit.png")
    quitpos = (800, 800)

    # EL MARCO QUE SI PULSAS DENTRO, SALES
    #                     posicion  ,  tamaño
    botonquit = pygame.Rect(800,800, 300, 85)

    
 
    # BUCLE DE EL JUEGO
    while True:

        # ACTIVACION DE IMAGENES 
        
        ventana.blit(superfondo, superfondopos)
        ventana.blit(cuadricula, cuadriculpos)
        pintar_cabeza(ventana)
        ventana.blit(borde,bordepos)
        pintar_manzana(ventana)

        
        ventana.blit(quit, quitpos)

        # SI LAS POSICIONES TOCAN ESAS CORDENADAS, SE CIERRA EL JUEGO 
        if col < 0 or col > 12 or fila < 0 or fila > 12:
            exit()
        # SI SE TOCA UNA TECLA, PASA ALGO, RESPECTIVAMENTE
        for evento in pygame.event.get():
            if evento.type == QUIT:     # AQUI PARA CERRAR EL PROGRAMA
                pygame.quit()
                sys.exit()

                    # AQUI LA PARTE QUE HACE FUNCIONAR EL QUIT
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botonquit.collidepoint(evento.pos):
                    pygame.quit()
                    quit()


        # AQUI EL MOVIMIENTO DE LA SERPIENTE OCN SU FOTO
            elif evento.type == KEYDOWN:
                if evento.key == K_a and serpiente_direccion != 'derecha':
                    serpiente_direccion = 'izquierda'
                elif evento.key == K_d and serpiente_direccion != 'izquierda':
                    serpiente_direccion = 'derecha'
                elif evento.key == K_w and serpiente_direccion != 'abajo':
                    serpiente_direccion = 'arriba'
                elif evento.key == K_s and serpiente_direccion != 'arriba':
                    serpiente_direccion = 'abajo'
        
        # ==========================
        # MOVIMIENTO DE LA SERPIENTE
        # ==========================

        # actualizar la posición de la serpiente en función de su dirección actual
        if serpiente_direccion == 'derecha':
            col+=1
        elif serpiente_direccion == 'izquierda':
            col-=1
        elif serpiente_direccion == 'arriba':
            fila-=1
        elif serpiente_direccion == 'abajo':
            fila+=1
        

        """
        pos=cell2coord(col,fila)
        posX = pos[0]
        posY = pos[1]
        
        # limitar la posición de la serpiente para que no se mueva fuera de la pantalla
        if posX < 0:
            posX = 0
        elif posX >= ventana.get_width():
            posX = ventana.get_width() - añadirpixeles
        if posY < 0:
            posY = 0
        elif posY >= ventana.get_height():
            posY = ventana.get_height() - añadirpixeles
        """
        # ==============================================


        pygame.display.update()
        reloj.tick(FPS)
abrir_juego()