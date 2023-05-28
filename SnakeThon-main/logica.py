import random
import datetime


def mover_cabeza(serp, dir):
    x = serp[0][0]
    y = serp[0][1]
    if dir == "w":
        x -= 1
    if dir == "s":
        x += 1
    if dir == "a":
        y -= 1
    if dir == "d":
        y += 1
    serp.insert(0, [x, y])

def desplazar_cola(serp):
    serp.pop()

def mostrar_serp(serp, tablero):
    tablero[serp[0][0]][serp[0][1]] = 7
    # dibuixar cap
    for celda in serp [1:]:
        tablero[celda[0]][celda[1]] = 1
        #dicuixar cua


def savepoints():
    archivo = open("puntuacion.txt", "a")
    archivo.write(str(datetime.datetime.now())+','+str(nManzanas)+"\n")
    archivo.close()


def mostrar():
    tablero = mostrar_tablero()
    mostrar_serp(serp, tablero)
    mostrar_manzana(manzpos, tablero)
    for fila in tablero:
        print(fila)


def generar_posicion_aleatoria():
    x = random.randint(0, 8)
    y = random.randint(0, 8)
    return [x, y]



def crear_manzana(serp):
    manzpos = generar_posicion_aleatoria()
    if manzpos in serp:
        return crear_manzana(serp)
    else:
        return manzpos

def mostrar_manzana(manzpos, tablero):
    tablero[manzpos[0]][manzpos[1]] = 2


def mostrar_tablero():
    # insertar imatge taulell
    return [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

serp = [[4, 4]]
dir = "O"


manzpos = crear_manzana(serp)
nManzanas = 0
dirant= ""
posant= [0,0]

while True:
    
    tablero = mostrar_tablero()
    mostrar()
    dir = input("dir:")
    if dir == "w" and dirant == "s":
        dir = "s"

    if dir == "s" and dirant == "w":
        dir= "w"

    if dir == "a" and dirant == "d":
        dir = "d"

    if dir == "d" and dirant == "a":
        dir = "a"
    
    mover_cabeza(serp, dir)
    desplazar_cola(serp)

    if serp[0][0] < 0 or serp[0][0] >= len(tablero) or serp[0][1] < 0 or serp[0][1] >= len(tablero[0]):

        print("¡Perdido!")
        savepoints()
        break

    if serp[0] == manzpos:
        serp.insert(0, manzpos)
        manzpos = crear_manzana(serp)
        nManzanas += 1
        mostrar_serp(serp,tablero)
        



    elif serp[0] in serp[1:]:
        print("¡Perdido!")
        savepoints()
        break

    dirant = dir
