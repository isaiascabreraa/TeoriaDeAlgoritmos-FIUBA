import time
from utils import generar_barcos_random

#Funciones Auxiliares
def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)
    print("\n")

def imprimir_demandas(demanda_filas_actual, demanda_columnas_actual):
    print(f"La demanda de filas es: {demanda_filas_actual} y la demanda de columnas es: {demanda_columnas_actual}")

#Pre: -
#Post: -
def validar_horizontal(tablero, fila, columna, largo, demanda_filas, demanda_columnas):
    n = len(demanda_filas)
    m = len(demanda_columnas)

    if columna + largo - 1 >= m:  #Chequeo si es posible que entre en la matriz.
        return False
    if demanda_filas[fila] - largo < 0:
        return False

    for i in range(largo):
        if demanda_columnas[columna + i] - 1 < 0:
            return False
    
    if columna != 0 and tablero[fila][columna - 1] != 0:  #Chequeo si la posicion anterior no esta ocupada
        return False
    if columna + largo < m and tablero[fila][columna + largo] != 0:  #Chequeo que la posicion siguiente no esta ocupada.
        return False
    
    for i in range(largo):  #Chequeo que las posiciones por arriba, por debajo y a lo largo no esten ocupadas.
        if fila != 0 and fila < n - 1:
            if tablero[fila - 1][columna + i] != 0 or tablero[fila + 1][columna + i] != 0:
                return False
        elif fila != 0 and fila == n - 1:
            if tablero[fila - 1][columna + i] != 0:
                return False
        elif fila == 0 and fila < n - 1:
            if tablero[fila + 1][columna + i] != 0:
                return False
        if tablero[fila][columna + i] != 0:  #Chequeo que no esten ocupados los lugares internos
            return False

    cota_derecha = columna + largo - 1
    cota_izquierda = columna
    if cota_derecha < m - 1:  # Si existe derecha..
        if fila > 0:  # Si existe un arriba..
            if tablero[fila - 1][columna + largo] != 0:  # Y es distinto de 0..
                return False
        if fila < n - 1:  # Si existe un abajo..
            if tablero[fila + 1][columna + largo] != 0:  # Y es distinto de 0..
                return False
    if cota_izquierda > 0:  # Si existe izquierda..
        if fila - 1 >= 0:  # Si existe un arriba..
            if tablero[fila - 1][columna - 1] != 0:  # Y es distinto de 0..
                return False
        if fila + 1 < n:  # Si existe un abajo..
            if tablero[fila + 1][columna - 1] != 0:  # Y es distinto de 0..
                return False
    return True

#Pre: -
#Post: -
def validar_vertical(tablero, fila, columna, largo, demanda_filas, demanda_columnas):
    n = len(demanda_filas)
    m = len(demanda_columnas)

    if fila + largo - 1 >= n:  #Chequeo si es posible que entre en la matriz.
        return False
    if demanda_columnas[columna] - largo < 0:
        return False

    for i in range(largo):
        if demanda_filas[fila + i] - 1 < 0:
            return False
    
    if fila != 0 and tablero[fila - 1][columna] != 0:  #Chequeo que la posicion anterior no este ocupada.
        return False
    if fila + largo < n and tablero[fila + largo][columna] != 0:  #Chequeo que la posicion siguiente no esta ocupada.
        return False
    
    for i in range(largo):  #Chequeo que las posiciones por izquierda, por derecha y a lo largo no esten ocupadas.
        if tablero[fila + i][columna] != 0:  #Chequeo que no esten ocupados los lugares internos
            return False
        if columna != 0 and columna < m - 1:
            if tablero[fila + i][columna - 1] != 0 or tablero[fila + i][columna + 1] != 0:
                return False
        elif columna != 0 and columna == m - 1:
            if tablero[fila + i][columna - 1] != 0:
                return False
        elif columna == 0 and columna < m - 1:
            if tablero[fila + i][columna + 1] != 0:
                return False

    cota_superior = fila + largo - 1
    cota_inferior = fila
    if cota_superior < n - 1: # Verificar la diagonal inferior izquierda y derecha
        if columna - 1 >= 0:
            if tablero[fila + largo][columna - 1] != 0:
                return False
        if columna + 1 < m:
            if tablero[fila + largo][columna + 1] != 0:
                return False
    if cota_inferior > 0: # Verificar la diagonal superior izquierda y derecha
        if columna - 1 >= 0:
            if tablero[fila - 1][columna - 1] != 0:
                return False
        if columna + 1 < m:
            if tablero[fila - 1][columna + 1] != 0:
                return False
    return True

