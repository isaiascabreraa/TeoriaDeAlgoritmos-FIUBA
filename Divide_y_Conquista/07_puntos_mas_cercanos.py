
"""
Problema 07:

Resolucion:

La complejidad algoritmica es del orden de:
"""

def puntos_mas_cercanos_rec(puntos_x, puntos_y):

    n = len(puntos_x)
    if n <= 3:
        min_dist = float('inf')
        pareja = None
        for i in range(n):
            for j in range(i + 1, n):
                d = ((puntos_x[i][0] - puntos_x[j][0]) ** 2 + (puntos_x[i][1] - puntos_x[j][1]) ** 2) ** 0.5
                if d < min_dist:
                    min_dist = d
                    pareja = (puntos_x[i], puntos_x[j])
        return pareja, min_dist

    mid = n // 2
    puntos_x_izq = puntos_x[:mid]
    puntos_x_der = puntos_x[mid:]
    punto_medio = puntos_x[mid][0]
    puntos_y_izq = [p for p in puntos_y if p[0] <= punto_medio]
    puntos_y_der = [p for p in puntos_y if p[0] > punto_medio]

    pareja_izq, dist_izq = puntos_mas_cercanos_rec(puntos_x_izq, puntos_y_izq)
    pareja_der, dist_der = puntos_mas_cercanos_rec(puntos_x_der, puntos_y_der)

    d_min = min(dist_izq, dist_der)
    mejor_pareja = pareja_izq if dist_izq < dist_der else pareja_der

    banda = [p for p in puntos_y if abs(p[0] - punto_medio) < d_min]

    for i in range(len(banda)):
        for j in range(i + 1, min(i + 7, len(banda))):
            d = ((banda[i][0] - banda[j][0]) ** 2 + (banda[i][1] - banda[j][1]) ** 2) ** 0.5
            if d < d_min:
                d_min = d
                mejor_pareja = (banda[i], banda[j])

    return mejor_pareja, d_min


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
