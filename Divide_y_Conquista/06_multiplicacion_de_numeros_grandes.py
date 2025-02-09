
"""
Problema 06: Implementar un algoritmo de multiplicación de dos números grandes de longitud n, por división y conquista, con un orden de complejidad mejor que O(n^2). 
Justificar el orden del algoritmo mediante el teorema maestro.

Resolucion: Para la resolucion de este ejercicio se empleó el algoritmo de Karatsuba. Primero, los números se dividen en dos partes (alta y baja) tomando la mitad de su 
longitud. Luego, se realizan tres multiplicaciones recursivas: una para las partes bajas, una para las partes altas, y una para las sumas de las partes altas y bajas de ambos 
números. Al reducir el número de multiplicaciones necesarias de cuatro a tres, el algoritmo mejora la eficiencia. Finalmente, los resultados de estas multiplicaciones se 
combinan usando una fórmula específica de Karatsuba, que evita el cálculo de multiplicaciones redundantes.

La complejidad algoritmica es del orden de: O(n^1,6) ya que empleando el teorema maestro tenemos un problema que dividimos en cada paso a la mitad por lo que B = 2, A = 3 
ya que hacemos tres llamados recursivos por cada llamada a la funcion y f(n) = O(n) por lo que C = 1. Con estos datos podemos plantear que T(n) = 3T(n/2) + O(n), lo cual implica 
que como Log2(3) ~= 1.58 y C = 1, entonces estamos en el caso 2 en donde logB(A) > C por lo que la complejidad es O(n^1.6).
"""

def multiplicar(a, b):
    if a < 10 or b < 10:
        return a * b

    longitud_maxima = max(len(str(a)), len(str(b)))
    mitad = longitud_maxima // 2

    parte_superior_a = a // 10**mitad
    parte_inferior_a = a % 10**mitad
    parte_superior_b = b // 10**mitad
    parte_baja_b = b % 10**mitad

    producto_baja  = multiplicar(parte_inferior_a, parte_baja_b)
    producto_alta   = multiplicar(parte_superior_a, parte_superior_b)
    producto_cruzado   = multiplicar(parte_inferior_a + parte_superior_a, parte_baja_b + parte_superior_b)

    return producto_alta * 10**(2 * mitad) + (producto_cruzado - producto_alta - producto_baja) * 10**mitad + producto_baja


def main():
    resultado = multiplicar(50, 100)
    print(f"{resultado}")

if __name__ == "__main__":
    main()