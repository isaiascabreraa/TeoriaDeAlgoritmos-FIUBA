from backtracking import *

def colocar_barco(tablero, fila, columna, barco, orientacion):
    if orientacion == 'H':
        for i in range(barco):
            tablero[fila][columna + i] = 1
    else:
        for i in range(barco):
            tablero[fila + i][columna] = 1
        
    return tablero

def actualizar_demandas(demanda_filas, demanda_columnas, fila, columna, barco, orientacion):
    
    if orientacion == 'H':
        demanda_filas[fila] -= barco
        for i in range(barco):
            demanda_columnas[columna + i] -= 1
    else:
        demanda_columnas[columna] -= barco
        for i in range(barco):
            demanda_filas[fila + i] -= 1

    return demanda_filas, demanda_columnas

def poner_barco_en_fila(tablero, demanda_filas, demanda_columnas, barco, fila): #O((m-l)*l)
    cantidad_columnas = len(demanda_columnas)
    orientacion = 'H'
    barco_colocado = False
    for col in range(0,cantidad_columnas):
        if validar_horizontal(tablero, fila, col, barco, demanda_filas, demanda_columnas):
            tablero_actual = colocar_barco(tablero, fila, col, barco, orientacion)
            demanda_filas_actual, demanda_columnas_actual = actualizar_demandas(demanda_filas, demanda_columnas, fila, col, barco, orientacion)
            barco_colocado = True
            return tablero_actual, demanda_filas_actual, demanda_columnas_actual, barco_colocado
    return tablero, demanda_filas, demanda_columnas, barco_colocado

def poner_barco_en_col(tablero, demanda_filas, demanda_columnas, barco, columna): # O((n-l)*l)
    cantidad_filas = len(demanda_filas)
    orientacion = 'V'
    barco_colocado = False
    for fila in range(0,cantidad_filas): # O((n-l)*l)
        if validar_vertical(tablero, fila, columna, barco, demanda_filas, demanda_columnas):# O(l)
            tablero_actual = colocar_barco(tablero, fila, columna, barco, orientacion) # O(l)
            demanda_filas_actual, demanda_columnas_actual = actualizar_demandas(demanda_filas, demanda_columnas, fila, columna, barco, orientacion) # O(l)
            barco_colocado = True
            return tablero_actual, demanda_filas_actual, demanda_columnas_actual, barco_colocado
    return tablero, demanda_filas, demanda_columnas, barco_colocado

def poner_barco(tablero, demanda_filas, demanda_columnas, barco, fila_max_d, col_max_d): # O( (n-l)*l + (m-l)*l )

    if demanda_filas[fila_max_d] > demanda_columnas[col_max_d]:
        return poner_barco_en_fila(tablero, demanda_filas, demanda_columnas, barco, fila_max_d) # O((m-l)*l)
    elif demanda_filas[fila_max_d] < demanda_columnas[col_max_d]:
        return poner_barco_en_col(tablero, demanda_filas, demanda_columnas, barco, col_max_d) # O((n-l)*l)
    else: # O((n-l)*l) + O((m-l)*l)
        tablero, demanda_filas, demanda_columnas, barco_colocado = poner_barco_en_fila(tablero, demanda_filas, demanda_columnas, barco, fila_max_d)
        if not barco_colocado:
            return poner_barco_en_col(tablero, demanda_filas, demanda_columnas, barco, col_max_d)
        return tablero, demanda_filas, demanda_columnas, barco_colocado


# O( (n-l)*l + (m-l)*l )
# def poner_barco(tablero, demanda_filas, demanda_columnas, barco, fila_max_d, col_max_d):
#     barco_colocado = False

#     # colocar el barco en la fila
#     if barco <= demanda_filas[fila_max_d]:
#         if len(tablero[fila_max_d]) >= barco:
#             for i in range(barco):
#                 tablero[fila_max_d][i] = 1
#             demanda_filas[fila_max_d] -= barco
#             barco_colocado = True

#     # colocar el barco en la columna si no se colocó en la fila
#     if not barco_colocado and barco <= demanda_columnas[col_max_d]:
#         if len(tablero) >= barco:
#             for i in range(barco):
#                 tablero[i][col_max_d] = 1
#             demanda_columnas[col_max_d] -= barco
#             barco_colocado = True

#     return tablero, demanda_filas, demanda_columnas, barco_colocado


