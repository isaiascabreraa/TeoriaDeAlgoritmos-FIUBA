
def max_subarreglo_cruzado(arr, inicio, actual, fin):
    def encontrar_suma_izquierda(arr, actual, inicio, suma_actual, suma_maxima, max_izquierda):
        if actual < inicio:
            return suma_maxima, max_izquierda
        suma_actual += arr[actual]
        if suma_actual > suma_maxima:
            suma_maxima = suma_actual
            max_izquierda = actual
        return encontrar_suma_izquierda(arr, actual-1, inicio, suma_actual, suma_maxima, max_izquierda)

    def encontrar_suma_derecha(arr, actual, fin, suma_actual, suma_maxima, max_derecha):
        if actual > fin:
            return suma_maxima, max_derecha
        suma_actual += arr[actual]
        if suma_actual > suma_maxima:
            suma_maxima = suma_actual
            max_derecha = actual
        return encontrar_suma_derecha(arr, actual+1, fin, suma_actual, suma_maxima, max_derecha)

    suma_izquierda, max_izquierda = encontrar_suma_izquierda(arr, actual, inicio, 0, float('-inf'), actual)
    suma_derecha, max_derecha = encontrar_suma_derecha(arr, actual+1, fin, 0, float('-inf'), actual+1)

    return max_izquierda, max_derecha, suma_izquierda + suma_derecha

def encontrar_max_subarreglo(arr, inicio, fin):
    if fin == inicio:
        return inicio, fin, arr[inicio]
    else:
        actual = (inicio + fin) // 2
        inicio_izquierda, fin_izquierda, suma_izquierda = encontrar_max_subarreglo(arr, inicio, actual)
        inicio_derecha, fin_derecha, suma_derecha = encontrar_max_subarreglo(arr, actual+1, fin)
        inicio_cruzado, fin_cruzado, suma_cruzada = max_subarreglo_cruzado(arr, inicio, actual, fin)

        if suma_izquierda >= suma_derecha and suma_izquierda >= suma_cruzada:
            return inicio_izquierda, fin_izquierda, suma_izquierda
        elif suma_derecha >= suma_izquierda and suma_derecha >= suma_cruzada:
            return inicio_derecha, fin_derecha, suma_derecha
        else:
            return inicio_cruzado, fin_cruzado, suma_cruzada

def max_subarray(arr):
    max_arr_actual = max_arr = arr[0]
    inicio = fin = actual = 0

    for i in range(1, len(arr)):
        if arr[i] > max_arr_actual + arr[i]:
            max_arr_actual = arr[i]
            actual = i
        else:
            max_arr_actual += arr[i]

        if max_arr_actual > max_arr:
            max_arr = max_arr_actual
            inicio = actual
            fin = i

    return arr[inicio:fin+1]

def main():
    arr = [-50, 3, -5, -5, 3, 70, -1, 2]
    max_arr = max_subarray(arr)
    print(f"El subarreglo de máxima suma es {max_arr}")

if __name__ == "__main__":
    main()