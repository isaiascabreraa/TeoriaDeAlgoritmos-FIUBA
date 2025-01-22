
from lib.grafo import Grafo

"""
Problema 05:
Un camino hamiltoniano, es un camino de un grafo, que visita todos los vértices del grafo una sola vez. Implementar un algoritmo por backtracking que encuentre un 
camino hamiltoniano de un grafo dado.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""


def bt_camino_hamiltoniano(grafo, camino, visitados, vertice_actual):
    # Si el camino incluye todos los vértices, hemos encontrado un camino hamiltoniano
    if len(camino) == len(grafo.obtener_vertices()):
        return camino

    # Recorrer los adyacentes al vértice actual
    for vecino in grafo.adyacentes(vertice_actual):
        if vecino not in visitados:
            # Marcar el vecino como visitado y agregarlo al camino
            visitados.add(vecino)
            camino.append(vecino)

            # Llamada recursiva
            resultado = bt_camino_hamiltoniano(grafo, camino, visitados, vecino)
            if resultado:  # Si encontramos un camino hamiltoniano
                return resultado

            # Backtracking: desmarcar y eliminar el vecino del camino
            visitados.remove(vecino)
            camino.pop()

    # Si no se encuentra un camino hamiltoniano desde este punto, retornar None
    return None


def camino_hamiltoniano(grafo):
    # Obtener los vértices del grafo
    vertices = grafo.obtener_vertices()
    if not vertices:
        return []

    # Probar con cada vértice como punto de inicio
    for vertice_inicio in vertices:
        camino = [vertice_inicio]
        visitados = {vertice_inicio}

        resultado = bt_camino_hamiltoniano(grafo, camino, visitados, vertice_inicio)
        if resultado:  # Si se encuentra un camino hamiltoniano
            return resultado

    # Si no se encuentra ningún camino hamiltoniano, retornar lista vacía
    return []



def main():
    
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #Tamaño 10
    grafo = generar_grafo(vertices)

    camino_encontrado = camino_hamiltoniano(grafo)
    print(f"Camino Hamiltoniano: {camino_encontrado}")

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