
"""
Problema 17:
Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. Implementar un algoritmo que dé la cantidad mínima de faros 
que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las 
directamente adyacentes a estas (es decir, un “radio de 2 celdas”).


Resolucion: ...

La complejidad algoritmica es del orden de: O(2^n)
"""

#Pre: -
#Post: Iluminamos las celdas adyacentes a un faro en un radio de 2 celdas.
def iluminar_area(matriz, fila, columna, celdas_iluminadas):
    for delta_fila in range(-2, 3):
        for delta_columna in range(-2, 3):
            fila_nueva, columna_nueva = fila + delta_fila, columna + delta_columna
            if 0 <= fila_nueva < len(matriz) and 0 <= columna_nueva < len(matriz[0]):
                celdas_iluminadas.add((fila_nueva, columna_nueva))

def submarinos_bt(matriz):
    faros_activados = set()
    celdas_iluminadas = set()

    #Identificamos las celdas con submarinos
    submarinos = set((fila, columna) for fila in range(len(matriz)) for columna in range(len(matriz[0])) if matriz[fila][columna])

    while submarinos:
        mejor_faro = None
        mejor_cobertura = 0

        # Intentamos colocar un faro en cada celda con submarino
        for fila, columna in submarinos:
            celdas_cubiertas = set()
            iluminar_area(matriz, fila, columna, celdas_cubiertas)

            # Ver cuántos submarinos cubre esta colocación de faro
            cobertura = len(celdas_cubiertas & submarinos)
            if cobertura > mejor_cobertura:
                mejor_faro = (fila, columna)
                mejor_cobertura = cobertura

        # Colocamos el faro en la mejor posición encontrada
        if mejor_faro:
            faros_activados.add(mejor_faro)
            iluminar_area(matriz, mejor_faro[0], mejor_faro[1], celdas_iluminadas)
            submarinos -= celdas_iluminadas  # Elimina las celdas iluminadas

    return faros_activados

def submarinos(matriz):
    if not matriz:
        return []
    
    return submarinos_bt(matriz)


def main():

    matriz = [
        [False, True, False, False],
        [False, False, True, False],
        [True, False, False, False],
        [False, False, False, True]
    ]

    faros = submarinos(matriz)
    print(f"Faros necesarios para iluminar todos los submarinos: {len(faros)}")
    print("Posiciones de los faros:", faros)


if __name__ == "__main__":
    main()