#Pre: -
#Post: -
def es_valida_colocacion(tablero, fila, columna, largo, orientacion, demanda_filas, demanda_columnas):
    if not tablero:
        return False
    posicion_valida = False
    if orientacion == 'H':
        posicion_valida = validar_horizontal(tablero, fila, columna, largo, demanda_filas, demanda_columnas)
    elif orientacion == 'V':
        posicion_valida = validar_vertical(tablero, fila, columna, largo, demanda_filas, demanda_columnas)
    else:
        print("Orientacion no valida")
    return posicion_valida

#Pre: -
#Post: -
def colocar_barco(tablero, fila, columna, barco, orientacion):
    tablero_actual = [fila[:] for fila in tablero]
    if orientacion == 'H':
        for i in range(barco):
            tablero_actual[fila][columna + i] = 1
    else:
        for i in range(barco):
            tablero_actual[fila + i][columna] = 1
        
    return tablero_actual

#Pre: -
#Post: -
def calcular_demanda_total(demanda_filas, demanda_columnas):
    demanda_total = sum(demanda_filas + demanda_columnas)
    return demanda_total

#Pre: -
#Post: -
def actualizar_demandas(demanda_filas, demanda_columnas, fila, columna, barco, orientacion):
    demanda_filas_actual = demanda_filas.copy()
    demanda_columnas_actual = demanda_columnas.copy()
    
    if orientacion == 'H':
        demanda_filas_actual[fila] -= barco
        for i in range(barco):
            demanda_columnas_actual[columna + i] -= 1
    else:
        demanda_columnas_actual[columna] -= barco
        for i in range(barco):
            demanda_filas_actual[fila + i] -= 1

    return demanda_filas_actual, demanda_columnas_actual

#Pre: -
#Post: -
def contar_demandas_satisfechas(demanda_filas, demanda_columnas, demanda_total):
    return demanda_total - sum(demanda_filas + demanda_columnas)

