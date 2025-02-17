
"""
Problema 13:
Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. 
Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover. Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un 
conjunto de vértices que representen un mínimo Vertex Cover del mismo.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

from lib.grafo import Grafo

def contiene_aristas(subconjunto, aristas):
    if not aristas:
        return not subconjunto  # Si no hay aristas, el subconjunto debe estar vacío para ser válido

    vertices_en_subconjunto = set(subconjunto)

    for v, w in aristas: #Por cada vertice unido por una arista, chequeo si uno de los dos vertices se encuentra en el subconjunto.
        if v not in vertices_en_subconjunto and w not in vertices_en_subconjunto:
            return False  # Falta cubrir esta arista

    return True  # Todas las aristas tienen al menos un extremo en el subconjunto


def vertex_cover(grafo, subconjunto, mejor_subconjunto, index, aristas, vertices):
    
    if mejor_subconjunto and len(subconjunto) >= len(mejor_subconjunto):
        return mejor_subconjunto  # Podamos ramas innecesarias si ya superamos la mejor solución conocida

    for i in range(index, len(vertices)):
        vertice_actual = vertices[i]
        subconjunto.append(vertice_actual)

        if contiene_aristas(subconjunto, aristas):
            if not mejor_subconjunto or len(subconjunto) < len(mejor_subconjunto):
                mejor_subconjunto = subconjunto  # Actualizamos la mejor solución encontrada
        else:
            mejor_subconjunto = vertex_cover(grafo, subconjunto, mejor_subconjunto, i + 1, aristas, vertices)

        subconjunto.pop()

    return mejor_subconjunto


def vertex_cover_min(grafo):
    if not grafo:
        return []
    
    vertices = grafo.obtener_vertices()

    #Set de par de vertices unidos por una arista.
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