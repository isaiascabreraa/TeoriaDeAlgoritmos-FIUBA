
"""
Problema 13:
Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. 
Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover. Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un 
conjunto de vértices que representen un mínimo Vertex Cover del mismo.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

from lib.grafo import Grafo

def contiene_aristas(grafo, subconjunto, aristas):
    if not aristas:
        return not subconjunto 
    else:
        aristas_actuales = set([(min(v, w), max(v, w)) for v in subconjunto for w in grafo.adyacentes(v)])
        return aristas == aristas_actuales


def vertex_cover(grafo, subconjunto, mejor_subconjunto, index, aristas, vertices):
    for i in range(index, len(vertices)):
        vertice_actual = vertices[i]
        nuevo_subconjunto = subconjunto + [vertice_actual]

        if not contiene_aristas(grafo, nuevo_subconjunto, aristas):
            mejor_subconjunto = vertex_cover(grafo, nuevo_subconjunto, mejor_subconjunto, i + 1, aristas, vertices)
        else:
            if len(nuevo_subconjunto) < len(mejor_subconjunto) or not mejor_subconjunto:
                mejor_subconjunto = nuevo_subconjunto

    return mejor_subconjunto


def vertex_cover_min(grafo):
    if not grafo:
        return []
    
    vertices = grafo.obtener_vertices()
    aristas = set([(min(v, w), max(v, w)) for v in grafo.obtener_vertices() for w in grafo.adyacentes(v)])

    subconjunto_buscado = vertex_cover(grafo, [], [], 0, aristas, vertices)
    print(f"El subconjunto obtenido es: {subconjunto_buscado}")
    return subconjunto_buscado



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