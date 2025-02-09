
"""
Problema 03: Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n, en tiempo O(log n). Por ejemplo, para 
n = 10 debe devolver 3, y para n = 25 debe devolver 5. Justificar el orden del algoritmo.

Resolucion: Comenzamos encontrando el valor medio entre la raiz buscada y cero, el resultado lo elevamos al cuadrado para obtener la potencia y ver si efectivamente ese valor
era la raiz (ya que al elevar al cuadrado un numero que se supone es la raiz cuadrada de ese numero deberia darnos ese numero). Si el resultado es mayor que el valor del cual
queremos tomar la raiz, entonces seguimos buscando en los numeros menores al actual; si es mayor, en los numeros mayores al actual; y si es justo el numero entonces retornamos.
Notemos que en cada paso vamos dividiendo el problema en dos para obtener la raiz cuadrada.

La complejidad algoritmica es del orden de: O(log n) ya que empleando el teorema maestro tenemos un problema que dividimos en cada paso a la mitad por lo que B = 2, A = 1 ya 
que solo hacemos un llamado recursivo por cada llamada a la funcion y f(n) = 1 por lo que C = 0 ya que todas las demas operaciones son O(1). Con estos datos podemos plantear
que T(n) = T(n/2) + O(1), lo cual implica que como Log2(1) = 0 y C = 0, entonces estamos en el caso 2 en donde logB(A) = C por lo que la complejidad es O(log n).
"""

def busqueda_parte_entera(raiz_buscada, minimo_actual, maximo_actual):

    if minimo_actual + 1 >= maximo_actual:
        return minimo_actual

    numero_encontrado = (minimo_actual+maximo_actual) // 2
    valor_obtenido = numero_encontrado*numero_encontrado

    if valor_obtenido > raiz_buscada:
        return busqueda_parte_entera(raiz_buscada, minimo_actual, numero_encontrado)

    elif valor_obtenido < raiz_buscada:
        return busqueda_parte_entera(raiz_buscada, numero_encontrado, maximo_actual)
       
    else:
        return numero_encontrado

def parte_entera_raiz(n):
    if n == 1:
        return 1
    
    return busqueda_parte_entera(n, 0, n)

def main():

    numero = 9
    raiz_encontrada = parte_entera_raiz(numero)
    print(f"Raiz de {numero} es {raiz_encontrada}")

if __name__ == "__main__":
    main()