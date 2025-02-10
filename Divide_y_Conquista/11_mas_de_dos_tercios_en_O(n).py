
"""
Problema 10: Implementar una función (que utilice división y conquista) de orden O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún 
elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución. NO esta permitido usar una tabla de hash.

Resolucion: Para resolver el problema tomamos el mismo enfoque del problema anterior pero en este caso lo que buscamos corroborar al final es si el candidato aparece al
menos en 2/3 de nuestro arreglo.

La complejidad algoritmica es del orden de: O(n) debido a que aplicando el teorema maestro tenemos que A = 1, B = 2 y C = 1 ya que todas las demas operaciones son O(n).
Por este motivo al aplicar el teorema maestro tenemos el caso 1 en el que LogB(A) < C y debido a que 1 < 0 y por lo tanto la complejidad es O(n).
"""

def mas_de_dos_tercios_rec(arr, cantidad_elementos):
    if not arr:
        return None
    
    if cantidad_elementos == 1:
        return arr[0]

    nuevo_arr = []

    for i in range(1, cantidad_elementos, 2):
         if arr[i] == arr[i-1]:
            nuevo_arr.append(arr[i])

    return mas_de_dos_tercios_rec(nuevo_arr, len(nuevo_arr))


def mas_de_dos_tercios(arr):
    if not arr:
        return False

    candidato = mas_de_dos_tercios_rec(arr, len(arr))

    if candidato != None and arr.count(candidato) > 2 * (len(arr) // 3):
        return candidato
    elif len(arr) % 2 != 0 and arr.count(arr[-1]) >  2 * (len(arr) // 3):
        return arr[-1]

    return False


def main():

    array = [1, 2, 3, 1, 1, 1, 1]
    repeticiones = mas_de_dos_tercios(array)
    
    if repeticiones:
        print("Hay mas de la mitad de repeticiones!")
    else:
        print("No hay mas de la mitad de repeticiones")

if __name__=='__main__':
    main()