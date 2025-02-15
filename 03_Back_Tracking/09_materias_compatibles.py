
#from compatibles import *

"""
Problema 09:
Se tiene una lista de materias que deben ser cursadas en el mismo cuatrimestre, cada materia está representada con una lista de cursos/horarios posibles a cursar (solo debe 
elegirse un horario por cada curso). Cada materia puede tener varios cursos. Implementar un algoritmo de backtracking que devuelva un listado con todas las combinaciones 
posibles que permitan asistir a un curso de cada materia sin que se solapen los horarios. Considerar que existe una función son_compatibles(curso_1, curso_2) que dados dos 
cursos devuelve un valor booleano que indica si se pueden cursar al mismo tiempo.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""


def son_compatibles(curso_1, curso_2):
    inicio_1, fin_1 = curso_1
    inicio_2, fin_2 = curso_2

    return fin_1 <= inicio_2 or fin_2 <= inicio_1

def bt_obtener_combinaciones(materias, combinaciones, combinacion_actual, indice_materia):
    
    if indice_materia == len(materias):
        combinaciones.append(combinacion_actual[:])
        return

    for curso in materias[indice_materia]:

        if all(son_compatibles(curso, seleccionado) for seleccionado in combinacion_actual):
            combinacion_actual.append(curso)

            bt_obtener_combinaciones(materias, combinaciones, combinacion_actual, indice_materia + 1)

            combinacion_actual.pop()


def obtener_combinaciones(materias):
    combinaciones = []
    combinacion_actual = []
    bt_obtener_combinaciones(materias, combinaciones, combinacion_actual, 0)
    return combinaciones

def main():
   
    materias = [
        [(8, 10), (10, 12)],    # Materia 1: dos cursos con diferentes horarios
        [(9, 11), (13, 15)],    # Materia 2: dos cursos con diferentes horarios
        [(11, 13), (15, 17)]    # Materia 3: dos cursos con diferentes horarios
    ]

    combinaciones = obtener_combinaciones(materias)

    print("Combinaciones posibles:")
    for i, combinacion in enumerate(combinaciones):
        print(f"Combinación {i + 1}: {combinacion}")


if __name__ == "__main__":
    main()
