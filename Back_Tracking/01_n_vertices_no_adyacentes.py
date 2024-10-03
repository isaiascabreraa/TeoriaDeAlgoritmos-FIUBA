
"""
Problema 01:
Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V, devuelva si es posible obtener un subconjunto de n vertices tal 
que ningun par de vertices sea adyacente entre si.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

from lib.grafo import Grafo

def subconjunto_no_adyacente(grafo, n, subconjunto, index, vertices):

    if len(subconjunto) == n:
        return subconjunto

    for i in range(index, len(vertices)):
        vertice_actual = vertices[i]
        
        es_adyacente = any(grafo.estan_unidos(vertice_actual, v) for v in subconjunto)
        
        if not es_adyacente:
            subconjunto.append(vertice_actual)
            resultado = subconjunto_no_adyacente(grafo, n, subconjunto, i + 1, vertices)
            
            if resultado:
                return resultado
            
            subconjunto.pop()

    return None

def no_adyacentes(grafo, n):
    if not grafo:
        return None

    vertices = grafo.obtener_vertices()
    print("El subconjunto esperado es: ['A', 'D', 'G', 'J']")
    
    subconjunto_buscado = subconjunto_no_adyacente(grafo, n, [], 0, vertices)
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

    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #Tamaño 10

    grafo = generar_grafo(vertices)
    grafo_sin_aristas = Grafo(False, vertices)

    '''Dadas las disposiciones del grafo, tiene como maximo 4 vertices adyacentes. 
    Si n > 4 el resultado será None.'''
    n = 4

    no_adyacentes(grafo, n)

    
if __name__ == "__main__":
    main()