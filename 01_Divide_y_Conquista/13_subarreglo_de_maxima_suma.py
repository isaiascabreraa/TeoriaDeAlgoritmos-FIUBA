
"""
Problema 13: Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista. 
Indicar y justificar la complejidad del algoritmo. Ejemplos:

[5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
[5, 3, -5, 4, -1] ->  [5, 3]
[5, -4, 2, 4, -1] -> [5, -4, 2, 4]
[5, -4, 2, 4] -> [5, -4, 2, 4]
[-3, 4, -1, 2, 1, -5] -> [4, -1, 2, 1]

Resolucion: El proceso comienza dividiendo el arreglo en dos mitades y recursivamente buscando el subarreglo con la suma máxima en cada mitad. Sin embargo, al hacerlo de 
manera independiente, puede que no se detecten subarreglos cuya suma máxima se extienda a través del punto medio del arreglo. Por esta razón, el algoritmo también calcula 
la suma cruzada, es decir, el subarreglo que puede empezar en la mitad izquierda y extenderse hacia la mitad derecha. Luego, compara las tres posibles sumas máximas: la 
suma máxima en la mitad izquierda, en la mitad derecha y la suma cruzada. Finalmente, selecciona la que sea mayor y devuelve tanto la suma máxima como el subarreglo 
correspondiente.

La complejidad algoritmica es del orden de: O(n log n) debido a que A = 2, B = 2 y C = 1 por lo que al aplicar el teorema obtenemos que Log2(2) = C y por lo tanto la complejidad es
de O(n^C log n) que en este caso seria O(n log n).
"""

def max_subarray_rec(arr, inicio, fin):
    # Caso base: si inicio es igual a fin, retornamos el único elemento de la subarreglo y el subarreglo que lo contiene.
    if inicio == fin:
        return arr[inicio], [arr[inicio]]

    # Calculamos el punto medio del arreglo.
    medio = (inicio + fin) // 2

    # Llamadas recursivas para encontrar el subarreglo máximo en las mitades izquierda y derecha.
    max_izquierda_suma, subarreglo_max_izquierda = max_subarray_rec(arr, inicio, medio)
    max_derecha_suma, subarreglo_max_derecha = max_subarray_rec(arr, medio + 1, fin)

    # Encontramos el subarreglo máximo que cruza la mitad del arreglo.
    suma_izq = 0
    max_izquierda_cruzando = None
    max_izquierda_index = medio

    #Calculamos la maxima suma contigua partiendo desde el medio y yendo hacia el inicio.
    for i in range(medio, inicio - 1, -1):
        suma_izq += arr[i]
        if max_izquierda_cruzando is None or suma_izq > max_izquierda_cruzando:
            max_izquierda_cruzando = suma_izq
            max_izquierda_index = i

    suma_der = 0
    max_derecha_cruzando = None
    max_derecha_index = medio + 1
    
    #Calculamos la maxima suma contigua partiendo desde el medio y yendo hacia el fin.
    for i in range(medio + 1, fin + 1):
        suma_der += arr[i]
        if max_derecha_cruzando is None or suma_der > max_derecha_cruzando:
            max_derecha_cruzando = suma_der
            max_derecha_index = i

    #Sumamos el maximo de la izquierda con el de la derecha.
    max_cruzado =  (max_izquierda_cruzando or 0) + (max_derecha_cruzando or 0)

    # Comparamos las tres posibilidades: el máximo subarreglo en la izquierda,
    # el máximo subarreglo en la derecha, y el máximo subarreglo que cruza la mitad.
    max_suma = max(max_izquierda_suma, max_derecha_suma, max_cruzado)

    # Retornamos el máximo subarreglo correspondiente.
    if max_suma == max_izquierda_suma:
        return max_suma, subarreglo_max_izquierda
    
    elif max_suma == max_derecha_suma:
        return max_suma, subarreglo_max_derecha
    
    else:
        return max_cruzado, arr[max_izquierda_index:max_derecha_index + 1]



def max_subarray(arr):
    if not arr:
        return []
    
    max_suma, max_subarreglo = max_subarray_rec(arr, 0, len(arr) - 1)
    return max_subarreglo

def main():
    arr = [-50, 3, -5, -5, 3, 70, -1, 2]
    max_arr = max_subarray(arr)
    print(f"El subarreglo de máxima suma es {max_arr}")

if __name__ == "__main__":
    main()