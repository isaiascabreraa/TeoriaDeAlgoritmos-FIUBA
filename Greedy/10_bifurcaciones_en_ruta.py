
"""
Problema 10:
Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado (ordenado por nombre del pueblo) contiene el número de kilómetro donde está ubicada 
cada una. Se desea ubicar la menor cantidad de policiales (en las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a más de 50 km. Justificar que la 
solución es óptima. Indicar y justificar la complejidad del algoritmo implementado.
Ejemplo:

| Ciudad      | Bifurcación |
|-------------|-------------|
| Castelli    | 185         |
| Gral Guido  | 242         |
| Lezama      | 156         |
| Maipú       | 270         |
| Sevigne     | 194         |

Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero no Gral Guido y Maipú. Necesitaría en ese caso, poner otro. Agrego otro patrullero en Gral 
Guido. Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a todas las ciudades con distancia menor a 50km. En un caso alternativo donde solamente 
se consideren las bifurcaciones de Castelli, Gral Guido y Sevigne, la única solución óptima sería colocar un móvil policial en Sevigne.

Resolucion:
Nuestra regla Greedy sera: "Colocar un patrullero en la bifurcación más alejada dentro del rango de 50 km desde la última posición cubierta"
Este algoritmo encuentra siempre la solución óptima porque estamos cubriendo las bifurcaciones en el menor número de patrulleros posible, comenzando con la 
colocación del patrullero más alejado dentro del rango de cobertura.

Este es un algoritmo Greedy porque toma decisiones locales óptimas en cada paso (colocar el patrullero en la bifurcación más alejada dentro del rango de cobertura) con la 
esperanza de que estas decisiones locales conduzcan a una solución global óptima (cubrir todas las bifurcaciones con el menor número de patrulleros).

Lo que se hace...

La complejidad algoritmica es del orden de: O(n log n)
"""

def bifurcaciones_con_patrulla(ciudades):

    ciudades_ordenadas = sorted(ciudades, key=lambda x: x[1])
    resultado = []
    cantidad_ciudades = len(ciudades_ordenadas)
    i = 0

    while i < cantidad_ciudades:

        # Determino la posicion de la ciudad que se encuentra fuera de rango de la posicion actual
        j = i
        while j < cantidad_ciudades and ciudades_ordenadas[j][1] <= ciudades_ordenadas[i][1] + 50:
            j += 1

        # Coloco el patrullero en la última bifurcación dentro del rango
        patrullero = ciudades_ordenadas[j - 1]
        resultado.append(patrullero)

        # Avanzo el índice más allá del rango cubierto por el patrullero
        while j < cantidad_ciudades and ciudades_ordenadas[j][1] <= patrullero[1] + 50:
            j += 1

        i = j #Actualizo el indice.

    return resultado


def main():

    ciudades = [('a', 50), ('b', 75), ('c', 150), ('d', 250), ('e', 282), ('f', 301)]
    resultado = [('b', 75), ('c', 150), ('e', 282)]

    puestos_policiales = bifurcaciones_con_patrulla(ciudades)
    
    print("Los puestos policiales a colocar son:", puestos_policiales)
    print("El resultado esperado es: ", resultado)


if __name__ == "__main__":
    main()