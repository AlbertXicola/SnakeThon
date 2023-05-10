import csv

class Jugador:
    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion

def crear_ranking(jugadores):
    ranking = sorted(jugadores, key=lambda jugador: jugador.puntuacion, reverse=True)
    return ranking

def guardar_ranking(ranking):
    with open('ranking.csv', mode='w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['Nombre', 'Puntuacion'])
        for jugador in ranking:
            writer.writerow([jugador.nombre, jugador.puntuacion])

def cargar_ranking():
    jugadores = []
    try:
        with open('ranking.csv', mode='r') as archivo:
            reader = csv.reader(archivo)
            next(reader)  # Omitir la primera fila (encabezados)
            for fila in reader:
                nombre = fila[0]
                puntuacion = int(fila[1])
                jugador = Jugador(nombre, puntuacion)
                jugadores.append(jugador)
    except FileNotFoundError:
        print("No se encontró el archivo del ranking. Se creará uno nuevo al guardar el ranking.")
    return jugadores

jugadores = cargar_ranking()

nombre_jugador = input("Ingresa tu nombre: ")
puntuacion_jugador = int(input("Ingresa tu puntuación: "))
jugador_actual = Jugador(nombre_jugador, puntuacion_jugador)
jugadores.append(jugador_actual)

ranking = crear_ranking(jugadores)
guardar_ranking(ranking)

print("Ranking actualizado y guardado correctamente.")
