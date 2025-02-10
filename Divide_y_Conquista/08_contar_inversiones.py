

"""
Problema 08: Dados un conjunto de n elementos, y 2 arreglos de longitud n, con dichos elementos. El arreglo A está completamente ordenado de menor a mayor. El arreglo B se 
encuentra desordenado. Indicar, por división y conquista, la cantidad de inversioes necesarias al arreglo B para que quede ordenado de menor a mayor, con un orden de 
complejidad mejor que O(n^2). Justificar el orden del algoritmo mediante el teorema maestro.

Que es una inversion? Dos elementos estan invertidos si bi > bj (con i < j), o sea que es cuando tengo un elemento mas grande antes que uno mas chico. Ahora, si tenemos un 
arreglo como [2, 4, 1, 3, 5] entonces notemos que 2 esta antes que 1, 4 esta antes que 1 y 4 esta antes que tres, por lo que para ordenar el arreglo debo de realizar un 
total de tres inversiones.

Resolucion:

La complejidad algoritmica es del orden de:
"""

def merge_contar_inversiones(izq, der):
    i, j = 0, 0
    inversiones = 0
    
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            i += 1
        else:
            inversiones += len(izq) - i  # Todos los elementos restantes en izq son mayores
            j += 1
    
    return inversiones


def contar_inversiones_rec(arr):
    if len(arr) <= 1:
        return 0
    
    mid = len(arr) // 2
    inv_izq = contar_inversiones_rec(arr[:mid])
    inv_der = contar_inversiones_rec(arr[mid:])
    inv_merge = merge_contar_inversiones(arr[:mid], arr[mid:])
    
    return inv_izq + inv_der + inv_merge


def contar_inversiones(A, B):
    if not A or not B:
        return 0
    
    return contar_inversiones_rec(B)


def main():

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    resultado = contar_inversiones(A, B)
    print(f"{resultado}")

if __name__=='__main__':
    main()