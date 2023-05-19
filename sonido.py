import pygame, sys
from pygame.locals import *
from self import self


#Cargar una cancion/musica de fondo
self.Cargar = pygame.mixer.music.load('songs/Game.mp3')
#Poner en play un sonido/musica de fondo en bucle
self.play = pygame.mixer.music.play(-1)
#Pausar musica/sonido de fondo
self.play = pygame.mixer.music.pause


#Establecer el sonido de la manzana 
self.manzana = pygame.mixer.Sound('songs/manzana.mp3')
#play una sola vez el sonido de la manzana
self.manzana.play()


#Establecer el sonido de la muerte
self.lose = pygame.mixer.Sound('songs/Lose.mp3')
#play una sola vez el sonido de la muerte
self.lose.play()


#Establecer el sonido de los botones
self.button = pygame.mixer.Sound('songs/button.mp3')
#play una sola vez el sonido de los botones
self.button.play()