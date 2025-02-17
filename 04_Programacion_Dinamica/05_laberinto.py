
"""
Problema 05: Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM. Los movimientos 
permitidos son hacia abajo o hacia la derecha y se inicia desde la esquina superior izquierda (el (0,0)). Pasar por un casillero determinado (i, j) nos da una ganancia de 
V_{i,j}. Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto. Hacer una reconstrucción del camino que 
se debe transitar. Indicar y justificar la complejidad del algoritmo implementado. Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar
para resolver el mismo problema?

Resolucion: Para la resolucion de este problema vamos recorriendo la matriz por cada columna de cada fila y corroborando si el valor maximo es el valor que se encuentra arriba
de mi posicion actual o el que se encuentra a la izquierda (esto solo porque es posible desplazarse hacia abajo y derecha desde la coordenada (0,0)). A este valor le sumo el
valor de mi posicion actual (que si es 0 no afecta en nada a la mayor ganancia) y asi sigo hasta recorrer toda la matriz y llegar al punto (n,m) con la mayor ganancia.
Mi ecuacion de recurrencia es: M_LAB[i][j] = max(M_LAB[i - 1][j],  M_LAB[i][j - 1]) + ganancias[i][j] con ligeras alteraciones en los casos borde como si nos encontramos
en la fila o columna = 0.
Para reconstruir la solucion debemos de empezar de la posicion (n,m) e ir desplazandonos hacia el mayor elemento (teniendo en cuenta que solo puedo moverme hacia arriba
o a la izquierda), e ir guardando los indices a cada paso.

En caso de tener obstaculos, unicamente debemos indicar de alguna forma que esa casilla no debe de contabilizarse para la sumatoria de mayor ganancia. Podemos por ejemplo
poner un 0 en ella y continuar con las siguientes.

La complejidad algoritmica es del orden de: O(n^2)
"""

def reconstruir_solucion(mayores_ganancias, n , m):
    i = n - 1
    j = m - 1
    posiciones_mayor_ganancia = []

    while i != 0 or j != 0:
        posiciones_mayor_ganancia.append((i,j))
        if i == 0:
            j -= 1

        elif j == 0:
            i -= 1

        else:
            if mayores_ganancias[i - 1][j] > mayores_ganancias[i][j - 1]:
                i -= 1
            else:
                j -= 1

    posiciones_mayor_ganancia.append((i,j))
    return posiciones_mayor_ganancia[::-1]


def laberinto(matriz):

    if not matriz:
        return []

    n = len(matriz) 
    m = len(matriz[0])
    ganancias = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            ganancias[i][j] = matriz[i][j]

    mayores_ganancias = laberinto_dinamico(ganancias, n, m)
    return reconstruir_solucion(mayores_ganancias, n, m) #El problema no nos pide la reconstruccion pero la agregamos de todas formas


def laberinto_dinamico(ganancias, n, m):

    M_LAB = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):

            if i == 0 or j == 0:
                if j == 0 and i != 0:
                    M_LAB[i][j] = M_LAB[i - 1][j] + ganancias[i][j]

                elif i == 0 and j != 0:
                    M_LAB[i][j] = M_LAB[i][j - 1] + ganancias[i][j]
                
                else:
                    M_LAB[i][j] = ganancias[i][j]
            else:
                M_LAB[i][j] = max(M_LAB[i - 1][j],  M_LAB[i][j - 1]) + ganancias[i][j]

    return M_LAB


def main():

    matriz = [
        [5, 30, 2, 1],
        [1, 2, 10, 8],
        [50, 3, 2, 6],
        [2, 1, 20, 1]]
    
    resultado = laberinto(matriz)
    print(f"Camino obtenido: {resultado}")

    camino_esperado = "[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3)]"
    print(f"Camino esperado: {camino_esperado}")

if __name__=='__main__':
    main()