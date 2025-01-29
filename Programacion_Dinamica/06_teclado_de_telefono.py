
from lib.grafo import Grafo

"""
Problema 06: Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad de posibles números de longitud N empezando por botón del número inicial k. 
Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual. 
Indicar y justificar la complejidad del algoritmo implementado. Ejemplos:
    Para n=1 empezando por cualquier dígito, solamente hay un número válido (el correspondiente dígito)
    Para N=2, depende de cuál dígito se comienza.
    Empezando por 0, son válidos 00, 08 (cantidad: 2)
    Empezando por 1, son válidos 11, 12, 14 (cantidad: 3)
    Empezando por 2, son válidos 22, 21, 23, 25 (cantidad: 4)
    Empezando por 3, son válidos 33, 32, 36 (cantidad: 3)
    Empezando por 4, son válidos 44, 41, 45, 47 (cantidad: 4)
    Empezando por 5, son válidos 55, 52, 54, 56, 58 (cantidad: 5)
    Empezando por 6, son válidos 66, 63, 65, 69 (cantidad: 4)
    Empezando por 7, son válidos 77, 74, 78 (cantidad: 3)
    Empezando por 8, son válidos 88, 80, 85, 87, 89 (cantidad: 5)
    Empezando por 9, son válidos 99, 96, 98 (cantidad: 3)

Resolucion:

La complejidad algoritmica es del orden de: O(n^2)
"""

def numeros_posibles(k, n):

    if k < 0 or k > 9 or n == 0:
        return 0
    
    vertices = list(range(10))
    teclado = Grafo(False, vertices)
    cantidad_teclas = len(vertices)
    adyacencias = { 
        0: [0, 8], 
        1: [1, 2, 4], 
        2: [2, 1, 3, 5], 
        3: [3, 2, 6], 
        4: [4, 1, 5, 7], 
        5: [5, 2, 4, 6, 8], 
        6: [6, 3, 5, 9], 
        7: [7, 4, 8], 
        8: [8, 5, 7, 9, 0], 
        9: [9, 6, 8] }
    
    for v, vecinos in adyacencias.items():
        for w in vecinos:
            if not teclado.estan_unidos(v, w):
                teclado.agregar_arista(v, w)

    return numeros_posibles_dinamico(teclado, k, n, cantidad_teclas)


def numeros_posibles_dinamico(teclado, tecla_inicial, largo, cantidad_teclas):

    anterior = [1] * cantidad_teclas
    actual = [0] * cantidad_teclas

    for _ in range(2, largo + 1):  
        for tecla in range(cantidad_teclas):

            actual[tecla] = sum(anterior[adyacente] for adyacente in teclado.adyacentes(tecla))
        
        anterior, actual = actual, [0] * cantidad_teclas  

    return anterior[tecla_inicial]


def main():
    k = 5
    n = 3
    resultado = numeros_posibles(k, n)
    print(f"Caminos posibles: {resultado}")

if __name__=='__main__':
    main()