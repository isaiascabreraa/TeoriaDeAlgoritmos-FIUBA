
"""
Problema 07: Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. Queremos maximizar 
el valor de lo que llevamos sin exceder la capacidad. Implementar un algoritmo que reciba los valores y pesos de los elementos, y devuelva qué elementos deben ser 
guardados para maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado.

Resolucion:

La complejidad algoritmica es del orden de: O(n * w)
"""

def reconstruir_solucion(elementos_optimos, elementos, cantidad_elementos, W):

    j = W
    i = cantidad_elementos
    elementos_seleccionados = []

    while i > 0 and j > 0:

        if elementos_optimos[i][j] != elementos_optimos[i - 1][j]:
            elementos_seleccionados.append(elementos[i - 1])
            j -= elementos[i - 1][1]
        
        i -= 1

    return elementos_seleccionados[::-1]

def mochila(elementos, W):

    if not elementos or W <= 0:
        return []
    
    cantidad_elementos = len(elementos)
    elementos_optimos = mochila_dinamica(elementos, cantidad_elementos, W)
    return reconstruir_solucion(elementos_optimos, elementos, cantidad_elementos, W)

def mochila_dinamica(elementos, cantidad_elementos, W):

    M_OPTIMOS = [[0] * (W + 1) for _ in range(cantidad_elementos + 1)]

    for i in range(1, cantidad_elementos + 1):
        for j in range(1, W + 1):

            if elementos[i - 1][1] <= j:
                M_OPTIMOS[i][j] = max(
                    M_OPTIMOS[i - 1][j],  # No incluyo el elemento

                    #Sumo el mayor valor obtenido cuando el peso era peso actual menos peso del objeto actual y le sumo el valor del objeto actual.
                    M_OPTIMOS[i - 1][j - elementos[i - 1][1]] + elementos[i - 1][0]  # Incluyo el elemento
                )
            else:
                M_OPTIMOS[i][j] = M_OPTIMOS[i - 1][j]  # No incluyo el elemento

    return M_OPTIMOS


def main():

    # Cada elemento es de la forma (valor, peso)
    elementos = [(10, 6), (1, 1), (8, 3), (100, 100), (6, 4), (11, 2), (7, 8), (2, 7), (11, 9)]
    W = 20

    resultado = mochila(elementos, W)
    print(f"{resultado}")

if __name__=='__main__':
    main()