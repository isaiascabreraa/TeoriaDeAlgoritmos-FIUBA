
"""
Problema 08:

Resolucion:
Nuestra regla Greedy sera:

Lo que se hace...

La complejidad algoritmica es del orden de: 
"""

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    # Calcula la relación valor/peso para cada elemento
    elementos = [(valor, peso, valor / peso) for valor, peso in elementos]
    
    elementos.sort(key=lambda x: x[2], reverse=True)
    
    capacidad_restante = W
    valor_total = 0
    elementos_seleccionados = []

    for valor, peso, ratio in elementos:
        if peso <= capacidad_restante:
            # Si el peso del elemento no excede la capacidad restante, lo agregamos
            elementos_seleccionados.append((valor, peso))
            valor_total += valor
            capacidad_restante -= peso
    
    return elementos_seleccionados, valor_total

def main():
    elementos = [(60, 10), (100, 20), (120, 30), (240, 40), (150, 25), (200, 35)]
    W = 60
    elementos_seleccionados, valor_total = mochila(elementos, W)
    print("Elementos seleccionados para la mochila:", elementos_seleccionados)
    print("Valor total:", valor_total)

if __name__ == "__main__":
    main()
