import pygame
from pygame.locals import *
from random import randint
import datetime
import pygame.font

def reiniciar_juego():
    global serpiente
    global serpiente_direccion
    global fila
    global col
    global puntManzanas
    global serpiente_cuerpo
    global colman
    global filaman

    serpiente = ""
    fila = 6
    col = 1
    serpiente_direccion = 'derecha'
    puntManzanas = 0
    colman, filaman = 8, 6
    serpiente_cuerpo = [(col, fila)]
    
serpiente = ""
fila = 6
col = 1
serpiente_direccion = 'derecha'
puntManzanas = 0
manzana = ""
colman, filaman = 8, 6   # Posición inicial de la manzana

def nivel3():
    pygame.mixer.music.load("songs/nivel3.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    def cell2coord(row, col):
        return (275 + (CELLSIZE * row), 125 + (CELLSIZE * col))

    CELLSIZE = 50

    def mostrar_marcador(ventana, puntManzanas):
        fuente = pygame.font.SysFont("impact", 36,)  # Fuente y tamaño del texto
        texto = fuente.render(str(puntManzanas), False, (30, 64, 24))  # Crear el texto a mostrar
        posicion = (1089, 451)  # Posición del texto en la ventana
        ventana.blit(texto, posicion)  # Dibujar el texto en la ventana


    def savepoints():
        archivo = open("puntuacion.txt", "a")
        archivo.write(str(datetime.datetime.now()) + ', NIVEL DIFICIL: ' + str(puntManzanas) + "\n")
        archivo.close()

    def pintar_cabeza(ventana):
        global serpiente
        global serpiente_direccion
        # SERPIENTE, IMAGEN Y POSICION
        if serpiente_direccion == 'derecha':
            serpiente = pygame.image.load("images/serpiente1/caraderecha.png")
        elif serpiente_direccion == 'izquierda':
            serpiente = pygame.image.load("images/serpiente1/caraizquierda.png")
        elif serpiente_direccion == 'arriba':
            serpiente = pygame.image.load("images/serpiente1/cararriba.png")
        elif serpiente_direccion == 'abajo':
            serpiente = pygame.image.load("images/serpiente1/carabajo.png")
        pos = cell2coord(col, fila)
        posX = pos[0]
        posY = pos[1]
        ventana.blit(serpiente, (posX, posY))

    def pintar_cuerpo(ventana):
        global serpiente_cuerpo
        for i, segmento in enumerate(serpiente_cuerpo[1:]):
            col_segmento, fila_segmento = segmento
            col_anterior, fila_anterior = serpiente_cuerpo[i]
            direccion_x = col_segmento - col_anterior
            direccion_y = fila_segmento - fila_anterior
            if direccion_x == 1:
                imagen_segmento = pygame.image.load("images/serpiente1/cuerpo.png")
            elif direccion_x == -1:
                imagen_segmento = pygame.image.load("images/serpiente1/cuerpo.png")
            elif direccion_y == 1:
                imagen_segmento = pygame.image.load("images/serpiente1/cuerpo.png")
            else:
                imagen_segmento = pygame.image.load("images/serpiente1/cuerpo.png")
            pos = cell2coord(col_segmento, fila_segmento)
            posX = pos[0]
            posY = pos[1]
            ventana.blit(imagen_segmento, (posX, posY))

  


    def pintar_manzana(ventana):
        global manzana
        manzana = pygame.image.load("images/comida.png")
        pos = cell2coord(colman, filaman)
        posX = pos[0]
        posY = pos[1]
        ventana.blit(manzana, (posX, posY))

    def crear_manzana():
        global colman, filaman
        while (colman, filaman) in serpiente_cuerpo:
            colman, filaman = randint(0, 12), randint(0, 12)

    def abrir_juego():
        global serpiente
        global serpiente_direccion
        global fila
        global col
        global puntManzanas
        global serpiente_cuerpo

        # INICIACION DE PYGAME
        pygame.init()
        # VENTANA TAMAÑO
        ventana = pygame.display.set_mode((1200, 900))

        # VELOCIDAD POR SEGUNDO A CUANTO SE MUEVE LA SERPIENTE
        FPS = 20
        reloj = pygame.time.Clock()

        serpiente_cuerpo = [(col, fila)]

        pintar_cabeza(ventana)

        # CUADRICULA, IMAGEN Y POSICION
        cuadricula = pygame.image.load("images/cuadricula-roja.png")
        cuadriculpos = (275, 125)

        # Movida
        movida = pygame.image.load("images/movida.png")
        posmovida = (985, 210)

        movida1 = pygame.image.load("images/movida.png")
        posmovida1 = (50, 210)

        # FONDO, IMAGEN Y POSICION
        superfondo = pygame.image.load("images/superfondo-dificil.png")
        superfondopos = (0, 0)

        # PUNTUACION FONDO
        fondopuntuacion = pygame.image.load("images/fondopunt.png")
        cordfondopunt = (1020, 450)
        # menu again
        pmenuagain = pygame.image.load("images/quit.png")
        corsmenuagain = (630, 400)

        # play
        playagain = pygame.image.load("images/again.png")
        corsplayagain = (270, 400)
        
        cuadriculaperd = pygame.image.load("images/cuadricula-roja_perdido.png")
        cuadriculposperd = (275, 125)

        # BORDE, IMAGEN Y POSICION
        borde = pygame.image.load("images/borde.png")
        bordepos = (266, 116)



        # BUCLE DE EL JUEGO
        while True:
            # ACTIVACION DE IMAGENES
            
            ventana.blit(superfondo, superfondopos)
            ventana.blit(movida, posmovida)
            ventana.blit(movida1, posmovida1)
            ventana.blit(cuadricula, cuadriculpos)
            ventana.blit(fondopuntuacion, cordfondopunt)
            pintar_cabeza(ventana)
            pintar_cuerpo(ventana)
            ventana.blit(borde, bordepos)
            pintar_manzana(ventana)        
            mostrar_marcador(ventana, puntManzanas)

            
            if (col, fila) in serpiente_cuerpo[1:]:
                pygame.mixer.music.set_volume(0.5)
                ventana.blit(cuadriculaperd, cuadriculposperd)
                ventana.blit(pmenuagain, corsmenuagain)
                ventana.blit(playagain, corsplayagain)
                botonagain = pygame.Rect(270, 400, 300, 85)
                botonmenu = pygame.Rect(630, 400, 300, 85)
                for evento in pygame.event.get():
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if botonmenu.collidepoint(evento.pos):
                            savepoints()
                            reiniciar_juego()
                            return 
     
                        if botonagain.collidepoint(evento.pos):

                            savepoints()
                            reiniciar_juego()
     

            if col < 0 or col > 12 or fila < 0 or fila > 12:
                
                pygame.mixer.music.set_volume(0.5)
                ventana.blit(cuadriculaperd, cuadriculposperd)
                ventana.blit(pmenuagain, corsmenuagain)
                ventana.blit(playagain, corsplayagain)
                botonagain = pygame.Rect(270, 400, 300, 85)
                botonmenu = pygame.Rect(630, 400, 300, 85)
                for evento in pygame.event.get():
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if botonmenu.collidepoint(evento.pos):
                            savepoints()
                            reiniciar_juego()
                            return 
     
                        if botonagain.collidepoint(evento.pos):

                            savepoints()
                            reiniciar_juego()
     
            

            # SI SE TOCA UNA TECLA, PASA ALGO, RESPECTIVAMENTE
            for evento in pygame.event.get():
                if evento.type == QUIT:  # AQUI PARA CERRAR EL PROGRAMA
                    savepoints()
                    pygame.quit()
                    quit()


                # AQUI EL MOVIMIENTO DE LA SERPIENTE CON SU FOTO
                elif evento.type == KEYDOWN:
                
                    if evento.key == K_a and serpiente_direccion != 'derecha':
                        serpiente_direccion = 'izquierda'
                    elif evento.key == K_d and serpiente_direccion != 'izquierda':
                        serpiente_direccion = 'derecha'
                    elif evento.key == K_w and serpiente_direccion != 'abajo':
                        serpiente_direccion = 'arriba'
                    elif evento.key == K_s and serpiente_direccion != 'arriba':
                        serpiente_direccion = 'abajo'

            # MOVIMIENTO DE LA SERPIENTE
            if serpiente_direccion == 'derecha':
                col += 1
            elif serpiente_direccion == 'izquierda':
                col -= 1
            elif serpiente_direccion == 'arriba':
                fila -= 1
            elif serpiente_direccion == 'abajo':
                fila += 1

            # Agregar nueva posición de la cabeza al inicio del cuerpo de la serpiente
            serpiente_cuerpo.insert(0, (col, fila))

            # Si la posición de la serpiente coincide con la posición de la manzana, generar una nueva posición para la manzana
            if (fila, col) == (filaman, colman):

                puntManzanas += 1
                crear_manzana()
            else:
                # Si no come una manzana, eliminar la última posición del cuerpo de la serpiente
                serpiente_cuerpo.pop()

            pygame.display.update()
            reloj.tick(FPS)
    abrir_juego()