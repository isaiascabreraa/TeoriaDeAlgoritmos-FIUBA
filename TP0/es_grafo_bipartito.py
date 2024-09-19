
class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = {}

    def agregar_arista(self, origen, destino):
        if origen in self.adyacencia and destino in self.adyacencia:
            self.adyacencia[origen][destino] = True
            self.adyacencia[destino][origen] = True

    def hay_arista(self, origen, destino):
        return destino in self.adyacencia[origen]

    def adyacentes(self, vertice):
        return list(self.adyacencia[vertice].keys())

    def vertices(self):
        return list(self.adyacencia.keys())

def es_grafo_bipartito(grafo, vertice_inicial):
    colores = {}
    cola = [vertice_inicial]
    colores[vertice_inicial] = 0

    while cola:
        v = cola.pop(0)
        for w in grafo.adyacentes(v):
            if w in colores:
                if colores[w] == colores[v]: 
                    return False
            else:
                colores[w] = 1 - colores[v]
                cola.append(w)
    return True

def es_bipartito(grafo):
    colores = {}
    for vertice in grafo.vertices():
        if vertice not in colores:
            if not es_grafo_bipartito(grafo, vertice):
                return False
    return True



def main():

    grafo = Grafo()
    for vertice in range(6):
        grafo.agregar_vertice(vertice)

    # Agregar aristas
    #aristas = [(0, 1), (1, 2), (0, 3), (1, 3), (3, 4), (2, 5), (4, 5), (2, 4)] #NO es bipartito
    aristas = [(0, 1), (0, 3), (1, 4), (2, 3), (2, 5), (4, 5)] #SI es bipartito
    for origen, destino in aristas:
        grafo.agregar_arista(origen, destino)

    print(es_bipartito(grafo)) 

if __name__ == "__main__":
    main()
