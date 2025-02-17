
"""
Problema 15: Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad 
de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el 
grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden 
sentarse. Implementar un algoritmo que, por backtracking, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, 
que dejan la menor cantidad de espacios vacíos).
"""

def bt_max_grupos_bodegon(P, W, indice, seleccion_actual, ocupacion_actual, mejor_seleccion, mejor_ocupacion):
    # Si la ocupación actual es mejor, la guardamos
    if ocupacion_actual > mejor_ocupacion[0]:
        mejor_ocupacion[0] = ocupacion_actual
        mejor_seleccion[:] = seleccion_actual[:]

    # Si ya pasamos el espacio máximo o no quedan más grupos, cortamos
    if ocupacion_actual >= W or indice >= len(P):
        return

    for i in range(indice, len(P)):
        if ocupacion_actual + P[i] <= W:
            # Elegimos el grupo P[i]
            seleccion_actual.append(P[i])
            bt_max_grupos_bodegon(P, W, i + 1, seleccion_actual, ocupacion_actual + P[i], mejor_seleccion, mejor_ocupacion)
            # Deshacemos la elección
            seleccion_actual.pop()

def max_grupos_bodegon(P, W):
    mejor_seleccion = []
    mejor_ocupacion = [0]  # Usamos una lista para que sea mutable
    bt_max_grupos_bodegon(P, W, 0, [], 0, mejor_seleccion, mejor_ocupacion)
    return mejor_seleccion
