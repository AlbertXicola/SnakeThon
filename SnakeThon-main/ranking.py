import pygame, sys
from pygame.locals import *
from random import randint

pygame.mixer.init()


def rankingmenu():
    # INICIACION DE PYGAME
    pygame.init()

    pygame.mixer.music.load("songs/intro.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    def mostrar_puntuacion():
    # Abre el archivo de puntuación en modo de lectura
        with open("puntuacion.txt", "r",) as archivo:
            puntuacion = archivo.read()
            lineas = archivo.readlines()

        # Inicialización de Pygame
        pygame.init()

        # FUENTE DE LOS TEXTOS
        fuente = pygame.font.Font(None, 20)

        # Renderiza el contenido del archivo como un objeto de texto
        tecsto = fuente.render(puntuacion, True, (255, 255, 255))
        menu.blit(tecsto, (100, 100))
            # Dibuja el objeto de texto en la pantalla
        for linea in lineas:
            puntuacion += linea.strip() + " "

    # PANTALLA VENTANA
    W,H = 1200,900
    menu = pygame.display.set_mode((W,H))

    # VELOCIDAD POR SEGUNDO A CUANTO SE MUEVE ALGO
    fps = 800
    reloj = pygame.time.Clock()

    # FUENTE DE LOS TEXTOS
    fuente = pygame.font.Font(None, 20)

    # FONDO DEL JUEGO
    fondo = pygame.image.load("images/fondomenu2.png")
    # Variable de el fondo, x empieza en 0
    x=0



    # IMAGENES MENU Y SUS COORDS

    back = pygame.image.load("images/back.png")
    coordsback = (450, 720)


    # ICONO Y TITULO
    pygame.display.set_caption("SnakeThon")
    icon = pygame.image.load('images/logo.png').convert()
    pygame.display.set_icon(icon)

    # TEXTO DE LA PANTALLA
    text = "snapshot V3.1"
    mensaje = fuente.render(text, 10, (255,255,255))
    coordstextoversion = (1100, 880)

    # EL MARCO QUE SI PULSAS DENTRO, PASA LO QUE DICE EN EL BUCLE

    #                        posicion  ,  tamaño
    botonback = pygame.Rect(450, 720,300, 85)


    while True:


        #SE PUEDE DESGLOSaR PERO ES MEJOR ASI 


        # FONDO EN MOVIMIENTO
        # SE DIVIDE EL VALOR DE X POR  EL ANCHO DE LA IMAGEN DEL FONDO Y DEVUELVE EL RESTO
        x_bailonga = x % fondo.get_rect().width
        menu.blit(fondo,(x_bailonga - fondo.get_rect().width,0))
        if x_bailonga < W:
            menu.blit(fondo,(x_bailonga,0))
        x -= 1

        # DIBUJA LAS IMAGENES
        menu.blit(mensaje, coordstextoversion)
        menu.blit(back, coordsback)
        mostrar_puntuacion()





        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botonback.collidepoint(evento.pos):
                    from menu import menumain
                    menu.menumain
                    quit()

        pygame.display.update()
        reloj.tick(fps)
        mostrar_puntuacion()




