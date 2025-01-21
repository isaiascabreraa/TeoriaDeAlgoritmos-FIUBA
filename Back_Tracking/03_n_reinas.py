
from lib.grafo import Grafo

"""
Problema 03:
Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique (si es posible) a n reinas de tal manera que ninguna pueda comerse con ninguna.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

def nreinas(n):
    return [(0, 0)]


def main():

    n = 4
    if nreinas(n):
        print(f"Es posible colocar la N reinas!")

    else:
        print(f"No fue posible")

    return 0

if __name__ == "__main__":
    main()