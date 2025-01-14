
def busqueda_posicion_pico(arr_pico, inicio, fin):
    if inicio > fin:
        return None

    mitad = (inicio + fin) // 2

    if arr_pico[mitad - 1] < arr_pico[mitad] and arr_pico[mitad] > arr_pico[mitad + 1]:
        return mitad

    pico_encontrado = busqueda_posicion_pico(arr_pico, mitad + 1, fin)
    if not pico_encontrado:
        return busqueda_posicion_pico(arr_pico, inicio, mitad - 1)

    return pico_encontrado


def posicion_pico(v, ini, fin):
    if not v:
        return None
    return busqueda_posicion_pico(v, ini, fin)


def main():
    arr_pico = [1, 2, 3, 1, 0, -2]
    pico = posicion_pico(arr_pico, 0, len(arr_pico) - 1)
    print(f"El pico del array {arr_pico} es {pico}")

if __name__ == "__main__":
    main()