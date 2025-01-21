

"""
Problema 14:
Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. Implementar un algoritmo Greedy que dé la cantidad mínima de 
faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las 
directamente adyacentes a estas (es decir, un “radio de 2 celdas”). Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado da siempre la 
solución óptima? Justificar

Resolucion:
Nuestra regla Greedy sera: "".

Lo que se hace...

La complejidad algoritmica es del orden de: O(n)
"""



def submarinos(matriz):
    return[0,0]

"""
def submarinos(matriz):
    n, m = len(matriz), len(matriz[0])
    iluminado = [[False] * m for _ in range(n)]  # Matriz para marcar celdas iluminadas
    faros = []

    def celdas_iluminadas(x, y):
        iluminadas = []
        for i in range(-2, 3):
            for j in range(-2, 3):
                nx, ny = x + i, y + j
                if 0 <= nx < n and 0 <= ny < m and not iluminado[nx][ny]:
                    iluminadas.append((nx, ny))
        return iluminadas

    while any(matriz[i][j] and not iluminado[i][j] for i in range(n) for j in range(m)):
        mejor_faro = None
        max_cobertura = 0

        # Buscar la celda que maximiza la cobertura de submarinos no iluminados
        for x in range(n):
            for y in range(m):
                if matriz[x][y]:  # Solo considerar celdas con submarinos
                    iluminadas = celdas_iluminadas(x, y)
                    cobertura = sum(1 for ix, iy in iluminadas if matriz[ix][iy])

                    if cobertura > max_cobertura:
                        max_cobertura = cobertura
                        mejor_faro = (x, y)

        # Colocar el faro y marcar las celdas iluminadas
        if mejor_faro:
            faros.append(mejor_faro)
            for ix, iy in celdas_iluminadas(*mejor_faro):
                iluminado[ix][iy] = True

    return faros
"""

def main():

    #INCOMPLETO, FALTA TERMINAR
    matriz = [
    [True, False, False, False, True],
    [False, False, True, False, False],
    [False, True, False, False, False],
    [False, False, False, True, False],
    [True, False, False, False, True]]


    faros_colocados = submarinos(matriz)
    print(f"Faros colocados: {faros_colocados}")


if __name__ == "__main__":
    main()