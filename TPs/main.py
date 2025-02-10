import sys, time, os
from greedy import solucion_greedy
from prog_dinamica import solucion_prog_dinamica
from backtracking import solucion_backtracking
from aproximacion import solucion_aproximada
from utils import leer_monedas, leer_barcos

ARG_CANT = 3
ARG_INDICE_ALGORITMO = 1
ARG_INDICE_INPUT_FILE = 2
DIRECTORIO_BASE_PARTE2 = "ejemplos_parte2"
DIRECTORIO_BASE_PARTE3 = "ejemplos_parte3"
DIRECTORIO_BASE_PARTE1 = "ejemplos_parte1"

def buscar_archivo(archivo, directorio_base):
    ruta_directorio = os.path.join(directorio_base, archivo)
    if os.path.isfile(ruta_directorio):
        return ruta_directorio
    elif os.path.isfile(archivo):  
        return archivo
    else:
        return None 

def main():
    args = sys.argv
    if len(args) != ARG_CANT:
        print("Error: Cantidad invalida de argumentos, modo de uso: python main.py <algoritmo> <path>")
        return
    
    algoritmo = args[ARG_INDICE_ALGORITMO]
    input_file = args[ARG_INDICE_INPUT_FILE]

    if algoritmo == "gr":
        ruta_archivo = buscar_archivo(input_file, DIRECTORIO_BASE_PARTE1)
        if not ruta_archivo:
            print(f"Error: El archivo '{input_file}' no se encuentra.")
            return
        monedas = leer_monedas(ruta_archivo)

    elif algoritmo == "pd":
        ruta_archivo = buscar_archivo(input_file, DIRECTORIO_BASE_PARTE2)
        if not ruta_archivo:
            print(f"Error: El archivo '{input_file}' no se encuentra.")
            return
        monedas = leer_monedas(ruta_archivo)

    elif algoritmo in ("bt", "aprox"):
        ruta_archivo = buscar_archivo(input_file, DIRECTORIO_BASE_PARTE3)
        if not ruta_archivo:
            print(f"Error: El archivo '{input_file}' no se encuentra.")
            return
        requisitos_filas, requisitos_columnas, barcos = leer_barcos(ruta_archivo)

    else:
        print("Error: Algoritmo Invalido")
        return

    if algoritmo == "gr":
        resultado = solucion_greedy(monedas)
    elif algoritmo == "pd":
        resultado = solucion_prog_dinamica(monedas)
    elif algoritmo == "bt":
        resultado = solucion_backtracking(requisitos_filas, requisitos_columnas, barcos)
    elif algoritmo == "aprox":
        resultado = solucion_aproximada(requisitos_filas, requisitos_columnas, barcos)
    else:
        print("Error: Algoritmo Invalido")
        return
    

if __name__ == "__main__":
    main()
