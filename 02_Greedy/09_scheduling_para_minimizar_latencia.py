

"""
Problema 09:
Tenemos tareas con una duración y un deadline (fecha límite), pero pueden hacerse en cualquier momento, intentando que se hagan antes del deadline. Una tarea puede completarse 
luego de su deadline, pero ello tendra una penalización de latencia. Para este problema, buscamos minimizar la latencia máxima en el que las tareas se ejecuten. 

Es decir, dados los arreglos de: T (tiempo de duraciones de las tareas) y L (representando al deadline de cada tarea), si definimos que una tarea i empieza en S_i, entonces 
termina en F_i = S_i + T_i, y su latencia es L_i = F_i - D_i (si F_i > D_i, sino 0). Nuestra latencia máxima será aquella i que maximice el valor L_i. 

Implementar un algoritmo que defina en qué orden deben realizarse las tareas, sabiendo que al terminar una tarea se puede empezar la siguiente. Indicar y justificar la 
complejidad del algoritmo implementado. Devolver un arreglo de tuplas, una tupla por tarea, en el orden en que deben ser realizadas, y que cada tupla indique: (el tiempo de 
la tarea i T_tareas[i] y la latencia resultante L_i de esa tarea). ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un 
algoritmo Greedy? Justificar


Resolucion:
Nuestra regla Greedy sera: "Tomar primero las tareas que tengan una deadline mas corta (ya que generarán mayor latencia)"
Este algoritmo también encuentra la solución óptima para minimizar la latencia máxima debido a que al priorizar las tareas con deadlines más cercanos, minimizas la posibilidad 
de que una tarea tarde demasiado y, por lo tanto, cause una alta penalización.

Es un algoritmo Greedy porque en cada paso toma una decisión localmente óptima: seleccionar la tarea que debe completarse más pronto, lo que lleva a una solución global 
óptima. Como es común en los algoritmos Greedy, el algoritmo no se preocupa por los efectos futuros de su decisión, solo elige lo que parece mejor en el momento para 
minimizar la latencia máxima.

Lo que se hace...

La complejidad algoritmica es del orden de: O(n log n)
"""



def minimizar_latencia(L_deadline, T_tareas):

    scheduling = []
    horario_fin = 0
    horario_inicio = 0
    scheduling_ordenado = []

    for i in range(len(L_deadline)): #Las acomodo un poco para que sea mas comodo.
        scheduling_ordenado.append((T_tareas[i], L_deadline[i]))
        
    scheduling_ordenado = sorted(scheduling_ordenado, key=lambda x: x[1])
    
    for i in range(len(scheduling_ordenado)):
        horario_fin = horario_inicio + scheduling_ordenado[i][0]
        latencia = horario_fin - scheduling_ordenado[i][1]

        if latencia < 0:
            latencia = 0

        scheduling.append((scheduling_ordenado[i][0], latencia))
        horario_inicio = horario_fin

    return scheduling


def main():

    # Cada tarea contiene su duracion.
    tareas = [5, 3, 2, 4, 19, 18, 22, 10, 1, 8, 14, 10, 7, 9]
    #tareas = [5, 3, 2, 4]
    #tareas = [1, 10]

    #Cada deadline contiene la fecha limite de finalizacion de la tarrea correspondiente.
    deadline = [1, 2, 5, 14, 11, 6, 8, 9, 15, 18, 12, 3, 4, 24]
    #deadline = [1, 2, 3, 4]
    #deadline = [100, 10]

    resultado = [(5, 4), (3, 6), (10, 15), (7, 21), (2, 22), (18, 39), (22, 59), (10, 68), (19, 85), (14, 98), (4, 100), (1, 100), (8, 105), (9, 108)]
    #resultado = [(5, 4), (3, 6), (2, 7), (4, 10)]
    #resultado = [(10, 0), (1, 0)]

    elementos_seleccionados = minimizar_latencia(deadline, tareas)
    print("El orden de tareas es:", elementos_seleccionados)
    print("El resultado correcto es: ", resultado)

if __name__ == "__main__":
    main()