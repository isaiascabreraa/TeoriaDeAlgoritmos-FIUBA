
"""
Problema 06:
Dada una matriz de 9x9, implementar un algoritmo por backtracking que llene la matriz con números del 1 al 9, dadas las condiciones del Sudoku (si es posible). Las 
condiciones son:
                (i) Las celdas están dispuestas en 9 subgrupos de 3x3.
                (ii) Cada columna y cada fila no puede repetir número.
                (iii) Cada subgrupo de 3x3 no puede repetir número.
                Las posiciones de la matriz con valor 0 se espera que se completen, las posiciones con valores entre 1 y 9 no deben modificarse.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

def es_posicion_valida(matriz, tamanio_matriz, tamanio_subgrupo, k, posicion):

    fila, columna = posicion

    for numero in range(tamanio_matriz):
        if matriz[fila][numero] == k or matriz[numero][columna] == k:
            return False
        
    grupo_inicio_fila = (fila // tamanio_subgrupo) * tamanio_subgrupo
    grupo_inicio_columna = (columna // tamanio_subgrupo) * tamanio_subgrupo

    for i in range(grupo_inicio_fila, grupo_inicio_fila + tamanio_subgrupo):
        for j in range(grupo_inicio_columna, grupo_inicio_columna + tamanio_subgrupo):
            if matriz[i][j] == k:
                return False
    return True

#Pre: La matriz debe de ser cuadrada
#Post: Devuelve True si es posible resolver el sudoku o False en caso contrario.
def bt_resolver_sudoku(matriz, tamanio_matriz, tamanio_subgrupo, posicion):
    
    fila, columna = divmod(posicion, tamanio_matriz)
    
    if posicion == tamanio_matriz * tamanio_matriz:
        return True

    if matriz[fila][columna] == 0:
        for k in range(1, tamanio_matriz + 1):

            if es_posicion_valida(matriz, tamanio_matriz, tamanio_subgrupo, k, (fila, columna)):
                matriz[fila][columna] = k
                
                if bt_resolver_sudoku(matriz, tamanio_matriz, tamanio_subgrupo, posicion + 1):
                    return True
                
                matriz[fila][columna] = 0

        return False

    else:
        return bt_resolver_sudoku(matriz, tamanio_matriz, tamanio_subgrupo, posicion + 1)



def resolver_sudoku(matriz):

    if not matriz:
        return []
    
    tamanio_subgrupos = 3
    tamanio_matriz = len(matriz)

    if bt_resolver_sudoku(matriz, tamanio_matriz, tamanio_subgrupos, 0):
        print("Sudoku resuelto")
    else:
        print("No se ha podido resolver el sudoku")

    return matriz
    


def comparar_matrices(matriz1, matriz2):

    if len(matriz1) != len(matriz2) or any(len(fila1) != len(fila2) for fila1, fila2 in zip(matriz1, matriz2)):
        return False

    for fila1, fila2 in zip(matriz1, matriz2):
        for elem1, elem2 in zip(fila1, fila2):
            if elem1 != elem2:
                return False
    return True

def main():

    sudoku_completo = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],]

    sudoku_sin_resolver = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 0, 0, 1, 9, 5, 3, 0, 8],
    [0, 9, 8, 0, 0, 0, 5, 6, 7],
    [8, 0, 0, 0, 6, 0, 4, 2, 3],
    [4, 0, 6, 8, 0, 3, 7, 9, 1],
    [7, 0, 0, 0, 2, 0, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [3, 0, 5, 0, 8, 0, 0, 7, 9],]

    sudoku_resuelto = resolver_sudoku(sudoku_sin_resolver)
    
    if comparar_matrices(sudoku_resuelto, sudoku_completo):
        print("Resolucion exitosa, sudoku completado!")
        
    else:
        print("El sudoku no ha sido resulto correctamente")


if __name__ == "__main__":
    main()