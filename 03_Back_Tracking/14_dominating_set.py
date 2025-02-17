
from lib.grafo import Grafo

"""
Problema 14:
Dado un grafo G, un Dominating Set es el subconjunto D para el cual se incluyen la minima cantidad de vertices tal que como mucho los demas vertices esten 
a una arista de distancia del conjunto D o sean parte de dicho conjunto. Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho 
grafo con la mínima cantidad de vértices.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

def es_dominante(grafo, subconjunto, vertices):
    for v in vertices:
        if v in subconjunto:
            continue
        
        # Si el vértice no está en el subconjunto, verificamos si está conectado a alguno de sus elementos
        esta_cubierto = any(grafo.estan_unidos(v, u) for u in subconjunto)
        
        # Si no está cubierto, el subconjunto no es dominante
        if not esta_cubierto:
            return False

    return True

def dominating_set(grafo, subconjunto, subconjunto_dominante, index, vertices):

    if subconjunto_dominante and len(subconjunto) >= len(subconjunto_dominante):
        return subconjunto_dominante  # Podamos ramas innecesarias si ya superamos la mejor solución conocida.

    #Por cada vertice en vertices, corroboro si esta en el conjunto o si alguno de los vertices tiene algun elemento del subconjunto como adyacente.
    if es_dominante(grafo, subconjunto, vertices):
        if not subconjunto_dominante or len(subconjunto) < len(subconjunto_dominante):
            return subconjunto[:]
        return subconjunto_dominante
    
    for i in range(index, len(vertices)):
        vertice_actual = vertices[i]

        if vertice_actual not in subconjunto:
            subconjunto.append(vertice_actual)
            subconjunto_dominante = dominating_set(grafo, subconjunto, subconjunto_dominante, i + 1, vertices)
            subconjunto.pop()

    return subconjunto_dominante

def dominating_set_min(grafo):
    if not grafo:
        return []

    vertices = grafo.obtener_vertices()
    subconjunto_dominante = dominating_set(grafo, [], [], 0, vertices)
    print(f"El subconjunto dominante obtenido es: {subconjunto_dominante}")
    return subconjunto_dominante

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

    dominating_set_min(grafo)
 
if __name__ == "__main__":
    main()