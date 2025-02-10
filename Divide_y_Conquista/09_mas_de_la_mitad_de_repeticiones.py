
"""
Problema 09: Implementar una función (que utilice división y conquista) de orden O(n log n) que dado un arreglo de n números enteros devuelva true o false según si existe 
algún elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución. El arreglo NO puedo ordenarse bajo ningun termino. Ejemplos:

[1, 2, 1, 2, 3] -> false
[1, 1, 2, 3] -> false
[1, 2, 3, 1, 1, 1] -> true
[1] -> true

Resolucion: Dividimos el problema a la mitad hasta quedarnos solo con dos elementos (la parte izquierda y la derecha). Si ambos son el mismo elemento entonces lo retornamos, 
y si sin diferentes entonces buscamos en el arreglo original (desde el inicio actual hasta el fin actual), cual de ellos aparece mas veces. Al ser el inicio actual y el fin
actual nunca recorreremos todo el arreglo para corroborar esto (solo será una parte de él). Seguimos retornando el mayor elemento hasta que obtengamos el mayor elemento del 
arreglo original o None en caso de no hacerlo.

La complejidad algoritmica es del orden de: O(n log n) debido a que aplicando el teorema maestro tenemos que A = 2, B = 2 y C = 1 ya que todas las demas operaciones son O(n).
Por este motivo al aplicar el teorema maestro tenemos el caso 2 en el que LogB(A) = C y debido a que ambos son 1 y por lo tanto la complejidad es O(n^C log n) = O(n log n).
"""

def mas_de_la_mitad_rec(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio]

    mitad = (inicio + fin) // 2
    mayor_izquierda = mas_de_la_mitad_rec(arr, inicio, mitad)
    mayor_derecha = mas_de_la_mitad_rec(arr, mitad + 1, fin)

    if mayor_izquierda == mayor_derecha:
        return mayor_izquierda

    conteo_izq = sum(1 for x in arr[inicio:fin + 1] if x == mayor_izquierda)
    conteo_der = sum(1 for x in arr[inicio:fin + 1] if x == mayor_derecha)

    if conteo_izq > (fin - inicio + 1) // 2:
        return mayor_izquierda
    elif conteo_der > (fin - inicio + 1) // 2:
        return mayor_derecha

    return None


def mas_de_la_mitad(arr):
    if not arr:
        return False

    cantidad_elementos = len(arr)
    mayor_repeticion = mas_de_la_mitad_rec(arr, 0, cantidad_elementos - 1)
    if mayor_repeticion is not None:
        return True

    return False



def main():

    array = [1, 2, 3, 1, 1, 1]
    repeticiones = mas_de_la_mitad(array)
    
    if repeticiones:
        print("Hay mas de la mitad de repeticiones!")
    else:
        print("No hay mas de la mitad de repeticiones")

if __name__=='__main__':
    main()