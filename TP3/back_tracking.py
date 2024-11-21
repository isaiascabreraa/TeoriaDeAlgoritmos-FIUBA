
import copy
import time


#Pre: -
#Post: -
def es_posible_colocar_barco(tablero, demanda_filas, demanda_columnas, i, j, largo, orientacion):
    n = len(tablero)
    m = len(tablero[0])

    if orientacion == 'H':
        if j + largo <= m and all(tablero[i][j + k] == 0 for k in range(largo)):
            if demanda_filas[i] >= largo and all(demanda_columnas[j + k] > 0 for k in range(largo)):
                return True
    else: 
        if i + largo <= n and all(tablero[i + k][j] == 0 for k in range(largo)):
            if demanda_columnas[j] >= largo and all(demanda_filas[i + k] > 0 for k in range(largo)):
                return True
    return False


#https://algoritmos-rw.github.io/tda_bg/tps/2024_anual/tp/
#https://github.com/TomasGarciaA/tda-tp-asinc
#https://drive.google.com/drive/u/0/folders/1ACnAyHhEQ957aPDHObRsjO2UUzjt_Hb7

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

#Funciones de colocacion

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

    # Verificar la diagonal superior derecha
    if cota_derecha < m - 1:  # Si existe derecha..
        if fila > 0:  # Si existe un arriba..
            if tablero[fila - 1][columna + largo] != 0:  # Y es distinto de 0..
                return False
        if fila < n - 1:  # Si existe un abajo..
            if tablero[fila + 1][columna + largo] != 0:  # Y es distinto de 0..
                return False

    # Verificar la diagonal inferior izquierda
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
        if columna != 0 and columna < m - 1:
            if tablero[fila + i][columna - 1] != 0 or tablero[fila + i][columna + 1] != 0:
                return False
        elif columna != 0 and columna == m - 1:
            if tablero[fila + i][columna - 1] != 0:
                return False
        elif columna == 0 and columna < m - 1:
            if tablero[fila + i][columna + 1] != 0:
                return False
        if tablero[fila + i][columna] != 0:  #Chequeo que no esten ocupados los lugares internos
            return False

    cota_superior = fila + largo - 1
    cota_inferior = fila

    # Verificar la diagonal inferior izquierda y derecha
    if cota_superior < n - 1:
        if columna - 1 >= 0:
            if tablero[fila + largo][columna - 1] != 0:
                return False
        if columna + 1 < m:
            if tablero[fila + largo][columna + 1] != 0:
                return False

    # Verificar la diagonal superior izquierda y derecha
    if cota_inferior > 0:
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

    tablero_actual = copy.deepcopy(tablero)
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
    demanda_total = 0
    for i in range(len(demanda_filas)):
        demanda_total += demanda_filas[i]
    for j in range(len(demanda_columnas)):
        demanda_total += demanda_columnas[j]
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
def backtracking_batalla_naval(tablero, mejor_tablero, fila, columna, demanda_filas, demanda_columnas, barcos, mejor_demanda, demanda_total):

    if not barcos:
        return mejor_tablero, mejor_demanda
    #print("Nueva iteración")
    barco = barcos[0]
    cantidad_filas = len(demanda_filas)
    cantidad_columnas = len(demanda_columnas)
    for i in range(fila, cantidad_filas):
        for j in range(columna, cantidad_columnas):
            #print(f"Fila: {i} - Columna: {j}")
            if demanda_filas[i] == 0 or demanda_columnas[j] == 0:
                continue
            if barco > cantidad_filas-1-i and barco > cantidad_columnas-1-j:
                return mejor_tablero, mejor_demanda

            ##HORIZONTAL
            if es_valida_colocacion(tablero, i, j, barco, 'H', demanda_filas, demanda_columnas):
                tablero_actual = colocar_barco(tablero, i, j, barco, 'H')
                demanda_filas_actual, demanda_columnas_actual = actualizar_demandas(demanda_filas, demanda_columnas, i, j, barco, 'H')
                demanda_actual = contar_demandas_satisfechas(demanda_filas_actual, demanda_columnas_actual, demanda_total)
                #print(f"Comparando tableros: Actual = {demanda_actual}, Mejor = {mejor_demanda}")
                if demanda_actual > mejor_demanda:
                    mejor_demanda =  demanda_actual
                    mejor_tablero = tablero_actual
                    #imprimir_tablero(tablero_actual)
                mejor_tablero, mejor_demanda = backtracking_batalla_naval(tablero_actual, mejor_tablero, i, j, demanda_filas_actual, demanda_columnas_actual, barcos[1:], mejor_demanda, demanda_total)
                #if not es_posible_colocar_barco(tablero, demanda_filas, demanda_columnas, i, j, barco, 'H'):
                #   return mejor_tablero, mejor_demanda

            ##VERTICAL
            if es_valida_colocacion(tablero, i, j, barco, 'V', demanda_filas, demanda_columnas):
                tablero_actual = colocar_barco(tablero, i, j, barco, 'V')
                demanda_filas_actual, demanda_columnas_actual = actualizar_demandas(demanda_filas, demanda_columnas, i, j, barco, 'V')
                demanda_actual = contar_demandas_satisfechas(demanda_filas_actual, demanda_columnas_actual, demanda_total)
                #print(f"Comparando tableros: Actual = {demanda_actual}, Mejor = {mejor_demanda}")
                if demanda_actual > mejor_demanda:
                    mejor_demanda =  demanda_actual
                    mejor_tablero = tablero_actual
                    #imprimir_tablero(tablero_actual)
                mejor_tablero, mejor_demanda = backtracking_batalla_naval(tablero_actual, mejor_tablero, i, j, demanda_filas_actual, demanda_columnas_actual, barcos[1:], mejor_demanda, demanda_total)
                #if not es_posible_colocar_barco(tablero, demanda_filas, demanda_columnas, i, j, barco, 'V'):
                #   return mejor_tablero, mejor_demanda
        
        columna = 0
    fila = 0

    #print("Fin de la iteración\n")
    return mejor_tablero, mejor_demanda


