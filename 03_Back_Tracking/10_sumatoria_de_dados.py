
"""
Problema 10:
Implementar un algoritmo tipo Backtracking que reciba una cantidad de dados n y una suma s. La función debe devolver todas las tiradas posibles de n dados 
cuya suma es s. Por ejemplo, con n = 2 y s = 7, debe devolver [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

def bt_sumatoria_dados(restantes, s, suma_actual, tirada, resultado):
    if restantes == 0:
        if suma_actual == s:
            resultado.append(tirada[:])
        return
    
    for dado in range(1, 7):

        #Si tomara este valor y luego todos los dados fueran 1 e incluso asi supero a S entonces descarto la combinacion.
        #Si tomara este valor y luego todos los dados fueran 6 e incluso asi no llego a S descarto esta combinacion.
        if suma_actual + dado + (restantes - 1) > s or suma_actual + dado + (restantes - 1) * 6 < s:
            continue
        
        tirada.append(dado)
        bt_sumatoria_dados(restantes - 1, s, suma_actual + dado, tirada, resultado)
        tirada.pop()

def sumatoria_dados(n, s):
    resultado = []
    bt_sumatoria_dados(n, s, 0, [], resultado)
    return resultado


def main():

    n = 6
    s = 2
    sumatoria_dados(n ,s)
 
if __name__ == "__main__":
    main()