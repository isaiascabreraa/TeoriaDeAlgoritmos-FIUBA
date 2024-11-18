
import copy

#https://algoritmos-rw.github.io/tda_bg/tps/2024_anual/tp/
#https://github.com/TomasGarciaA/tda-tp-asinc
#https://drive.google.com/drive/u/0/folders/1ACnAyHhEQ957aPDHObRsjO2UUzjt_Hb7

#Funciones Auxiliares
def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)
    print("\n")

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
    n = len(demanda_filas) - 1
    m = len(demanda_columnas) - 1

    #Chequeo si es posible que entre en la matriz.
    if columna + largo > m:
            return False
    
    #Chequeo si la posicion anteior no esta ocupada
    if columna != 0:
        if tablero[fila][columna-1] != 0:
            return False
    
    #Chequeo que la posicion siguiente no este ocupada.
    if (columna + largo) <= m:
        if tablero[fila][columna + largo] != 0:
            return False
    
    #Chequeo que las posiciones por arriba, por debajo y a lo largo no esten ocupadas.
    for i in range(largo):
        if fila != 0 and fila < n:
            if tablero[fila - 1][columna + i] != 0 or tablero[fila + 1][columna + i] != 0:
                return False
            
        elif fila != 0 and fila == n:
            if tablero[fila - 1][columna + i] != 0:
                return False
            
        elif fila == 0 and fila < n:
             if tablero[fila + 1][columna + i] != 0:
                return False
             
        #Chequeo que no esten ocupados los lugares internos
        if tablero[fila][columna+i] != 0:
            return False
             
        #CHEQUEO SI LA DEMADNA ES VALIDA
        if (i + 1) > demanda_filas[columna+i] or 1 > demanda_columnas[columna+i]:
            return False

    cota_derecha = columna + largo
    cota_izquierda = columna

    if cota_derecha < m:
        if (fila - 1) >= 0:
            if tablero[fila - 1][columna + 1] != 0:
                return False
        
        if (fila + 1) <= n:
            if tablero[fila + 1][columna + 1] != 0:
                return False

    if cota_izquierda > 0:
        if (fila - 1) >= 0:
            if tablero[fila - 1][columna - 1] != 0:
                return False
        
        if (fila + 1) <= n:
            if tablero[fila + 1][columna - 1] != 0:
                return False
        
    return True

#Pre: -
#Post: -
def validar_vertical(tablero, fila, columna, largo, demanda_filas, demanda_columnas):
    n = len(demanda_filas) - 1
    m = len(demanda_columnas) - 1

    #Chequeo si es posible que entre en la matriz.
    if fila + largo > n:
            return False
    
    #Chequeo que la posicion anterior no este ocupada.
    if fila != 0:
        if tablero[fila - 1][columna] != 0:
            return False
        
    #Chequeo que la posicion siguiente no este ocupada.
    if (fila + largo) <= n:
        if tablero[fila + largo][columna] != 0:
            return False
    
    #Chequeo que las posiciones por izquierda, por derecha t a lo largo no esten ocupadas.
    for i in range(largo):
        if columna != 0 and columna < m:
            if tablero[fila + i][columna - 1] != 0 or tablero[fila + i][columna + 1] != 0:
                return False
            
        elif columna != 0 and columna == m:
            if tablero[fila + i][columna - 1] != 0:
                return False
            
        elif columna == 0 and columna < m:
             if tablero[fila + i][columna + 1] != 0:
                return False
             
        #Chequeo que no esten ocupados los lugares internos
        if tablero[fila+i][columna] != 0:
            return False
             
        #CHEQUEO SI LA DEMADNA ES VALIDA
        if (i + 1) > demanda_columnas[columna] or 1 > demanda_filas[fila+i]:
            return False

    cota_superior = fila + largo
    cota_inferior = fila

    if cota_superior < n:
        if (columna - 1) >= 0:
            if tablero[fila + 1][columna - 1] != 0:
                return False
        
        if (columna + 1) <= n:
            if tablero[fila + 1][columna + 1] != 0:
                return False

    if cota_inferior > 0:
        if (columna - 1) >= 0:
            if tablero[fila - 1][columna - 1] != 0:
                return False
        
        if (columna + 1) <= n:
            if tablero[fila - 1][columna + 1] != 0:
                return False

    return True



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
def contar_demandas_satisfechas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    demandas_satisfechas = 0

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 1:
                demandas_satisfechas += 2

    return demandas_satisfechas

#Pre: -
#Post: -
def es_mejor_tablero(tablero_actual, mejor_tablero):
    demandas_satisfechas_actual = contar_demandas_satisfechas(tablero_actual)
    demandas_satisfechas_mejor = contar_demandas_satisfechas(mejor_tablero)

    print(f"Comparando tableros: Actual = {demandas_satisfechas_actual}, Mejor = {demandas_satisfechas_mejor}")
    return demandas_satisfechas_actual > demandas_satisfechas_mejor

