
"""
Problema 14:
Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. Implementar un algoritmo Greedy que dé la cantidad mínima de 
faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las 
directamente adyacentes a estas (es decir, un “radio de 2 celdas”). Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado da siempre la 
solución óptima? Justificar

Resolucion:
Nuestra regla Greedy sera: "Seleccionar siempre la posición en la que se pueda iluminar la mayor cantidad de submarinos". No es siempre optimo ya que seleccionar siempre la 
celda ilumina mas subarinos puede llevar a una solucion global no optima como en el caso de
El algoritmo es considerado Greedy porque Si hay varias opciones para colocar un faro, el algoritmo elige la que ilumina más submarinos en ese momento, sin evaluar cómo 
afectará la distribución de los faros en pasos futuros.

A grandes rasgos lo que se hace es contar submarinos cercanos a cada celda de la matriz (considerando un radio de 2 celdas), seleccionar la celda que ilumina la mayor 
cantidad de subamrinos, colocar el faro en esa celda y marcar las celdas iluminadas (eliminando submarinos). Esto lo repite hasta que no queden submarinos.

La complejidad algoritmica es del orden de: O(nm) ⋅ O(nm) = O((nm))²
"""


# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y)
# matriz booleana, indica True en las posiciones con submarinos
def iluminar(matriz, x, y):
    n = len(matriz)
    m = len(matriz[0])
    for i in range(max(0, x-2), min(n, x+3)):
        for j in range(max(0, y-2), min(m, y+3)):
            matriz[i][j] = False

def contar_submarinos(matriz, x, y):
    n = len(matriz)
    m = len(matriz[0])
    cuenta_submarinos = 0
    for i in range(max(0, x-2), min(n, x+3)):
        for j in range(max(0, y-2), min(m, y+3)):
            if matriz[i][j]:
                cuenta_submarinos += 1
    return cuenta_submarinos


def submarinos(matriz):
    if not matriz:
        return []

    faros = []
    n = len(matriz)
    m = len(matriz[0])

    while any(any(row) for row in matriz):
        max_submarinos = 0
        mejor_posicion = None

        for i in range(n):
            for j in range(m):
                cuenta_submarinos = contar_submarinos(matriz, i, j)
                if cuenta_submarinos > max_submarinos:
                    max_submarinos = cuenta_submarinos
                    mejor_posicion = (i, j)

        if mejor_posicion:
            x, y = mejor_posicion
            faros.append((x, y))
            iluminar(matriz, x, y)

    return faros


def main():

    matriz = [
        [True, False, True, False],
        [False, True, False, True],
        [True, False, True, False],
        [False, True, False, True]
    ]

    faros = submarinos(matriz)
    print("Posiciones de los faros:", faros)

if __name__ == "__main__":
    main()