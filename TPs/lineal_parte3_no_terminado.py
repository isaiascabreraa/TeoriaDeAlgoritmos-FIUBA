from pulp import *

# Nota para el corrector: El algoritmo no se probo en profundidad y no terminado, faltan restricciones para que los barcos no se superpongan y que no sean abyasentes.
# En los ejemplos probados se entrega una solución 'optimal' que cumplen con las restricciones del tablero pero al no tener las suficientes restricciones el algoritmo
# corta y pega partes de los barcos para cumplir las restricciones.
# Agradecemos que esta parte del TP fue pase a opcional :)

def mostrar_resultado(prob, tablero, n, m):
    print("Status:", LpStatus[prob.status])
    print("\nTablero:")
    for i in range(n):
        row = ""
        for j in range(m):
            if value(tablero[i][j]) == 1:
                row += " * "
            else:
                row += " o "
        print(row)

def batalla_naval_individual(n : int, m : int, barcos : list, restricciones_filas : list, restricciones_columnas : list):
    # Crear el modelo
    prob = LpProblem("Batalla_Naval", LpMinimize)

    # Crear las variables binarias: 1 si la celda (i, j) está ocupada, 0 si no
    tablero = LpVariable.dicts("Celda", (range(n), range(m)), 0, 1, LpInteger)

    # Restricción: Número de casillas ocupadas en cada fila
    for i in range(n):
        prob += lpSum([tablero[i][j] for j in range(m)]) == restricciones_filas[i]

    # Restricción: Número de casillas ocupadas en cada columna
    for j in range(m):
        prob += lpSum([tablero[i][j] for i in range(n)]) == restricciones_columnas[j]

    # Variables y restricciones para los barcos
    for k, barco in enumerate(barcos):
        # Variable para marcar si una celda es el inicio de un barco horizontal o vertical
        inicio_horizontal = LpVariable.dicts(f"Barco{k+1}_H", (range(n), range(m)), 0, 1, LpInteger)
        inicio_vertical = LpVariable.dicts(f"Barco{k+1}_V", (range(n), range(m)), 0, 1, LpInteger)
        
        # Restricción: Colocar el barco horizontalmente si cabe
        for i in range(n):
            for j in range(m - barco + 1):  # Verifica que haya espacio horizontal
                prob += lpSum([tablero[i][j + l] for l in range(barco)]) >= inicio_horizontal[i][j]
            for j in range(m):  # Limita a que sea inicio o no
                prob += inicio_horizontal[i][j] <= 1

        # Restricción: Colocar el barco verticalmente si cabe
        for j in range(m):
            for i in range(n - barco + 1):  # Verifica que haya espacio vertical
                prob += lpSum([tablero[i + l][j] for l in range(barco)]) >= inicio_vertical[i][j]
            for i in range(n):  # Limita a que sea inicio o no
                prob += inicio_vertical[i][j] <= 1

        # Cada barco debe ser colocado exactamente una vez (en alguna orientación)
        prob += lpSum([inicio_horizontal[i][j] for i in range(n) for j in range(m)]) + \
                lpSum([inicio_vertical[i][j] for i in range(n) for j in range(m)]) == 1

    # Resolver el problema
    prob.solve()
    mostrar_resultado(prob, tablero, n, m)

# Dimensiones del tablero y configuración inicial
"""
n, m = 10, 10  # Dimensiones del tablero
barcos = [1,1,1,1,2,2,2,3,3,4]  # Longitudes de los barcos
restricciones_filas = [3,2,2,4,2,1,1,2,3,0]  # Restricciones por fila
restricciones_columnas = [1,2,1,3,2,2,3,1,5,0]  # Restricciones por columna
"""
n, m = 3, 3  # Dimensiones del tablero
barcos = [1, 2]  # Longitudes de los barcos
restricciones_filas = [1, 0, 2]  # Restricciones por fila
restricciones_columnas = [2, 1, 0]  # Restricciones por columna
batalla_naval_individual(n,m,barcos,restricciones_filas, restricciones_columnas)
