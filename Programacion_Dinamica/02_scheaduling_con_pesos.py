

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

    for i in range(1, len(charlas)):

        if charlas[i][0] >= scheduling[-1][1]:
            scheduling.append(charlas[i])
        else:
            prioridad_ganada = charlas[i][2]
            prioridad_perdida = 0
            posicion_sched = len(scheduling) - 1

            while posicion_sched >= 0 and scheduling[posicion_sched][1] > charlas[i][0]:
                prioridad_perdida += scheduling[posicion_sched][2]
                posicion_sched -= 1

            if prioridad_perdida < prioridad_ganada:
                scheduling = scheduling[:posicion_sched+1]
                scheduling.append(charlas[i])

    return scheduling



def scheduling(charlas):
    if not charlas:
        return []

    charlas_programadas = scheduling_con_pesos(charlas)
    print("Obtenido:", charlas_programadas)
    return charlas_programadas


def main():

    # Cada tripla es (hora_inicio, hora_fin, prioridad)
    #charlas = [(1, 4, 10),(3, 5, 70),(0, 6, 20),(5, 7, 60),(3, 8, 75),(5, 9, 4),(2, 10, 150),(8, 11, 90),(8, 12, 30),(2, 13,10),(12, 14,15)]
    charlas = [(1, 3, 2), 
 (2, 5, 3), 
 (3, 6, 5), 
 (4, 7, 1), 
 (5, 9, 4), 
 (6, 10, 6), 
 (8, 11, 2), 
 (10, 12, 8)]

    esperado = [(2, 5, 3), 
 (6, 10, 6), 
 (10, 12, 8)]


    print(f"Esperado: {esperado}")

    scheduling(charlas)


if __name__=='__main__':
    main()