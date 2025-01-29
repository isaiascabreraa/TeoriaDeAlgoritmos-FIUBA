

"""
Problema 05: Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM. Los movimientos 
permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia la derecha. Pasar por un casillero determinado (i, j) nos da una 
ganancia de V_{i,j}. Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto. Hacer una reconstrucción del camino que 
se debe transitar. Indicar y justificar la complejidad del algoritmo implementado. Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar
para resolver el mismo problema?

Resolucion:

La complejidad algoritmica es del orden de:
"""

def laberinto(matriz):
    return 0

def main():

    matriz = [(1, 4, 10),(3, 5, 70),(0, 6, 20),(5, 7, 60),(3, 8, 75),(5, 9, 4),(2, 10, 150),(8, 11, 90),(8, 12, 30),(2, 13,10),(12, 14,15)]

    resultado = laberinto(matriz)
    print(f"{resultado}")

if __name__=='__main__':
    main()