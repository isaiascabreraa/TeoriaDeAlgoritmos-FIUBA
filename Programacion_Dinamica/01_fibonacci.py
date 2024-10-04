
"""
Problema 01:
Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor del n-ésimo número de fibonacci. Indicar y justificar la complejidad del 
algoritmo implementado.

Definición:
n = 0 --> Debe devolver 1
n = 1 --> Debe devolver 1
n --> Debe devolver la suma entre los dos anteriores números de fibonacci (los fibonacci n-2 y n-1)

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""


def fibonacci(n):

    if n < 2:
        return 1

    fib = [None] * (n+1)

    fib[0] = 1
    fib[1] = 1

    for i in range (2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


def main():

    n = 30
    print(f"La sumatoria se hará con n = {n}")

    #Secuencia Fibonacci: 0,1,1,2,3,5,8,13,21,34,55,89

    resultado = fibonacci(n)
    print(f"El resultado de fibonacci es: {resultado}")

if __name__=='__main__':
    main()