#Pre: -
#Post: -
def backtracking_batalla_naval(tablero, mejor_tablero, fila, columna, demanda_filas, demanda_columnas, barcos, mejor_demanda, demanda_satisfecha, demanda_total):

    if not barcos:
        return mejor_tablero, mejor_demanda

    barco = barcos[0]
    es_posible_colocar = False
    cantidad_filas = len(demanda_filas)
    cantidad_columnas = len(demanda_columnas)

    demanda_maxima_posible = sum(barcos) * 2 + demanda_satisfecha
    if demanda_maxima_posible <= mejor_demanda:
        return mejor_tablero, mejor_demanda

    for i in range(fila, cantidad_filas):
        for j in range(columna if i == fila else 0, cantidad_columnas):
            if demanda_filas[i] == 0 or demanda_columnas[j] == 0:
                continue

            for orientacion in ['V', 'H']:
                if es_valida_colocacion(tablero, i, j, barco, orientacion, demanda_filas, demanda_columnas):
                    tablero_actual = colocar_barco(tablero, i, j, barco, orientacion)
                    demanda_filas_actual, demanda_columnas_actual = actualizar_demandas(demanda_filas, demanda_columnas, i, j, barco, orientacion)
                    demanda_actual = contar_demandas_satisfechas(demanda_filas_actual, demanda_columnas_actual, demanda_total)
                    es_posible_colocar = True

                    if demanda_actual > mejor_demanda:
                        mejor_demanda = demanda_actual
                        mejor_tablero = tablero_actual

                    next_fila = i
                    next_columna = j + 1
                    if next_columna == cantidad_columnas:
                        next_fila += 1
                        next_columna = 0

                    if len(barcos) > 1:
                        if barco == barcos[1]:
                            mejor_tablero, mejor_demanda = backtracking_batalla_naval(tablero_actual, mejor_tablero, next_fila, next_columna, demanda_filas_actual, demanda_columnas_actual, barcos[1:], mejor_demanda, demanda_actual, demanda_total)
                        else:
                            mejor_tablero, mejor_demanda = backtracking_batalla_naval(tablero_actual, mejor_tablero, 0, 0, demanda_filas_actual, demanda_columnas_actual, barcos[1:], mejor_demanda, demanda_actual, demanda_total)
                    else:
                        return mejor_tablero, mejor_demanda

    if len(barcos) > 1:
        if barco == barcos[1] and es_posible_colocar:
            barcos_filtrados = [b for b in barcos if b != barco]
            return backtracking_batalla_naval(tablero, mejor_tablero, 0, 0, demanda_filas, demanda_columnas, barcos_filtrados, mejor_demanda, demanda_satisfecha, demanda_total)

    return backtracking_batalla_naval(tablero, mejor_tablero, 0, 0, demanda_filas, demanda_columnas, barcos[1:], mejor_demanda, demanda_satisfecha, demanda_total)



#Pre: -
#Post: -
def batalla_naval(tablero, demanda_filas, demanda_columnas, barcos):
    if not tablero:
        print("No hay tablero")
        return None

    mejor_demanda = 0
    mejor_tablero = [[0] * len(demanda_columnas) for _ in range(len(demanda_filas))]
    demanda_total = calcular_demanda_total(demanda_filas, demanda_columnas)
    tablero_obtenido, demanda_actual = backtracking_batalla_naval(tablero, mejor_tablero, 0, 0, demanda_filas, demanda_columnas, barcos, mejor_demanda, 0, demanda_total)

    print(f"La demanda total es: {demanda_total}")
    print(f"La demanda cumplida es: {demanda_actual}")

    return tablero_obtenido


def filtrar_barcos_imposibles(demanda_filas, demanda_columnas, barcos):
    barcos_posibles = []
    n = len(demanda_filas)
    m = len(demanda_columnas)

    for indice, barco in enumerate(barcos):
        posible = False

        for i in range(n):
            for j in range(m - barco + 1):
                if all(demanda_columnas[j + k] > 0 for k in range(barco)) and demanda_filas[i] >= barco:
                    posible = True
                    break
            if posible:
                break
        if not posible:
            for j in range(m):
                for i in range(n - barco + 1):
                    if all(demanda_filas[i + k] > 0 for k in range(barco)) and demanda_columnas[j] >= barco:
                        posible = True
                        break
                if posible:
                    break
        if posible:
            barcos_posibles.extend(barcos[indice:])
            break

    return barcos_posibles


#Pre: -
#Post: -
def solucion_backtracking(demanda_filas, demanda_columnas, barcos):
    n = len(demanda_filas)
    m = len(demanda_columnas)

    tablero = [[0 for _ in range(m)] for _ in range(n)]
    print("Tablero inicial")
    imprimir_tablero(tablero)

    barcos.sort(reverse=True)
    barcos_procesados = filtrar_barcos_imposibles(demanda_filas, demanda_columnas, barcos)
    print(f"Barcos antes de procesar: {barcos}. Total: {len(barcos)}")
    print(f"Barcos luego de procesar: {barcos_procesados}. Total: {len(barcos_procesados)}")

    inicio = time.time()
    tablero_obtenido = batalla_naval(tablero, demanda_filas, demanda_columnas, barcos_procesados)
    fin = time.time()
    print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")

    print("Tablero obtenido")
    imprimir_tablero(tablero_obtenido)