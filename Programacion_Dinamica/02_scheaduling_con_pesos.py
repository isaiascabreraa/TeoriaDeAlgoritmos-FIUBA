

"""
Problema 02:
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Además, cada charla tiene asociado un valor de ganancia. 
Implementar un algoritmo que, utilizando programación dinámica, reciba un arreglo que en cada posición tenga una charla representada por una tripla 
de inicio, fin y valor de cada charla, e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. Indicar y justificar la complejidad 
del algoritmo implementado.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

def busqueda_binaria(charlas, start):
    low, high = 0, len(charlas) - 1
    while low <= high:
        mid = (low + high) // 2
        if charlas[mid][1] <= start:
            low = mid + 1
        else:
            high = mid - 1
    return high

def scheduling(charlas):
    
    charlas.sort(key=lambda x: x[1])

    n = len(charlas)
    max_ganancias = [0] * (n + 1) 
    secuencia_charlas = [None] * (n + 1)

    for j in range(1, n + 1):
       
        p = busqueda_binaria(charlas, charlas[j - 1][0])
        if p != -1:
            ganancia_incluida = charlas[j - 1][2] + max_ganancias[p + 1]
        else:
            ganancia_incluida = charlas[j - 1][2] 

        if ganancia_incluida > max_ganancias[j - 1]:
            max_ganancias[j] = ganancia_incluida
            secuencia_charlas[j] = j - 1 
        else:
            max_ganancias[j] = max_ganancias[j - 1]
            secuencia_charlas[j] = secuencia_charlas[j - 1]

    resultado = []
    j = n
    while j > 0:
        if secuencia_charlas[j] is not None and (max_ganancias[j] != max_ganancias[j - 1]):
            resultado.append(charlas[secuencia_charlas[j]])
            j = busqueda_binaria(charlas, charlas[secuencia_charlas[j]][0]) + 1
        else:
            j -= 1

    resultado.reverse()
    return resultado



def main():

    # Cada tripla es (hora_inicio, hora_fin, prioridad)
    charlas = [(1, 4, 10),(3, 5, 70),(0, 6, 20),(5, 7, 60),(3, 8, 75),(5, 9, 4),(2, 10, 150),(8, 11, 90),(8, 12, 30),(2, 13,10),(12, 14,15)]

    charlas_obtenidas = scheduling(charlas)
    print(f"{charlas_obtenidas}")

if __name__=='__main__':
    main()