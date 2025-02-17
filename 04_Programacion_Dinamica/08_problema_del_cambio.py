
"""
Problema 08: Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar “cambio” de una determinada cantidad de plata. Se desea devolver el cambio pedido, usando 
la mínima cantidad de monedas/billetes. Implementar un algoritmo que reciba un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y devuelva 
qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda. Indicar y justificar la complejidad del algoritmo implementado.

Resolucion:
Itero sobre el monto y por cada monto pruebo con que monedas puedo lograr esa cantidad. Por ejemplo si el monto es 4 primero
pruebo el caso base en donde monto es 1 y veo con que divisas puedo conseguirlo. Con moneda = 1 la cantidad de monedas a emplear es 1. Con cualquier otra moneda se supera
el monto actual por lo que continuo con el siguiente monto. Con monto = 2 tengo que puedo lograrlo con las monedas de 1 requeridas para el monto anterior + 1 por lo que
agrego eso a mi mejor opcion y continuo iterando en donde encuentro que tambien puedo lograrlo con una moneda de 2 y como 1 moneda es mejor que dos monedas, reemplazo mi 
mejor opcion hasta el momento. Como resultado obtengo un arreglo en donde tengo la mejor cantidad de monedas a emplear por cada monto de 0 al monto indicado. La ecuacion
de recurrencia a emplear es: cantidad_monedas = M_CAMBIO[i - moneda] + 1.

Para reconstruir la solucion lo que hago es recorrer el arreglo de monedas y primero me fijo si la moneda actual es menor o igual al monto, si es mayor la descarto. Luego
comparo si la cantidad de monedas a emplear para el monto es igual a la cantidad de monedas necesarias si es que utilizo la moneda actual. Por ejemplo: Si mi moneda actual
es 10 y mi monto es 12, entonces al ver la cantidad de monedas necesarias para un monto reducido de 12 (monto) - 10 (moneda actual) = 2, si cantidad_monedas[2] + 1 (porque 
use la moneda de 10) = cantidad_monedas[monto] entonces quiere decir que 10 forma parte de la solucion optima y debo agregar esa moneda. De esta forma irá iterando sobre
las monedas hasta llegar al monto total.

La complejidad algoritmica es del orden de: O(n * m) y es pseudo-polinomial.
""" 

def reconstruir_solucion(monedas, monto, cantidad_monedas):
    if not cantidad_monedas:
        return []

    monedas_utilizadas = []
    while monto > 0:
        for moneda in monedas:
            if moneda <= monto and cantidad_monedas[monto] == cantidad_monedas[monto - moneda] + 1:
                monedas_utilizadas.append(moneda)
                monto -= moneda
                break
                
    return monedas_utilizadas


def cambio(monedas, monto):

    if not monedas or monto == 0:
        return []

    cantidad_monedas = cambio_dinamico(monedas, monto)
    return reconstruir_solucion(monedas, monto, cantidad_monedas)


def cambio_dinamico(monedas, monto):
   
    M_CAMBIO = [0] * (monto + 1)

    """
    Inicializo mi vector del tamaño del monto total con ceros y resuelvo caso por caso desde el monto 0 hasta el monto recibido.
    Por cada monto itero probando si puedo logarlo con la divisa actual. Si no es posible va un -1, si es posible pongo la cantidad
    de monedas necesarias para lograr el monto que tendriamos si al monto actual le quito la moneda actual. A esto le agrego valor + 1 
    correspondiente a emplear la divisa actual (ya que mi vector contiene la cantidad de divisas empleadas y NO cuales).

    Si el monto actual menos la divisa es -1 entonces no califica y el valor en el vector será -1, indicando que es imposible lograrlo.
    """
    
    for i in range(1, monto + 1):
        mejor_opcion = -1

        for moneda in monedas:
            if moneda <= i:
                cantidad_monedas = M_CAMBIO[i - moneda] + 1

                if M_CAMBIO[i - moneda] != -1 and (mejor_opcion == -1 or cantidad_monedas < mejor_opcion):
                    mejor_opcion = cantidad_monedas

        M_CAMBIO[i] = mejor_opcion

    return M_CAMBIO if M_CAMBIO[monto] != -1 else []


def main():

    monedas = [2, 5, 10, 20, 50, 100]
    monto = 11

    resultado = cambio(monedas, monto)
    print(f"{resultado}")

if __name__=='__main__':
    main()