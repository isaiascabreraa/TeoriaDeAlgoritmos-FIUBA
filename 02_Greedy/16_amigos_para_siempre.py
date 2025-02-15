
"""
Problema 16:
El club de Amigos de Siempre prepara una cena en sus instalaciones en la que desea invitar a la máxima cantidad de sus n socios. Sin embargo por protocolo cada persona 
invitada debe cumplir un requisito: Sólo puede ser invitada si conoce a al menos otras 4 personas invitadas. Dada un lista de tuplas (duplas) de personas que se conocen:
a. Nos solicitan seleccionar el mayor número posible de invitados. 
b. Proponer una estrategia greedy óptima para resolver el problema.

Resolucion:
Nuestra regla Greedy sera: "Eliminar iterativamente a las personas que conocen menos de 4". Si, siempre es optimo ya que ...
El algoritmo es considerado Greedy porque ...

La complejidad algoritmica es del orden de: ...
"""

# conocidos: lista de pares de invitados que se conocen, cada elemento es un (a,b)
from lib.grafo import Grafo

def obtener_invitados(conocidos):

    grafo = Grafo()
    vertices = grafo.obtener_vertices()

    for (conocido1, conocido2) in conocidos:
        if conocido1 not in vertices:
            grafo.agregar_vertice(conocido1)
        if conocido2 not in vertices:
            grafo.agregar_vertice(conocido2)

        if not grafo.estan_unidos(conocido1, conocido2):
            grafo.agregar_arista(conocido1, conocido2)

    cambio = True
    while cambio:
        cambio = False
        borrar= []
        for vertice in vertices:
            if len(grafo.adyacentes(vertice)) < 4:
                borrar.append(vertice)
                cambio = True #Si saco uno, debo volver a chequear a los demas ya que los que antes podian conocer a 4, ahora pueden llegar a conocer solo 3.
        for vertice in borrar:
            grafo.borrar_vertice(vertice)

    resultado = []
    for vertice in grafo.obtener_vertices():
        resultado.append(vertice)

    return resultado

def main():
    conocidos = [
        ("Ana", "Luis"), ("Ana", "Carlos"), ("Luis", "Carlos"),
        ("Carlos", "Pedro"), ("Pedro", "Ana"), ("Pedro", "Luis"),
        ("Luis", "Marta"), ("Marta", "Carlos"), ("Marta", "Ana")]
    
    invitados = obtener_invitados(conocidos)
    print("Lista de invitados:", invitados)

if __name__ == "__main__":
    main()