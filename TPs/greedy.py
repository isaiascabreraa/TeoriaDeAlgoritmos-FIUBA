#algoritmo sin los print ni la estructura de datos que guardaba las decisiones
def iter_greedy_optimizado(monedas):
    total_sophia = 0
    total_mateo = 0
    turno_sofia = True
    fin_actual = len(monedas) - 1
    inicio_actual = 0

    while inicio_actual < fin_actual:
        if turno_sofia:
            if monedas[inicio_actual] >= monedas[fin_actual]:
                total_sophia += monedas[inicio_actual]
                inicio_actual += 1
            else:
                total_sophia += monedas[fin_actual]
                fin_actual -= 1
        else:
            if monedas[inicio_actual] <= monedas[fin_actual]:
                total_mateo += monedas[inicio_actual]
                inicio_actual += 1
            else:
                total_mateo += monedas[fin_actual]
                fin_actual -= 1

        turno_sofia = not turno_sofia

    return total_sophia, total_mateo


def iter_greedy(monedas):
    total_sophia = 0
    total_mateo = 0
    turno_sofia = True
    inicio_actual = 0
    fin_actual = len(monedas) - 1
    historial = ""

    while inicio_actual < fin_actual:
        if turno_sofia:
            if monedas[inicio_actual] >= monedas[fin_actual]:
                historial += f"Sophia debe agarrar la primera ({monedas[inicio_actual]}); "
                total_sophia += monedas[inicio_actual]
                inicio_actual += 1
            else:
                historial += f"Sophia debe agarrar la última ({monedas[fin_actual]}); "
                total_sophia += monedas[fin_actual]
                fin_actual -= 1
        else:
            if monedas[inicio_actual] <= monedas[fin_actual]:
                historial += f"Mateo agarra la primera ({monedas[inicio_actual]}); "
                total_mateo += monedas[inicio_actual]
                inicio_actual += 1
            else:
                historial += f"Mateo agarra la última ({monedas[fin_actual]}); "
                total_mateo += monedas[fin_actual]
                fin_actual -= 1

        turno_sofia = not turno_sofia

    return total_sophia, total_mateo, historial.strip("; ")


def solucion_greedy(monedas):
    total_sophia, total_mateo, historial = iter_greedy(monedas)
    print(historial)
    print(f"Ganancia Sophia: {total_sophia}")
    print(f"Ganancia Mateo: {total_mateo}")    