#Pre: -
#Post: -
def backtracking_batalla_naval(tablero_actual, mejor_tablero, demanda_filas, demanda_columnas, barcos):
    if not barcos:
        if es_mejor_tablero(tablero_actual, mejor_tablero):
            print("Nuevo mejor tablero encontrado")
            mejor_tablero[:] = copy.deepcopy(tablero_actual)
        return

    print("Nueva iteración")
    barco = barcos[0]
    for i in range(len(demanda_filas)):
        if demanda_filas[i] == 0:
            continue

        for j in range(len(demanda_columnas)):
            if demanda_columnas[j] == 0:
                continue

            print(f"Trato de colocar en fila: {i} y columna: {j}")

            if es_valida_colocacion(tablero_actual, i, j, barco, 'H', demanda_filas, demanda_columnas):
                print(f"Colocando barco horizontal en ({i}, {j})")
                tablero_copia = copy.deepcopy(tablero_actual)
                demanda_filas_copia = copy.deepcopy(demanda_filas)
                demanda_columnas_copia = copy.deepcopy(demanda_columnas)

                colocar_barco(tablero_copia, i, j, barco, 'H', 1)
                imprimir_tablero(tablero_copia)
                actualizar_demandas(demanda_filas_copia, demanda_columnas_copia, i, j, barco, 'H', 1)
                backtracking_batalla_naval(tablero_copia, mejor_tablero, demanda_filas_copia, demanda_columnas_copia, barcos[1:])

            if es_valida_colocacion(tablero_actual, i, j, barco, 'V', demanda_filas, demanda_columnas):
                print(f"Colocando barco vertical en ({i}, {j})")
                tablero_copia = copy.deepcopy(tablero_actual)
                demanda_filas_copia = copy.deepcopy(demanda_filas)
                demanda_columnas_copia = copy.deepcopy(demanda_columnas)

                colocar_barco(tablero_copia, i, j, barco, 'V', 1)
                imprimir_tablero(tablero_copia)
                actualizar_demandas(demanda_filas_copia, demanda_columnas_copia, i, j, barco, 'V', 1)
                backtracking_batalla_naval(tablero_copia, mejor_tablero, demanda_filas_copia, demanda_columnas_copia, barcos[1:])

    print("Fin de la iteración")
    return

#Pre: -
#Post: -
def batalla_naval(tablero, demanda_filas, demanda_columnas, barcos):
    if not tablero:
        print("No hay tablero")
        return None

    mejor_tablero = [[0] * len(tablero[0]) for _ in range(len(tablero))]
    demanda_total = calcular_demanda_total(demanda_filas, demanda_columnas)

    backtracking_batalla_naval(tablero, mejor_tablero, demanda_filas, demanda_columnas, barcos)
    demanda_satisfecha = contar_demandas_satisfechas(mejor_tablero)

    print(f"La demanda total es: {demanda_total}")
    print(f"La demanda cumplida es: {demanda_satisfecha}")
    return mejor_tablero

#Pre: -
#Post: -
def colocar_barco(tablero, fila, columna, barco, orientacion, valor):
    largo = barco
    if orientacion == 'H':
        for i in range(largo):
            tablero[fila][columna + i] += valor
    else:
        for i in range(largo):
            tablero[fila + i][columna] += valor

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
def actualizar_demandas(demanda_filas, demanda_columnas, fila, columna, barco, orientacion, valor):
    largo = barco
    if orientacion == 'H':
        demanda_filas[fila] -= valor
        for i in range(largo):
            demanda_columnas[columna + i] -= valor
    else:
        demanda_columnas[columna] -= valor
        for i in range(largo):
            demanda_filas[fila + i] -= valor


#Pre: -
#Post: -
def main():
    #demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/3_3_2.txt")
    demanda_filas, demanda_columnas, barcos = leer_datos("archivos_prueba/5_5_6.txt")

    n = len(demanda_filas)
    m = len(demanda_columnas)

    print(f"Hay un total de {len(barcos)} barcos")
    posicion = 0
    for barco in barcos:
        print(f"El barco {posicion} tiene un tamaño de {barco}")
        posicion += 1
    print("\n")

    tablero = [[0 for _ in range(m)] for _ in range(n)]
    print("Tablero inicial")
    imprimir_tablero(tablero)

    nuevo_tablero = batalla_naval(tablero, demanda_filas, demanda_columnas, barcos)
    
    print("Tablero obtenido")
    imprimir_tablero(nuevo_tablero)

if __name__ == "__main__":
    main()
