
"""
Problema 12: Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo es potencia de 2 (por 
ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, 
sin utilizar espacio adicional (obviando el utilizado por la recursividad y variables de tipos simples). ¿Cual es la complejidad del algoritmo?

Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.

Resolucion: Resolución:
Para resolver el problema, notamos que podemos dividir el arreglo en dos mitades:
- La primera mitad contiene los elementos `{C1, C2, ..., Cn}`.
- La segunda mitad contiene los elementos `{D1, D2, ..., Dn}`.

El objetivo es entrelazar ambas mitades sin utilizar espacio adicional. Para lograr esto mediante **División y Conquista**, seguimos los siguientes pasos:

1. **Dividimos** el arreglo en dos mitades iguales.
2. **Intercambiamos** los elementos centrales de cada mitad, de manera que los primeros elementos de la segunda mitad queden en sus posiciones correctas.
3. **Llamamos recursivamente** sobre cada mitad hasta alcanzar el caso base de tamaño 2, donde los elementos están en el orden correcto.

El patrón que seguimos se puede ver en arreglos pequeños:
- Para `n = 2`: `{C1, C2, D1, D2}` → `{C1, D1, C2, D2}` (caso base, se mantiene sin cambios).
- Para `n = 4`: `{C1, C2, C3, C4, D1, D2, D3, D4}` → Intercambiamos `{C2, C3} ↔ {D1, D2}`, aplicamos recursión en ambas mitades.
- Para `n = 8`: Intercambiamos bloques más grandes y aplicamos recursión.

Este proceso sigue un **árbol de recursión** donde en cada nivel realizamos `O(n)` intercambios, y la profundidad de la recursión es `O(log n)`, ya que en cada paso reducimos el problema a la mitad.

La complejidad algorítmica es del orden de: **O(n log n)**.
Esto se obtiene aplicando el **Teorema Maestro** con los parámetros:
- **A = 2** (hacemos dos llamadas recursivas por nivel).
- **B = 2** (el tamaño del problema se reduce a la mitad en cada paso).
- **C = 1** (el costo fuera de la recursión es O(n), ya que recorremos una parte del arreglo para intercambiar elementos).

Aplicando el teorema, tenemos el **caso 2** donde `C = log_B(A)`, lo que resulta en una complejidad **O(n log n)**.
"""

def alternar_rec(arr, inicio, fin):
    if fin - inicio == 2:
        return

    n = (fin - inicio) // 2
    mitad = inicio + n // 2

    for i in range(mitad, mitad + n // 2):
        arr[i], arr[i + n // 2] = arr[i + n // 2], arr[i]

    alternar_rec(arr, inicio, mitad + n // 2)
    alternar_rec(arr, mitad + n // 2, fin)

def alternar(arr):
    if not arr:
        return []
    return alternar_rec(arr, 0, len(arr))


def main():

    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    arr_alternado = alternar(arr)
    print("Después:", arr_alternado)


if __name__ == "__main__":
    main()
