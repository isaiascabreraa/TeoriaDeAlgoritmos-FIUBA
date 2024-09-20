
"""
Problema 08:
Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes. El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada. 

Resolucion:
Nuestra regla Greedy sera:

Lo que se hace...

La complejidad algoritmica es del orden de: 
"""

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    return []

def main():

    elementos = [(60, 10),(100, 20),(120, 30),(240, 40),(150, 25),(200, 35)]
    W = 60

    elementos_seleccionados = mochila(elementos, W)
    print("Elementos seleccionados para la mochila:", elementos_seleccionados)

if __name__ == "__main__":
    main()