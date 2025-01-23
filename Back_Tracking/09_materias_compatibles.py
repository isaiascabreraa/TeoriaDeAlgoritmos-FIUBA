
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


def obtener_combinaciones(materias):
    # codigo de muestra
    combinaciones = []
    resul = []
    # por cada materia
    for materia in materias:
        # agrega el primer curso que encuentra
        # pero no está considerando todas las opciones, 
        # ni las compatibilidades!
        resul.append(materia[0])
    combinaciones.append(resul)
    return combinaciones