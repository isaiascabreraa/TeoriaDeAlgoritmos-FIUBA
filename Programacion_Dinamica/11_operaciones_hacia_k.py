
"""
Problema 11:
Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones posibles son:
(i) aumentar el valor del operando en 1 y (ii) duplicar el valor del operando.
Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones a realizar (y cuáles son dichas operaciones)
y devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2'.
"""

def calcular_operaciones(k):

    min_operaciones = [None] * (k + 1)
    secuencia_operaciones = [None] * (k + 1)
    min_operaciones[0] = 0
    
    for i in range(1, k + 1):

        if min_operaciones[i] is None:
            min_operaciones[i] = k + 1
        
        # Caso 1: aumentar en 1 (mas1)
        if min_operaciones[i - 1] is not None and min_operaciones[i - 1] + 1 < min_operaciones[i]:
            min_operaciones[i] = min_operaciones[i - 1] + 1
            secuencia_operaciones[i] = 'mas1'
        
        # Caso 2: duplicar el valor (por2) si i es divisible por 2
        if i % 2 == 0 and min_operaciones[i // 2] is not None and min_operaciones[i // 2] + 1 < min_operaciones[i]:
            min_operaciones[i] = min_operaciones[i // 2] + 1
            secuencia_operaciones[i] = 'por2'
    
    resultado = []

    # Reconstruye la solución
    while k > 0:
        resultado.append(secuencia_operaciones[k])
        if secuencia_operaciones[k] == 'mas1':
            k -= 1
        elif secuencia_operaciones[k] == 'por2':
            k //= 2
    
    return resultado[::-1]
def operaciones(k):
    return calcular_operaciones(k)

def main():
    k = 10
    resultado = operaciones(k)
    print(f"Operaciones para llegar a {k}: {resultado}")

if __name__ == "__main__":
    main()