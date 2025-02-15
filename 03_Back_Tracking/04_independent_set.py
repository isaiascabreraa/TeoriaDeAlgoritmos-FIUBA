
from lib.grafo import Grafo

"""
Problema 04:
Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un máximo Independent Set del mismo.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

#Pre: -
#Post: Devuelve una lista con la mayor combinacion posible de vertices tales que ninguno de ellos sea adyacente a los demas.
def bt_independent_set(grafo, subconjunto_actual, mejor_subconjunto, vertices, posicion):

    cantidad_vertices = len(vertices)
    for i in range(posicion, cantidad_vertices):

        print(f"Posicion: {i}")
        print(f"{subconjunto_actual}")

        adyacentes = grafo.adyacentes(vertices[i])
        if all(adyacente not in subconjunto_actual for adyacente in adyacentes):
            subconjunto_actual.append(vertices[i])

            mejor_subconjunto = bt_independent_set(grafo, subconjunto_actual, mejor_subconjunto, vertices, i+1)
            subconjunto_actual.pop()

    if len(subconjunto_actual) > len(mejor_subconjunto):
        return subconjunto_actual[:]
    else:
        return mejor_subconjunto


def independent_set(grafo):
    vertices = grafo.obtener_vertices()
    return bt_independent_set(grafo, [], [], vertices, 0)


def main():

    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #Tamaño 10
    grafo = generar_grafo(vertices)

    independent_set_encontrado = independent_set(grafo)
    print(f"Independent set: {independent_set_encontrado}")

def generar_grafo(vertices):
    grafo = Grafo(False, vertices)

    for i in range(len(vertices)-1):
        grafo.agregar_arista(vertices[i], vertices[i+1])

    indice = 0
    while indice < len(vertices)-1:
        grafo.agregar_arista(vertices[indice], vertices[indice+2])
        indice += 3
    return grafo


if __name__ == "__main__":
    main()