
def leer_datos(filename):
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

#https://algoritmos-rw.github.io/tda_bg/tps/2024_anual/tp/
#https://github.com/TomasGarciaA/tda-tp-asinc
#https://drive.google.com/drive/u/0/folders/1ACnAyHhEQ957aPDHObRsjO2UUzjt_Hb7


def main():

    requisitos_filas, requisitos_columnas, barcos = leer_datos("archivos_prueba/3_3_2.txt")
    n = len(requisitos_filas)
    m = len(requisitos_columnas)

    print(f"Hay un total de {len(barcos)} barcos")
    posicion = 0
    for barco in barcos:
        print(f"El barco {posicion} tiene un tamaño de {barco}")
        posicion += 1


    #tablero = [[0]*m for _ in range(n)]
    #print(f"{tablero}")


if __name__ == "__main__":
    main()

