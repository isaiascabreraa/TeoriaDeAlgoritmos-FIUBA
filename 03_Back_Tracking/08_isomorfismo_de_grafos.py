
from lib.grafo import Grafo

"""
Problema 08:
Implementar un algoritmo de backtracking que, dados dos grafos, determine si existe un Isomorfismo entre ambos, dando a entender isomorfismo como que ambos grafos tengan
la misma cantidad de vertices unidos a la misma cantidad (que ambos grafos sean iguales pero con diferente nombre).

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

def contar_aristas(grafo, vertices, aristas):
    for v1 in vertices:
        for v2 in grafo.adyacentes(v1):
            if v1 < v2:
                aristas.add((v1, v2))

def bt_hay_isomorfismo(g1, g2, vertices_1, vertices_2, asignacion, cantidad_asignados):

    if cantidad_asignados == len(vertices_1):
        return True
    
    vertice_1 = vertices_1[cantidad_asignados]

    for vertice_2 in vertices_2:
       
        if vertice_2 not in asignacion.values(): #Si no hay ninguna clave con el valor del vertice 2...
            asignacion[vertice_1] = vertice_2

            es_valido = True
           
            for vertice in g1.adyacentes(vertice_1):
              
                if vertice in asignacion: #Si el vertice actual no es una clave del diccionario...
                    if not g2.estan_unidos(asignacion[vertice], vertice_2): #Si cuando busco el valor del vertice en la asignacion no me da que este unido al vertice 2...
                        es_valido = False
                        break

            if es_valido and bt_hay_isomorfismo(g1, g2, vertices_1, vertices_2, asignacion, cantidad_asignados + 1):
                return True

            del asignacion[vertice_1] #Quito el vertice

    return False


def hay_isomorfismo(g1, g2):

    vertices_1 = g1.obtener_vertices()
    vertices_2 = g2.obtener_vertices()
    if len(vertices_1) != len(vertices_2):
        return False
    
    aristas_1 = set()
    aristas_2 = set()
    contar_aristas(g1, vertices_1, aristas_1)
    contar_aristas(g2, vertices_2, aristas_2)

    if len(aristas_1) != len(aristas_2):
        return False
    
    asignacion = {}
    return bt_hay_isomorfismo(g1, g2, vertices_1, vertices_2, asignacion, 0)
     



def main():

    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #Tamaño 10
    g1 = generar_grafo(vertices)
    g2 = generar_grafo(vertices)

    if hay_isomorfismo(g1, g2):
        print(f"Los grafos son isomorfos!")
    else:
        print(f"No hay isomorfismo de grafos")

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