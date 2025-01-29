
"""
Problema 03:
Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos, encontrar cuántas formas diferentes hay de subir la escalera 
hasta el paso n. Indicar y justificar la complejidad del algoritmo implementado.

Ejemplos:
n = 0 --> Debe devolver 1 (no moverse)
n = 1 --> Debe devolver 1 (paso de 1)
n = 2 --> Debe devolver 2 (dos pasos de 1, o un paso de 2)
n = 3 --> Debe devolver 4 (un paso de 3, o tres pasos de 1, o un paso de 2 y uno de 1, o un paso de 1 y un paso de 2)
n = 4 --> Debe devolver 7
n = 5 --> Debe devolver 13

Resolucion: 
Una vez obtenida esta informacion procedemos a emplear nuestra ecuacion de recurrencia: M_ESC[i] = M_ESC[i-1] + M_ESC[i-2] + M_ESC[i-3], unicamente iteramos cobre la cantidad
de escalones disponibles para y calculandolos en base a los resultados anteriores. Este ecuacion es de la forma f(n)= f(n-1) + f(n-2)+ f(n-3, con condiciones iniciales de
f(0) = 1, f(1) = 1 y f(2) = 2.

La complejidad algoritmica es del orden de: O(n)
"""

def escalones(n):
    if n < 0:
        return []
    
    return escalones_dinamico(n)


def escalones_dinamico(n):

    M_ESC = [0] * (n + 1)
    M_ESC[0] = 1

    for i in range(1, n + 1):

        if n == 1:
            M_ESC[i] = M_ESC[i-1]

        elif n == 2:
            M_ESC[i] = M_ESC[i-1] + M_ESC[i-2]

        else:
            M_ESC[i] = M_ESC[i-1] + M_ESC[i-2] + M_ESC[i-3]

    return M_ESC[-1]


def main():

    n = 7
    resultado = escalones(n)

    print(f"Se puede subir de: {resultado} formas distintas")

if __name__=='__main__':
    main()