
from lib.grafo import Grafo

def independent_set(grafo):
    return []


def main():

    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #Tamaño 10
    grafo = generar_grafo(vertices)

    independent_set_encontrado = independent_set(grafo)
    print(f"Independent set: {independent_set_encontrado}")

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