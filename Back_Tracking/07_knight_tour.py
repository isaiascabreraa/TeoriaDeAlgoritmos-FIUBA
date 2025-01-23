
"""
Problema 07:
Implementar un algoritmo de backtracking que, dado una pieza de caballo en un tablero de ajedrez de n x n, determine si existen los movimientos a realizar para que el caballo 
logre pasar por todos los casilleros del tablero una única vez. Recordar que el caballo mueve en forma de L (dos casilleros en una dirección, y un casillero en forma 
perpendicular).

Resolucion: ...

Grafo: Se puede reutilizar el algoritmo de camino hamiltoneano para resolver este mismo problema. Unicamente tengo que convertir el tablero en un grafo, uniendo por medio
de aristas los vertices de los posibles movimiento del caballo (forma de L) y aplicar el algoritmo mencionado a ese grafo.

La complejidad algoritmica es del orden de: ...
"""


def movimientos_posibles_caballo(fila, columna, n, casillas):
    
    movimientos = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    posibles_posiciones = []
    
    for movimiento in movimientos:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]
        
        if 0 <= nueva_fila < n and 0 <= nueva_columna < n:

            posicion = nueva_fila * n + nueva_columna

            if posicion not in casillas:
                posibles_posiciones.append(posicion)

    #Ordeno los posibles movimientos en base a cual movimiento tiene mas movimientos posibles a continuacion.
    posibles_posiciones.sort(key=lambda siguiente_posicion: sum( 1 for fila_movimientos, columna_movimientos in movimientos
        if 0 <= (siguiente_posicion // n + fila_movimientos) < n 
        and 0 <= (siguiente_posicion % n + columna_movimientos) < n 
        and ((siguiente_posicion // n + fila_movimientos) * n + (siguiente_posicion % n + columna_movimientos)) not in casillas
    ))
    return posibles_posiciones


def bt_knight_tour(n, casillas, casillas_recorridas, posicion):

    if casillas_recorridas == n*n:
        return True
    
    fila, columna = divmod(posicion, n)
    posibles_movimientos = movimientos_posibles_caballo(fila, columna, n, casillas)

    for movimento in posibles_movimientos:
        casillas.add(movimento)
        if bt_knight_tour(n, casillas, casillas_recorridas+1, movimento):
            return True
        casillas.remove(movimento)

    return False


def knight_tour(n):
    casillas = set()
    posicion_inicial = 0
    casillas.add(posicion_inicial)
    return bt_knight_tour(n, casillas, 1, posicion_inicial)


def main():

    n = 6
    if knight_tour(n):
        print(f"Es posible que el caballo recorra todo el tablero!")
    else:
        print(f"Debido a las dimensiones del tablero es imposible que el caballo lo recorra.")
 
if __name__ == "__main__":
    main()