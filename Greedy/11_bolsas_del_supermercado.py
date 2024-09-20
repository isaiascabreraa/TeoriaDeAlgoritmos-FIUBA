
"""
Problema 11:
Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los productos 
en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los 
pesos: [ 4, 2, 1, 3, 5 ].

Resolucion:
Nuestra regla Greedy sera: "Se toma el valor mas grande y si sobra espacio, se busca el siguiente elemento mas grande para llenar el espacio"

Lo que se hace...

La complejidad algoritmica es del orden de: O(n²)
"""

def distribuir_en_bolsas(capacidad, productos):
    if capacidad <= 0 or not productos:
        return []

    bolsas = []
    productos_usados = set()
    productos.sort(reverse=True) 					#O(nlog(n))

    for i in range(len(productos)): 				#O(n)
        if i in productos_usados: 					#O(1)
            continue

        bolsa = []
        capacidad_actual = capacidad

        for j in range(i, len(productos)): 			#O(n)

            if j not in productos_usados and productos[j] <= capacidad_actual: #O(1)

                bolsa.append(productos[j])			#O(1)
                capacidad_actual -= productos[j]	#O(1)
                productos_usados.add(j) 			#O(1)

        bolsas.append(bolsa) 						#O(1)

    return bolsas

def bolsas(capacidad, productos):
    return distribuir_en_bolsas(capacidad, productos)

def main():

    peso_maximo = 9
    pesos = [4, 2, 1, 3, 5, 7, 3, 1]

    bolsas_cargadas = bolsas(peso_maximo, pesos)

    print("Distribución de productos en bolsas:")
    print("Bolsas:", bolsas_cargadas)

if __name__ == "__main__":
    main()
