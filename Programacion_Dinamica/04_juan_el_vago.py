
"""
Problema 04: Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto 
esperado a ganar cada día, determinar el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos. Hacer una reconstrucción para verificar qué días debe 
trabajar. Indicar y justificar la complejidad del algoritmo implementado.

Ejemplo:
Para: [100, 5, 50, 1, 1, 200]
Devolver: [0, 2, 5]

Resolucion: De manera similar al problema de scheduling, empleado la ecucacion de recurrencia: M_JOBS[i] = max(M_JOBS[i - 1], M_JOBS[i - 2] + ganancias[i]), para ir
memorizando los valores de la sumatoria maxima actual si decidimos tomar la decision de trabajar el dia actual o no. Si decidimos trabajar (M_JOBS[i - 2] + ganancias[i]),
entonces el valor será la ganancia que obtenemos de trabajar el dia actual + la ganancia maxima que teniamos hasta trabajar dos dias atras (ya que no se puede trabajar
dos dias seguidos). Si no decidimos trabajar (M_JOBS[i - 1]), unicamente nos quedamos con la ganancia maxima que teniamos hasta el dia anterior. De esta forma obtenemos
un arreglo que nos indica el valor maximo obtenido con cada iteracion.
En base a esto podemos reconstruir la solucion final y obtener los indices de los dias laborales.

La complejidad algoritmica es del orden de: O(n)
"""

def reconstruir_solucion(M_JOB, ganancias, n):
    j = n
    dias_laborales = []

    while j > 0:
        if j == 1 or M_JOB[j] == M_JOB[j - 2] + ganancias[j]:
            dias_laborales.append(j - 1)
            j -= 2
        else:
            j -= 1

    return dias_laborales[::-1] 


def juan_el_vago(trabajos):

    if not trabajos:
        return []
    
    elif len(trabajos) == 1:
        return [0]
    
    n = len(trabajos)
    ganancias = [0] * (n + 1)

    for i in range(1, n + 1):
        ganancias[i] = trabajos[i - 1]

    M_JOB = juan_el_vago_dinamico(trabajos, ganancias, n)
    return reconstruir_solucion(M_JOB, ganancias, n)


def juan_el_vago_dinamico(trabajos, ganancias, n):

    M_JOBS = [0] * (n + 1)
    M_JOBS[0] = 0

    if n > 0:
        M_JOBS[1] = trabajos[0]
        M_JOBS[2] = max(trabajos[0], trabajos[1])

    if n > 2:
        for i in range(2, n + 1):
            M_JOBS[i] = max(M_JOBS[i - 1], M_JOBS[i - 2] + ganancias[i])

    return M_JOBS


def main():

    trabajos =[100, 5, 50, 1, 1, 200]
    resultado = juan_el_vago(trabajos)
    print(f"Monto obtenido: {resultado}")

if __name__=='__main__':
    main()