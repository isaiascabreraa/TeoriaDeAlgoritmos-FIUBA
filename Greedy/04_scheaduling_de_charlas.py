
"""
Problema 04:
Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando en tuplas los horarios de inicios de las charlas, y sus horarios de fin, e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. Indicar y justificar la complejidad del algoritmo implementado.

Resolucion:
Nuestra regla Greedy sera: "Tomaremos las charlas que finalicen antes primero"

Como el objetivo es unicamente acomodar la mayor cantidad de charlas en el horario esperado empezamos tomando la charla que termine antes y colocandola
en un vector 'charlas', luego a medida que recorremos el vector de 'horarios_ordenados' vamos comparando elemento a elemento con el ultimo del vector
de charlas ya que si no se superpone con él, no se superpone con ninguno de los anteriores. Si se superpone, seguimos con el siguiente, si no lo hace
lo sumamos al vector de 'charlas'.

La complejidad algoritmica es del orden de: O(n log(n)) debido a que requerimos ordenar el vector (O(N log(n))) y luego recorrer el vector ordenado para
compararlo con el ultimo elemento de nuestro vector de charlas (O(n)), con lo que finalmente tenemos que la complejidad es: O(N log(n)) + (O(n)), sumandole 
ademas otras operaciones O(1) que al final hacen que la complejidad se quede en O(N log(n)).
"""

def ordenar_por_horario_fin(horarios):
    return sorted(horarios, key=lambda x: x[1])

def hay_interseccion(charlas, horario):
    return horario[0] < charlas[1]

def distribuir_charlas(horarios):
    horarios_ordenados = ordenar_por_horario_fin(horarios)
    charlas = []
    for horario in horarios_ordenados:
        if len(charlas) == 0 or not hay_interseccion(charlas[-1], horario):
            charlas.append(horario)
    return charlas

def charlas(horarios): 
    return distribuir_charlas(horarios)

def main():

    # Cada tupla es (hora_inicio, hora_fin)
    horarios = [(1, 4),(3, 5),(0, 6),(5, 7),(3, 8),(5, 9),(6, 10),(8, 11),(8, 12),(2, 13),(12, 14)]

    charlas_programadas = charlas(horarios)
    charlas_esperadas = [(1,4),(5,7),(8,11),(12,14)]
    print("Horarios obtenidos:", charlas_programadas)
    print("Horarios esperados:", charlas_esperadas)

if __name__ == "__main__":
    main()