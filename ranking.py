import pygame, sys
from pygame.locals import *
from random import randint
from juego import abrir_juego

def abrir_ranking():
    # INICIACION DE PYGAME
    pygame.init()

    # PANTALLA VENTANA
    W,H = 1200,900
    menu = pygame.display.set_mode((W,H))

    # VELOCIDAD POR SEGUNDO A CUANTO SE MUEVE ALGO
    fps = 600
    reloj = pygame.time.Clock()

    # FUENTE DE LOS TEXTOS
    fuente = pygame.font.Font(None, 20)

    # FONDO DEL JUEGO
    fondo = pygame.image.load("images/fondomenu.png")
    # Variable de el fondo, x empieza en 0
    x=0

    # IMAGENES MENU Y SUS COORDS
    score = pygame.image.load("images/score.png")
    coordscore = (350, 50)
    quit = pygame.image.load("images/quit.png")
    coordsquit = (30, 700)

    # ICONO Y TITULO
    pygame.display.set_caption("SnakeThon")
    icon = pygame.image.load('images/logo.png').convert()
    pygame.display.set_icon(icon)

    # TEXTO DE LA PANTALLA
    text = "snapshot V1.1"
    mensaje = fuente.render(text, 10, (255,255,255))
    coordstextoversion = (1100, 880)

    # EL MARCO QUE SI PULSAS DENTRO, PASA LO QUE DICE EN EL BUCLE
    #                    posicion  ,  tamaño
    botonquit = pygame.Rect(150,700,300, 85)



    # BUCLE DEL JUEGO

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Verifica si se hizo clic en el botón
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botonquit.collidepoint(evento.pos):
                    pygame.quit()
                    quit()
            

        #SE PUEDE DESGLOSaR PERO ES MEJOR ASI 


        # FONDO EN MOVIMIENTO
        # SE DIVIDE EL VALOR DE X POR  EL ANCHO DE LA IMAGEN DEL FONDO Y DEVUELVE EL RESTO
        x_bailonga = x % fondo.get_rect().width
        menu.blit(fondo,(x_bailonga - fondo.get_rect().width,0))
        if x_bailonga < W:
            menu.blit(fondo,(x_bailonga,0))
        x -= 1

        # DIBUJA LAS IMAGENES
        menu.blit(score, coordscore)
        menu.blit(mensaje, coordstextoversion)
        menu.blit(quit, coordsquit)

        pygame.display.update()
        reloj.tick(fps)