#Pre: -
#Post: -
def batalla_naval(tablero, demanda_filas, demanda_columnas, barcos):
    if not tablero:
        print("No hay tablero")
        return None

    mejor_demanda = 0
    mejor_tablero = [[0] * len(demanda_columnas) for _ in range(len(demanda_filas))]
    demanda_total = calcular_demanda_total(demanda_filas, demanda_columnas)
    tablero_obtenido, demanda_actual = backtracking_batalla_naval(tablero, mejor_tablero, 0, 0, demanda_filas, demanda_columnas, barcos, mejor_demanda, demanda_total)

    print(f"La demanda total es: {demanda_total}")
    print(f"La demanda cumplida es: {demanda_actual}")
    return tablero_obtenido


#Pre: -
#Post: -
def main():
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/3_3_2.txt") #0.0005 segundos
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/5_5_6.txt") #0.0006 segundos
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/8_7_10.txt") #Indefinido
    demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/10_10_10.txt") #0.0200 segundos
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/20_20_20.txt")
    
    n = len(demanda_filas)
    m = len(demanda_columnas)

    tablero = [[0 for _ in range(m)] for _ in range(n)]
    print("Tablero inicial")
    imprimir_tablero(tablero)

    barcos.sort(reverse=True)
    barcos_procesados = []
    for barco in barcos:
        contador_filas = 0
        for demanda in demanda_filas:
            if barco > demanda:
                contador_filas += 1
        contador_columnas = 0
        for demanda in demanda_columnas:
            if barco > demanda:
                contador_columnas += 1
        if contador_columnas == len(demanda_columnas) or contador_filas == len(demanda_filas):
            continue
        barcos_procesados.append(barco)

    inicio = time.time()
    nuevo_tablero = batalla_naval(tablero, demanda_filas, demanda_columnas, barcos_procesados)
    fin = time.time()
    print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")

    print("Tablero obtenido")
    imprimir_tablero(nuevo_tablero)

if __name__ == "__main__":
    main()