def batalla_naval_aproximada(tablero, demanda_filas, demanda_columnas, barcos):
    for barco in barcos: # O (k * ( ( (n-l)*l + (m-l)*l ) + n + m) )
        fila_max_d = demanda_filas.index(max(demanda_filas)) # O(n)
        col_max_d = demanda_columnas.index(max(demanda_columnas)) # O(m)

        if demanda_filas[fila_max_d] == 0 and demanda_columnas[col_max_d] == 0:
            return tablero, demanda_filas, demanda_columnas

        if barco <= demanda_filas[fila_max_d] or barco <= demanda_columnas[col_max_d]:
            tablero, demanda_filas, demanda_columnas, barco_colocado = poner_barco(tablero, demanda_filas, demanda_columnas, barco, fila_max_d, col_max_d)

    return tablero, demanda_filas, demanda_columnas


def batalla_naval(tablero, demanda_filas, demanda_columnas, barcos): # O (k * ( ( (n-l)*l + (m-l)*l ) + n + m) ) + O (n + m)
    demanda_total = sum(demanda_filas) + sum(demanda_columnas) # O(n + m)
    tablero_final, demanda_filas_final, demanda_columnas_final = batalla_naval_aproximada(tablero, demanda_filas, demanda_columnas, barcos)
    demanda_actual = sum(demanda_filas_final + demanda_columnas_final)
    
    print(f"La demanda total es: {demanda_total}")
    print(f"La demanda cumplida es: {demanda_total - demanda_actual}")
    return tablero_final

#Post: -
# def main():

#     file_paths = [
#         "archivos_prueba/3_3_2.txt", #0.0001 segundos [MAXIMO DE: 11 total | 4 OPTIMO por bt |  4 aproximado por greedy]
#         "archivos_prueba/5_5_6.txt", #0.0023 segundos [MAXIMO DE: 18 total | 12 OPTIMO por bt |  12 aproximado por greedy]
#         "archivos_prueba/8_7_10.txt", #0.0008 segundos [MAXIMO DE: 53 total | 26 OPTIMO por bt |  22 aproximado por greedy]
#         "archivos_prueba/10_3_3.txt", #0.0009 segundos [MAXIMO DE: 14 total | 6 OPTIMO por bt |  6 aproximado por greedy]
#         "archivos_prueba/10_10_10.txt", #0.009 segundos [MAXIMO DE: 40 total | 40 OPTIMO por bt |  38 aproximado por greedy]
#         "archivos_prueba/12_12_21.txt", #0.1519 segundos [MAXIMO DE: 58 total | 46 OPTIMO por bt |  40 aproximado por greedy] 
#         "archivos_prueba/15_10_15.txt", #0.0018 segundos [MAXIMO DE: 67 total | 40 OPTIMO por bt |  38 aproximado por greedy]
#         "archivos_prueba/20_20_20.txt", #0.0110 segundos [MAXIMO DE: 120 total | 104 OPTIMO por bt |  90 aproximado por greedy]
#         "archivos_prueba/20_25_30.txt", #0.0122 segundos [MAXIMO DE: 247 total | 172 OPTIMO por bt |  136 aproximado por greedy]
#         "archivos_prueba/30_25_25.txt"  #19 segundos [MAXIMO DE: 360 total | 202 OPTIMO por bt |  94 aproximado por greedy]
#     ]

#     for file_path in file_paths:
#         demanda_filas, demanda_columnas, barcos = leer_datos(file_path)
    
#         n = len(demanda_filas)
#         m = len(demanda_columnas)

#         print(f"\n Tablero: {file_path}")
#         tablero = [[0 for _ in range(m)] for _ in range(n)]

#         barcos.sort(reverse=True) # O(k log k)
#         #print(f"Barcos antes de procesar: {barcos}. Total: {len(barcos)}")
#         #print(f"Barcos luego de procesar: {barcos_procesados}. Total: {len(barcos_procesados)}")

#         inicio = time.time()
#         tablero_obtenido = batalla_naval(tablero, demanda_filas, demanda_columnas, barcos) # O (k * ( ( (n-l)*l + (m-l)*l ) + n + m) ) + O (n + m)
#         fin = time.time()
#         print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
#         #print("Tablero obtenido")
#         #imprimir_tablero(tablero_obtenido)

# if __name__ == "__main__":
#     main()

def solucion_aproximada(demanda_filas, demanda_columnas, barcos):
    n = len(demanda_filas)
    m = len(demanda_columnas)

    tablero = [[0 for _ in range(m)] for _ in range(n)]
    print("Tablero inicial")
    imprimir_tablero(tablero)

    barcos.sort(reverse=True)
    #print(f"Barcos antes de procesar: {barcos}. Total: {len(barcos)}")
    #print(f"Barcos luego de procesar: {barcos_procesados}. Total: {len(barcos_procesados)}")

    inicio = time.time()
    tablero_obtenido = batalla_naval(tablero, demanda_filas, demanda_columnas, barcos)
    fin = time.time()
    print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")

    print("Tablero obtenido")
    imprimir_tablero(tablero_obtenido)