

"""
Problema 09: Tenemos un conjunto de números v_1, v_2, ... , v_n, y queremos obtener un subconjunto de todos esos números tal que su suma sea igual o menor a un valor V, 
tratando de aproximarse lo más posible a V. Implementar un algoritmo que reciba un arreglo de valores, y la suma objetivo V, y devuelva qué elementos deben ser utilizados 
para aproximar la suma lo más posible a V, sin pasarse. Indicar y justificar la complejidad del algoritmo implementado.

Resolucion: Lo que hago inicialmente es generar una matriz de N * V en la cual voy probando caso a caso si agrego o no el elemento para diferentes valores menores o iguales 
a V. Por ejemplo, inicio considerando si debo de agregar el primer elemento cuando V = 0, luego se lo agrego cuando V = 1 y asi hasta que V = V. Luego continuo con el
elemento siguiente y asi sucesivamente. En caso de no poder agregar el elemento me quedo con el optimo cuando habia un elemento menos (Optimo[i - 1][j]) y si puedo agregarlo
entonces uso el valor mas grande entre el optimo anterior (Optimo[i - 1][j]) y el valor obtenido de el elemento actual + el optimo que habia en la posicion que resulta de
restar a la columna actual el valor del elemento actual (Optimo[i - 1][j - elemento_actual]).

Mi ecuacion de recurrencia resulta de la forma: SUBSET_OPTIMOS[i][j] = max(SUBSET_OPTIMOS[i - 1][j], SUBSET_OPTIMOS[i - 1][j - elementos[i - 1]] + elementos[i - 1]), en donde
para recontruir la solucion recorro la matriz obtenida (empezando por [N][V]) y verifico si la posicion actual i vale lo mismo que el optimo con un elemento menos (i - 1) y si 
es asi entonces retrocedo una fila (i -= 1) y sigo probando hasta encontrar encontrar el elemento que difiera del optimo anterior (Optimo[i][j] != Optimo[i - 1][j])) ya que 
ese será el que debemos utilizar, y una vez encontrado agregamos el valor de elemento[i - 1] a nuestra solucion y seguiremos con la fila anterior y la columna determinada
por Optimos[i - 1][j - elementos[i - 1]].

La complejidad algoritmica es del orden de: O(n * V)
"""


def reconstruir_subconjunto(elementos, dp, V):

    resultado = []
    i, j = len(elementos), V

    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            resultado.append(elementos[i - 1])
            j -= elementos[i - 1]
        i -= 1

    return resultado[::-1]


def subset_sum(elementos, v):

    subset_obtenido = subset_sum_dinamico(elementos, v)
    return reconstruir_subconjunto(elementos, subset_obtenido, v)


def subset_sum_dinamico(elementos, v):

    n = len(elementos)
    SUBSET_OPTIMOS = [[0] * (v + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(v + 1):

            if elementos[i - 1] > j:
                SUBSET_OPTIMOS[i][j] = SUBSET_OPTIMOS[i - 1][j]  # No podemos incluir este elemento
            else:
                SUBSET_OPTIMOS[i][j] = max(SUBSET_OPTIMOS[i - 1][j], SUBSET_OPTIMOS[i - 1][j - elementos[i - 1]] + elementos[i - 1])

    return SUBSET_OPTIMOS


def main():

    elementos = [3, 4, 12, 5, 2, 10]
    V = 19

    resultado = subset_sum(elementos, V)
    print(f"{resultado}")

if __name__=='__main__':
    main()