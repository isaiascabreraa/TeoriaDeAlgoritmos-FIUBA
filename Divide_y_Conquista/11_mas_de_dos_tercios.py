
"""
Problema 10: Implementar una función (que utilice división y conquista) de orden O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún 
elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución. NO esta permitido usar una tabla de hash.

Resolucion: Para resolver el problema tenemos que notar que para que un elemento se repita mas de la mitad de las veces necesariamente en algun momento estará al lado de 
el mismo, por ejemplo: Si el 1 es un elemento repetido mas de la mitad de las veces, necesariamente tendremos una secuencia de [1,1] en algún momento. Debido a esto es que
podemos reducir la complejidad teniendo un unico llamado recursivo al cual le pasamos una version en la que en el peor caso tendrá la mitad del tamaño original.
Lo que hacemos es generar un nuevo arreglo que contenga los paredes de elementos que se repiten (si tenemos [1,1] entonces agregamos 1 al nuevo arreglo, si tenemos [1,2] 
entonces no lo agregamos). Si nuestro arreglo es impar entonces quitamos el elemento uno de los elementos para considerarlo al final y realizamos el procedimiento con
el arreglo par.
Una vez obtenido el candidato, lo comparamos con el que no consideramos antes si es que el arreglo era impar o simplemente retornamos el candidato actual si es que aparece
mas de la mitad de las veces.

La complejidad algoritmica es del orden de: O(n) debido a que aplicando el teorema maestro tenemos que A = 1, B = 2 y C = 1 ya que todas las demas operaciones son O(n).
Por este motivo al aplicar el teorema maestro tenemos el caso 1 en el que LogB(A) < C y debido a que 1 < 0 y por lo tanto la complejidad es O(n).
"""

def mas_de_la_mitad_rec(arr, cantidad_elementos):
    if not arr:
        return None
    
    if cantidad_elementos == 1:
        return arr[0]

    nuevo_arr = []

    for i in range(1, cantidad_elementos, 2):
         if arr[i] == arr[i-1]:
            nuevo_arr.append(arr[i])

    return mas_de_la_mitad_rec(nuevo_arr, len(nuevo_arr))


def mas_de_la_mitad(arr):
    if not arr:
        return False

    candidato = mas_de_la_mitad_rec(arr, len(arr))

    if candidato != None and arr.count(candidato) > len(arr) // 2:
        return candidato
    elif len(arr) % 2 != 0 and arr.count(arr[-1]) > len(arr) // 2:
        return arr[-1]

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