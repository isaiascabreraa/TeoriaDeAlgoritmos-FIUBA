
"""
Problema 11:
Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los productos 
en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los 
pesos: [ 4, 2, 1, 3, 5 ].

Resolucion:
Nuestra regla Greedy sera: "Colocar el producto más pesado disponible en la bolsa mientras no supere la capacidad"
No, el algoritmo no garantiza siempre la solución óptima. El enfoque greedy de "tomar el producto más pesado primero" no siempre conducirá a la 
distribución óptima de productos. En algunos casos, puede ser necesario hacer ajustes o realizar una búsqueda más exhaustiva para encontrar la 
mejor distribución posible.

Un ejemplo donde no se cumpla es si mis productos son [4, 2, 1, 3, 5 ] y mi capacidad es 5 en donde nuestro algoritmo nos dará la distribucion
de [[1, 2], [3], [4], [5]] usando 4 bolsas pero la solucion mas optima es [[3, 2], [4], [5, 1]] unicamente usando 3 bolsas.

Lo que se hace...

La complejidad algoritmica es del orden de: O(n²)
"""

def distribuir_en_bolsas(capacidad, productos):
    if capacidad <= 0 or not productos:
        return []
    
    bolsa = []
    bolsas = []
    productos.sort()
    peso_acumulado = 0

    for i in productos:
        # Si el producto cabe en la bolsa actual sin exceder la capacidad
        if peso_acumulado + i <= capacidad:
            bolsa.append(i)
            peso_acumulado += i  # Actualiza el peso acumulado en la bolsa

        else: # Si el producto no cabe, guarda la bolsa actual y empieza una nueva
            bolsas.append(bolsa)
            if i <= capacidad:
                bolsa = []
                bolsa.append(i)
                peso_acumulado = i
            else:
                bolsa = []
                peso_acumulado = 0

    if len(bolsa) != 0:
        bolsas.append(bolsa)

    return bolsas

def bolsas(capacidad, productos):
    return distribuir_en_bolsas(capacidad, productos)

def main():

    peso_maximo = 5
    pesos = [4, 2, 1, 3, 5]

    bolsas_cargadas = bolsas(peso_maximo, pesos)

    print("Distribución de productos en bolsas:")
    print("Bolsas:", bolsas_cargadas)

if __name__ == "__main__":
    main()
