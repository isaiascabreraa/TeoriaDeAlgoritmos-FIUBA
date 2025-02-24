
#La complejidad de Ford Fulkerson es (V * E^2) pero si el grafo es bipartito entonces es O(V * E).

def forf_fulkerson(grafo, s, t):

    if not grafo:
        return {}
    
    flujo = {}
    for v in grafo.obtener_vertices():
        for w in v.adyacentes():
            flujo[(v, w)] = 0

    red_residual = copiar(grafo)

    while ((camino = obtener_camino(red_residual, s, t))) is not None:

        flujo_actualizado = min_peso(grafo_residual, camino)

        for v in range(1 , len(camino)):

            if grafo.hay_arista((camino[v-1],camino[v])):
                flujo[(camino[v-1], camino[v])] += flujo_actualizado
                actualizar_red_residual(red_residual, camino[v-1], camino[v], flujo_actualizado)

            else:
                flujo[(camino[v], camino[v-1])] -= flujo_actualizado
                actualizar_red_residual(red_residual, camino[v-1], camino[v], flujo_actualizado) 

    return flujo

def actualizar_red_residual(grafo_residual, u, v, valor):
    peso_anterior = grafo_residual.peso(u, v)
    if peso_anterior == valor:
        grafo_residual.remover_arista(u, v)
    else:
        grafo_residual.cambiar_peso(u, v, peso_anterior - valor)

    if not grafo_residual.hay_arista(v, u):
        grafo_residual.agregar_arista(v, u, valor)
    
    else:
        grafo_residual.cambiar_peso(v, u, peso_anterior + valor)
