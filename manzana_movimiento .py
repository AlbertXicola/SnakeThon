import pygame, sys

pygame.init()

# Configuración de la pantalla
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mostrar GIF")

# Cargar el archivo de imagen GIF
gif_image = pygame.image.load("images/comida.gif")

# Configuración de la ubicación inicial de la imagen
image_x = 250
image_y = 250

# Iniciar el bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar la pantalla y dibujar la imagen
    screen.fill((255, 255, 255))
    screen.blit(gif_image, (image_x, image_y))

    # Actualizar la pantalla
    pygame.display.update()

    # Esperar un tiempo antes de cambiar la imagen
    pygame.time.delay(300)

    # Cambiar la posición de la imagen
    image_y += 3

    # Si la imagen llega a la posicion + 3, volver a su posición inicial
    if image_y > 254:
        image_x = 250
        image_y = 250