
"""
Problema 04: Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: estrictamente creciente hasta una determinada posición p, y estrictamente decreciente a partir 
de ella (con 0 < p < N - 1). Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2. Se pide:

1. Implementar un algoritmo de división y conquista de orden O(log n) que encuentre la posición p del pico: func PosicionPico(v []int, ini, fin int) int. La función será 
invocada inicialmente como: PosicionPico(v, 0, len(v)-1), y tiene como pre-condición que el arreglo tenga forma de pico.
2. Justificar el orden del algoritmo mediante el teorema maestro.

Resolucion: Lo que hacemos es emplear una busqueda binaria en donde si el elemento actual es el pico lo retornamos pero si no lo es chequeamos que el valor actual sea menor
que el anterior ya que en caso de serlo debemos avanzar hacia adelante y en caso contrario hacia atras. De esta forma vamos diviendo el problema en dos y buscando la solucion
en partes cada vez mas pequeñas hasta encontrar el pico.

La complejidad algoritmica es del orden de: O(log n) ya que empleando el teorema maestro tenemos un problema que dividimos en cada paso a la mitad por lo que B = 2, A = 1 ya 
que solo hacemos un llamado recursivo por cada llamada a la funcion y f(n) = 1 por lo que C = 0 ya que todas las demas operaciones son O(1). Con estos datos podemos plantear
que T(n) = T(n/2) + O(1), lo cual implica que como Log2(1) = 0 y C = 0, entonces estamos en el caso 2 en donde logB(A) = C por lo que la complejidad es O(log n).
"""

#Pre: El arreglo debe tener un pico.
#Post: Nos devuelve en que posicion se encuentra ese pico.
def busqueda_posicion_pico(arr_pico, inicio, fin):
    if inicio == fin:
        return inicio

    mitad = (inicio + fin) // 2

    if arr_pico[mitad] > arr_pico[mitad - 1] and arr_pico[mitad] > arr_pico[mitad + 1]:
        return mitad
    
    elif arr_pico[mitad] < arr_pico[mitad - 1]:
        return busqueda_posicion_pico(arr_pico, inicio, mitad)
    
    else:
        return busqueda_posicion_pico(arr_pico, mitad + 1, fin)

def posicion_pico(v, ini, fin):
    if not v:
        return None
    
    if len(v) == 1:
        return 0
    else:
        return busqueda_posicion_pico(v, ini, fin)


def main():
    arr_pico = [1, 2, 3, 1, 0, -2]
    pico = posicion_pico(arr_pico, 0, len(arr_pico) - 1)
    print(f"El pico del array {arr_pico} es {pico}")

if __name__ == "__main__":
    main()