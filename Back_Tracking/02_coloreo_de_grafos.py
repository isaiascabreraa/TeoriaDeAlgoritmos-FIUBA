
from lib.grafo import Grafo

"""
Problema 02:
Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, indique si es posible pintar cada vértice con n colores de tal forma que no hayan 
dos vértices adyacentes con el mismo color.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""


def es_color_valido(color, colores, adyacentes):
    for adyacente in adyacentes:
        if color == colores[adyacente]:
            return False
    return True

def bt_colorear(grafo, n, colores, v_coloreados, posicion, vertices):

    if v_coloreados == len(vertices):
        return True

    for color in range(n):
        adyacentes = grafo.adyacentes(vertices[posicion])

        if es_color_valido(color, colores, adyacentes):
            colores[vertices[posicion]] = color
            if bt_colorear(grafo, n, colores, v_coloreados+1, posicion+1, vertices):
                return True
            colores[vertices[posicion]] = -1
    return False

def colorear(grafo, n):
    vertices = grafo.obtener_vertices()
    colores = {vertice: -1 for vertice in vertices}
    return bt_colorear(grafo, n, colores, 0, 0, vertices)



def main():
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #Tamaño 10
    grafo = generar_grafo(vertices)
    n = 1

    grafo_coloreado = colorear(grafo, n)
    print(f"Grafo coloreado: {grafo_coloreado}")

def generar_grafo(vertices):
    grafo = Grafo(False, vertices)

    for i in range(len(vertices)-1):
        grafo.agregar_arista(vertices[i], vertices[i+1])
        print(f"Union de vertices: {vertices[i]} y {vertices[i+1]}")

    indice = 0
    while indice < len(vertices)-1:
        grafo.agregar_arista(vertices[indice], vertices[indice+2])
        print(f"Union de vertices: {vertices[indice]} y {vertices[indice+2]}")
        indice += 3
    return grafo


if __name__ == "__main__":
    main()