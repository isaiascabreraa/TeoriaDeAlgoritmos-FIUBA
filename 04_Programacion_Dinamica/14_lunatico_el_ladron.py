
"""
Problema 14:
Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar toda una calle en un barrio privado, que 
tiene la particularidad de ser circular. Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos 
enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n-1, 
que nos daría gn-1. Toda casa se considera adyacente a las casas i-1 e i+1. Además, como la calle es circular, la casas 0 y n-1 también son vecinas.

El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. No 
le daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. El Lunático nos encarga saber 
cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a 
este problema. Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a partir de recibir un 
arreglo de las ganancias obtenibles.

Complejidad algoritmica: O(n).El algoritmo solo hace un recorrido lineal en cada una de las dos ejecuciones de la función de programación dinámica. No hay 
anidación de bucles ni operaciones cuadráticas o exponenciales, lo que asegura que el tiempo de ejecución crece de manera lineal con el tamaño de la entrada.
"""

def lunatico_dinamico(ganancias):
    n = len(ganancias)
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0] if ganancias[0] >= ganancias[1] else [1]
    
    mejor_ganancia = [0] * n
    casas_robadas = [0] * n
    mejor_ganancia[0] = ganancias[0]
    casas_robadas[0] = 0
    mejor_ganancia[1] = max(ganancias[0], ganancias[1])
    casas_robadas[1] = 0 if ganancias[0] >= ganancias[1] else 1

    for i in range(2, n):
        ganancia_con_casa_actual = ganancias[i] + mejor_ganancia[i - 2]
        ganancia_sin_casa_actual = mejor_ganancia[i - 1]
        if ganancia_con_casa_actual > ganancia_sin_casa_actual:
            mejor_ganancia[i] = ganancia_con_casa_actual
            casas_robadas[i] = i
        else:
            mejor_ganancia[i] = ganancia_sin_casa_actual
            casas_robadas[i] = casas_robadas[i - 1]

    return reconstruir_solucion(casas_robadas, n)

def reconstruir_solucion(casas_robadas, n):
    resultado = []
    i = n - 1
    while i >= 0:
        if casas_robadas[i] == i:
            resultado.append(i)
            i -= 2
        else:
            i -= 1
    resultado.reverse()
    return resultado

def lunatico(ganancias):
    if not ganancias:
        return []
    if len(ganancias) == 1:
        return [0]
    
    # Escenario 1: Excluyendo la última casa
    resultado_1 = lunatico_dinamico(ganancias[:-1])
    ganancia_1 = sum(ganancias[i] for i in resultado_1)
    
    # Escenario 2: Excluyendo la primera casa
    resultado_2 = lunatico_dinamico(ganancias[1:])
    resultado_2 = [i + 1 for i in resultado_2]
    ganancia_2 = sum(ganancias[i] for i in resultado_2)
    
    return resultado_1 if ganancia_1 > ganancia_2 else resultado_2


def main():

    ganancias = [2, 7, 9, 3, 1, 8]
    casas_robadas = lunatico(ganancias)
    print(f"Casas robadas: {casas_robadas}")


if __name__ == "__main__":
    main()
