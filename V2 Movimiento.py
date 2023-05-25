import random
def mover_cabeza(serp,dir):
    x = serp[0][0]
    y = serp[0][1]
    if dir=="w":
        x-=1
    if dir=="s":
        x+=1
    if dir=="a":
        y-=1
    if dir=="d":
        y+=1
    serp.insert(0, [x, y])

def desplazar_cola(sert):

    serp.pop()

def mostrar_serp(serp,tablero):
    for celda in serp:
        tablero[celda[0]][celda[1]]=1

def mostrar():
    tablero=mostrar_tablero()
    mostrar_manzana()

    mostrar_serp(serp,tablero)
    for fila in tablero:
        print(fila)

def generar_posicion_aleatoria():  
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    return [x,y]

def crear_manzana(serp):
    manzpos = generar_posicion_aleatoria()
    if manzpos in serp:
        return crear_manzana(serp)
    else:
        return manzpos

def mostrar_manzana(manzpos,tablero):
    tablero[manzpos[0]][manzpos[1]]=2

tablero=[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]

serp=[[4,4],[4,5],[4,6],[4,7],[3,7]]
dir="O"

def mostrar_tablero():
    return [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]

while(True):    
    mostrar()
    dir=input ("dir:")
    desplazar_cola(serp)
    mover_cabeza(serp,dir)
    