
import time

#Funciones Auxiliares
def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)
    print("\n")

def imprimir_demandas(demanda_filas_actual, demanda_columnas_actual):
    print(f"La demanda de filas es: {demanda_filas_actual} y la demanda de columnas es: {demanda_columnas_actual}")

def leer_datos(filename):
    with open(filename, 'r') as file:
        lineas = file.readlines()

    secciones = [[]]
    seccion_actual = 0
    for linea in lineas: 
        if not linea.startswith('#'):
            if linea == '\n':
                seccion_actual += 1
                secciones.append([])
            else:
                secciones[seccion_actual].append(linea.strip())

    print(f"{secciones}\n")
    requisitos_filas = [int(valor) for valor in secciones[0]]
    requisitos_columnas = [int(valor) for valor in secciones[1]]
    barcos = [int(valor) for valor in secciones[2]]

    return requisitos_filas, requisitos_columnas, barcos

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
def backtracking_batalla_naval(tablero, mejor_tablero, fila, columna, demanda_filas, demanda_columnas, barcos, mejor_demanda, demanda_actual, demanda_total):
    if not barcos:
        return mejor_tablero, mejor_demanda

    barco = barcos[0]
    cantidad_filas = len(demanda_filas)
    cantidad_columnas = len(demanda_columnas)

    demanda_maxima_posible = sum(barcos)*2 + demanda_actual
    if demanda_maxima_posible <= mejor_demanda:
        return mejor_tablero, mejor_demanda
    
    for i in range(fila, cantidad_filas):
        for j in range(columna if i == fila else 0, cantidad_columnas):
            if demanda_filas[i] == 0 or demanda_columnas[j] == 0:
                continue
            
            for orientacion in ['H', 'V']:
                if es_valida_colocacion(tablero, i, j, barco, orientacion, demanda_filas, demanda_columnas):
                    tablero_actual = colocar_barco(tablero, i, j, barco, orientacion)
                    demanda_filas_actual, demanda_columnas_actual = actualizar_demandas(demanda_filas, demanda_columnas, i, j, barco, orientacion)
                    demanda_actual = contar_demandas_satisfechas(demanda_filas_actual, demanda_columnas_actual, demanda_total)
                    
                    if demanda_actual >= mejor_demanda:
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

    return backtracking_batalla_naval(tablero, mejor_tablero, 0, 0, demanda_filas, demanda_columnas, barcos[1:], mejor_demanda, demanda_actual, demanda_total)


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
    
    for barco in barcos:
        posible = False
        for demanda_fila in demanda_filas:
            for demanda_columna in demanda_columnas:
                if barco <= demanda_fila and barco <= demanda_columna:
                    barcos_posibles.append(barco)
                    posible = True
                if posible:
                    break
            if posible:
                break
    return barcos_posibles


#Pre: -
#Post: -
def main():
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/3_3_2.txt") #0.0001 segundos [OPTIMO DE: 11 total | 4 satisfecho]
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/5_5_6.txt") #0.0023 segundos [OPTIMO DE: 18 total | 12 satisfecho]
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/8_7_10.txt") #0.0008 segundos [OPTIMO DE: 53 total | 26 satisfecho]
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/10_3_3.txt") #0.0009 segundos [OPTIMO DE: 14 total | 6 satisfecho]
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/10_10_10.txt") #0.009 segundos [OPTIMO DE: 40 total | 40 satisfecho]
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/12_12_21.txt") #0.1519 segundos [OPTIMO DE: 58 total | 46 satisfecho]
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/15_10_15.txt") #0.0018 segundos [OPTIMO DE: 67 total | 40 satisfecho]
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/20_20_20.txt") #0.0110 segundos [OPTIMO DE: 120 total | 104 satisfecho]
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/20_25_30.txt") #0.0122 segundos [OPTIMO DE: 247 total | 172 satisfecho]
    demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/30_25_25.txt") #19 segundos [OPTIMO DE: 360 total | 202 satisfecho]
    
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

if __name__ == "__main__":
    main()
