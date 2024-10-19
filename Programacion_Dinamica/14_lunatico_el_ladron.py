
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
"""

"""def lunatico(ganancias):
    n = len(ganancias)

    # Manejo de casos base
    if n == 0:
        return []
    elif n == 1:
        return [0]  # Solo se puede robar la casa 0
    elif n == 2:
        return [0] if ganancias[0] >= ganancias[1] else [1]  # Elegir la de mayor ganancia

    # Arreglos para almacenar las mejores ganancias y las casas robadas
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
            casas_robadas[i] = casas_robadas[i - 1]  # Mantener la casa robada anterior

    # Reconstrucción de la solución
    resultado = []
    i = n - 1
    while i >= 0:
        if casas_robadas[i] == i:
            resultado.append(i)  # Agregar la casa robada
            i -= 2  # Saltar la casa vecina
        else:
            i -= 1  # Pasar a la casa anterior

    resultado.reverse()  # Invertir para mantener el orden original
    return resultado"""

def calcular_mejor_ganancia(ganancias):
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
    resultado_1 = calcular_mejor_ganancia(ganancias[:-1])
    ganancia_1 = sum(ganancias[i] for i in resultado_1)
    
    # Escenario 2: Excluyendo la primera casa
    resultado_2 = calcular_mejor_ganancia(ganancias[1:])
    resultado_2 = [i + 1 for i in resultado_2]
    ganancia_2 = sum(ganancias[i] for i in resultado_2)
    
    return resultado_1 if ganancia_1 > ganancia_2 else resultado_2


def main():

    # Ejemplo 1: Ganancias crecientes
    ganancias1 = [1, 2, 3, 4, 5]
    #[1,2,4,6,9] [0,0,0,0,0]
    casas_robadas1 = lunatico(ganancias1)
    print(f"Casas robadas (ganancias crecientes): {casas_robadas1}")

    # Ejemplo 2: Ganancias decrecientes
    ganancias2 = [5, 4, 3, 2, 1]
    casas_robadas2 = lunatico(ganancias2)
    print(f"Casas robadas (ganancias decrecientes): {casas_robadas2}")

    # Ejemplo 3: Alternando ganancias altas y bajas
    ganancias3 = [2, 7, 9, 3, 1, 8]
    casas_robadas3 = lunatico(ganancias3)
    print(f"Casas robadas (altas y bajas): {casas_robadas3}")

    # Ejemplo 4: Solo una casa
    ganancias4 = [10]
    casas_robadas4 = lunatico(ganancias4)
    print(f"Casas robadas (solo una casa): {casas_robadas4}")

    # Ejemplo 5: Sin ganancias
    ganancias5 = []
    casas_robadas5 = lunatico(ganancias5)
    print(f"Casas robadas (sin ganancias): {casas_robadas5}")

    # Ejemplo 6: Patrón más complejo
    ganancias6 = [1, 100, 1, 100, 1]
    casas_robadas6 = lunatico(ganancias6)
    print(f"Casas robadas (patrón complejo): {casas_robadas6}")

    #Ejemplo 7: Patron variado
    ganancias7 = [2, 3, 7, 5, 1, 8]
    casas_robadas7 = lunatico(ganancias7)
    print(f"Casas robadas (patrón variado): {casas_robadas7}")

if __name__ == "__main__":
    main()
