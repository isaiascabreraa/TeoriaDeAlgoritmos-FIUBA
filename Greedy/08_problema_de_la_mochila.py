
"""
Problema 08:
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que 
llevamos sin exceder la capacidad. Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos, y devuelva qué elementos deben ser guardados 
para maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. 
¿Por qué se trata de un algoritmo Greedy? Justificar

Resolucion:
Nuestra regla Greedy sera: "Tomar primero los elementos que tengan una mejor relacion valor/peso"
Los elementos con la mayor relación valor/peso son los que nos dan más valor por cada unidad de peso que ocupan. Sin embargo, para el problema de la mochila 0-1 (donde los 
elementos no se pueden dividir), este algoritmo no siempre garantiza una solución óptima.

Un ejemplo donde no se cumpla es si tengo: [(60, 10), (100, 20), (120, 30)] y W =50. En este caso mi solucion con esta regla quedaria en que debo colocar los elementos 1 y 2
pero el optimo realmente es colocar los elementos 2 y 3.

Es un algoritmo Greedy porque en cada paso toma la decisión localmente óptima (seleccionar el elemento con la mejor relación valor/peso), sin considerar el impacto de esa 
decisión en el futuro. Esta estrategia no garantiza que la solución global sea óptima, pero a menudo produce una solución que es lo suficientemente buena de manera 
eficiente.

Lo que se hace...

La complejidad algoritmica es del orden de: O(n log n)
"""

def mochila(elementos, W):

    i = 0
    peso_total = 0
    elementos_seleccionados = []
    elementos_ordenados = sorted(elementos, key=lambda x: (x[0], x[1]), reverse=True)

    while i < len(elementos_ordenados):

        if elementos_ordenados[i][1] + peso_total <= W:
            elementos_seleccionados.append(elementos_ordenados[i])
            peso_total += elementos_ordenados[i][1]
        i += 1
    return elementos_seleccionados

def main():

    # Cada elemento es de la forma (valor, peso)
    elementos = [(60, 10), (100, 20), (120, 30), (240, 40), (150, 25), (200, 35)]
    W = 200

    elementos_seleccionados = mochila(elementos, W)
    print("Elementos seleccionados para la mochila:", elementos_seleccionados)

if __name__ == "__main__":
    main()










"""
def mochila(elementos, W):
    # Calcula la relación valor/peso para cada elemento
    elementos = [(valor, peso, valor / peso) for valor, peso in elementos]
    
    elementos.sort(key=lambda x: x[2], reverse=True)
    
    capacidad_restante = W
    valor_total = 0
    elementos_seleccionados = []

    for valor, peso, ratio in elementos:
        if peso <= capacidad_restante:
            # Si el peso del elemento no excede la capacidad restante, lo agregamos
            elementos_seleccionados.append((valor, peso))
            valor_total += valor
            capacidad_restante -= peso
    
    return elementos_seleccionados, valor_total
"""