
"""
Problema 14:
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo  vértice de G: (1) pertenece a D, 
o bien (2) es adyacente a un vértice en D. Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con 
la mínima cantidad de vértices.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

from lib.grafo import Grafo

def dominating_set_min(grafo):
    return []


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

def main():

    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    grafo = generar_grafo(vertices) #10 vertices - 12 aristas
    grafo_sin_aristas = Grafo(False, vertices)

    vertex_cover_min(grafo)
 
if __name__ == "__main__":
    main()