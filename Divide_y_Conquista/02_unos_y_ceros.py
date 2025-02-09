
"""
Problema 02: Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros). Se pide una función de orden O(log(n)) que encuentre el índice del primer 0. 
Si no hay ningún 0 (solo hay unos), debe devolver -1.

Resolucion: Empleo la busqueda binaria para ir dividiendo el problema en mitades cada vez mas chicas con el objetivo de ir acercandome al cero. En cada posicion consulto si
mi valor actual esta antes de un 0 y si es asi, devuelvo la posicion donde encontré el cero. Si no lo hago continuo la busqueda dividiendo el arreglo a la mitad hasta dar con
el valor (o no).

La complejidad algoritmica es del orden de: O(log n) ya que empleando el teorema maestro tenemos un problema que dividimos en cada paso a la mitad por lo que B = 2, A = 1 ya 
que solo hacemos un llamado recursivo por cada llamada a la funcion y f(n) = 1 por lo que C = 0 ya que todas las demas operaciones son O(1). Con estos datos podemos plantear
que T(n) = T(n/2) + O(1), lo cual implica que como Log2(1) = 0 y C = 0, entonces estamos en el caso 2 en donde logB(A) = C por lo que la complejidad es O(log n).
"""

def busqueda_primer_cero(arr, inicio, fin):
    if inicio > fin: #No se encontró ningun cero
        return -1

    mitad = (inicio + fin) // 2

    if arr[mitad] == 1 and arr[mitad + 1] == 0:
        return mitad + 1
    
    elif arr[mitad] == 0 and arr[mitad - 1] == 1:
        return mitad

    if arr[mitad] == 1:
        return busqueda_primer_cero(arr, mitad + 1, fin)
    
    elif arr[mitad] == 0:
        return busqueda_primer_cero(arr, inicio, mitad - 1)


def indice_primer_cero(arr):
    if arr[0] == 0:
        return 0
    
    if arr[len(arr)-1] == 1:
        return -1
    
    return busqueda_primer_cero(arr, 0, len(arr) - 1)

def main():
    arr = [1,1,1,1,1,0,0,0,0,0,0,0]
    indice_buscado = indice_primer_cero(arr)
    print(f"Indice buscado: {indice_buscado}")


if __name__ == "__main__":
    main()