import pygame

pygame.init()

# Crea la superficie y establece las dimensiones
width, height = 800, 600
surface = pygame.display.set_mode((width, height))

# Carga la imagen
image = pygame.image.load("images/fondo.png")

# Dibuja una línea en la superficie
start_pos = (0, 300)
end_pos = (800, 300)
color = (255, 255, 255)
line_width = 5
pygame.draw.line(surface, color, start_pos, end_pos, line_width)

# Dibuja la imagen debajo de la línea en la misma superficie
image_x, image_y = 50, 350
surface.blit(image, (image_x, image_y))

# Actualiza la pantalla para ver el resultado
pygame.display.update()

# Mantén la ventana abierta hasta que se cierre
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
