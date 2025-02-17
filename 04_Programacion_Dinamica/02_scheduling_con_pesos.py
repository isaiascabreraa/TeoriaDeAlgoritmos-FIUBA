
"""
Problema 02:
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Además, cada charla tiene asociado un valor de ganancia. 
Implementar un algoritmo que, utilizando programación dinámica, reciba un arreglo que en cada posición tenga una charla representada por una tripla 
de inicio, fin y valor de cada charla, e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. Indicar y justificar la complejidad 
del algoritmo implementado.

Resolucion: Para resolver el problema partimos de un ordenamiento en base a los tiempos de finalizacion de cada charla. Luego creamos un arreglo “valor” en donde tenemos el mejor valor posible hasta el momento 
en base a las charlas que decidimos dar (inicialmente todas son 0 y la posicion 0 esta reservada para el caso en el que no haya ninguna charla). Tambien creamos otro arreglo “p” en donde la posicion de p indica 
la charla a partir de la cual comienzan a superponerse unas con otras. Ej: Si estoy considerando el uso de las primeras 4 charlas, entonces p[3] nos indicará a partir de que charla es que no tengo superposiciones 
(siendo en este caso la charla 2 ya que la charla 4 parece superponerse con todas las anteriores). Si tuvieras solo las primeras 5 charlas, notemos que en p[4] el valor es 0 debido a que la charla 5 se superpone
con todas las anteriores.

Una vez obtenida esta informacion procedemos a emplear nuestra ecuacion de recurrencia: M_SCHE[j] = max(valor[j] + M_SCHE[p[j]], M_SCHE[j - 1])
Con ella consideramos si emplear o no la charla actual. Si decidimos emplearla y no hay superposicion, el valor de M_SCHE[j] será el valor acumulado hasta ahora + el valor de la charla actual. Si hay superposicion
podemos decidir por quedarnos con el valor anterior y no considerar la charla.
En este caso nos es de mucha ayuda el hecho de tener el arreglo p ya que este nos indica a partir de que posicion NO hay supoerposicion y por lo tanto al hacer M_SCHE[p[j]] estamos obteniendo el mejor valor posible
considerando que tomamos todas las charlas anteriores que no se superponen con la actual.

De esta forma podemos obtener un arreglo que contenga en cada posicion cual fue el mejor valor obtenido que nos permite reconstruir la solucion final. Si bien es posible crear una lista e ir modificandola dentro
de nuestra ecuacion de recurrencia para no tener que reconstruir la solucion, esto implica un aumento en la complejidad algoritmica (haciendo que se eleve hasta O(n^2)). Por este motivo es que la reconstruccion
se hace despues.

La complejidad algoritmica es del orden de: O(n log n)
"""

def busqueda_binaria(charlas, inicio, fin, objetivo):
    left, right = inicio, fin
    indice = -1  
    while left <= right:
        mid = (left + right) // 2
        if charlas[mid][1] <= objetivo:
            indice = mid 
            left = mid + 1
        else:
            right = mid - 1
    return indice


def reconstruir_solucion(M_SCHE, charlas, valor, p, n):
    charlas_seleccionadas = []
    j = n
    while j > 0:

        #Si esto pasa es porque consideré la charla.
        if M_SCHE[j] == valor[j] + M_SCHE[p[j]]:
            charlas_seleccionadas.append(charlas[j - 1])
            j = p[j]

        #Si no pasa es porque no la emplee a la charla.    
        
        j -= 1
    return charlas_seleccionadas[::-1]


def scheduling(charlas):
    if not charlas or len(charlas) == 0:
        return []
    
    n = len(charlas)
    charlas.sort(key=lambda x: x[1])
    
    p = [0] * (n + 1)
    valor = [0] * (n + 1)

    for i in range(n):
        #Busco en que posicion el inicio de mi charla actual se superpone la finalizacion de alguna charla anterior.
        j = busqueda_binaria(charlas, 0, i - 1, charlas[i][0]) #Debo emplear la busqueda binaria para encontrar p para mantener la complejidad en O(n log n)
        valor[i + 1] = charlas[i][2]
        p[i + 1] = j + 1
    
    M_SCHE = sche_dinamico(n, p, valor)
    return reconstruir_solucion(M_SCHE, charlas, valor, p, n) #Reconstruyo la solucion con una complejidad lineal.


def sche_dinamico(n, p, valor):
    if n == 0:
        return 0
    
    M_SCHE = [0] * (n + 1)
    M_SCHE[0] = 0
    
    for j in range(1, n + 1):
        M_SCHE[j] = max(valor[j] + M_SCHE[p[j]], M_SCHE[j - 1])

    return M_SCHE

def main():

    # Cada tripla es (hora_inicio, hora_fin, prioridad)
    charlas = [(1, 4, 10),(3, 5, 70),(0, 6, 20),(5, 7, 60),(3, 8, 75),(5, 9, 4),(2, 10, 150),(8, 11, 90),(8, 12, 30),(2, 13,10),(12, 14,15)]

    charlas_obtenidas = scheduling(charlas)
    print(f"{charlas_obtenidas}")

if __name__=='__main__':
    main()