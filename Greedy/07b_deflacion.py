
"""
Problema 07 b:
En Wakanda, tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos, 
pero Wakanda está atravesando una era de deflación y los precios disminuyen todo el tiempo. El precio del producto i el día j+1 es exactamente la mitad del precio en el día j. 
El arreglo R[i] indica todos los precios del primer día. Si bien para reducir costos se debería esperar a que los productos sigan bajando, los tiempos de entrega no nos 
permiten esperar, y cada día debemos comprar uno de los productos. Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. 
Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo 
Greedy? Justificar

Resolucion:
Nuestra regla Greedy será: "Comprar los elementos mas baratos primero"
"""


def precios_inflacion_minima(R):
    precios = 0
    for i in range(0, len(R)):
        precios += R[i] / (2**i)
    return precios


def precios_deflacion(R):
    if not R:
        return 0
    R.sort()
    return precios_inflacion_minima(R)


def main():
    R = [10.05, 5, 20.2, 10]
    precio_minimo = precios_deflacion(R)
    print(f"El precio minimo posible es: {precio_minimo}")

if __name__ == "__main__":
    main()