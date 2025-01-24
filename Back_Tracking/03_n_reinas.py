
from lib.grafo import Grafo

"""
Problema 03:
Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique (si es posible) a n reinas de tal manera que ninguna pueda comerse con ninguna.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

def es_posicion_valida(tablero, n, n_reinas, posicion):
    x, y = posicion

    # Verificacion horizontal y vertical
    for reinas in n_reinas:
        if reinas[0] == x or reinas[1] == y:
            return False

    # Verifica diagonal principal (↘)
    i, j = x, y
    while i >= 0 and j >= 0:
        if tablero[i][j] != 0:
            return False
        i -= 1
        j -= 1

    i, j = x, y
    while i < n and j < n:
        if tablero[i][j] != 0:
            return False
        i += 1
        j += 1

    # Verifica diagonal secundaria (↙)
    i, j = x, y
    while i >= 0 and j < n:
        if tablero[i][j] != 0:
            return False
        i -= 1
        j += 1

    i, j = x, y
    while i < n and j >= 0:
        if tablero[i][j] != 0:
            return False
        i += 1
        j -= 1

    return True

#Pre: -
#Post: Devuelve una lista con las posiciones en las que colocar a las n reinas del tablero nxn tal que ninguna de ellas puede comerse a las demas.
#       Si no es posible devuelve la lista vacia.
def colocar_nreinas(tablero, n, n_reinas, posicion):
    if len(n_reinas) == n:
        return n_reinas

    fila, columna = posicion

    for i in range(fila, n):
        for j in range(columna if i == fila else 0, n):
            if tablero[i][j] == 0 and es_posicion_valida(tablero, n, n_reinas, (i, j)):
                tablero[i][j] = 1
                n_reinas.append((i, j))

                resultado = colocar_nreinas(tablero, n, n_reinas, (i, j + 1))
                if len(resultado) == n:
                    return resultado

                n_reinas.pop()
                tablero[i][j] = 0

    return n_reinas


def nreinas(n):
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    resultado = colocar_nreinas(tablero, n, [], (0, 0))
    return resultado if len(resultado) == n else []



def main():
    n = 8
    posiciones_posibles = nreinas(n)
    if posiciones_posibles:
        print(f"Es posible colocar la N reinas!: {posiciones_posibles}")
    else:
        print(f"No fue posible")

if __name__ == "__main__":
    main()