
"""
Problema 15:
Dada una soga de n metros (n mayor o igual a 2) implementar un algoritmo que, utilizando programación dinámica, permita cortarla (en partes 
de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. El algoritmo debe devolver el valor 
del producto máximo alcanzable. Tener en cuenta que la soga puede cortarse varias veces, como se muestra en el ejemplo con n = 10.

Ejemplos:

n = 2 --> Debe devolver 1 (producto máximo es 1 * 1)
n = 3 --> Debe devolver 2 (producto máximo es 2 * 1)
n = 4 --> Debe devolver 4 (producto máximo es 2 * 2)
n = 5 --> Debe devolver 6 (producto máximo es 2 * 3)
n = 6 --> Debe devolver 9 (producto máximo es 3 * 3)
n = 7 --> Debe devolver 12 (producto máximo es 3 * 4)
n = 10 --> Debe devolver 36 (producto máximo es 3 * 3 * 4)
"""

def problema_soga(n):
    
    longitud_soga = n

    if longitud_soga == 2:
        return 1
    if longitud_soga == 3:
        return 2
    maximo_producto = [0] * (longitud_soga + 1)
    maximo_producto[1], maximo_producto[2], maximo_producto[3] = 1, 2, 3

    for i in range(4, longitud_soga + 1):
        for j in range(1, i // 2 + 1):
            maximo_producto[i] = max(maximo_producto[i], maximo_producto[j] * maximo_producto[i - j])
    return maximo_producto[longitud_soga]

def main():
    print("Probando la función problema_soga:")
    print("n = 2:", problema_soga(2))
    print("n = 3:", problema_soga(3))
    print("n = 4:", problema_soga(4))
    print("n = 5:", problema_soga(5))
    print("n = 6:", problema_soga(6))
    print("n = 7:", problema_soga(7))
    print("n = 8:", problema_soga(8))
    print("n = 9:", problema_soga(9))
    print("n = 10:", problema_soga(10))
    print("n = 20:", problema_soga(20))
    print("n = 50:", problema_soga(50))

if __name__ == "__main__":
    main()

