import numpy as np
import random

def mostrar_instrucciones():
    print("=== Instrucciones del juego  HUNDIR LA FLOTA ===")
    print("El objetivo del juego es destruir todos los barcos del oponente antes de que él destruya los tuyos.")
    print("Cada jugador tiene un tablero de 10x10 donde colocarán aleatoriamente sus barcos de diferentes tamaños: \n\t4 lanchas de 1 de eslora. \n\t3 barcos de 2 de eslora. \n\t2 destructores de 3 de eslora. \n\t1 acorazado de 4 de eslora. ")
    print("Los jugadores se turnan para hacer disparos en el tablero del oponente, intentando adivinar la ubicación de los barcos.")
    print("Si un disparo acierta en un barco, repetirá turno y se le indica al jugador que acertó y se marca en el tablero del oponente.")
    print("El juego termina cuando un jugador ha destruido todos los barcos del oponente.")

mostrar_instrucciones()


def crear_tablero_vacio():
    tablero = np.full((10, 10), '-')
    return tablero


def crear_barco_random(eslora, tablero):
    barco_random = []   # Crear una lista vacía para el barco aleatorio generado
    fila_random = random.randint(0, 9)  # Generar una fila aleatoria en el tablero
    columna_random = random.randint(0, 9)  # Generar una columna aleatoria en el tablero
    barco_random.append((fila_random, columna_random))  # Agregar la coordenada aleatoria generada a la lista de coordenadas del barco aleatorio

    orient = random.choice(["N", "S", "E", "O"])  # Seleccionar una orientación aleatoria para el barco aleatorio generado

    while len(barco_random) < eslora:  # Mientras la longitud de la lista de coordenadas del barco aleatorio sea menor que la eslora del barco:
        if orient == "O":  # Si la orientación es Oeste
            columna_random -= 1  # Disminuir la columna en 1 para ir hacia el Oeste
        if orient == "E":  # Si la orientación es Este
            columna_random += 1  # Aumentar la columna en 1 para ir hacia el Este
        if orient == "N":  # Si la orientación es Norte
            fila_random -= 1  # Disminuir la fila en 1 para ir hacia el Norte
        if orient == "S":  # Si la orientación es Sur
            fila_random += 1  # Aumentar la fila en 1 para ir hacia el Sur

        if not (0 <= fila_random < 10 and 0 <= columna_random < 10):  # Si las coordenadas generadas están fuera del rango del tablero
            fila_random = random.randint(0, 9)  # Generar nuevas coordenadas aleatorias para el barco
            columna_random = random.randint(0, 9)
            orient = random.choice(["N", "S", "E", "O"])  # Seleccionar una nueva orientación aleatoria
            barco_random = [(fila_random, columna_random)]  # Reiniciar la lista de coordenadas del barco aleatorio con las nuevas coordenadas generadas
            continue

        barco_random.append((fila_random, columna_random))  # Agregar las nuevas coordenadas generadas a la lista de coordenadas del barco aleatorio

    return barco_random  # Devolver la lista de coordenadas del barco aleatorio generado


def crear_barcos(tablero):
    # crear 4 lanchas de 1 de eslora
    lancha_1 = crear_barco_random(1, tablero)
    lancha_2 = crear_barco_random(1, tablero)
    lancha_3 = crear_barco_random(1, tablero)
    lancha_4 = crear_barco_random(1, tablero)
    
    # crear 3 barcos de 2 de eslora
    barco_1 = crear_barco_random(2, tablero)
    barco_2 = crear_barco_random(2, tablero)
    barco_3 = crear_barco_random(2, tablero)
    
    # crear 2 destructores de 3 de eslora
    destructor_1 = crear_barco_random(3, tablero)
    destructor_2 = crear_barco_random(3, tablero)
    
    # crear 1 acorazado de 4 de eslora
    acorazado = crear_barco_random(4, tablero)
    
    # retornar una lista con los barcos creados
    return [lancha_1, lancha_2, lancha_3, lancha_4, barco_1, barco_2, barco_3, destructor_1, destructor_2, acorazado]

