
from lib.grafo import Grafo

"""
Problema 06: Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad de posibles números de longitud N empezando por el botón del número inicial k. 
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

Resolucion: Primero formo un grafo que representa cada una de las teclas numericas de un celular y añado sus correspondientes vecinos segun como se encuentran dispuestos
en el telefono. Con esta informacion, lo que hago es iniciar con un caso base en donde n = 0 para el cual la cantidad de reclas recorridas es 1 para cada tecla ya que no 
me muevo de la posicion. Añado un 1 a cada una de las posiciones de mi arreglo denominado "teclas_recorridas".

Luego el siguiente caso es si n = 1 por lo que puedo desplazarme una posicion desde mi tecla inicial. Reviso las teclas adyacentes a mi tecla actual y sumo el 
total de sus recorridos anteriores por lo que si k = 5 (siendo k la tecla de inicio) y los vecinos de mi tecla_actual son 2, 4, 6 y 8, debo sumar teclas_recorridas[2], 
teclas_recorridas[4], teclas_recorridas[6] y teclas_recorridas[8] para luego almacenarlo en teclas_actuales[tecla_actual] para indicar que esa es la cantidad de 
movimiento posibles si k = 5 y n = 2. 

Continuo haciendo esto para cada tecla y cuando finalice el recorrido con cada una de ellas para el largo correspondiente el resultado estará almacenado en 
teclas_recorridas[tecla_inicial]. Mi ecuacion de recurrencia es: teclas_actual[tecla] = sum(teclas_recorridas[adyacente] for adyacente in teclado.adyacentes(tecla))

Como aclaración, si bien podria haber usado una matriz en vez de dos listas del tamaño de la cantidad de vertices (teclas). El hecho de usar dos listas fué por
una optimizacion de complejidad espacial innecesaria.

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

    teclas_recorridas = [1] * cantidad_teclas
    teclas_actual = [0] * cantidad_teclas

    for _ in range(2, largo + 1):  
        for tecla in range(cantidad_teclas):

            teclas_actual[tecla] = sum(teclas_recorridas[adyacente] for adyacente in teclado.adyacentes(tecla))
        
        teclas_recorridas, teclas_actual = teclas_actual, [0] * cantidad_teclas

    return teclas_recorridas[tecla_inicial]


def main():
    k = 5
    n = 3
    resultado = numeros_posibles(k, n)
    print(f"Caminos posibles: {resultado}")

if __name__=='__main__':
    main()