import pygame, sys
from pygame.locals import *
from random import randint

def abrir_juego():

    # INICIACION DE PYGAME
    pygame.init()

    # VENTANA TAMAÑO
    ventana = pygame.display.set_mode((1200,900))

    # CADA CUANTO SE MUEVE LA SERPIENTE
    añadirpixeles = 50

    # VELOCIDAD POR SEGUNDO A CUANTO SE MUEVE LA SERPIENTE
    FPS = 10
    reloj = pygame.time.Clock()

    # COLORES
    naranja = (250, 87, 0)
    azul = (0, 113, 250)
    rojo = (227, 24, 14)
    amarillo = (219, 212, 9)
    lila = ( 153, 9, 219)
    negro = (0,0,0)
    blanco = (255, 255, 255)
    verde = (0, 250, 54)

    # SERPIENTE , IMAGEN Y POSICION y
    serpiente_direccion = 'derecha' # dirección inicial
    serpiente = pygame.image.load("images/serpiente/serpientecabeza-derecha.png")
    posX = 275
    posY = 125
    
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
    manzana = pygame.image.load("images/comida.gif")
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
        ventana.blit(serpiente, (posX, posY))
        ventana.blit(borde,bordepos)
        ventana.blit(manzana, manzanapos)
        ventana.blit(quit, quitpos)

        # SI LAS POSICIONES TOCAN ESAS CORDENADAS, SE CIERRA EL JUEGO 
        if posX < 275 or posX > 900 or posY < 125 or posY > 760:
            pygame.quit()
            sys.exit()

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
                    serpiente = pygame.image.load("images/serpiente/serpientecabeza-izquierda.png")
                elif evento.key == K_d and serpiente_direccion != 'izquierda':
                    serpiente_direccion = 'derecha'
                    serpiente = pygame.image.load("images/serpiente/serpientecabeza-derecha.png")
                elif evento.key == K_w and serpiente_direccion != 'abajo':
                    serpiente_direccion = 'arriba'
                    serpiente = pygame.image.load("images/serpiente/serpientecabeza-arriba.png")
                elif evento.key == K_s and serpiente_direccion != 'arriba':
                    serpiente_direccion = 'abajo'
                    serpiente = pygame.image.load("images/serpiente/serpientecabeza-abajo.png")
        
        # ==========================
        # MOVIMIENTO DE LA SERPIENTE
        # ==========================

        # actualizar la posición de la serpiente en función de su dirección actual
        if serpiente_direccion == 'derecha':
            posX += añadirpixeles
        elif serpiente_direccion == 'izquierda':
            posX -= añadirpixeles
        elif serpiente_direccion == 'arriba':
            posY -= añadirpixeles
        elif serpiente_direccion == 'abajo':
            posY += añadirpixeles
        
        # limitar la posición de la serpiente para que no se mueva fuera de la pantalla
        if posX < 0:
            posX = 0
        elif posX >= ventana.get_width():
            posX = ventana.get_width() - añadirpixeles
        if posY < 0:
            posY = 0
        elif posY >= ventana.get_height():
            posY = ventana.get_height() - añadirpixeles

        # ==============================================


        """
        #LINEAS INTERIOR NEGRO VERTICALES(650x650)
        pygame.draw.line(ventana,negro,(334,774),(334,125),1) #LINEAV1
        pygame.draw.line(ventana,negro,(393,774),(393,125),1) #LINEAV2
        pygame.draw.line(ventana,negro,(452,774),(452,125),1) #LINEAV3
        pygame.draw.line(ventana,negro,(511,774),(511,125),1) #LINEAV4
        pygame.draw.line(ventana,negro,(570,774),(570,125),1) #LINEAV5
        pygame.draw.line(ventana,negro,(629,774),(629,125),1) #LINEAV6
        pygame.draw.line(ventana,negro,(688,774),(688,125),1) #LINEAV7
        pygame.draw.line(ventana,negro,(747,774),(747,125),1) #LINEAV8
        pygame.draw.line(ventana,negro,(806,774),(806,125),1) #LINEAV9
        pygame.draw.line(ventana,negro,(865,774),(865,125),1) #LINEAV10

        #LINEAS INTERIOR NEGRO HORIZONTALES(650x650)
        pygame.draw.line(ventana,negro,(275,184),(924,184),1) #LINEAH1
        pygame.draw.line(ventana,negro,(275,243),(924,243),1) #LINEAH2
        pygame.draw.line(ventana,negro,(275,302),(924,302),1) #LINEAH3
        pygame.draw.line(ventana,negro,(275,361),(924,361),1) #LINEAH4
        pygame.draw.line(ventana,negro,(275,420),(924,420),1) #LINEAH5
        pygame.draw.line(ventana,negro,(275,479),(924,479),1) #LINEAH6
        pygame.draw.line(ventana,negro,(275,538),(924,538),1) #LINEAH7
        pygame.draw.line(ventana,negro,(275,597),(924,597),1) #LINEAH8
        pygame.draw.line(ventana,negro,(275,656),(924,656),1) #LINEAH9
        pygame.draw.line(ventana,negro,(275,715),(924,715),1) #LINEAH10

        #LINEAS BORDE (650x650)
        pygame.draw.line(ventana,rojo,(275,125),(924,125),1) #ROJO
        pygame.draw.line(ventana,naranja,(924,125),(924,774),1) #NARANJA
        pygame.draw.line(ventana,lila,(924,774),(275,774),1) #LILA
        pygame.draw.line(ventana,azul,(275,774),(275,125),1) #AZUL

        #PUNTO CENTRAL DEL MAPA (600-450)
        pygame.draw.circle(ventana, (8,70,120),(600,450),1) #CIRCULO

        """

        # El mapa es desde el punto 275,125 hasta el punto 924,774
        # el mapa es un 650 x 650
        # 50x50 pixeles dentro de el cuadrado

        pygame.display.update()
        reloj.tick(FPS)