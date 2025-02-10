import random

def leer_monedas(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.readlines()
        monedas = []
        for linea in contenido:
            linea = linea.strip()
            if linea and not linea.startswith('#'):  
                monedas.extend(map(int, linea.split(';'))) 
    return monedas

def leer_barcos(filename):
    with open(filename, 'r') as file:
        lineas = file.readlines()

    secciones = [[]]
    seccion_actual = 0
    for linea in lineas: 
        if not linea.startswith('#'):
            if linea == '\n':
                seccion_actual += 1
                secciones.append([])
            else:
                secciones[seccion_actual].append(linea.strip())

    print(f"{secciones}\n")
    requisitos_filas = [int(valor) for valor in secciones[0]]
    requisitos_columnas = [int(valor) for valor in secciones[1]]
    barcos = [int(valor) for valor in secciones[2]]

    return requisitos_filas, requisitos_columnas, barcos

def generar_monedas_random(n):
    monedas = []
    for _ in range(n):
        monedas.append(random.randint(1, 1000))
    return monedas


def generar_barcos_random(n):
    # Generar n filas con las demandas de las filas
    requisitos_filas = [random.randint(1, 10) for _ in range(n)]

    # Generar m filas con las demandas de las columnas
    requisitos_columnas = [random.randint(1, 10) for _ in range(n)]

    # Generar k filas con el largo de los barcos
    barcos = [random.randint(1, 5) for _ in range(n)]

    return requisitos_filas, requisitos_columnas, barcos

def generar_archivo(nombre_archivo, n, m, k):
    with open(nombre_archivo, 'w') as archivo:
        # Generar n filas con las demandas de las filas
        for _ in range(n):
            archivo.write(f"{random.randint(1, 20)}\n")
        
        archivo.write("\n")
        
        # Generar m filas con las demandas de las columnas
        for _ in range(m):
            archivo.write(f"{random.randint(1, 20)}\n")
        
        archivo.write("\n")
        
        # Generar k filas con el largo de los barcos
        for _ in range(k):
            archivo.write(f"{random.randint(1, 20)}\n")
