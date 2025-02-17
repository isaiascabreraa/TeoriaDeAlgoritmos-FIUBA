
"""
Problema 11:
Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones posibles son:
(i) aumentar el valor del operando en 1 y (ii) duplicar el valor del operando.
Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones a realizar (y cuáles son dichas operaciones)
y devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2'.
"""

def calcular_operaciones(k):

    M_OPERACIONES = [0] * (k + 1) #Almacena la cantidad de operaciones para llegar a k.
    for i in range(1, k + 1):

        #Voy iterando desde 0 a k y si quiero saber como llegar de k-1 a k tengo dos opciones. O los mismo que
        # costaba ir a k-1 + la operacion actual de + 1 o tambien, lo que costaba de ir a k/2 + la operacion actual de * 2. 
        M_OPERACIONES[i] = min(M_OPERACIONES[i - 1], M_OPERACIONES[i // 2] + M_OPERACIONES[i % 2]) + 1
    
    return reconstruir_operaciones(M_OPERACIONES, k)


def reconstruir_operaciones(operaciones, k):
    operaciones_minimas = []
    while k > 0:
        if operaciones[k] == operaciones[k-1] + 1:
            k -= 1
            operaciones_minimas.append("mas1")
        else:
            k //= 2
            operaciones_minimas.append("por2")
    return operaciones_minimas[::-1]


def operaciones(k):
    return calcular_operaciones(k)

def main():
    k = 10
    resultado = operaciones(k)
    print(f"Operaciones para llegar a {k}: {resultado}")

if __name__ == "__main__":
    main()