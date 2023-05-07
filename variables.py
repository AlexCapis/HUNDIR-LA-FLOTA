import numpy as np
import random
from funciones_hundir_flota import *


# Las variables que he usado en el proyecto de HUNDIR LA FLOTA son las siguientes:

tablero = np.full((10, 10), '-') # para la creación del tablero
barco_random = []   # Crear una lista vacía para el barco aleatorio generado
fila_random = random.randint(0, 9)  # Generar una fila aleatoria en el tablero
columna_random = random.randint(0, 9)  # Generar una columna aleatoria en el tablero
barco_random.append((fila_random, columna_random))  # Agregar la coordenada aleatoria generada a la lista de coordenadas del barco aleatorio
orient = random.choice(["N", "S", "E", "O"])  # Seleccionar una orientación aleatoria para el barco aleatorio generado

# los distintos barcos
lancha_1 = crear_barco_random(1, tablero)
lancha_2 = crear_barco_random(1, tablero)
lancha_3 = crear_barco_random(1, tablero)
lancha_4 = crear_barco_random(1, tablero)
barco_1 = crear_barco_random(2, tablero)
barco_2 = crear_barco_random(2, tablero)
barco_3 = crear_barco_random(2, tablero)
destructor_1 = crear_barco_random(3, tablero)
destructor_2 = crear_barco_random(3, tablero)
acorazado = crear_barco_random(4, tablero)

fila, columna = barco[0] # Obtiene la fila y la columna de la posición inicial del barco

fila = random.randint(0, 9)  # se elige una fila al azar entre 0 y 9
columna = random.randint(0, 9)  # se elige una columna al azar entre 0 y 9

tablero = crear_tablero_vacio() # creación de un tablero vacío
barcos = crear_barcos(tablero) # para la creación de barcos aleatorios

coordenadas_disparo = turno_jugador_humano()

opcion = input() # el usuario introduzca la opción que quiera
opcion2 = input() # el usuario introduzca la opción que quiera
