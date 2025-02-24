
from lib.grafo import Grafo

"""
Problema 18:
Implementar un algoritmo que, por backtracking, obtenga la cantidad total de posibles ordenamientos topológicos de un grafo dirigido y acíclico.


Resolucion: ...

La complejidad algoritmica es del orden de: O(2^n)
"""


def obtener_predecesores(grafo, v):
    #Retorna los predecesores de un vértice en un grafo dirigido.
    return [w for w in grafo.obtener_vertices() if grafo.estan_unidos(w, v)]

def contar_ordenamientos_bt(grafo, orden_actual, visitados, orden_total, vertices, vertices_actualizados):
    #Genera todos los ordenamientos topológicos posibles por backtracking.
    
    if len(orden_actual) == len(vertices):
        orden_total.append(orden_actual[:])
        return
    
    vertices_actualizados = vertices[:]

    for v in vertices[:]:
    
        if v not in visitados and all(predecesor in visitados for predecesor in obtener_predecesores(grafo, v)):
        #El vertice V solo se agrega si aun no fue visitado y si todos sus predecesores ya fueron agregados al orden.

            visitados.add(v)
            orden_actual.append(v)
            vertices_actualizados.remove(v)

            contar_ordenamientos_bt(grafo, orden_actual, visitados, orden_total, vertices, vertices_actualizados)

            visitados.remove(v)
            orden_actual.pop()
            vertices_actualizados.append(v)

def contar_ordenamientos(grafo):
    if not grafo:
        return 0

    orden_total = []
    visitados = set()
    vertices = grafo.obtener_vertices()
    contar_ordenamientos_bt(grafo, [], visitados, orden_total, vertices, vertices)

    return len(orden_total)


def main():
    vertices = ['A', 'B', 'C', 'D', 'E']
    grafo = generar_grafo(vertices)
    cantidad_ordenamientos = contar_ordenamientos(grafo)
    print(f"La cantidad total de ordenamientos topológicos es: {cantidad_ordenamientos}")


def generar_grafo(vertices):
    grafo = Grafo(True, vertices)  # Grafo dirigido
    grafo.agregar_arista('A', 'B')
    grafo.agregar_arista('A', 'C')
    grafo.agregar_arista('A', 'F')
    grafo.agregar_arista('B', 'D')
    grafo.agregar_arista('C', 'D')
    grafo.agregar_arista('D', 'E')
    grafo.agregar_arista('F', 'E')
    return grafo


if __name__ == "__main__":
    main()