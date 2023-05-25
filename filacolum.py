import random



def cell2coord(row,col):
    return (275+(CELLSIZE*row), 125+(CELLSIZE*col))
CELLSIZE=50

def generar_posicion_aleatoria():
    x = random.randint(0, 12)
    y = random.randint(0, 12)
    return [x, y]

