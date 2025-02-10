import random
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import math

# Codigo de generador maestro de graficos para todas las partes. El codigo se debe ejecutar como:
# Python3 generador_graficos.py <algoritmo> , siendo algoritmo:
# gr para parte 1, Greedy
# pd para parte 2, Programacion dinamica
# bt para parte 3 Backtracking

from greedy import iter_greedy_optimizado
from prog_dinamica import solucion_prog_dinamica
from backtracking import solucion_backtracking
from aproximacion import solucion_aproximada
from utils import generar_monedas_random, generar_barcos_random

MAX_MUESTRAS = 500
MAX_MUESTRAS_BARCOS = 500
NUMERO_DE_GRUPOS = 3


def medir_tiempo(monedas, algoritmo):
    inicio = time.perf_counter()
    if algoritmo == "gr":
        iter_greedy_optimizado(monedas)
    elif algoritmo == "pd":
        solucion_prog_dinamica(monedas, reconstruir=False)
    fin = time.perf_counter()
    return (fin - inicio) * 1000

def graficar_complejidad(algoritmo):
    monedas_lista = [
        # valor de las monedas ---------------- cantidad de monedas
        [random.randint(1, 1000) for _ in range(random.randint(10, 1000))]
        #[random.choice([random.randint(1, 5), random.randint(900, 1000)]) for _ in range(random.randint(10, 1000))]
        # cantidad de listas de monedas
        for _ in range(100)
    ]

    tamanios = [len(monedas) for monedas in monedas_lista]
    tiempos = [medir_tiempo(monedas, algoritmo) for monedas in monedas_lista]

    orden = np.argsort(tamanios)
    tamanios = np.array(tamanios)[orden]
    tiempos = np.array(tiempos)[orden]

    # ajuste linea roja segun algortimo
    if algoritmo == "gr":
        coef_tiempo = np.polyfit(tamanios, tiempos, 1)
        linea_tiempo = np.polyval(coef_tiempo, tamanios)
        label_ajuste = f'Línea O(n): y={coef_tiempo[0]:.2e}x+{coef_tiempo[1]:.2e}'
    elif algoritmo == "pd":
        coef_tiempo = np.polyfit(tamanios, tiempos, 2)
        linea_tiempo = np.polyval(coef_tiempo, tamanios)
        label_ajuste = f'Línea O(n^2): y={coef_tiempo[0]:.2e}x^2+{coef_tiempo[1]:.2e}x+{coef_tiempo[2]:.2e}'

    # grafico
    plt.figure(figsize=(10, 6))
    plt.scatter(tamanios, tiempos, color='blue', label='Tiempos de ejecución (ms)', alpha=0.7)
    plt.plot(tamanios, linea_tiempo, color='red', linestyle='--', label=label_ajuste)

    plt.title(f'Complejidad Temporal del Algoritmo {"Greedy" if algoritmo == iter_greedy_optimizado else "Programación Dinámica"}')
    plt.xlabel('Tamaño de la lista de monedas')
    plt.ylabel('Tiempo de ejecución (milisegundos)')
    plt.legend()
    plt.grid()
    plt.show()

def plot(algoritmo, algoritmo_nombre):
    plt.figure()
    _, ax = plt.subplots()

    ax.set_title(f"Análisis de Complejidad Temporal {algoritmo_nombre}")
    if algoritmo == iter_greedy_optimizado or algoritmo == solucion_prog_dinamica:
        plt.xlabel("Cantidad de monedas (n)")
    else:
        plt.xlabel("Cantidad de barcos (n)")
    plt.ylabel("Tiempo de ejecución (milisegundos)")

    plot_algorithm_complexity(algoritmo)
    ax.legend([f"{algoritmo_nombre} tiempo de ejecución"])

    if algoritmo == iter_greedy_optimizado or algoritmo == solucion_prog_dinamica:  
        plt.xlim(5, MAX_MUESTRAS)
    else:
        plt.xlim(5, MAX_MUESTRAS_BARCOS)
    plt.show()

def plot_algorithm_complexity(algoritmo):
    numero_de_repeticiones = 3

    if algoritmo == iter_greedy_optimizado or algoritmo == solucion_prog_dinamica:
        n_samples = range(NUMERO_DE_GRUPOS, MAX_MUESTRAS + 1, 1)
    else:
        n_samples = range(NUMERO_DE_GRUPOS, MAX_MUESTRAS_BARCOS + 1, 1)
    time_complexity = []

    for n in n_samples:
        if algoritmo == iter_greedy_optimizado or algoritmo == solucion_prog_dinamica:
            monedas = generar_monedas_random(n)
        else:
            requisitos_filas, requisitos_columnas, barcos = generar_barcos_random(n)
        
        tiempos = []
        for _ in range(numero_de_repeticiones):
            start = time.perf_counter()
            
            algoritmo(requisitos_filas, requisitos_columnas, barcos)
            
            end = time.perf_counter()
            tiempos.append((end - start) * 1000) # convertido a milisegundos

        time_complexity.append(sum(tiempos) / len(tiempos))

    plt.plot(n_samples, time_complexity, 'r-')

ARG_CANT = 2
ARG_ALGORITMO_INDICE = 1

def main():
    args = sys.argv
    if len(args) != ARG_CANT:
        print(f"Error: Cantidad invalida de argumentos, uso: Python3 generador_graficos.py <algoritmo>")
        return
    
    algoritmo = args[ARG_ALGORITMO_INDICE]
    algoritmo, algoritmo_nombre = obtener_algoritmo_con_nombre(algoritmo)
    if algoritmo is None:
        return
    
    plot(algoritmo, algoritmo_nombre)

def obtener_algoritmo_con_nombre(algoritmo):
    if algoritmo == "gr":
        return graficar_complejidad(algoritmo), "Greedy"
    elif algoritmo == "pd":
        return graficar_complejidad(algoritmo), "Programacion Dinamica"
    elif algoritmo == "bt":
        return solucion_backtracking, "Backtracking"
    elif algoritmo == "aprox":
        return solucion_aproximada, "Aproximacion"
    else:
        print(f"Error: Algoritmo no encontrado")
        return None, None  

if __name__ == "__main__":
    main()
