
"""
Problema 05: Implementar Merge Sort. Justificar el orden del algoritmo mediante el teorema maestro.

Resolucion: Comienzo dividiendo el problema en dos (parte izquierda y derecha) en donde para cada parte voy a invocar una funcion de merge que lo que hará es generar un nuevo
arreglo en el que los numeros se coloquen ordenados. De esta forma los primeros casos seran ordenamientos entre dos numeros pero a medida que progresa el algoritmo iremos
mergeando arreglos izquierdos y derechos cada vez mas grandes hasta finalizar.

La complejidad algoritmica es del orden de: O(n log n) ya que empleando el teorema maestro tenemos un problema que dividimos en cada paso a la mitad por lo que B = 2, A = 2 
ya que hacemos dos llamados recursivos por cada llamada a la funcion y f(n) = O(n) por lo que C = 1. Con estos datos podemos plantear que T(n) = 2T(n/2) + O(n), lo cual implica 
que como Log2(2) = 1 y C = 1, entonces estamos en el caso 2 en donde logB(A) = C por lo que la complejidad es O(n log n).
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    izquierda = arr[:mid]
    derecha = arr[mid:]

    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = 0
    j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1
    return resultado

def main():
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print(f"{sorted_arr}")

if __name__ == "__main__":
    main()