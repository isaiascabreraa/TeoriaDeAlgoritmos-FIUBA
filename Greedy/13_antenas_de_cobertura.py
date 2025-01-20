
"""
Problema 13:
Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que usa mucho sus celulares. El intendente a cargo la ruta 
debe renovar por completo el sistema de antenas, teniendo que construir sobre la ruta nuevas antenas. Cada antena tiene un rango de cobertura de R kilómetros (valor constante 
conocido).Implementar un algoritmo Greedy que reciba las ubicaciones de las casas, en número de kilómetro sobre esta ruta (números reales positivos) desordenadas, y devuelva 
los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura, y se construya para esto la menor cantidad de antenas posibles. Indicar 
y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo da la solución óptima siempre?

Resolucion:
Nuestra regla Greedy sera: "Colocar las antenas en base a la posicion de las casas de forma creciente"

Lo que se hace...

La complejidad algoritmica es del orden de: O(n²)
"""


def cobertura(casas, R, K):

    casas.sort()
    antenas_colocadas = []
    cantidad_casas = len(casas)

    i = 0
    while i < cantidad_casas:
        
        j = i
        while j < cantidad_casas and casas[j] <= casas[i] + R:
            j += 1
        

        antena = casas[i] + 50
        if antena > K:
            antena = K
        
        antenas_colocadas.append(antena)
            

        while i < cantidad_casas and casas[i] <= antena + R:
            i += 1

    return antenas_colocadas


def main():

    casas = [10, 30, 59, 31, 37, 40, 42, 69, 80, 87, 97] #Posicion de las casas en kilometros
    R = 15 #Rango de cobertura de cada antena
    K = 1000 #Largo de la ruta en kilometros

    antenas_colocadas = cobertura(casas, R, K)
    print(f"Las antenas colcoadas son: {antenas_colocadas}")


if __name__ == "__main__":
    main()