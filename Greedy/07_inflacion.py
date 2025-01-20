
"""
Problema 07:
Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos 
en una era de inflación y los precios aumentan todo el tiempo. El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0). Implementar un algoritmo greedy que nos 
indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra 
siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

Resolucion:
Nuestra regla Greedy será: "Comprar los elementos mas caros primero"
"""

def precios_inflacion_minimo(R):
    precios = 0
    for i in range(0, len(R)):
        precios += R[i] ** (i+1)
    return precios


def precios_inflacion(R):
    if not R:
        return 0
    
    R.sort(reverse=True)
    return precios_inflacion_minimo(R)

def main():
    R = [10.05, 5, 20.2, 10]
    precio_minimo = precios_inflacion(R)
    print(f"El precio minimo posible es: {precio_minimo}")

if __name__ == "__main__":
    main()