
"""
Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de 
integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el 
grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo 
pueden sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en 
la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos).
"""

def resolver_dinamico(P, W):
    n = len(P)
    
    #Crea una tabla de n x W
    combinaciones = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):  # Itera sobre los grupos
        for j in range(W + 1):  # Itera sobre el espacio disponible

            # No incluye el grupo actual
            combinaciones[i][j] = combinaciones[i - 1][j]

            # Incluye el grupo actual si hay suficiente espacio
            if j >= P[i - 1]:

                #Compara si es mejor incluir el grupo actual en la combinación de espacios ocupados. Si el espacio j puede 
                # acomodar al grupo i, se queda con el mayor valor entre lo que ya tiene en combinaciones[i][j] y el resultado 
                # de incluir el grupo, que es el mejor resultado del espacio restante más el peso del grupo actual.
                combinaciones[i][j] = max(combinaciones[i][j], combinaciones[i - 1][j - P[i - 1]] + P[i - 1])

    #Combinaciones nos dice si es posible, para cada grupo y cada capacidad W, llenar exactamente W espacios usando los grupos 
    #considerados hasta ese momento.

    print(f"{combinaciones}")
    
    # Encuentra el espacio máximo ocupado
    max_espacios_ocupados = 0
    for j in range(W, -1, -1):
        if combinaciones[n][j] > max_espacios_ocupados:
            max_espacios_ocupados = j
    
    # Reconstruye la solución
    resultado = []
    j = max_espacios_ocupados
    for i in range(n, 0, -1):
        if combinaciones[i][j] != combinaciones[i - 1][j]:  # Si se incluyó el grupo
            resultado.append(P[i - 1])  # Agrega el grupo a la solución
            j -= P[i - 1]  # Reduce el espacio ocupado
    
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
