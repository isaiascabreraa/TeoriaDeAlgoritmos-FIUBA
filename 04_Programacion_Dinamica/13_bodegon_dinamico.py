
"""
Problema 13:
Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de 
integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el 
grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo 
pueden sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en 
la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos).
"""

def resolver_dinamico(grupo, capacidad):

    def calcular_min_operaciones(k):
    # Inicializa la tabla para almacenar el mínimo de operaciones
    M_OPERACIONES = [None] * (k + 1)
    secuencia_operaciones = [None] * (k + 1)
    M_OPERACIONES[0] = 0
    
    for i in range(1, k + 1):

        if M_OPERACIONES[i] is None:
            M_OPERACIONES[i] = k + 1
        
        # Caso 1: aumentar en 1 (mas1)
        if M_OPERACIONES[i - 1] is not None and M_OPERACIONES[i - 1] + 1 < M_OPERACIONES[i]:
            M_OPERACIONES[i] = M_OPERACIONES[i - 1] + 1
            secuencia_operaciones[i] = 'mas1'
        
        # Caso 2: duplicar el valor (por2) si i es divisible por 2
        if i % 2 == 0 and M_OPERACIONES[i // 2] is not None and M_OPERACIONES[i // 2] + 1 < M_OPERACIONES[i]:
            M_OPERACIONES[i] = M_OPERACIONES[i // 2] + 1
            secuencia_operaciones[i] = 'por2'

    return M_OPERACIONES, secuencia_operaciones

    
    # Reconstruye la solución
    resultado = []
    j = capacidad
    for i in range(n, 0, -1):
        if M_COMBINACIONES[i][j] != M_COMBINACIONES[i - 1][j]:  # Si se incluyó el grupo
            resultado.append(grupo[i - 1])  # Agrega el grupo a la solución
            j -= grupo[i - 1]  # Reduce el espacio ocupado
    
    return resultado[::-1]

def bodegon_dinamico(P, W):
    return resolver_dinamico(P, W)

def main():

    grupos = [
        ([2, 4, 3, 5, 1], 10),          # Caso 1: suma exacta
        ([3, 2, 5, 1], 6),              # Caso 2: múltiples combinaciones
        ([1, 1, 1, 1, 1, 1, 1], 4),     # Caso 3: muchos grupos pequeños
        ([4, 5, 6, 2], 8),              # Caso 4: grupos que no caben
        ([2, 2, 2, 2], 8),              # Caso 5: todos los grupos caben
        ([7, 3, 5, 2], 10)              # Caso 6: combinación óptima
    ]

    #P = Cantidad de personas por cada grupo.
    #W = Cantidad de lugares en la mesa.

    #Ejemplo: En el caso 1, hay 5 grupos en donde la cantidad de integrantes es [2,4,3,5,1] respectivamente por cada grupo, y
    #la mesa solo tiene un total de 10 lugares disponibles en esta ocasion.

    for i, (P, W) in enumerate(grupos):
        print(f"Grupo {i}")
        print(f"Integrantes por grupo = {P} - Lugares disponibles = {W}")
        resultado = bodegon_dinamico(P, W)
        print(f"Grupos seleccionados: {resultado}\n")

if __name__ == "__main__":
    main()