def colocar_barcos(tablero, barco):
    fila, columna = barco[0] # Obtiene la fila y la columna de la posición inicial del barco
    if not (0 <= fila <= 9 and 0 <= columna <= 9): # Verifica que el barco no esté fuera de los límites del tablero
        return False # Si está fuera, devuelve False
    else:
        if len(barco) == 1: # Si el barco es de eslora 1, simplemente se coloca en la posición inicial
            if tablero[fila][columna] == "-": # Verifica que la posición inicial esté libre
                tablero[fila][columna] = "B" # Si está libre, coloca el barco
                return True
            else:
                return False # Si la posición no está libre, devuelve False
        else:
            orientacion = random.choice(["H", "V"]) # Si el barco es de eslora mayor que 1, se elige una orientación aleatoria (horizontal o vertical)
            if orientacion == "H": # Si la orientación es horizontal
                if columna + len(barco) > 10: # Verifica que el barco no se salga del tablero en la dirección horizontal
                    return False
                else:
                    casillas = [(fila, columna+i) for i in range(len(barco))] # Genera una lista con las casillas que ocupará el barco
            else: # Si la orientación es vertical
                if fila + len(barco) > 10: # Verifica que el barco no se salga del tablero en la dirección vertical
                    return False
                else:
                    casillas = [(fila+i, columna) for i in range(len(barco))] # Genera una lista con las casillas que ocupará el barco
            if all([tablero[fila][columna] == "-" for fila, columna in casillas]): # Verifica que todas las casillas estén libres
                for fila, columna in casillas: # Si están libres, coloca el barco en todas ellas
                    tablero[fila][columna] = "X"
                return True
            else:
                return False # Si alguna de las casillas no está libre, devuelve False

def disparar(casilla, tablero):
    if tablero[casilla] == "B": # Si la casilla contiene un barco, entonces es tocado
        tablero[casilla] = "X" # Se marca como tocado en el tablero
        print("Tocado")
    else: # Si no, entonces es agua
        tablero[casilla] = "-" # Se marca como agua en el tablero
        print("Agua")
    return tablero # Devuelve el tablero actualizado

def turno_jugador_humano():
    # Pedir al jugador las coordenadas donde quiere disparar
    fila, columna = input("Introduce la fila y columna a la que quieres disparar entre el 0 al 9 (ejemplo: 3,4): ").split(",")
    # Convertir los valores de fila y columna a enteros
    fila = int(fila)
    columna = int(columna)
    # Retornar las coordenadas como una tupla
    return (fila, columna)

def turno_jugador_computadora(tablero):
    # Este es un bucle infinito, que se detendrá cuando se cumplan ciertas condiciones
    while True:
        fila = random.randint(0, 9)  # se elige una fila al azar entre 0 y 9
        columna = random.randint(0, 9)  # se elige una columna al azar entre 0 y 9
        if tablero[fila][columna] == "-" or tablero[fila][columna] == "O":  # si la casilla elegida es agua o un barco sin tocar
            return (fila, columna)  # devuelve las coordenadas de la casilla elegida como una tupla (fila, columna)

# Función para comprobar si todos los barcos están hundidos
def todos_los_barcos_hundidos(tablero, barcos):
    # Recorremos todos los barcos
    for barco in barcos:
        # Comprobamos si todas las casillas del barco están marcadas con X (hundidas)
        for casilla in barco:
            if tablero[casilla] == "X":
                continue
            else:
                return False
    # Si todos los barcos están hundidos, devolvemos True
    return True

# Función que inicia y ejecuta el juego de hundir la flota
def juego():
    # Creamos un tablero vacío
    tablero = crear_tablero_vacio()
    # Creamos los barcos aleatorios
    barcos = crear_barcos(tablero)
    # Colocamos los barcos en el tablero
    for barco in barcos:
        while not colocar_barcos(tablero, barco):
            barco = crear_barco_random(len(barco), tablero)
    # Iniciamos el turno de juego
    while True:
        # Turno del jugador humano
        print("Turno del jugador humano:")
        coordenadas_disparo = turno_jugador_humano()
        disparar(coordenadas_disparo, tablero)
        # Comprobamos si se han hundido todos los barcos
        if todos_los_barcos_hundidos(tablero, barcos):
            print("Has ganado!")
            break
        # Turno de la computadora
        print("Turno de la computadora:")
        coordenadas_disparo = turno_jugador_computadora(tablero)
        disparar(coordenadas_disparo, tablero)
        # Comprobamos si se han hundido todos los barcos
        if todos_los_barcos_hundidos(tablero, barcos):
            print("La computadora ha ganado.")
            break



# Función para iniciar el juego, ver instrucciones o salirse del juego
def inicio_juego():
    print("Bienvenido al juego de HUNDIR LA FLOTA\nPreparate para demostrar tus habilidades.\n¿Podrás ganar a una maquina?")
    while True:
        print("Seleccione una opción (indicando solamente el número):")
        print("1. Jugar")
        print("2. Instrucciones del juego")
        print("3. Salir")
        opcion = input()
        if opcion == "1":
            print("¡Que empiece el juego!")
            juego()
            break
        elif opcion == "2":
            mostrar_instrucciones()
            print("¿Que desea realizar? Seleccione una opción(indicando solamente el número):")
            print("1. Jugar")
            print("2. Salir")
            opcion2 = input()
            if opcion2 == "1":
                print("¡Que empiece el juego!")
                juego()
                break
            elif opcion2 == "2":
                print("¡Hasta pronto! ")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


