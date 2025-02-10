

"""
Problema 15: 
Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo [a, b], y que en el punto a es positiva y en el punto b es negativa (o viceversa), 
necesariamente debe haber (al menos) una raíz en dicho intervalo. Implementar una función raiz que reciba una función (univariable) y los extremos mencionados a y b, 
y devuelva una raíz dentro de dicho intervalo (si hay más de una, simplemente quedarse con una). La complejidad de dicha función debe ser logarítmica del largo del 
intervalo [a, b]. Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos valores: Se puede trabajar con floats, y el algoritmo será equivalente, 
simplemente se plantea con ints para no generar confusiones con la complejidad. Justificar la complejidad de la función implementada.

Resolucion: Para encontrar la raiz (valor para el cual f(c) = 0 en donde C se encuentra entre A y B) primero corroboramos que se cumplan las condiciones para aplicar el
teorema de Bolzano: Si al multiplicar f(a) * f(b) nos da algo mayor que cero quiere decir o bien que ambos son negativo o ambos positivos por lo que no se cumpla que
a sea positivo y b negativo (o viceversa).
A continuacion dividimos el problema a la mitad y corroboramos que ese valor no sea una raiz. Si no lo es, evaluo si f(a) * f(mitad) tienen el mismo signo ya que si lo 
tienen entonces significa que la raiz se encuentra en la otra mitad del arreglo; y de forma similar proceso para corroborar en el lado derecho. De esta forma voy 
dividiendo el problema a la mitad hasta encontrar la raiz.


La complejidad algoritmica es del orden de: O(log) debido a que A = 1 ya que hay solo un llamado recursivo, B = 2 porque el problema se divide siempre a la mitad y 
C = 0 ya que todas las demas operaciones son O(1). De esta forma obtengo el caso 2 donde  LogB(A) = C y 0 = 0 por lo que mi complejidad es O(n^C * log n) = O(log n).
"""

def raiz(funcion, a, b):
    if not funcion:
        return None
    
    valor_a = funcion(a)
    valor_b = funcion(b)
    if valor_a * valor_b > 0:
        return None

    mitad = (a + b) / 2

    if funcion(mitad) == 0:
        return mitad

    if valor_a * funcion(mitad) < 0:
        return raiz(funcion, a, mitad)
    else:
        return raiz(funcion, mitad, b)

def main():
    a = 1
    b = 3
    funcion = (lambda x: x * 2 - 5)

    resultado = raiz(funcion, a, b)
    print(f"Raíz encontrada: {resultado}")  # Debe devolver 2.5

if __name__ == '__main__':
    main()
