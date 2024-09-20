
"""
Problema 12:
Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia, y determine a cuáles se les otorgará control, de forma 
que no hayan dos mafias ocupando mismo territorio, y a su vez maximizando la cantidad de pedidos otorgados. Indicar y justificar la complejidad del 
algoritmo implementado.

Resolucion:
Nuestra regla Greedy sera: "Priorizar los permisos que tengan una distancia mas pequeña entre el inicio y el fin". El algoritmo planteado es Greedy 
porque sigue una estrategia de selección localmente óptima en cada paso con la esperanza de encontrar una solución globalmente óptima. En este caso, 
el algoritmo selecciona siempre el pedido que termina más temprano y que no se solapa con los pedidos ya seleccionados. Esta elección localmente óptima 
(seleccionar el intervalo que termina más temprano) se repite en cada paso hasta que no queden más intervalos que puedan ser seleccionados sin solaparse.

Lo que se hace...

La complejidad algoritmica es del orden de: O(n)
"""

def distribuir_mafias(pedidos):

	pedidos_ordenados = sorted(pedidos, key=lambda x: (x[1], x[0]))
	ultimo_fin = 0.0
	seleccionados = []

	for pedido in pedidos_ordenados:
		inicio, fin = pedido

		if inicio >= ultimo_fin:
			seleccionados.append(pedido)
			ultimo_fin = fin

	return seleccionados

# pedidos: lista de tuplas con (km inicio, km fin)
def asignar_mafias(pedidos):
    return distribuir_mafias(pedidos)


def main():

	pedidos = [(1, 3.5), (3.3333, 8), (2, 5), (6, 10), (8, 9)]
	resultado = asignar_mafias(pedidos)
	print("Pedidos seleccionados:", resultado)

if __name__ == "__main__":
    main()