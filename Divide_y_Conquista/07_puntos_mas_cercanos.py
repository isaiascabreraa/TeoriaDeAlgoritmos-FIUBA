
"""
Problema 07: Implementar un algoritmo que dados n puntos en un plano, busque la pareja que se encuentre más cercana, por división y conquista, con un orden de complejidad 
mejor que O(n^2). Justificar el orden del algoritmo mediante el teorema maestro.

Resolucion: Primero, ordenamos los puntos en dos listas: puntos_x (ordenados por la coordenada x) y puntos_y (ordenados por la coordenada y). Luego, en la función recursiva
si hay 3 o menos puntos, calculamos directamente las distancias entre cada par de puntos y devolvemos el par con la distancia más corta. Si hay más de 3 puntos, dividimos 
el conjunto en dos mitades basadas en la coordenada x, resolviendo de manera recursiva en cada mitad. Después, se calcula la distancia mínima entre las dos mitades.
A continuación, se crea una "franja" de puntos cercanos al límite de división y se comparan entre sí solo los puntos dentro de esta franja, limitando las comparaciones a un 
máximo de 6 puntos por cada punto en la franja (para mejorar la eficiencia). Este paso es esencial porque los puntos más cercanos pueden estar cerca de la línea divisoria, 
y sin analizar esta franja, podríamos pasar por alto la pareja más cercana que se encuentre en ambos lados de la división. Finalmente, la función devuelve el par de puntos 
con la menor distancia entre ellos y su respectiva distancia.

La complejidad algoritmica es del orden de: O(n log n) ya que empleando el teorema maestro tenemos un problema que dividimos en cada paso a la mitad por lo que B = 2, A = 2 
ya que hacemos dos llamados recursivos por cada llamada a la funcion y f(n) = O(n) por lo que C = 1. Con estos datos podemos plantear que T(n) = 2T(n/2) + O(n), lo cual 
implica que como Log2(2) = 1 y C = 1, entonces estamos en el caso 2 en donde logB(A) = C por lo que la complejidad es O(n log n).
El ordenamiento inicial esta por fuera de la funcion recursiva por lo que no se considera a O(n log n) como el valor de f(n).
"""

def puntos_mas_cercanos_rec(puntos_x, puntos_y):

    cantidad_puntos = len(puntos_x)
    if cantidad_puntos <= 3:
        punto_a, punto_b, punto_c = puntos_x
        distancia_ab = ((punto_a[0] - punto_b[0]) ** 2 + (punto_a[1] - punto_b[1]) ** 2) ** 0.5
        distancia_ac = ((punto_a[0] - punto_c[0]) ** 2 + (punto_a[1] - punto_c[1]) ** 2) ** 0.5
        distancia_bc = ((punto_b[0] - punto_c[0]) ** 2 + (punto_b[1] - punto_c[1]) ** 2) ** 0.5

        if distancia_ab <= distancia_ac and distancia_ab <= distancia_bc:
            return (punto_a, punto_b), distancia_ab
        elif distancia_ac <= distancia_ab and distancia_ac <= distancia_bc:
            return (punto_a, punto_c), distancia_ac
        else:
            return (punto_b, punto_c), distancia_bc

    mid = cantidad_puntos // 2
    puntos_x_izq = puntos_x[:mid]
    puntos_x_der = puntos_x[mid:]

    punto_medio = puntos_x[mid][0]
    puntos_y_izq = [p for p in puntos_y if p[0] <= punto_medio]
    puntos_y_der = [p for p in puntos_y if p[0] > punto_medio]

    pareja_izq, dist_izq = puntos_mas_cercanos_rec(puntos_x_izq, puntos_y_izq)
    pareja_der, dist_der = puntos_mas_cercanos_rec(puntos_x_der, puntos_y_der)

    distancia_min = min(dist_izq, dist_der)
    mejor_pareja = pareja_izq if dist_izq < dist_der else pareja_der


    franja_cercana = [p for p in puntos_y if abs(p[0] - punto_medio) < distancia_min]
    cantidad_franja = len(franja_cercana)

    for i in range(len(cantidad_franja)):
        for j in range(i + 1, min(i + 7, len(franja_cercana))):
            distancia_actual = ((franja_cercana[i][0] - franja_cercana[j][0]) ** 2 + (franja_cercana[i][1] - franja_cercana[j][1]) ** 2) ** 0.5
            if distancia_actual < distancia_minima:
                distancia_minima = distancia_actual
                mejor_pareja = (franja_cercana[i], franja_cercana[j])

    return mejor_pareja, distancia_min


def puntos_mas_cercanos(puntos):
    if not puntos:
        return None

    puntos_x = sorted(puntos, key=lambda p: p[0])
    puntos_y = sorted(puntos, key=lambda p: p[1])
    pareja, _ = puntos_mas_cercanos_rec(puntos_x, puntos_y)
    return pareja

def main():
    puntos = [(2, 5), (4, 8), (7, 1), (3, 6), (9, 4), (2, 4)]
    pareja = puntos_mas_cercanos(puntos)
    print(f"{pareja}")

if __name__ == "__main__":
    main()
