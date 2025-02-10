import sys
import os

def solucion_prog_dinamica(monedas, reconstruir=True):
    n = len(monedas)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = monedas[i]

    for longitud in range(2, n + 1):  
        for i in range(n - longitud + 1):
            j = i + longitud - 1  

            if monedas[i + 1] > monedas[j]:
                eleccion_izq = dp[i + 2][j] if i + 2 <= j else 0
            else:
                eleccion_izq = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0

            if monedas[i] > monedas[j - 1]:
                eleccion_der = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
            else:
                eleccion_der = dp[i][j - 2] if i <= j - 2 else 0

            dp[i][j] = max(monedas[i] + eleccion_izq, monedas[j] + eleccion_der)

    if reconstruir:
        reconstruir_solucion(dp, monedas)
    return dp[0][n - 1]


def reconstruir_solucion(dp, monedas):
    i, j = 0, len(monedas) - 1
    elecciones = []
    turno_sophia = True

    ganancia_sophia = 0
    ganancia_mateo = 0

    while i <= j:
        if turno_sophia:  # Turno de Sophia
            if i + 1 <= j and monedas[i + 1] > monedas[j]:
                eleccion_izq = dp[i + 2][j] if i + 2 <= j else 0
            else:
                eleccion_izq = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0

            if i <= j - 1 and monedas[i] > monedas[j - 1]:
                eleccion_der = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
            else:
                eleccion_der = dp[i][j - 2] if i <= j - 2 else 0

            if monedas[i] + eleccion_izq == dp[i][j]:
                elecciones.append(f"Sophia debe agarrar la primera ({monedas[i]})")
                ganancia_sophia += monedas[i]
                i += 1
            else:
                elecciones.append(f"Sophia debe agarrar la ultima ({monedas[j]})")
                ganancia_sophia += monedas[j]
                j -= 1
        else:  # Turno de Mateo
            if monedas[i] > monedas[j]:
                elecciones.append(f"Mateo agarra la primera ({monedas[i]})")
                ganancia_mateo += monedas[i]
                i += 1
            else:
                elecciones.append(f"Mateo agarra la ultima ({monedas[j]})")
                ganancia_mateo += monedas[j]
                j -= 1

        turno_sophia = not turno_sophia

    for eleccion in elecciones:
        print(eleccion)

    print(f"\nGanancia Sophia: {ganancia_sophia}")
    print(f"Ganancia Mateo: {ganancia_mateo}")
