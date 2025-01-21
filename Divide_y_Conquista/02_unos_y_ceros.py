
def busqueda_primer_cero(arr, inicio, fin):
    if inicio > fin:
        return -1

    mitad = (inicio + fin) // 2

    if arr[mitad] == 1 and arr[mitad + 1] == 0:
        return mitad + 1
    elif arr[mitad] == 0 and arr[mitad - 1] == 1:
        return mitad

    if arr[mitad] == 1:
        return busqueda_primer_cero(arr, mitad + 1, fin)
    elif arr[mitad] == 0:
        return busqueda_primer_cero(arr, inicio, mitad - 1)


def indice_primer_cero(arr):
    if arr[0] == 0:
        return 0
    
    if arr[len(arr)-1] == 1:
        return -1
    
    return busqueda_primer_cero(arr, 0, len(arr) - 1)

def main():
    arr = [1,1,1,1,1,0,0,0,0,0,0,0]
    indice_buscado = indice_primer_cero(arr)
    print(f"Indice buscado: {indice_buscado}")


if __name__ == "__main__":
    main()