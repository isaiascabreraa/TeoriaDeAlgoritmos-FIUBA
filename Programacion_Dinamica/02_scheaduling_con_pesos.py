

"""
Problema 02:
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Además, cada charla tiene asociado un valor de ganancia. 
Implementar un algoritmo que, utilizando programación dinámica, reciba un arreglo que en cada posición tenga una charla representada por una tripla 
de inicio, fin y valor de cada charla, e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. Indicar y justificar la complejidad 
del algoritmo implementado.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""


"""
Cuales son mis subproblemas? 
Me conviene ordenarlos todos por horario de finalizacion.
Al estar ordenados, tengo estos casos:
    Caso 0: Sin charlas
    Caso 1: Una sola charla (esa es la elegida)
    Caso 2: Dos charlas, se superponen?
        Si: Entonces me quedo con la que tenga mas valor
        No: Entonces agrego las dos.
    Caso 3: Tengo 3 charlas, esta ultima, se superpone?
        Si: Si se superpone con la ultima entonces veo si se superpone con la anterior a esa, y asi hasta que encuentre una con la que no se
            superponga. CUando llegue a esa comparo si es mas valiosa esta ultima charla o todas las demas.
        No: Si no se superpone con la ultima entonces no se superpone con ninguna de las anteriores ya que la anterior no se superpone con las anteriores.
            En esta caso solo agrego la charla y continuo.
"""


def scheduling_con_pesos(charlas):

    if len(charlas) == 1:
        return charlas

    scheduling = []
    charlas.sort(key=lambda x: x[1])

    scheduling.append(charlas[0])
    prioridad_total = charlas[0][2]

    for i in range (len(charlas)-1):

        prioridad_ganada = 0
        prioridad_perdida = 0

        #No se superponen
        if charlas[i][1] <= charlas[i+1][0]:
            scheduling.append(charlas[i+1])
            prioridad_total += charlas[i+1][2]

        #Se superponen
        else:
            posicion = i
            horarios_superpuestos = True
            prioridad_perdida = charlas[i][2]
            prioridad_ganada = charlas[i+1][2]

            while horarios_superpuestos:

                if posicion < 0:
                    break

                if charlas[posicion-1][1] > charlas[i][0]:
                    prioridad_perdida += charlas[posicion-1][2]
                    print(f"Prioridad perdida: {prioridad_perdida}")
                    posicion -= 1
                    continue

                else:
                    if prioridad_perdida < prioridad_ganada:
                        print(f"Prioridad ganada: {prioridad_ganada}")
                        scheduling = scheduling[:posicion]
                        scheduling.append(charlas[i+1])
                        prioridad_total -= prioridad_perdida
                        prioridad_total += prioridad_ganada

                horarios_superpuestos = False

    print(f"Prioridad total: {prioridad_total}")

    return scheduling


def scheduling(charlas):
    if not charlas:
        return []

    charlas_programadas = scheduling_con_pesos(charlas)
    print("Horarios obtenidos:", charlas_programadas)
    return charlas_programadas


def main():

    # Cada tripla es (hora_inicio, hora_fin, prioridad)
    #charlas = [(1, 4, 10),(3, 5, 70),(0, 6, 20),(5, 7, 60),(3, 8, 75),(5, 9, 4),(6, 10, 50),(8, 11, 90),(8, 12, 30),(2, 13,10),(12, 14,15)]
    charlas = [(1, 4, 10),(3, 5, 70),(5, 7, 60),(8, 11, 90),(12, 14,15)]

    scheduling(charlas)


if __name__=='__main__':
    main()