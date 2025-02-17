
"""
Problema 10: Manejamos un negocio que atiende clientes en Londres y en California. Nos interesa cada mes decidir si operar en una u otra ciudad. Los costos de operación para 
cada mes pueden variar y son dados por 2 arreglos: L y C, con valores para todos los meses hasta n. Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una 
distinta, habrá un costo fijo M por la mudanza. Dados los arreglos de costos de operación en Londres (L) y California (C), indicar la secuencia de las n localizaciones en las 
que operar durante los n meses, sabiendo que queremos minimizar el total de los costos de operación. Se puede empezar en cualquier ciudad. Indicar y justificar la complejidad 
del algoritmo implementado.

Resolucion:

La complejidad algoritmica es del orden de:
"""


def reconstruir_solucion(L, C, M, costos_obtenidos):

    n = len(L)
    ciudades_seleccionadas = []
    
    # Determino la última ciudad con menor costo
    if costos_obtenidos[n-1][0] <= costos_obtenidos[n-1][1]:
        ciudad_actual = 0  # Londres
    else:
        ciudad_actual = 1  # California

    for i in range(n-1, -1, -1):
        ciudades_seleccionadas.append("londres" if ciudad_actual == 0 else "california")
        if i > 0:

            if ciudad_actual == 0:  # Si estamos en Londres
                if costos_obtenidos[i][0] == costos_obtenidos[i-1][1] + M + L[i]:  
                    ciudad_actual = 1  # Cambiamos a California

            else:  # Si estamos en California
                if costos_obtenidos[i][1] == costos_obtenidos[i-1][0] + M + C[i]:  
                    ciudad_actual = 0  # Cambiamos a Londres

    return ciudades_seleccionadas[::-1]


def plan_operativo(L, C, M):

    costos_obtenidos = plan_operativo_dinamico(L, C, M)
    return reconstruir_solucion(L, C, M, costos_obtenidos)


def plan_operativo_dinamico(L, C, M):

    n = len(L)
    
    COSTOS_OPTIMOS = [[0] * 2 for _ in range(n)]
    
    COSTOS_OPTIMOS[0][0] = L[0]
    COSTOS_OPTIMOS[0][1] = C[0]

    for i in range(1, n):
        COSTOS_OPTIMOS[i][0] = min(COSTOS_OPTIMOS[i-1][0] + L[i], COSTOS_OPTIMOS[i-1][1] + M + L[i])
        COSTOS_OPTIMOS[i][1] = min(COSTOS_OPTIMOS[i-1][1] + C[i], COSTOS_OPTIMOS[i-1][0] + M + C[i])

    return COSTOS_OPTIMOS


def main():
    
    L = [3, 2, 7, 4, 6, 8, 9, 0, 2, 4, 6, 10]  # Costos en Londres
    C = [5, 1, 3, 9, 2, 3, 7, 4, 9, 6, 1, 10]  # Costos en California
    M = 4  # Costo de mudanza entre ciudades

    resultado = plan_operativo(L, C, M)
    print(f"{resultado}")

if __name__ == '__main__':
    main()
