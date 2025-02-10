
"""
Problema 15:
Se tiene una colección de n libros con diferentes espesores, que pueden estar entre 1 y n (valores no necesariamente enteros). Tu objetivo es guardar esos libros en la menor 
cantidad de cajas. Todas las cajas disponibles son de la misma capacidad L (se asegura que L >= n). Obviamente, no podés partir un libro para que vaya en múltiples cajas, 
pero sí podés poner múltiples libros en una misma caja, siempre y cuando los espesores no superen esa capacidad L. Implementar un algoritmo Greedy que obtenga las cajas, tal 
que se minimicen la cantidad de cajas a utilizar. Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. ¿El 
algoritmo propuesto encuentra siempre la solución óptima? Justificar.

Resolucion:
Nuestra regla Greedy sera: "Colocar el libro más pesado disponible en la caja mientras no supere la capacidad". El algoritmo greedy no garantiza siempre la solución óptima 
aunque puede ser eficiente en muchos casos, hay configuraciones de espesores de libros donde una distribución diferente podría resultar en un menor número de cajas necesarias.

Este algoritmo es greedy porque en cada paso toma la decisión localmente óptima de colocar el libro más grueso disponible en la primera caja en la que quepa. No considera 
las consecuencias futuras de esta decisión, sino que se enfoca en minimizar el espacio desperdiciado en cada paso.

Lo que se hace...

La complejidad algoritmica es del orden de: O(n log n)
"""

def distribuir_en_cajas(capacidad, libros):
    caja = []
    cajas = []
    libros.sort(reverse=True)
    peso_acumulado = 0

    for libro in libros:
        # Si el libro cabe en la caja actual sin exceder la capacidad
        if peso_acumulado + libro <= capacidad:
            caja.append(libro)
            peso_acumulado += libro  # Actualiza el peso acumulado en la caja

        else: # Si el libro no cabe, guarda la caja actual y empieza una nueva
            cajas.append(caja)
            if libro <= capacidad:
                caja = []
                caja.append(libro)
                peso_acumulado = libro
            else:
                caja = []
                peso_acumulado = 0

    if len(caja) != 0:
        cajas.append(caja)

    return cajas


def cajas(capacidad, libros):
    if capacidad <= 0 or not libros:
        return []

    return distribuir_en_cajas(capacidad, libros)


def main():

    capacidad = 10
    libros = [2.5, 3.5, 1.5, 4.5, 2.0]

    libros_colocados = cajas(capacidad, libros)
    print(f"Libros colocados: {libros_colocados}")


if __name__ == "__main__":
    main()