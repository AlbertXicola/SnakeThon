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


serp=[[4,4],[4,5],[4,6]]
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

def mover_cabeza(serp,dir):
    if dir=="N":
        serp[0][0]-=1
    if dir=="S":
        serp[0][0]+=1
    if dir=="O":
        serp[0][1]-=1
    if dir=="E":
        serp[0][1]+=1


def desplazar_cola(serp):
    ant=serp[0]
    for celda in serp:
        celda[0]=ant[0]
        celda[1]=ant[1]
        ant=celda


def mostrar_serp(serp,tablero):
    for celda in serp:
        tablero[celda[0]][celda[1]]=1


def mostrar():
    tablero=mostrar_tablero()

    mostrar_serp(serp,tablero)
    for fila in tablero:
        print(fila)

while(True):    
    mostrar()
    dir=input ("dir:")
    desplazar_cola(serp)
    mover_cabeza(serp,dir)

