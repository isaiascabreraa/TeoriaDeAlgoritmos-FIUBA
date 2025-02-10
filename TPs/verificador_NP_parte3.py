def verificar_adyacencias(tablero, n, m, x, y, barco_tamano, orientacion):
    
    # Direcciones de las celdas adyacentes
    if orientacion == 'H':
        adyacentes = [
            (x-1, j) for j in range(y-1, y + barco_tamano + 1) if 0 <= j < m
        ] + [
            (x+1, j) for j in range(y-1, y + barco_tamano + 1) if 0 <= j < m
        ] + [
            (x, y-1), (x, y + barco_tamano)
        ]
    elif orientacion == 'V':
        adyacentes = [
            (i, y-1) for i in range(x-1, x + barco_tamano + 1) if 0 <= i < n
        ] + [
            (i, y+1) for i in range(x-1, x + barco_tamano + 1) if 0 <= i < n
        ] + [
            (x-1, y), (x + barco_tamano, y)
        ]
    else:
        adyacentes = [
            (x-1, y-1), (x-1, y), (x-1, y+1),
            (x, y-1),           (x, y+1),
            (x+1, y-1), (x+1, y), (x+1, y+1)
        ]

    # Verificar si alguna celda adyacente contiene un barco
    for i, j in adyacentes:
        if 0 <= i < n and 0 <= j < m and tablero[i][j] == 1:
            return False
    return True

def verificar_solucion(tablero, demanda_filas, demanda_columnas, barcos_esperados):
    n = len(tablero)
    m = len(tablero[0])
    
    demandas_filas_actual = [0] * n
    demandas_columnas_actual = [0] * m
    
    for i in range(n):
        for j in range(m):
            if tablero[i][j] == 1:
                demandas_filas_actual[i] += 1
                demandas_columnas_actual[j] += 1
    
    for i in range(n):
        if demandas_filas_actual[i] > demanda_filas[i]:
            print(f"Error: Demanda de la fila {i} excedida ({demandas_filas_actual[i]} > {demanda_filas[i]}).")
            return False
    
    for j in range(m):
        if demandas_columnas_actual[j] > demanda_columnas[j]:
            print(f"Error: Demanda de la columna {j} excedida ({demandas_columnas_actual[j]} > {demanda_columnas[j]}).")
            return False
    
    barcos_contados = []
    visitado = [[False for _ in range(m)] for _ in range(n)]
    
    def buscar_continuidad_barco(x, y, orientacion):
        if x < 0 or x >= n or y < 0 or y >= m or visitado[x][y] or tablero[x][y] == 0:
            return 0
        visitado[x][y] = True
        if orientacion == 'H':
            return 1 + buscar_continuidad_barco(x, y + 1, orientacion)
        elif orientacion == 'V':
            return 1 + buscar_continuidad_barco(x + 1, y, orientacion)
        return 1

    for i in range(n):
        for j in range(m):
            if tablero[i][j] == 1 and not visitado[i][j]:
                if j + 1 < m and tablero[i][j + 1] == 1:  # Horizontal
                    barco_tamano = buscar_continuidad_barco(i, j, 'H')
                    if not verificar_adyacencias(tablero,n, m, i, j, barco_tamano, 'H'):
                        print("Error: Barcos adyacentes detectados.")
                        return False
                elif i + 1 < n and tablero[i + 1][j] == 1:  # Vertical
                    barco_tamano = buscar_continuidad_barco(i, j, 'V')
                    if not verificar_adyacencias(tablero,n ,m, i, j, barco_tamano, 'V'):
                        print("Error: Barcos adyacentes detectados.")
                        return False
                else:  # Barco individual
                    barco_tamano = 1
                    if not verificar_adyacencias(tablero, n, m, i, j, barco_tamano, '1'):
                        print("Error: Barcos adyacentes detectados.")
                        return False
                
                barcos_contados.append(barco_tamano)
    
    barcos_contados.sort(reverse=True)
    barcos_esperados.sort(reverse=True)
    
    if barcos_contados != barcos_esperados:
        print(f"Error: Los barcos_esperados colocados {barcos_contados} no coinciden con los barcos_esperados esperados {barcos_esperados}.")
        return False
    
    print("La solución es válida.")
    return True