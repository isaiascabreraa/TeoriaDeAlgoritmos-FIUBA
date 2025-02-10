

"""
Problema 15: 
Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo [a, b], y que en el punto a es positiva y en el punto b es negativa (o viceversa), 
necesariamente debe haber (al menos) una raíz en dicho intervalo. Implementar una función raiz que reciba una función (univariable) y los extremos mencionados a y b, 
y devuelva una raíz dentro de dicho intervalo (si hay más de una, simplemente quedarse con una). La complejidad de dicha función debe ser logarítmica del largo del 
intervalo [a, b]. Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos valores: Se puede trabajar con floats, y el algoritmo será equivalente, 
simplemente se plantea con ints para no generar confusiones con la complejidad. Justificar la complejidad de la función implementada.

Resolucion:

La complejidad algoritmica es del orden de: O(log)
"""

def raiz(funcion, a, b):
    if funcion(a) == 0:
        return a
    elif funcion(b) == 0:
        return b
    
    while a <= b:
        centro = (a + b) / 2

        if funcion(centro) == 0:
            return centro

        if (funcion(a) > 0 and funcion(centro) < 0) or (funcion(a) < 0 and funcion(centro) > 0):
            b = centro
        else:
            a = centro

        if abs(a - b) < 1e-7:
            return centro

    return None

def main():
    a = 1
    b = 3
    funcion = (lambda x: x * 2 - 5)

    resultado = raiz(funcion, a, b)
    print(f"Raíz encontrada: {resultado}")  # Debe devolver 2.5

if __name__ == '__main__':
    main()