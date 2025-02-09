
"""
Problema 01: Implementar, por división y conquista, una función que dado un arreglo sin elementos repetidos y casi ordenado (todos los elementos se encuentran ordenados, salvo 
uno), obtenga el elemento fuera de lugar. Indicar y justificar el orden.

Resolucion: Comienza buscando en la primera mitad del arreglo si el valor actual es menor que el anterior o mayor que el siguiente. De no encontrar nada en la primer mitad,
continua buscando en la segunda.

La complejidad algoritmica es del orden de: O(n) ya que empleando el teorema maestro tenemos un problema que dividimos en cada paso a la mitad por lo que B = 2, A = 2 ya 
que hacemos 2 llamados recursivos por cada llamada a la funcion y f(n) = 1 por lo que C = 0 ya que todas las demas operaciones son O(1). Con estos datos podemos plantear
que T(n) = 2T(n/2) + O(1), lo cual implica que como Log2(2) = 1 y C = 0, entonces estamos en el caso 3 en donde logB(A) = C por lo que la complejidad es O(n).
"""


def busqueda_elemento_desordenado(arr, inicio, fin):
    if inicio > fin: #No encontró el elemento
        return None
    
    mitad = (inicio + fin) // 2
        
    if mitad > 0 and arr[mitad] < arr[mitad-1]:
            return arr[mitad-1]
    
    if mitad < len(arr)-1 and arr[mitad] > arr[mitad + 1]:
        return arr[mitad]
    
    valor_buscado = busqueda_elemento_desordenado(arr, mitad + 1, fin)
    if not valor_buscado:
        valor_buscado = busqueda_elemento_desordenado(arr, inicio, mitad - 1)

    return valor_buscado

def elemento_desordenado(arr):
    return busqueda_elemento_desordenado(arr, 0, len(arr) - 1)


def main():
    arr = [0,1,2,3,4,5,8,11,15,13,16,18]
    elemento_encontrado = elemento_desordenado(arr)
    print(f"Elemento: {elemento_encontrado}")

if __name__ == "__main__":
    main()
