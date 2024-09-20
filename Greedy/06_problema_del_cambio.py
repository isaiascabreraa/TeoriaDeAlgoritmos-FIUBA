
"""
Problema 06:
Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes. El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada. 

Resolucion:
Nuestra regla Greedy sera: "Emplearemos los billetes de mayor denominacion primero".

Lo que se hace es ver el monto, tomar el billete mas grande que pueda y dividirlo por el mismo. Si el la division me da mayor que 1, me alcanza con ese billete y me quedo 
solo con la parte entera. Luego agrego a mi vector 'vuelto' la denominacion de la moneda una cantidad de n veces (parte entera) y por ultimo resto la cantidad de divisas 
empleadas al resto actual para la siguiente iteracion. Hago lo mismo hasta llegar al monto total o quedarme sin divisas.

La complejidad algoritmica es del orden de: O(n²) ya que en el peor caso debo recorrer toda la lista de divisas monetarias (O(n)) y por cada una de esas divisas debo de 
agregarlas al vector la cantidad de veces que estas se emplean (O(n)).

"""

def ordenar_por_horario_fin(horarios):
    return sorted(horarios, key=lambda x: x[1])

def cantidad_minima_monedas(monedas, monto):
    vuelto = []
    resto = monto
    indice = len(monedas) - 1 #O(1)

    while resto != 0 and indice >= 0: #O(n)
        costo = resto / monedas[indice]
        if costo >= 1:
            cantidad = int(costo)
            for _ in range(cantidad): #O(n)
                vuelto.append(monedas[indice])

            resto = resto - cantidad * monedas[indice]
        indice -= 1
    return vuelto


def cambio(monedas, monto):
    return cantidad_minima_monedas(monedas, monto)


def main():
    monedas = [1, 2, 5, 10, 20, 50, 100]
    monto = 287
    
    resultado = cambio(monedas, monto)
    
    print(f"Para dar un cambio de {monto}, se utilizan las siguientes monedas/billetes:")
    print(resultado)

if __name__ == "__main__":
    main()