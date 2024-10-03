
class Grafo:
    def __init__(self, dirigido=False, vertices_init=[]):
        self.dirigido = dirigido
        self.vertices = {}
        for v in vertices_init:
            self.agregar_vertice(v)

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = {}

    def borrar_vertice(self, v):
        if v in self.vertices:
            # Eliminar las aristas que conectan con el vértice
            for adyacente in list(self.vertices[v]):
                self.borrar_arista(v, adyacente)
            del self.vertices[v]

    def agregar_arista(self, v, w, peso=1):
        self.agregar_vertice(v)
        self.agregar_vertice(w)
        self.vertices[v][w] = peso
        if not self.dirigido:
            self.vertices[w][v] = peso

    def borrar_arista(self, v, w):
        if v in self.vertices and w in self.vertices[v]:
            del self.vertices[v][w]
        if not self.dirigido and w in self.vertices and v in self.vertices[w]:
            del self.vertices[w][v]

    def estan_unidos(self, v, w):
        return v in self.vertices and w in self.vertices[v]

    def peso_arista(self, v, w):
        return self.vertices[v].get(w, None)

    def obtener_vertices(self):
        return list(self.vertices.keys())

    def vertice_aleatorio(self):
        import random
        return random.choice(self.obtener_vertices())

    def adyacentes(self, v):
        return list(self.vertices[v].keys()) if v in self.vertices else []

    def __str__(self):
        result = ""
        for v in self.vertices:
            for w in self.vertices[v]:
                result += f"{v} <--> {w} (peso: {self.vertices[v][w]})\n"
        return result
